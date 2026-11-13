# funnelchat-python

The official Python SDK for the [Funnelchat API](https://developers-portal.funnelchat.app/docs/): connect your WhatsApp number, send messages, know when they are read, receive them and follow your groups, from Python.

- Every function the developer portal publishes for an API key: see [Every function of the portal](#every-function-of-the-portal).
- Python 3.9 or later. One dependency: [httpx](https://www.python-httpx.org/).
- Responses are plain dicts (the decoded JSON), typed with TypedDicts generated from the spec the portal publishes, so your editor completes their keys and `json.dumps` just works.
- Safe retries (a send is never repeated by itself), pagination by iterating, typed errors with the `X-Request-Id` of each response, and webhook signature verification.

```bash
pip install funnelchat
```

## First use

### 1. Create your key

In the Funnelchat panel, go to **Developers** and tap **Create key**, with the permissions of what you will use. Copy it: it is shown only once. Keep it in the `FUNNELCHAT_API_KEY` environment variable, where the client reads it.

```python
from funnelchat import Funnelchat

client = Funnelchat()  # reads FUNNELCHAT_API_KEY
```

For the five steps of this page, tick **WhatsApp numbers → View** and **Create, connect and delete**, **Contacts and conversations → Send**, **Notifications (webhooks) → View** and **Manage**, and **Groups and campaigns → View** and **Manage groups** (all of them: [Permissions](#permissions)).

### 2. Connect a number

Create a connect link: a single-use page, on the Funnelchat domain, that shows the QR code to scan from WhatsApp → **Linked devices**. Open it yourself, or send it to whoever has the phone:

```python
link = client.connect_links.create(type="qr")["data"]
print(link["url"])  # it carries the token and comes only now
```

Once the page is opened there are 10 minutes to scan the QR. Wait until the link ends; the number it created is the `device_id` you send with:

```python
import time

while True:
    link = client.connect_links.get(link["id"])["data"]
    if link["status"] != "pending":
        break
    time.sleep(5)

if link["device_id"] is None:  # failed, expired or revoked
    raise SystemExit(f"Not connected: {link['status']} {link['error_code']}")
device_id = link["device_id"]  # 9
```

A number you already connected is in `client.devices.list()`: `for device in client.devices.list(): print(device["id"], device["alias"], device["connected"])`. The `device.connected` webhook also says when a number is connected. More in [Connect a number](#connect-a-number).

### 3. Send a message

One call, from your number to a phone (with country code, digits only):

```python
result = client.messages.send_direct(device_id=device_id, phone="5491100000000", text="Hi Ana!")
message = result["message"]
print(message["id"], message["contact_id"], message["status"])  # 1002 2001 queued
```

If that phone is not a contact yet, it is created in the workspace of your key; `message["contact_id"]` is its id. The answer is the queued message: accepted is not delivered yet. With an official (WhatsApp Cloud) number, free text only goes within 24 hours of the contact's last message, so the first message to a new contact is an [approved template](#templates).

### 4. Know when it was read

Subscribe once to `message.status_changed`:

```python
subscription = client.webhooks.create(
    url="https://your-app.example/hooks/funnelchat",
    events=["message.status_changed", "message.received"],
)
# Keep subscription["secret"] (whsec_…) in FUNNELCHAT_WEBHOOK_SECRET: it is shown only once.
client.webhooks.test(subscription["id"])  # delivers a signed webhook.test now
```

At that URL, verify the signature over the raw body and read the status. With Flask:

```python
import os

from flask import Flask, request
from funnelchat import Funnelchat, WebhookVerificationError

app = Flask(__name__)
client = Funnelchat()

@app.post("/hooks/funnelchat")
def funnelchat_hook():
    try:
        event = client.webhooks.construct_event(
            request.get_data(),                          # the raw body, exactly as it arrived
            request.headers.get("X-Funnelchat-Signature"),
            os.environ["FUNNELCHAT_WEBHOOK_SECRET"],     # the full secret, with whsec_
        )
    except WebhookVerificationError:
        return "", 400

    if event["type"] == "message.status_changed" and event["data"]["status"] == "read":
        print(f"Message {event['data']['message_id']} was read")
    return "", 200
```

The status goes `sent`, `delivered`, `read` (or `failed`, with `error`). Answer within 10 seconds and do the slow work after. With FastAPI the raw body is `await request.body()`; with Django, `request.body`.

Without a server, ask for the message: `client.messages.get(message["contact_id"], message["id"])["status"]`.

### 5. Follow a group

Start from the groups your number is in, read live from WhatsApp, and follow one to learn who joins and leaves it:

```python
for group in client.groups.list_by_device(device_id):
    print(group["uid"], group["name"])  # 120363000000000001@g.us Customers

followed = client.groups.follow("120363000000000001@g.us", device_id=device_id)["data"]
print(followed["imported"], followed["is_admin"])  # True True
```

From then on, `group_participant.joined` and `group_participant.left` arrive at your webhook (subscribe to them like to any other event), with `group`, `participant` and `campaign`. More in [Groups](#groups).

## Receive messages

Add `message.received` to the events of your subscription. Each one brings the message, the contact and the number that received it, the one to answer from:

```python
if event["type"] == "message.received":
    data = event["data"]
    print(data["contact"]["phone"], data["message"]["text"])  # text is None for a file without caption

    if data["device_id"] and data["contact"]["id"]:
        client.messages.send_direct(device_id=data["device_id"], contact_id=data["contact"]["id"], text="Got it, thanks!")
```

On an official number, a message received opens the 24-hour window for free text.

## Every function of the portal

The SDK covers every function the developer portal publishes for an API key, the ones in [More functions](https://developers-portal.funnelchat.app/docs/mas-funciones/) included: numbers and their message queue, messages, templates and WhatsApp forms, groups and group actions, contacts, conversations and attending them, tags, custom fields and notes, automations, campaigns, scheduled sends and broadcasts, statistics, boards and tickets, quick replies, lead scoring, sales, custom domains, Meta's Conversions API and costs, your account and team, alerts and webhooks.

<!-- generated:functions — written by scripts/generate.py; do not edit by hand -->
**253 operations and 56 webhook events**, in the 30 groups of the portal (named as the portal names them):

- **[Primer uso](https://developers-portal.funnelchat.app/):** Mensajes.
- **[Funciones de WhatsApp](https://developers-portal.funnelchat.app/docs/mas-funciones/whatsapp/):** Números, Grupos, Atender una conversación, Cola de mensajes de un número, Acciones de grupo, Plantillas, Formularios, Conversions API, Costos y cuentas de Meta.
- **[Funciones de Funnelchat](https://developers-portal.funnelchat.app/docs/mas-funciones/funnelchat/):** Contactos, Conversaciones, Etiquetas, Campos personalizados, Automatizaciones, Campañas, Envíos programados, Estadísticas, Difusiones, Tableros, Tickets, Notas, Respuestas rápidas, Carpetas de flujos, Puntaje, Ventas, Dominios propios, Tu cuenta y tu equipo, Alertas, Webhooks.
<!-- /generated:functions -->

The resources ([The pieces](#the-pieces)) wrap the most used ones. Any of them is a call with [`request`](#any-route), or `paginate` for a list, by the method and path the portal shows:

```python
for broadcast in client.paginate("/api/v1/broadcasts", query={"perPage": 50}):
    print(broadcast["id"], broadcast["name"])

tickets = client.request("GET", "/api/v1/tickets")["data"]
```

`funnelchat.ROUTES` lists every operation with its group as the portal names it (`tag`), the category of the group as the portal shows it (`category`), its permission and its summary; `funnelchat.ROUTE_GROUPS` has the groups in the portal's order. An operation with `destructive=True` cannot be undone, such as deleting a number: **a script or an AI agent acting on its own should ask a person to confirm before calling it**. The docstring of such a method says so too. `destructive=None` means the spec does not say.

```python
from funnelchat import ROUTES

irreversible = [(r.method, r.path, r.summary) for r in ROUTES if r.destructive]
```

---

## Reference

### Client options

| Option | What it is | Default |
|---|---|---|
| `api_key` | Your key (`<id>\|fc_live_...`). | `FUNNELCHAT_API_KEY` |
| `environment` | `production` (`https://api.funnelchat.com`) or `staging`. | `production` |
| `base_url` | Another base URL, for example the [sandbox](#test-against-the-sandbox)'s; it wins over `environment`. | — |
| `timeout` | Maximum seconds of each attempt. | `30` |
| `max_retries` | Automatic retries (see [Retries](#retries)). `0` turns them off. | `2` |
| `default_headers` | Headers sent with every request. | — |
| `http_client` | Your own `httpx.Client` (proxies, transports); you close it. | one of its own |

Every request sends `Authorization: Bearer <key>`, `Accept: application/json` and `User-Agent: funnelchat-python/<version> python/<version>`. The key never shows up in `repr(client)` or in an error. `client.close()`, or `with Funnelchat() as client:`, closes the connections. The client is synchronous.

### The pieces

The same resources and methods as the [Node](https://github.com/Funnelchat20/funnelchat-node) and [PHP](https://github.com/Funnelchat20/funnelchat-php) SDKs, in snake_case. Path parameters go first, by position; the fields of the body or the query, by name.

| Resource | What it has |
|---|---|
| `client.devices` | Your WhatsApp numbers: `list` (filter by `external_reference`), `create` (a QR number), `qr`, `retrieve` (with `capabilities`), `update`, `delete`, `status`, `health`, `list_connection_history`. The `id` of a number is the `device_id` you send with. |
| `client.connect_links` | `create`, `get`, `list`, `revoke`: a page where you or your customer connect a number. |
| `client.messages` | `send_direct`, `send`, `send_form`, `send_contact_card`, `forward`, `get` (one message by id), `list` (the history of a contact), `react`, `remove_reaction`. |
| `client.templates` | `list`, `sync` (bring a number's templates from Meta), `create`, `retrieve`, `update`, `send`, `delete`. |
| `client.groups` | `list_by_device` (a number's live groups), `follow`, `send_message`, `retrieve_action`, `list`, `retrieve`, `metadata`, participants and their joins and leaves, scheduled messages and actions. |
| `client.webhooks` | Subscriptions (`create`, `list`, `retrieve`, `update`, `delete`, `test`, `list_deliveries`), the catalog (`events`), `verify` and `construct_event`. |
| `client.contacts` | `list`, `create`, `upsert`, `retrieve`, `update`, `delete`, tags, custom fields, `meta_window` (the 24-hour window), notes. |
| `client.conversations` | `list`, counters, mark everything as read or unread. |
| `client.forms` | WhatsApp forms: `list`, `templates`, `create`, `retrieve`, `update`, `delete`, `create_version`, `sync`, `publish`, numbers, `versions`, answers and `metrics`. |
| `client.tags` | `list`, `create`, `retrieve`, `update`, `delete`, `list_contacts`. |
| `client.custom_fields` | `list`, `create`, `retrieve`, `update`, `delete`. |

Every other function of the portal is a call with `request` or `paginate`: see [Every function of the portal](#every-function-of-the-portal). Each method's docstring says what it does, which permission it needs and, when it cannot be undone, that a person should confirm it first. An argument you leave out is not sent; `None` is sent as `null`. A field the SDK does not know yet goes in `extra_body` (or `extra_query`), and any header in `extra_headers`. Every method also takes `timeout` and `max_retries`.

### Permissions

A key has the permissions ticked when it was created. The panel groups them by area, with one checkbox per level; this README names each one as the panel shows it. **Send** includes **View** and **Edit**, and **Edit** includes **View**.

| To | You need |
|---|---|
| List numbers, read their status and connect links | **WhatsApp numbers → View** |
| Create numbers, show their QR, create and revoke connect links, delete numbers | **WhatsApp numbers → Create, connect and delete** |
| Send messages and templates | **Contacts and conversations → Send** |
| Read groups | **Groups and campaigns → View** |
| Send to a group | **Groups and campaigns → Send** (and **Manage groups** for one not in the account yet) |
| Follow a group | **Groups and campaigns → Manage groups** |
| Webhook subscriptions | **Notifications (webhooks) → View** to read, **Manage** for the rest, plus **View** of the area of each event |

Each key belongs to the workspace where it was created and only sees what is in it: anything of another workspace answers `404`. Every webhook event carries `data["workspace_id"]`, and a subscription only receives the events of its own workspace.

### Send a message

Every send answers right away with the registered message, `status` `queued`; what happens next arrives by `message.status_changed`, or is read with `messages.get()`.

- `send_direct(device_id=…, phone=…)` creates the contact when the phone is not one yet, as `contacts.upsert()` would. Instead of `phone`, `contact_id`; or, with an official number, `whatsapp_id`. With `phone` and `contact_id` they must be the same contact (`422 recipient_mismatch`).
- `messages.send(contact_id, device_id=…, phone=…, text=…)` writes to a contact you already have, checking that `phone` is that contact's.
- A file: `file` (its URL). When the URL does not end in a known extension (a signed URL), say what it is with `file_type` (`image`, `video`, `audio`, `document`, `sticker`) and, for a document, `file_name`.
- `client_reference` (1 to 64 visible ASCII characters) comes back in the history and in `message.status_changed`.

#### Templates

With an official number, an approved template is the only way to write to a contact after 24 hours. Send only the templates with `available` true (Meta pauses or disables the others):

```python
template = next(t for t in client.templates.list() if t["available"])
result = client.templates.send(device_id, str(template["id"]), phone="5491100000000", template_variables={"body": ["Lucía"]})
```

`template_variables["body"]` fills the body variables in order. A new phone becomes a contact, as with `send_direct`.

If a template created in Meta does not appear in `templates.list()`, bring it with `client.templates.sync(device_id)` and list again (in a few seconds when it answers `{"status": "in_progress"}`). Only official numbers; it needs **Contacts and conversations → Edit**.

#### When a send is stopped

A send that breaks a rule is neither sent nor stored: you get an error with its `code`.

| Error | What happened | What to do |
|---|---|---|
| `422 window_closed` | Free text with the window closed, on an official number. | Send an approved template. |
| `422 antiblock_duplicate_content` | The same content repeated to the same contact. | Change the text or wait. |
| `422 antiblock_unanswered_limit` | Too many messages in a row to someone who does not answer. | Wait until they answer. |
| `422 recipient_mismatch` | The `phone` or `whatsapp_id` is not the contact. | Use that contact's data. |
| `422 provider_unsupported` | The number cannot send that. | Check the `capabilities` of the number. |
| `422 device_unavailable` | The number is not connected. | Reconnect it. |
| `429 rate_limited` | You went over the pace of your number. It carries `retry_after`. | Wait those seconds and retry. |
| `429 mac_lockout_24h` | The 24-hour lockout after using up the monthly active contacts. | Waiting a few seconds does not fix it. |

`funnelchat.is_send_rule_error(error.code)` tells you whether the error is a rejected send; `SEND_ERROR_CODES` has all of them, with their HTTP status.

### Connect a number

```python
link = client.connect_links.create(
    type="qr",
    country="br",                                       # the country of the phone that will scan the QR
    external_reference="customer-81",                   # your own reference; it comes back in device.* webhooks
    return_url="https://your-app.example/whatsapp/done",
    expires_in_minutes=1440,                            # 30 to 10080; 24 hours by default
    idempotency_key="connect-customer-81",
)["data"]
```

- A link ends `completed` (with `device_id`), `failed` (with `error_code`), `expired` or `revoked`. `client.connect_links.list(status="pending")` lists the open ones and `revoke(link_id)` closes one. At most 20 are open (`429 too_many_open_links`).
- `device_id` reconnects a number you already have, without taking a new slot of the plan.
- `type="meta"` (an official WhatsApp Cloud number) answers `503 meta_connect_disabled` in production for now: official numbers are connected from the panel.
- Without a page: `client.devices.create(connection="qr")` creates a QR number and `client.devices.qr(device_id)["data"]` gives its QR as a PNG data URI (`qr_code`). Ask again every `expires_in` seconds and have it scanned right away: WhatsApp changes the code every few seconds.
- `idempotency_key` (both creates, 1 to 255 characters) is sent as `Idempotency-Key` and kept 24 hours: the same key with the same body answers the same link or number without creating another.
- The rejections of the plan's quota (`403 number_limit_reached`, `409 pending_number_exists`…) are in `NUMBER_ERROR_CODES`; `funnelchat.is_number_quota_error(error.code)` tells them apart.

### Groups

- `groups.list_by_device(device_id)` lists every group of the number, also those not in your account yet (for a key it is reused for a minute per number). `groups.list()` lists the groups already in the account.
- `groups.follow(uid, device_id=…)` is the panel's import: QR numbers only (`422 provider_unsupported` otherwise), with **Groups and campaigns → Manage groups** (`403 import_permission_required`), up to 5 groups per number per minute (`429 import_rate_limited`). `imported` is false when the group was already in the account.
- `groups.send_message(uid, device_id=…, type="text", text=…)` answers `{"action_id": …, "status": "queued"}` and the message goes out in the background; `groups.retrieve_action(action_id)["data"]` or the `group_action.completed` event say how it went. A file goes as `type="image"` (or `video`, `audio`, `document`) with its `https` `media_url`. A QR number must be admin of the group. Its rejections are in `GROUP_ACTION_ERROR_CODES`.

### Webhooks

```python
import funnelchat

event = funnelchat.webhooks.construct_event(raw_body, signature_header, secret)  # no client needed
ok = funnelchat.webhooks.verify(raw_body, signature_header, secret)              # True or False, never raises
```

- Verify over the **raw body**, exactly as it arrived (`bytes` or `str`): if you parse it and serialize it again, the signature changes.
- `construct_event` raises `WebhookVerificationError` with `reason`: `missing_secret`, `missing_header`, `malformed_header`, `timestamp_out_of_tolerance`, `signature_mismatch`, `invalid_body`, `invalid_json` or `invalid_event`. Answer `400`.
- Both reject a signature whose `t` is more than 300 seconds away from your clock; change it with `tolerance_seconds=600`.
- The algorithm is the portal's: `X-Funnelchat-Signature: t=<unix>,v1=<hex>`, where `v1` is the HMAC-SHA256, with the full secret, of `"<t>." + raw body`, compared in constant time. The tests use the portal's vectors.
- Deduplicate by `event["id"]`: a retry brings the same one. New event types can arrive before this SDK knows them: answer `2xx` to the ones you do not handle.
- `funnelchat.types.WebhookEvent` is the union of every event, discriminated by `type`: after `if event["type"] == "message.status_changed":`, your type checker knows the keys of `event["data"]`. `funnelchat.WEBHOOK_EVENTS` lists the types with their status (`live` or `planned`).
- To rotate the secret, use the panel: that route is not open to API keys.

### Pagination

`list…` methods return a `Page`. Iterating it walks every item of every page; `data` has the items of this page only:

```python
for contact in client.contacts.list(perPage=100, tag_ids=[12]):
    print(contact["id"])

page = client.tags.list(perPage=50)
print(page.data, page.request_id)
while page.has_next_page():
    page = page.get_next_page()
```

The SDK understands the three ways the API paginates: page numbers, cursors and lists that come whole. Query values are sent the way the API (Laravel) reads them: lists as `key[]=a&key[]=b`, booleans as `1` and `0`.

### Errors

Everything the SDK raises extends `FunnelchatError`. When the API answers with an error, it is an `APIError`:

| Attribute | What it is |
|---|---|
| `status` | The HTTP status. |
| `code` | The stable `error` of the body (`window_closed`, `rate_limited`, `route_not_available`…), or `None` (for example a validation `422`). |
| `message` | The `message` of the body, meant for people. Decide by `status` and `code`, not by `message`. |
| `request_id` | The `X-Request-Id` of the response. **Quote it when you report a problem.** |
| `retry_after` | The seconds of `Retry-After`, when present. |
| `errors` | In a validation `422`, the messages per field. |
| `body` | The full decoded body. |

Each status has its class: `BadRequestError` (400), `AuthenticationError` (401), `PermissionDeniedError` (403), `NotFoundError` (404), `ConflictError` (409), `UnsupportedMediaTypeError` (415), `UnprocessableEntityError` (422), `RateLimitError` (429) and `InternalServerError` (5xx). No response: `APIConnectionError`, and `APIConnectionTimeoutError` when it went over `timeout`.

```python
from funnelchat import APIError, RateLimitError

try:
    client.messages.send_direct(device_id=device_id, phone="5491100000000", text="Hi!")
except RateLimitError as error:
    print(f"Wait {error.retry_after} s")
except APIError as error:
    print(error.status, error.code, error.message, error.request_id)
```

`ACCESS_ERROR_CODES` has the errors of the API entry that apply to any route (`401 unauthenticated`, `403 permission_denied`, `403 route_not_available`, `429 daily_cap_exceeded`, `502 origin_unreachable`, `503 gate_unavailable`…). The `X-Request-Id` of a successful call is in `client.last_response.request_id`, and of each page in `page.request_id`.

### Retries

- Reads and writes that give the same result when repeated (`GET`, `PUT`, `DELETE`) are retried on a `429`, a `5xx` or a network error (also a timeout), up to `max_retries` times (2 by default).
- Other writes (`POST`, `PATCH`) are retried **only when the API guarantees they were not applied**: `429` and `503`. After a `500`, `502` or `504`, a timeout or a dropped connection the error is raised right away: read the state before repeating it. A create with `idempotency_key` is retried like a `PUT`, since the API answers the same resource to the same key.
- **A send is never retried automatically**: the `POST`s that need a **Send** permission (messages, templates, forms, cards, forwards and messages to a group), key or no key. If a `429 rate_limited` sent nothing and you want the SDK to retry for you, pass `retry_send=True` in that call: it then follows the rule of writes.
- `429 mac_lockout_24h`, `mac_limit_reached`, `too_many_pending_actions`, `too_many_open_links` and `503 meta_connect_disabled` are never retried.
- With `Retry-After`, the wait is exactly what it asks for; if it asks for more than 60 seconds, the error is raised right away with its `retry_after`. Without it, the wait is exponential: 0.5 s, 1 s, 2 s… up to 8 s, with some jitter.

### Any route

```python
contact = client.request("GET", "/api/v1/contacts/{contact}", path_params={"contact": 2001})
for broadcast in client.paginate("/api/v1/broadcasts"):
    print(broadcast)
```

`request` takes `path_params`, `query`, `body`, `headers`, `timeout`, `max_retries`, `retry_send` and `idempotency_key`, follows the same retry rules and returns the decoded body. It calls any route: every function of the portal without a method, or one the spec adds after this version of the SDK. `funnelchat.ROUTES` lists every operation the spec publishes, with its area, its permission, its group and category in the portal and whether it can be undone (`destructive`); `funnelchat.ROUTE_GROUPS` has the groups of the portal.

### Test against the sandbox

The sandbox imitates the API on your machine: sends with their status cycle, signed webhooks and the WhatsApp rules, without a real account. Start it with `npx @funnelchat-hq/sandbox` and point the client at it:

```python
client = Funnelchat(api_key="1|fc_live_sandbox", base_url="http://localhost:4010")
```

### Types

`funnelchat.types` has a TypedDict for the response of each method (`MessagesSendDirectResponse`, `PublicMessageResource`, `DeviceResource`…), for the schemas they use and for every webhook event (`MessageStatusChangedEvent`, `MessageReceivedEvent`…). At runtime they are plain dicts. The package ships `py.typed`.

### Pending of the spec

The types come from the spec the developer portal publishes (`spec/funnelchat.json`; where it came from, its URL, the portal's version and its `sha256`, in `spec/procedencia.json`). Where production answers otherwise than that spec says, or the spec shows an event only by an example or without one, a separate layer corrects it: `spec/pending.json`, kept in [funnelchat-node](https://github.com/Funnelchat20/funnelchat-node) and copied here unchanged, so both SDKs apply the same corrections. Generation applies each entry **only while the spec still says exactly what the entry corrects**, and each entry cites the production release it was read in:

- what a send answers (`{"message": …}`, never `null`), the body of `devices.qr`, the items of `templates.list`, and the answers of `webhooks.update` and `groups.retrieve_action`;
- the `data` of the events the spec shows only by an example, or without one, such as the `device.*` events, `message.received`, `message.status_changed` and the group events (`group.message_received` and `group.reaction_added` carry `message["uid"]`, as production sends them and the published example shows).

The layer never adds an operation or an event the portal does not publish. The `workspace_id` of every event, which is not OpenAPI, is added by the generator (`PENDING_COMMON_EVENT_DATA` in `scripts/generate.py`), as `Optional[int]` even where an example shows a number. The generator also corrects two fields of events that the spec and the layer type otherwise than production sends them (`PENDING_EVENT_FIELDS`), only while they still say it, and lists the ones a new spec made unnecessary: the `label` of each answer of `whatsapp_form.completed` is always a string (a question without a label sends its name), and `message["type"]` of `message.received` is one of the types the spec lists or any other string, since WhatsApp brings new kinds of message.

### Upgrading from 0.4

0.5.0 changes nothing at runtime, but two types of the events change, so a type checker may ask for a change:

- `message["type"]` of `message.received` is one of the types the spec lists or any other `str`: WhatsApp brings new kinds of message before the SDK lists them. Handle one you do not know instead of matching every known type exhaustively.
- The `label` of each answer of `whatsapp_form.completed` is `str`, never `None`.

### Upgrading from 0.1

0.4.0 types only what the portal publishes for an API key, and takes the version of the Node and PHP SDKs, which cover the same functions. Routes the portal does not publish are closed to keys in production, so these methods are gone:

- `devices.me` and `devices.check_phone`;
- `templates.quick_reply_buttons`;
- `groups.list_messages` (sending to a group, `groups.send_message`, stays);
- `conversations.update`;
- `webhooks.rotate_secret` (rotate the secret from the panel).

`funnelchat.ROUTES` no longer has the other routes the portal does not publish: the panel's webhook endpoints (`/api/v1/webhooks/endpoints…`; the subscriptions of a key are `/api/v1/webhooks`), `POST /api/v1/lead-score/events`, the logs of numbers (`/api/v1/devices/logs` and `/api/v1/devices/{device}/logs…`), `POST /api/v1/devices/{device}/extension-token`, the disconnect survey, the chats and open conversations of a number, the `update-webhook-received…` routes of a number, `GET /api/v1/stats/countries`, the participants and webhooks of a campaign, `GET /api/v1/flows/{flow}/active-contacts-list`, and creating, editing, verifying, testing and deleting an alert destination (`/api/v1/alerts/destinations…`; the rest of `/api/v1/alerts` is published). `WEBHOOK_EVENTS` and `WebhookEventType` no longer have the events the portal does not publish: `ai_quota.low_balance`, `ai_quota.topup_succeeded`, `ai_quota.topup_failed`, `billing.plan_blocked` and `subscription.expiring`. `Route` gains `category`, `tag`, `summary` and `destructive` (before `pending`), so unpack it by name, not by position.

### Development

```bash
python -m venv .venv && .venv/bin/pip install -e . pytest
.venv/bin/python scripts/generate.py --check   # the generated files and the README blocks are up to date with spec/
.venv/bin/python -m pytest                     # no network and no keys: a mocked transport
python -m build                                # or: uv build
```

Every pull request and every push to `main` runs these three checks on each Python the SDK supports, 3.9 to 3.14 (`.github/workflows/ci.yml`).

Everything generated comes from one script, standard library only. The spec in `spec/` was imported with these two commands, which the generator writes with the portal's version that `spec/procedencia.json` records (for a newer spec, the version the portal shows):

<!-- generated:import — written by scripts/generate.py from spec/procedencia.json; do not edit by hand -->
```bash
curl -fsSo /tmp/funnelchat.json https://developers-portal.funnelchat.app/specs/funnelchat.json
python scripts/generate.py --spec /tmp/funnelchat.json --source url=https://developers-portal.funnelchat.app/specs/funnelchat.json --source portal_version=v0.6.14
```
<!-- /generated:import -->

```bash
python scripts/generate.py --pending <funnelchat-node>/spec/pending.json   # the pending layer, from funnelchat-node
python scripts/generate.py                                                 # again from spec/, for example after editing spec/resources.json
```

1. With `--spec`, it copies the spec to `spec/funnelchat.json` and writes `spec/procedencia.json`: where it came from and the `sha256` of the file. Generate only from the spec the portal publishes (`/specs/funnelchat.json`): it carries every function an API key can use, and nothing closed to keys (the portal's full unified spec also has internal routes and routes closed to keys). For a downloaded file, say on the command line where it came from (`--source url=…`) and the version of the portal that published it (`--source portal_version=…`); `--expect-sha256 <hex>` refuses a file whose `sha256` is not the one announced. From a checkout of a repository, its repository, branch and commit are read from git (`--source key=value` and `--domain <area>=<sha>@<branch>@<snapshot_at>` declare what git cannot say; those fields are marked as declared). With `--pending`, it copies the layer and records its checkout, commit and `sha256`.
2. It applies `spec/pending.json` with the same rules as funnelchat-node: only while the spec still says what an entry corrects, never adding an operation or an event the spec does not publish. It lists the entries a new spec made unnecessary, and those it does not publish, so they can be deleted (in funnelchat-node).
3. It writes `src/funnelchat/_routes.py` (every operation, with area, permission, group, category and whether it can be undone, and the groups of the portal: the SDK reads it to know which requests are sends), `src/funnelchat/types.py`, `src/funnelchat/resources.py` (each method of `spec/resources.json`, with its parameters and response from the spec) and two blocks of this README: [Every function of the portal](#every-function-of-the-portal) and the commands that import the spec. The category of each group comes from the spec: `x-fc-categoria` on its `x-tagGroups` entry, named and linked as `x-fc-categorias` lists it.

**Regenerating never needs anything edited by hand.** A new operation of the spec is in `funnelchat.ROUTES`, called with `request` or `paginate`. A method of `spec/resources.json` whose operation the spec no longer publishes is left out of the SDK, and the generation says which one, so it can be deleted from there.

```
spec/                  the spec, the pending layer, their provenance and resources.json (the methods)
scripts/generate.py    the generator
src/funnelchat/        the package; _routes.py, types.py and resources.py are generated
tests/                 pytest, with httpx.MockTransport
```

To release, push a `vX.Y.Z` tag on a commit of `main`, matching `src/funnelchat/_version.py`. GitHub Actions runs the same checks and publishes it to PyPI with Trusted Publishing (`.github/workflows/publish.yml`); a tag whose commit is not on `main`, or that does not match the version, fails before publishing. A pre-release is `vX.Y.Z-rc.N` (or `-beta.N`, `-alpha.N`) with that same version in `_version.py`: PyPI takes it as a pre-release, which `pip install funnelchat` does not install unless asked (`pip install --pre funnelchat`).

## License

[MIT](LICENSE)

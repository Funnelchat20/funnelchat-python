"""GENERATED FILE — do not edit. Run `python scripts/generate.py`.

Source: spec/funnelchat.json (sha256 3e5bc8ef01a2c746…) + spec/pending.json + spec/resources.json.

The resources of the client: one class per piece of the API, from spec/resources.json.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, Union, cast

from ._resource import NOT_GIVEN, NotGiven, Resource
from .webhooks import WebhookHelpers

if TYPE_CHECKING:
    from ._client import Funnelchat
    from ._pagination import Page
    from .types import (
        ActionGroupResource,
        ApiGroupActionAcceptedResource,
        ChannelMetadataResource,
        ConnectLinkResource,
        ConnectLinksCreateResponse,
        ConnectLinksGetResponse,
        ContactCustomFieldResource,
        ContactNoteResource,
        ContactResource,
        ContactTagResource,
        ContactsAttachCustomFieldBodyItem,
        ContactsAttachCustomFieldResponseItem,
        ContactsAttachCustomFieldResponseItemVariant2,
        ContactsAttachCustomFieldResponseItemVariant3,
        ContactsAttachCustomFieldResponseItemVariant4,
        ContactsDeleteBodyCustomFieldFiltersItem,
        ContactsDeleteBodyTagFiltersItem,
        ContactsDetachCustomFieldBodyItem,
        ContactsDetachCustomFieldResponse,
        ContactsListQueryCustomFieldFiltersItem,
        ContactsListQueryTagFiltersItem,
        ContactsMetaWindowResponse,
        ContactsMetaWindowResponseVariant2,
        ContactsMetaWindowResponseVariant3,
        ConversationsCountAllResponse,
        ConversationsCountClosedResponse,
        ConversationsCountOpenResponse,
        ConversationsCountUnreadResponse,
        ConversationsCountUnreadResponseVariant2,
        ConversationsMarkAllReadResponse,
        ConversationsMarkAllUnreadResponse,
        CustomFieldResource,
        DeviceConnectionEventResource,
        DeviceHealthDetailResource,
        DeviceResource,
        DevicesCreateResponse,
        DevicesQrResponse,
        FormsAddNumberResponse,
        FormsCreateResponse,
        FormsDefinitionResponse,
        FormsDefinitionResponseVariant2,
        FormsMetricsResponse,
        FormsNumbersResponse,
        FormsPublishResponse,
        FormsRemoveNumberResponse,
        FormsRetrieveResponse,
        FormsRetrieveResponseResponse,
        FormsRetryNumbersResponse,
        FormsSyncResponse,
        FormsTemplatesResponse,
        FormsUpdateResponse,
        FormsVersionsResponse,
        ForwardMessageRequestTargetsItem2,
        GroupMetadataResource,
        GroupMinResource,
        GroupResource,
        GroupsFollowResponse,
        GroupsRetrieveActionResponse,
        MessageResource,
        MessagesForwardResponseItem,
        MessagesSendContactCardResponse,
        MessagesSendDirectResponse,
        MessagesSendFormResponse,
        MessagesSendResponse,
        ParticipantEventResource,
        ParticipantResource,
        PublicMessageResource,
        SaveWhatsappFormRequestDefinition2,
        ScheduledMessageResource,
        SendMessageRequestLinkPreviewMeta2,
        SendMessageRequestOptionsItem2,
        StoreContactRequestCustomFieldsItem2,
        StoreMessageTemplateRequestButtonsItem2,
        StoreWebhookSubscriptionRequestFilters2,
        TagResource,
        TemplateResource,
        TemplatesSendBodyTemplateVariables,
        TemplatesSendResponse,
        TemplatesSyncResponse,
        UpdateMessageTemplateRequestButtonsItem2,
        UpdateOrCreateContactRequestCustomFieldsItem2,
        UpdateWebhookSubscriptionRequestFilters2,
        WebhookSubscriptionCreatedResource,
        WebhookSubscriptionDeliveryResource,
        WebhookSubscriptionResource,
        WebhooksEventsResponse,
        WebhooksListResponseVariant2,
        WebhooksTestResponse,
        WhatsappFormResource,
    )

__all__ = [
    "Contacts",
    "Conversations",
    "Messages",
    "Templates",
    "Forms",
    "Tags",
    "CustomFields",
    "Groups",
    "Devices",
    "ConnectLinks",
    "Webhooks",
    "ClientResources",
]


class Contacts(Resource):
    """Contacts (conversations area): search, create, update, custom fields, notes and the 24-hour
    window.
    """

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven = NOT_GIVEN,
        whatsapp_id: str | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        image: str | NotGiven = NOT_GIVEN,
        created_at: str | NotGiven = NOT_GIVEN,
        created_from: str | NotGiven = NOT_GIVEN,
        created_to: str | NotGiven = NOT_GIVEN,
        tag_ids: List[int] | NotGiven = NOT_GIVEN,
        tag_mode: Literal["all", "any", "exclude"] | NotGiven = NOT_GIVEN,
        custom_field_ids: List[int] | NotGiven = NOT_GIVEN,
        custom_field_mode: Literal["all", "any", "exclude"] | NotGiven = NOT_GIVEN,
        custom_field_value: str | NotGiven = NOT_GIVEN,
        custom_field_date_from: str | NotGiven = NOT_GIVEN,
        custom_field_date_to: str | NotGiven = NOT_GIVEN,
        custom_field_numeric_operator: Literal["lt", "eq", "gt"] | NotGiven = NOT_GIVEN,
        custom_field_numeric_value: float | NotGiven = NOT_GIVEN,
        only_with_phone: str | NotGiven = NOT_GIVEN,
        only_with_mac: str | NotGiven = NOT_GIVEN,
        only_paused: str | NotGiven = NOT_GIVEN,
        scopeToAdvisor: str | NotGiven = NOT_GIVEN,
        lead_score_categories: Literal["insufficient_data", "hot", "warm", "cold"] | NotGiven = NOT_GIVEN,
        lead_score_min: int | NotGiven = NOT_GIVEN,
        lead_score_max: int | NotGiven = NOT_GIVEN,
        lead_score_disqualified: Optional[Literal["include", "exclude", "only"]] | NotGiven = NOT_GIVEN,
        tag_filters: List[ContactsListQueryTagFiltersItem] | NotGiven = NOT_GIVEN,
        custom_field_filters: List[ContactsListQueryCustomFieldFiltersItem] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["id", "name", "email", "phone", "status", "favorite", "unread_messages", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ContactResource]:
        """`GET /api/v1/contacts`, paginated. Filter by `phone` without the `+`.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/contacts",
            query={
                "name": name,
                "email": email,
                "phone": phone,
                "whatsapp_id": whatsapp_id,
                "country_codes": country_codes,
                "status": status,
                "image": image,
                "created_at": created_at,
                "created_from": created_from,
                "created_to": created_to,
                "tag_ids": tag_ids,
                "tag_mode": tag_mode,
                "custom_field_ids": custom_field_ids,
                "custom_field_mode": custom_field_mode,
                "custom_field_value": custom_field_value,
                "custom_field_date_from": custom_field_date_from,
                "custom_field_date_to": custom_field_date_to,
                "custom_field_numeric_operator": custom_field_numeric_operator,
                "custom_field_numeric_value": custom_field_numeric_value,
                "only_with_phone": only_with_phone,
                "only_with_mac": only_with_mac,
                "only_paused": only_paused,
                "scopeToAdvisor": scopeToAdvisor,
                "lead_score_categories": lead_score_categories,
                "lead_score_min": lead_score_min,
                "lead_score_max": lead_score_max,
                "lead_score_disqualified": lead_score_disqualified,
                "tag_filters": tag_filters,
                "custom_field_filters": custom_field_filters,
                "perPage": perPage,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def create(
        self,
        *,
        phone: str | NotGiven = NOT_GIVEN,
        whatsapp_id: str | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        image: Optional[str] | NotGiven = NOT_GIVEN,
        deviceId: Optional[int] | NotGiven = NOT_GIVEN,
        custom_fields: List[StoreContactRequestCustomFieldsItem2] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ContactResource:
        """`POST /api/v1/contacts`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ContactResource", self._request(
            "POST",
            "/api/v1/contacts",
            body={
                "phone": phone,
                "whatsapp_id": whatsapp_id,
                "name": name,
                "email": email,
                "image": image,
                "deviceId": deviceId,
                "custom_fields": custom_fields,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def upsert(
        self,
        *,
        phone: str,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        custom_fields: List[UpdateOrCreateContactRequestCustomFieldsItem2] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ContactResource:
        """`POST /api/v1/contacts/update-or-create`: creates the contact or updates the one with that
        phone.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ContactResource", self._request(
            "POST",
            "/api/v1/contacts/update-or-create",
            body={"phone": phone, "name": name, "email": email, "custom_fields": custom_fields},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        contact: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Any:
        """`GET /api/v1/contacts/{contact}`.

        Permission: **Contacts and conversations → View**.
        """
        return self._request(
            "GET",
            "/api/v1/contacts/{contact}",
            path_params={"contact": contact},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def update(
        self,
        contact: int,
        /,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        email: Optional[str] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        notes: Optional[str] | NotGiven = NOT_GIVEN,
        status: int | NotGiven = NOT_GIVEN,
        adviser_id: Optional[int] | NotGiven = NOT_GIVEN,
        active_conversation: bool | NotGiven = NOT_GIVEN,
        favorite: bool | NotGiven = NOT_GIVEN,
        fixed: bool | NotGiven = NOT_GIVEN,
        image: Optional[str] | NotGiven = NOT_GIVEN,
        can_execute_flows: bool | NotGiven = NOT_GIVEN,
        manually_unread: bool | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """`PUT /api/v1/contacts/{contact}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("Dict[str, Any]", self._request(
            "PUT",
            "/api/v1/contacts/{contact}",
            path_params={"contact": contact},
            body={
                "name": name,
                "email": email,
                "phone": phone,
                "notes": notes,
                "status": status,
                "adviser_id": adviser_id,
                "active_conversation": active_conversation,
                "favorite": favorite,
                "fixed": fixed,
                "image": image,
                "can_execute_flows": can_execute_flows,
                "manually_unread": manually_unread,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        *,
        all: bool | NotGiven = NOT_GIVEN,
        contactIds: List[int] | NotGiven = NOT_GIVEN,
        created_from: Optional[str] | NotGiven = NOT_GIVEN,
        created_to: Optional[str] | NotGiven = NOT_GIVEN,
        tag_mode: Optional[Literal["all", "any", "exclude"]] | NotGiven = NOT_GIVEN,
        tag_ids: Optional[List[int]] | NotGiven = NOT_GIVEN,
        tag_filters: Optional[List[ContactsDeleteBodyTagFiltersItem]] | NotGiven = NOT_GIVEN,
        custom_field_mode: Optional[Literal["all", "any", "exclude"]] | NotGiven = NOT_GIVEN,
        custom_field_ids: Optional[List[int]] | NotGiven = NOT_GIVEN,
        custom_field_value: Optional[str] | NotGiven = NOT_GIVEN,
        custom_field_date_from: Optional[str] | NotGiven = NOT_GIVEN,
        custom_field_date_to: Optional[str] | NotGiven = NOT_GIVEN,
        custom_field_numeric_operator: Optional[Literal["lt", "eq", "gt"]] | NotGiven = NOT_GIVEN,
        custom_field_numeric_value: Optional[float] | NotGiven = NOT_GIVEN,
        custom_field_filters: Optional[List[ContactsDeleteBodyCustomFieldFiltersItem]] | NotGiven = NOT_GIVEN,
        country_codes: List[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`POST /api/v1/contacts/delete`: deletes the contacts of the body (`contactIds`, or a
        filter).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("None", self._request(
            "POST",
            "/api/v1/contacts/delete",
            body={
                "all": all,
                "contactIds": contactIds,
                "created_from": created_from,
                "created_to": created_to,
                "tag_mode": tag_mode,
                "tag_ids": tag_ids,
                "tag_filters": tag_filters,
                "custom_field_mode": custom_field_mode,
                "custom_field_ids": custom_field_ids,
                "custom_field_value": custom_field_value,
                "custom_field_date_from": custom_field_date_from,
                "custom_field_date_to": custom_field_date_to,
                "custom_field_numeric_operator": custom_field_numeric_operator,
                "custom_field_numeric_value": custom_field_numeric_value,
                "custom_field_filters": custom_field_filters,
                "country_codes": country_codes,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_tags(
        self,
        contact: int,
        /,
        *,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ContactTagResource]:
        """`GET /api/v1/contacts/{contact}/tags`, paginated.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/contacts/{contact}/tags",
            path_params={"contact": contact},
            query={"perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def list_custom_fields(
        self,
        contact: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ContactCustomFieldResource]:
        """`GET /api/v1/contacts/{contact}/custom-fields`, paginated.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/contacts/{contact}/custom-fields",
            path_params={"contact": contact},
            query={"name": name, "perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def attach_custom_field(
        self,
        body: List[ContactsAttachCustomFieldBodyItem] | None = None,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> List[Union[ContactsAttachCustomFieldResponseItem, ContactsAttachCustomFieldResponseItemVariant2, ContactsAttachCustomFieldResponseItemVariant3, ContactsAttachCustomFieldResponseItemVariant4]]:
        """`POST /api/v1/contacts/attach-custom-field`: sets a custom field on contacts.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("List[Union[ContactsAttachCustomFieldResponseItem, ContactsAttachCustomFieldResponseItemVariant2, ContactsAttachCustomFieldResponseItemVariant3, ContactsAttachCustomFieldResponseItemVariant4]]", self._request(
            "POST",
            "/api/v1/contacts/attach-custom-field",
            body=body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def detach_custom_field(
        self,
        body: List[ContactsDetachCustomFieldBodyItem] | None = None,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ContactsDetachCustomFieldResponse:
        """`POST /api/v1/contacts/detach-custom-field`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ContactsDetachCustomFieldResponse", self._request(
            "POST",
            "/api/v1/contacts/detach-custom-field",
            body=body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def meta_window(
        self,
        contact: int,
        /,
        *,
        device_id: int,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Union[ContactsMetaWindowResponse, ContactsMetaWindowResponseVariant2, ContactsMetaWindowResponseVariant3]:
        """`GET /api/v1/contacts/{contact}/meta-window`: whether the 24-hour window with the contact is
        open on a WhatsApp Cloud number (`is_open`). Outside it, only templates can be sent.

        Permission: **Contacts and conversations → View**.
        """
        return cast("Union[ContactsMetaWindowResponse, ContactsMetaWindowResponseVariant2, ContactsMetaWindowResponseVariant3]", self._request(
            "GET",
            "/api/v1/contacts/{contact}/meta-window",
            path_params={"contact": contact},
            query={"device_id": device_id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_by_device(
        self,
        device: int,
        /,
        *,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ContactResource]:
        """`GET /api/v1/devices/{device}/contacts`, paginated: the contacts of one number.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/devices/{device}/contacts",
            path_params={"device": device},
            query={"perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def list_notes(
        self,
        contact: int,
        /,
        *,
        search: Optional[str] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ContactNoteResource]:
        """`GET /api/v1/contacts/{contact}/notes`, paginated.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/contacts/{contact}/notes",
            path_params={"contact": contact},
            query={"search": search, "perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def create_note(
        self,
        contact: int,
        /,
        *,
        body: str,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ContactNoteResource:
        """`POST /api/v1/contacts/{contact}/notes`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ContactNoteResource", self._request(
            "POST",
            "/api/v1/contacts/{contact}/notes",
            path_params={"contact": contact},
            body={"body": body},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete_note(
        self,
        contact: int,
        note: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`DELETE /api/v1/contacts/{contact}/notes/{note}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("None", self._request(
            "DELETE",
            "/api/v1/contacts/{contact}/notes/{note}",
            path_params={"contact": contact, "note": note},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Conversations(Resource):
    """Conversations (conversations area): the inbox, its counters, and marking everything as read or
    unread.
    """

    def list(
        self,
        *,
        perName: str | NotGiven = NOT_GIVEN,
        contactId: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        updated_since: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownContacts: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        deviceId: int | NotGiven = NOT_GIVEN,
        advisorId: int | NotGiven = NOT_GIVEN,
        advisorIds: str | NotGiven = NOT_GIVEN,
        activeConversation: bool | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        kanbanSettingId: int | NotGiven = NOT_GIVEN,
        kanbanStageIds: str | NotGiven = NOT_GIVEN,
        unreadMessages: bool | NotGiven = NOT_GIVEN,
        awaitingReply: bool | NotGiven = NOT_GIVEN,
        onlyWithMac: bool | NotGiven = NOT_GIVEN,
        paused: Literal["true", "false", "1", "0"] | NotGiven = NOT_GIVEN,
        leadScoreCategories: Optional[str] | NotGiven = NOT_GIVEN,
        leadScoreMin: int | NotGiven = NOT_GIVEN,
        leadScoreMax: int | NotGiven = NOT_GIVEN,
        leadScoreDisqualified: Optional[Literal["include", "exclude", "only"]] | NotGiven = NOT_GIVEN,
        metaWindowOpen: bool | NotGiven = NOT_GIVEN,
        metaWindowDeviceIds: Optional[str] | NotGiven = NOT_GIVEN,
        lastMessageDateFrom: Optional[str] | NotGiven = NOT_GIVEN,
        lastMessageDateTo: Optional[str] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        customFieldFilters: Optional[str] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[Dict[str, Any]]:
        """`GET /api/v1/conversations`, paginated by cursor.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/conversations",
            query={
                "perName": perName,
                "contactId": contactId,
                "cursor": cursor,
                "updated_since": updated_since,
                "favorites": favorites,
                "ownContacts": ownContacts,
                "ownAndUnassigned": ownAndUnassigned,
                "deviceId": deviceId,
                "advisorId": advisorId,
                "advisorIds": advisorIds,
                "activeConversation": activeConversation,
                "tags": tags,
                "kanbanSettingId": kanbanSettingId,
                "kanbanStageIds": kanbanStageIds,
                "unreadMessages": unreadMessages,
                "awaitingReply": awaitingReply,
                "onlyWithMac": onlyWithMac,
                "paused": paused,
                "leadScoreCategories": leadScoreCategories,
                "leadScoreMin": leadScoreMin,
                "leadScoreMax": leadScoreMax,
                "leadScoreDisqualified": leadScoreDisqualified,
                "metaWindowOpen": metaWindowOpen,
                "metaWindowDeviceIds": metaWindowDeviceIds,
                "lastMessageDateFrom": lastMessageDateFrom,
                "lastMessageDateTo": lastMessageDateTo,
                "timezone": timezone,
                "customFieldFilters": customFieldFilters,
                "perPage": perPage,
                "orderBy": orderBy,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def count_unread(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        withMine: bool | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Union[ConversationsCountUnreadResponse, ConversationsCountUnreadResponseVariant2]:
        """`GET /api/v1/conversations/count/unread`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("Union[ConversationsCountUnreadResponse, ConversationsCountUnreadResponseVariant2]", self._request(
            "GET",
            "/api/v1/conversations/count/unread",
            query={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
                "withMine": withMine,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def count_open(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConversationsCountOpenResponse:
        """`GET /api/v1/conversations/count/open`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("ConversationsCountOpenResponse", self._request(
            "GET",
            "/api/v1/conversations/count/open",
            query={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def count_closed(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConversationsCountClosedResponse:
        """`GET /api/v1/conversations/count/closed`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("ConversationsCountClosedResponse", self._request(
            "GET",
            "/api/v1/conversations/count/closed",
            query={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def count_all(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConversationsCountAllResponse:
        """`GET /api/v1/conversations/count/all`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("ConversationsCountAllResponse", self._request(
            "GET",
            "/api/v1/conversations/count/all",
            query={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def mark_all_read(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConversationsMarkAllReadResponse:
        """`POST /api/v1/conversations/mark-all-read`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ConversationsMarkAllReadResponse", self._request(
            "POST",
            "/api/v1/conversations/mark-all-read",
            body={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def mark_all_unread(
        self,
        *,
        advisorIds: str | NotGiven = NOT_GIVEN,
        favorites: bool | NotGiven = NOT_GIVEN,
        ownAndUnassigned: bool | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConversationsMarkAllUnreadResponse:
        """`POST /api/v1/conversations/mark-all-unread`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("ConversationsMarkAllUnreadResponse", self._request(
            "POST",
            "/api/v1/conversations/mark-all-unread",
            body={
                "advisorIds": advisorIds,
                "favorites": favorites,
                "ownAndUnassigned": ownAndUnassigned,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Messages(Resource):
    """Messages to one contact (conversations area): send text, files, buttons and forms, read the
    history or one message by id, forward, react.

    Every send answers right away with the registered message, `status` `queued`: accepted is not
    delivered. The rest arrives by `message.status_changed` (its `message_id` is the `id` of the
    message) or with `get()`. Sending with an API key needs **Contacts and conversations → Send**
    and follows the WhatsApp rules: `422 window_closed`, `422 antiblock_*`, `422 recipient_*`, `422
    provider_unsupported`, `429 rate_limited` (with `retry_after`) and `429 mac_lockout_24h`. A
    rejected send stores nothing (see `SEND_ERROR_CODES`). A send is never retried automatically
    unless you pass `retry_send=True`.
    """

    def send(
        self,
        contact: int,
        /,
        *,
        device_id: int,
        phone: str | NotGiven = NOT_GIVEN,
        whatsapp_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        contact_id: int | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        file_type: Optional[Literal["image", "video", "audio", "document", "sticker"]] | NotGiven = NOT_GIVEN,
        file_name: Optional[str] | NotGiven = NOT_GIVEN,
        temporal_uuid: str | NotGiven = NOT_GIVEN,
        note: bool | NotGiven = NOT_GIVEN,
        mentions: Optional[List[int]] | NotGiven = NOT_GIVEN,
        options: List[SendMessageRequestOptionsItem2] | NotGiven = NOT_GIVEN,
        reference_message_uid: Optional[str] | NotGiven = NOT_GIVEN,
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        link_preview: bool | NotGiven = NOT_GIVEN,
        link_preview_meta: SendMessageRequestLinkPreviewMeta2 | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> MessagesSendResponse:
        """`POST /api/v1/contacts/{contact}/message`: text, a file (`file`, a URL) or buttons and lists
        (`options`) to a contact. Returns `{"message": ...}`: the registered message, with its `id`
        and `status` `queued`.

        Send `phone` (or `whatsapp_id`) of the same contact: the API checks it (`422
        recipient_mismatch`). `contact_id` defaults to the contact of the route. A file from a URL
        without a known extension (a signed URL) needs `file_type` (`image`, `video`, `audio`,
        `document`, `sticker`), and a document `file_name`; an unsupported extension without
        `file_type` is a `415`. `client_reference` (1 to 64 visible ASCII characters) comes back in
        the history and in `message.status_changed`.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("MessagesSendResponse", self._request(
            "POST",
            "/api/v1/contacts/{contact}/message",
            path_params={"contact": contact},
            body={
                "phone": phone,
                "whatsapp_id": whatsapp_id,
                "device_id": device_id,
                "text": text,
                "contact_id": contact if contact_id is NOT_GIVEN else contact_id,
                "file": file,
                "file_type": file_type,
                "file_name": file_name,
                "temporal_uuid": temporal_uuid,
                "note": note,
                "mentions": mentions,
                "options": options,
                "reference_message_uid": reference_message_uid,
                "client_reference": client_reference,
                "link_preview": link_preview,
                "link_preview_meta": link_preview_meta,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def send_direct(
        self,
        *,
        device_id: int,
        text: str | NotGiven = NOT_GIVEN,
        contact_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        whatsapp_id: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        file_type: Optional[Literal["image", "video", "audio", "document", "sticker"]] | NotGiven = NOT_GIVEN,
        file_name: Optional[str] | NotGiven = NOT_GIVEN,
        temporal_uuid: str | NotGiven = NOT_GIVEN,
        local_id: Optional[str] | NotGiven = NOT_GIVEN,
        note: bool | NotGiven = NOT_GIVEN,
        mentions: Optional[List[int]] | NotGiven = NOT_GIVEN,
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> MessagesSendDirectResponse:
        """`POST /api/v1/message/send-message`: a send straight to a phone, in one call: `device_id`,
        `phone` (with country code, digits only) and the text or file. If the phone is not a contact
        yet, it is created in the workspace of your key (as `contacts.upsert()` would), and it stays
        created even if a WhatsApp rule then stops the send. Returns `{"message": ...}`, with the
        contact in `message["contact_id"]`.

        Instead of `phone`: `contact_id`, or `whatsapp_id` (Meta's id of the person, official
        numbers only). With `phone` and `contact_id`, they must be the same contact (`422
        recipient_mismatch`); a phone of a contact of another workspace answers `404`. It is a send:
        same rules as `send()`.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("MessagesSendDirectResponse", self._request(
            "POST",
            "/api/v1/message/send-message",
            body={
                "device_id": device_id,
                "text": text,
                "contact_id": contact_id,
                "phone": phone,
                "whatsapp_id": whatsapp_id,
                "file": file,
                "file_type": file_type,
                "file_name": file_name,
                "temporal_uuid": temporal_uuid,
                "local_id": local_id,
                "note": note,
                "mentions": mentions,
                "client_reference": client_reference,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def send_form(
        self,
        contact: int,
        /,
        *,
        form_id: int,
        device_id: int,
        text: str | NotGiven = NOT_GIVEN,
        button_text: str | NotGiven = NOT_GIVEN,
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> MessagesSendFormResponse:
        """`POST /api/v1/contacts/{contact}/message/form`: sends a published WhatsApp form (`form_id`
        is the form's `family_id`). Returns `{"message": ...}` with `type` `whatsapp_form`; the
        answers arrive by `whatsapp_form.completed`. It is a send: same rules as `send()`.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("MessagesSendFormResponse", self._request(
            "POST",
            "/api/v1/contacts/{contact}/message/form",
            path_params={"contact": contact},
            body={
                "form_id": form_id,
                "device_id": device_id,
                "text": text,
                "button_text": button_text,
                "client_reference": client_reference,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def get(
        self,
        contact: int,
        message: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> PublicMessageResource:
        """`GET /api/v1/contacts/{contact}/messages/{message}`: one message by the id a send or a
        webhook gave you (`message_id` of `message.status_changed`). `status` moves from `queued` to
        `sent`, `delivered`, `read` or `failed` (then `error` says why).

        Permission: **Contacts and conversations → View**.
        """
        return cast("PublicMessageResource", self._request(
            "GET",
            "/api/v1/contacts/{contact}/messages/{message}",
            path_params={"contact": contact, "message": message},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list(
        self,
        contact_id: int,
        /,
        *,
        cursor: str | NotGiven = NOT_GIVEN,
        updated_since: str | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[MessageResource]:
        """`GET /api/v1/contacts/{contactId}/messages`, paginated by cursor: the history of a contact.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/contacts/{contactId}/messages",
            path_params={"contactId": contact_id},
            query={"cursor": cursor, "updated_since": updated_since, "perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def send_contact_card(
        self,
        contact: int,
        /,
        *,
        device_id: int,
        contact_card_ids: List[int],
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> MessagesSendContactCardResponse:
        """`POST /api/v1/contacts/{contact}/message/contact-card`: sends up to 5 contact cards. Returns
        `{"messages": [...]}`, one message per card, in the order of `contact_card_ids`.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("MessagesSendContactCardResponse", self._request(
            "POST",
            "/api/v1/contacts/{contact}/message/contact-card",
            path_params={"contact": contact},
            body={
                "device_id": device_id,
                "contact_card_ids": contact_card_ids,
                "client_reference": client_reference,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def forward(
        self,
        contact: int,
        message: int,
        /,
        *,
        targets: List[ForwardMessageRequestTargetsItem2],
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> List[MessagesForwardResponseItem]:
        """`POST /api/v1/contacts/{contact}/messages/{message}/forward`: forwards a message to up to 5
        contacts. Returns one item per destination, in order: `status` (`queued`, or `blocked` with
        `reason`) and its `message`, or `None` when nothing was registered for that destination.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("List[MessagesForwardResponseItem]", self._request(
            "POST",
            "/api/v1/contacts/{contact}/messages/{message}/forward",
            path_params={"contact": contact, "message": message},
            body={"targets": targets, "client_reference": client_reference},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def react(
        self,
        contact: int,
        message: int,
        /,
        *,
        emoji: str,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`PUT /api/v1/contacts/{contact}/messages/{message}/reaction`: reacts with an emoji.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("None", self._request(
            "PUT",
            "/api/v1/contacts/{contact}/messages/{message}/reaction",
            path_params={"contact": contact, "message": message},
            body={"emoji": emoji},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def remove_reaction(
        self,
        contact: int,
        message: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`DELETE /api/v1/contacts/{contact}/messages/{message}/reaction`: removes your reaction.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("None", self._request(
            "DELETE",
            "/api/v1/contacts/{contact}/messages/{message}/reaction",
            path_params={"contact": contact, "message": message},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Templates(Resource):
    """WhatsApp message templates (conversations area): list, create, edit, send."""

    def list(
        self,
        *,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        uid: Optional[str] | NotGiven = NOT_GIVEN,
        language_code: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["PENDING", "APPROVED", "REJECTED", "PENDING_DELETION", "PAUSED", "DISABLED", "ARCHIVED"]] | NotGiven = NOT_GIVEN,
        category: Optional[str] | NotGiven = NOT_GIVEN,
        deviceId: Optional[int] | NotGiven = NOT_GIVEN,
        type: Optional[Literal["text", "image", "document", "video", "location", "default"]] | NotGiven = NOT_GIVEN,
        created_by_webhook: bool | NotGiven = NOT_GIVEN,
        quality: Optional[Literal["GREEN", "YELLOW", "RED", "UNKNOWN", "NOT_APPLICABLE"]] | NotGiven = NOT_GIVEN,
        include: Optional[Literal["quality_counts"]] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["name", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[TemplateResource]:
        """`GET /api/v1/templates`, paginated. Send only the templates with `available` true: Meta
        pauses or disables the others.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/templates",
            query={
                "name": name,
                "uid": uid,
                "language_code": language_code,
                "status": status,
                "category": category,
                "deviceId": deviceId,
                "type": type,
                "created_by_webhook": created_by_webhook,
                "quality": quality,
                "include": include,
                "perPage": perPage,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def sync(
        self,
        device: int,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> TemplatesSyncResponse:
        """`POST /api/v1/devices/{device}/templates`: brings into Funnelchat the templates an official
        number has in Meta: those created or changed directly in Meta, which otherwise arrive only
        with the daily sync; it also removes those of a WhatsApp Business account the number no
        longer uses. Returns `{"status": "completed"}` when it is done, or `{"status":
        "in_progress"}` when the first page (up to 100) is in and the rest keeps coming in the
        background: list again with `list()`, in a few seconds for `in_progress`. Official numbers
        only.

        Rejections (`TEMPLATE_SYNC_ERROR_CODES`): `404` (the number does not exist or is outside the
        key's workspace), `409 template_sync_in_progress` (one is already running for that number:
        do not start another), `422 number_not_connected_to_meta` (a QR number, or one without a
        WhatsApp Business account or credentials), `422 meta_rejected` (Meta refused and nothing was
        brought; its code in `error.body["meta_code"]`) and `502 meta_unavailable` (Meta did not
        answer).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("TemplatesSyncResponse", self._request(
            "POST",
            "/api/v1/devices/{device}/templates",
            path_params={"device": device},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create(
        self,
        *,
        name: str,
        language_code: Literal["af", "sq", "ar", "ar_EG", "ar_AE", "ar_LB", "ar_MA", "ar_QA", "az", "be_BY", "bn", "bn_IN", "bg", "ca", "zh_CN", "zh_HK", "zh_TW", "hr", "cs", "da", "prs_AF", "nl", "nl_BE", "en", "en_GB", "en_US", "en_AE", "en_AU", "en_CA", "en_GH", "en_IE", "en_IN", "en_JM", "en_MY", "en_NZ", "en_QA", "en_SG", "en_UG", "en_ZA", "et", "fil", "fi", "fr", "fr_BE", "fr_CA", "fr_CH", "fr_CI", "fr_MA", "ka", "de", "de_AT", "de_CH", "el", "gu", "ha", "he", "hi", "hu", "id", "ga", "it", "ja", "kn", "kk", "rw_RW", "ko", "ky_KG", "lo", "lv", "lt", "mk", "ms", "ml", "mr", "nb", "ps_AF", "fa", "pl", "pt_BR", "pt_PT", "pa", "ro", "ru", "sr", "si_LK", "sk", "sl", "es", "es_AR", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_HN", "es_MX", "es_PA", "es_PE", "es_ES", "es_UY", "sw", "sv", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "zu"],
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"],
        type: Literal["text", "image", "document", "video", "location", "default"],
        body: str,
        header: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        params: Optional[List[str]] | NotGiven = NOT_GIVEN,
        footer: Optional[str] | NotGiven = NOT_GIVEN,
        buttons: Optional[List[StoreMessageTemplateRequestButtonsItem2]] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> TemplateResource:
        """`POST /api/v1/templates`: creates a template and submits it to Meta.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("TemplateResource", self._request(
            "POST",
            "/api/v1/templates",
            body={
                "name": name,
                "language_code": language_code,
                "category": category,
                "type": type,
                "header": header,
                "file": file,
                "body": body,
                "params": params,
                "footer": footer,
                "buttons": buttons,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        template: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> TemplateResource:
        """`GET /api/v1/templates/{template}`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("TemplateResource", self._request(
            "GET",
            "/api/v1/templates/{template}",
            path_params={"template": template},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        template: int,
        /,
        *,
        device_id: int,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"],
        type: Literal["text", "image", "document", "video", "location", "default"],
        body: str,
        header: Optional[str] | NotGiven = NOT_GIVEN,
        file: str | NotGiven = NOT_GIVEN,
        params: Optional[List[str]] | NotGiven = NOT_GIVEN,
        footer: Optional[str] | NotGiven = NOT_GIVEN,
        buttons: Optional[List[UpdateMessageTemplateRequestButtonsItem2]] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`PUT /api/v1/templates/{template}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("None", self._request(
            "PUT",
            "/api/v1/templates/{template}",
            path_params={"template": template},
            body={
                "device_id": device_id,
                "category": category,
                "type": type,
                "header": header,
                "file": file,
                "body": body,
                "params": params,
                "footer": footer,
                "buttons": buttons,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def send(
        self,
        device: int,
        template: str,
        /,
        *,
        contact_id: Optional[int] | NotGiven = NOT_GIVEN,
        phone: Optional[str] | NotGiven = NOT_GIVEN,
        whatsapp_id: Optional[str] | NotGiven = NOT_GIVEN,
        template_variables: TemplatesSendBodyTemplateVariables | NotGiven = NOT_GIVEN,
        client_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> TemplatesSendResponse:
        """`POST /api/v1/devices/{device}/templates/{template}/send-template`: sends an approved
        template, the way to write to a contact outside the 24-hour window. Send `phone` alone (the
        contact is created when it does not exist, as with `messages.send_direct()`), or
        `contact_id`, or both when they are the same contact; `template_variables` `{"body": [...]}`
        fills the body variables in order. Returns `{"message": ...}`, the registered message with
        `status` `queued`. A variable that points to a field that does not exist is `422
        template_unresolved_placeholder`; a template this account cannot send, `404
        template_not_found`. It is a send: never retried automatically.

        Permission: **Contacts and conversations → Send**.
        """
        return cast("TemplatesSendResponse", self._request(
            "POST",
            "/api/v1/devices/{device}/templates/{template}/send-template",
            path_params={"device": device, "template": template},
            body={
                "contact_id": contact_id,
                "phone": phone,
                "whatsapp_id": whatsapp_id,
                "template_variables": template_variables,
                "client_reference": client_reference,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def delete(
        self,
        device: int,
        template: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`DELETE /api/v1/devices/{device}/templates/{template}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("None", self._request(
            "DELETE",
            "/api/v1/devices/{device}/templates/{template}",
            path_params={"device": device, "template": template},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Forms(Resource):
    """WhatsApp forms (conversations area): build them, version and publish them, choose their numbers
    and read the answers. To send one to a contact, `messages.send_form()`.

    A form has versions: the `{id}` routes take a version id, the `families/{familyId}` routes the
    form's id (`family_id`). Reading needs **Contacts and conversations → View** and changing
    **Contacts and conversations → Edit**. The answers also arrive by `whatsapp_form.completed`.
    """

    def list(
        self,
        *,
        q: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[Literal["draft", "published", "deprecated"]] | NotGiven = NOT_GIVEN,
        device_id: Optional[int] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[WhatsappFormResource]:
        """`GET /api/v1/forms`, paginated: one row per form, with its current version.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/forms",
            query={
                "q": q,
                "status": status,
                "device_id": device_id,
                "page": page,
                "perPage": perPage,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def templates(
        self,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsTemplatesResponse:
        """`GET /api/v1/forms/templates`: the templates to start a form from (`blank` is an empty one).

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsTemplatesResponse", self._request(
            "GET",
            "/api/v1/forms/templates",
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create(
        self,
        *,
        device_id: int,
        template_key: str,
        device_ids: List[int] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsCreateResponse:
        """`POST /api/v1/forms`: creates a draft from a template (`template_key`) for a number.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsCreateResponse", self._request(
            "POST",
            "/api/v1/forms",
            body={"device_id": device_id, "device_ids": device_ids, "template_key": template_key},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsRetrieveResponse:
        """`GET /api/v1/forms/{id}`: one version (`id` is the version id), with its lint issues,
        versions and numbers.

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsRetrieveResponse", self._request(
            "GET",
            "/api/v1/forms/{id}",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        id: int,
        /,
        *,
        definition: SaveWhatsappFormRequestDefinition2,
        name: str | NotGiven = NOT_GIVEN,
        expected_updated_at: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsUpdateResponse:
        """`PUT /api/v1/forms/{id}`: saves a draft. A published version answers `409 PUBLISHED`; with
        `expected_updated_at`, someone else's change answers `409 STALE`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsUpdateResponse", self._request(
            "PUT",
            "/api/v1/forms/{id}",
            path_params={"id": id},
            body={
                "name": name,
                "definition": definition,
                "expected_updated_at": expected_updated_at,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> List[Any]:
        """`DELETE /api/v1/forms/{id}`: deletes a draft (a published form is deprecated, not deleted).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("List[Any]", self._request(
            "DELETE",
            "/api/v1/forms/{id}",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create_version(
        self,
        id: int,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> str:
        """`POST /api/v1/forms/{id}/versions`: a new draft from this version, or the draft that already
        existed (`created` false).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("str", self._request(
            "POST",
            "/api/v1/forms/{id}/versions",
            path_params={"id": id},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def sync(
        self,
        id: int,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsSyncResponse:
        """`POST /api/v1/forms/{id}/sync`: validates the version in Meta (`502 META` when Meta rejects
        it).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsSyncResponse", self._request(
            "POST",
            "/api/v1/forms/{id}/sync",
            path_params={"id": id},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def publish(
        self,
        id: int,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsPublishResponse:
        """`POST /api/v1/forms/{id}/publish`: publishes the version (`422 LINT` with errors).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsPublishResponse", self._request(
            "POST",
            "/api/v1/forms/{id}/publish",
            path_params={"id": id},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def numbers(
        self,
        id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsNumbersResponse:
        """`GET /api/v1/forms/{id}/numbers`: the numbers of the form and their state.

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsNumbersResponse", self._request(
            "GET",
            "/api/v1/forms/{id}/numbers",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def add_number(
        self,
        id: int,
        /,
        *,
        device_id: int,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsAddNumberResponse:
        """`POST /api/v1/forms/{id}/numbers`: adds a number.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsAddNumberResponse", self._request(
            "POST",
            "/api/v1/forms/{id}/numbers",
            path_params={"id": id},
            body={"device_id": device_id},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def remove_number(
        self,
        id: int,
        device_id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsRemoveNumberResponse:
        """`DELETE /api/v1/forms/{id}/numbers/{deviceId}`: removes a number (not the primary one).

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsRemoveNumberResponse", self._request(
            "DELETE",
            "/api/v1/forms/{id}/numbers/{deviceId}",
            path_params={"id": id, "deviceId": device_id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retry_numbers(
        self,
        id: int,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsRetryNumbersResponse:
        """`POST /api/v1/forms/{id}/numbers/retry`: retries the numbers that failed.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("FormsRetryNumbersResponse", self._request(
            "POST",
            "/api/v1/forms/{id}/numbers/retry",
            path_params={"id": id},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def definition(
        self,
        family_id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Union[FormsDefinitionResponse, FormsDefinitionResponseVariant2]:
        """`GET /api/v1/forms/families/{familyId}/definition`: the published definition of a form, or
        `data` `None`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("Union[FormsDefinitionResponse, FormsDefinitionResponseVariant2]", self._request(
            "GET",
            "/api/v1/forms/families/{familyId}/definition",
            path_params={"familyId": family_id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def versions(
        self,
        family_id: int,
        /,
        *,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsVersionsResponse:
        """`GET /api/v1/forms/families/{familyId}/versions`: the versions of a form.

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsVersionsResponse", self._request(
            "GET",
            "/api/v1/forms/families/{familyId}/versions",
            path_params={"familyId": family_id},
            query={"perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_responses(
        self,
        family_id: int,
        /,
        *,
        from_: Optional[str] | NotGiven = NOT_GIVEN,
        to: Optional[str] | NotGiven = NOT_GIVEN,
        version_id: Optional[int] | NotGiven = NOT_GIVEN,
        origin: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[str] | NotGiven = NOT_GIVEN,
        kind: Optional[str] | NotGiven = NOT_GIVEN,
        effect_status: Optional[str] | NotGiven = NOT_GIVEN,
        search: Optional[str] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[Dict[str, Any]]:
        """`GET /api/v1/forms/families/{familyId}/responses`, paginated: the answers to a form, with
        `columns`.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/forms/families/{familyId}/responses",
            path_params={"familyId": family_id},
            query={
                "from": from_,
                "to": to,
                "version_id": version_id,
                "origin": origin,
                "status": status,
                "kind": kind,
                "effect_status": effect_status,
                "search": search,
                "page": page,
                "perPage": perPage,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def retrieve_response(
        self,
        family_id: int,
        run_id: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsRetrieveResponseResponse:
        """`GET /api/v1/forms/families/{familyId}/responses/{runId}`: one answer in detail.

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsRetrieveResponseResponse", self._request(
            "GET",
            "/api/v1/forms/families/{familyId}/responses/{runId}",
            path_params={"familyId": family_id, "runId": run_id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def metrics(
        self,
        family_id: int,
        /,
        *,
        from_: Optional[str] | NotGiven = NOT_GIVEN,
        to: Optional[str] | NotGiven = NOT_GIVEN,
        version_id: Optional[int] | NotGiven = NOT_GIVEN,
        origin: Optional[str] | NotGiven = NOT_GIVEN,
        status: Optional[str] | NotGiven = NOT_GIVEN,
        kind: Optional[str] | NotGiven = NOT_GIVEN,
        effect_status: Optional[str] | NotGiven = NOT_GIVEN,
        search: Optional[str] | NotGiven = NOT_GIVEN,
        per_page: Optional[int] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> FormsMetricsResponse:
        """`GET /api/v1/forms/families/{familyId}/metrics`: the funnel: sent, delivered, read,
        completed and the rates.

        Permission: **Contacts and conversations → View**.
        """
        return cast("FormsMetricsResponse", self._request(
            "GET",
            "/api/v1/forms/families/{familyId}/metrics",
            path_params={"familyId": family_id},
            query={
                "from": from_,
                "to": to,
                "version_id": version_id,
                "origin": origin,
                "status": status,
                "kind": kind,
                "effect_status": effect_status,
                "search": search,
                "per_page": per_page,
                "page": page,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Tags(Resource):
    """Tags (conversations area)."""

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        withContactCount: bool | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["name", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[TagResource]:
        """`GET /api/v1/tags`, paginated.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/tags",
            query={
                "name": name,
                "withContactCount": withContactCount,
                "perPage": perPage,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> TagResource:
        """`POST /api/v1/tags`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("TagResource", self._request(
            "POST",
            "/api/v1/tags",
            body={"name": name, "description": description, "color": color},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        tag: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> TagResource:
        """`GET /api/v1/tags/{tag}`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("TagResource", self._request(
            "GET",
            "/api/v1/tags/{tag}",
            path_params={"tag": tag},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        tag: int,
        /,
        *,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """`PUT /api/v1/tags/{tag}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("Dict[str, Any]", self._request(
            "PUT",
            "/api/v1/tags/{tag}",
            path_params={"tag": tag},
            body={"name": name, "description": description, "color": color},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        *,
        tagIds: List[str],
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """`POST /api/v1/tags/delete`: deletes the tags in `tagIds`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("Dict[str, Any]", self._request(
            "POST",
            "/api/v1/tags/delete",
            body={"tagIds": tagIds},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_contacts(
        self,
        tag: int,
        /,
        *,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["name", "last_message_time", "follow_up_date"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        sortBy: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[str]:
        """`GET /api/v1/tags/{tag}/contacts`, paginated: the contacts with a tag.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/tags/{tag}/contacts",
            path_params={"tag": tag},
            query={
                "perPage": perPage,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
                "sortBy": sortBy,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )


class CustomFields(Resource):
    """Custom fields of contacts (conversations area). To set a value on a contact,
    `contacts.attach_custom_field()`.
    """

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        type: Literal[0, 1, 2, 3, 4] | NotGiven = NOT_GIVEN,
        withContactCount: bool | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        orderBy: Literal["name", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[CustomFieldResource]:
        """`GET /api/v1/custom-fields`, paginated.

        Permission: **Contacts and conversations → View**.
        """
        return self._paginate(
            "/api/v1/custom-fields",
            query={
                "name": name,
                "description": description,
                "type": type,
                "withContactCount": withContactCount,
                "perPage": perPage,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def create(
        self,
        *,
        name: str,
        type: Literal[0, 1, 2, 3, 4],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> CustomFieldResource:
        """`POST /api/v1/custom-fields`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("CustomFieldResource", self._request(
            "POST",
            "/api/v1/custom-fields",
            body={"name": name, "description": description, "type": type},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        custom_field: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> CustomFieldResource:
        """`GET /api/v1/custom-fields/{customField}`.

        Permission: **Contacts and conversations → View**.
        """
        return cast("CustomFieldResource", self._request(
            "GET",
            "/api/v1/custom-fields/{customField}",
            path_params={"customField": custom_field},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        custom_field: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> CustomFieldResource:
        """`PUT /api/v1/custom-fields/{customField}`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("CustomFieldResource", self._request(
            "PUT",
            "/api/v1/custom-fields/{customField}",
            path_params={"customField": custom_field},
            body={"name": name, "description": description},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        *,
        customFieldIds: List[str],
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """`POST /api/v1/custom-fields/delete`.

        Permission: **Contacts and conversations → Edit**.
        """
        return cast("Dict[str, Any]", self._request(
            "POST",
            "/api/v1/custom-fields/delete",
            body={"customFieldIds": customFieldIds},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Groups(Resource):
    """WhatsApp groups (communities area): the groups of a number, live from WhatsApp
    (`list_by_device()`); following one (`follow()`), so its joins and leaves arrive as events;
    sending a message to a group (`send_message()`) and reading how it went (`retrieve_action()`);
    and the groups already in the account, with their participants, joins and leaves, scheduled
    messages and actions.

    Reading needs **Groups and campaigns → View**, sending **Groups and campaigns → Send** and
    following **Groups and campaigns → Manage groups**. Who joins and who leaves a followed group
    arrives by `group_participant.joined` and `group_participant.left`.
    """

    def list(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        orderBy: str | NotGiven = NOT_GIVEN,
        orderByMethod: str | NotGiven = NOT_GIVEN,
        type: Literal["1", "2", "3", "4"] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        status: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8"] | NotGiven = NOT_GIVEN,
        deviceId: int | NotGiven = NOT_GIVEN,
        noCampaign: bool | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[GroupResource]:
        """`GET /api/v1/groups`, paginated: the groups already in the account. Each group's `uid`
        (`…@g.us`) is what `send_message()` takes.

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/groups",
            query={
                "name": name,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
                "type": type,
                "perPage": perPage,
                "status": status,
                "deviceId": deviceId,
                "noCampaign": noCampaign,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def retrieve(
        self,
        group: str,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> GroupResource:
        """`GET /api/v1/groups/{group}`.

        Permission: **Groups and campaigns → View**.
        """
        return cast("GroupResource", self._request(
            "GET",
            "/api/v1/groups/{group}",
            path_params={"group": group},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_by_device(
        self,
        device: int,
        /,
        *,
        page: int | NotGiven = NOT_GIVEN,
        pageSize: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[GroupMinResource]:
        """`GET /api/v1/devices/{device}/groups`, paginated (`page`, `pageSize`): the groups of one
        number, read live from WhatsApp (for a key, reused for a minute per number), also those not
        in the account yet. A group already in the account brings `device_id`; any other can be
        followed with `follow()`. Its `uid` is the group of `follow()` and `send_message()`.

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/devices/{device}/groups",
            path_params={"device": device},
            query={"page": page, "pageSize": pageSize, "name": name},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def metadata(
        self,
        uid: str,
        /,
        *,
        device_id: int,
        group_uid: str,
        type: Literal["groups", "ad-groups", "channels"] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Union[GroupMetadataResource, ChannelMetadataResource]:
        """`GET /api/v1/groups/{groupUid}/metadata`: live metadata of a group by its WhatsApp uid, read
        through one number.

        Permission: **Groups and campaigns → View**.
        """
        return cast("Union[GroupMetadataResource, ChannelMetadataResource]", self._request(
            "GET",
            "/api/v1/groups/{groupUid}/metadata",
            path_params={"groupUid": uid},
            query={"device_id": device_id, "group_uid": group_uid, "type": type},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_participants(
        self,
        *,
        groupUid: str,
        phone: str | NotGiven = NOT_GIVEN,
        isAdmin: Literal["true", "false", "1", "0"] | NotGiven = NOT_GIVEN,
        eligibleForAdmin: Literal["true", "false", "1", "0"] | NotGiven = NOT_GIVEN,
        orderBy: str | NotGiven = NOT_GIVEN,
        orderDirection: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ParticipantResource]:
        """`GET /api/v1/groups/participants`, paginated: the participants of one group (`groupUid`).

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/groups/participants",
            query={
                "groupUid": groupUid,
                "phone": phone,
                "isAdmin": isAdmin,
                "eligibleForAdmin": eligibleForAdmin,
                "orderBy": orderBy,
                "orderDirection": orderDirection,
                "perPage": perPage,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def list_participant_events(
        self,
        group: str,
        /,
        *,
        search: Optional[str] | NotGiven = NOT_GIVEN,
        event_type: Optional[Literal["all", "join", "leave"]] | NotGiven = NOT_GIVEN,
        page: Optional[int] | NotGiven = NOT_GIVEN,
        perPage: Optional[int] | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        date_mode: Optional[Literal["both", "joins_only", "leaves_only"]] | NotGiven = NOT_GIVEN,
        selection_type: Optional[Literal["all", "none"]] | NotGiven = NOT_GIVEN,
        groups_uids: List[str] | NotGiven = NOT_GIVEN,
        participant_filter: Optional[Literal["all", "active"]] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ParticipantEventResource]:
        """`GET /api/v1/groups/{group}/participant-events`, paginated: joins and leaves.

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/groups/{group}/participant-events",
            path_params={"group": group},
            query={
                "search": search,
                "event_type": event_type,
                "page": page,
                "perPage": perPage,
                "start_date": start_date,
                "end_date": end_date,
                "timezone": timezone,
                "date_mode": date_mode,
                "selection_type": selection_type,
                "groups_uids": groups_uids,
                "participant_filter": participant_filter,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def list_scheduled_messages(
        self,
        group: str,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        orderBy: Literal["send_at", "name", "status", "id", "created_at", "updated_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ScheduledMessageResource]:
        """`GET /api/v1/groups/{group}/scheduled-messages`, paginated.

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/groups/{group}/scheduled-messages",
            path_params={"group": group},
            query={
                "name": name,
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
                "perPage": perPage,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def list_actions(
        self,
        group: str,
        /,
        *,
        orderBy: Literal["status", "created_at", "updated_at", "completed_at"] | NotGiven = NOT_GIVEN,
        orderByMethod: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ActionGroupResource]:
        """`GET /api/v1/groups/{group}/actions`, paginated.

        Permission: **Groups and campaigns → View**.
        """
        return self._paginate(
            "/api/v1/groups/{group}/actions",
            path_params={"group": group},
            query={
                "orderBy": orderBy,
                "orderByMethod": orderByMethod,
                "page": page,
                "perPage": perPage,
            },
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def send_message(
        self,
        group_uid: str,
        /,
        *,
        device_id: int,
        type: Literal["text", "image", "video", "audio", "document"],
        text: str | NotGiven = NOT_GIVEN,
        media_url: str | NotGiven = NOT_GIVEN,
        caption: str | NotGiven = NOT_GIVEN,
        file_name: str | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
        retry_send: bool = False,
    ) -> ApiGroupActionAcceptedResource:
        """`POST /api/v1/groups/{group}/messages`: sends a text (`type="text"`, `text`) or one file
        (`image`, `video`, `audio` or `document`, by its `https` `media_url`) to the group with that
        `uid` (`…@g.us`), from `device_id`. It answers `202` with `{"action_id": ..., "status":
        "queued"}` and goes out in the background: the result arrives by `group_action.completed`
        (or `group_action.failed`), with the same `action_id` in `action.uuid`, or with
        `retrieve_action()`. A QR number must be admin of the group; an official number, the one the
        group belongs to. A group not in the account yet is followed first (`follow()`, with its
        rules). Rejections: `GROUP_ACTION_ERROR_CODES`. It is a send: never retried automatically.

        Permission: **Groups and campaigns → Send**.
        """
        return cast("ApiGroupActionAcceptedResource", self._request(
            "POST",
            "/api/v1/groups/{group}/messages",
            path_params={"group": group_uid},
            body={
                "device_id": device_id,
                "type": type,
                "text": text,
                "media_url": media_url,
                "caption": caption,
                "file_name": file_name,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
            retry_send=retry_send,
        ))

    def follow(
        self,
        group_uid: str,
        /,
        *,
        device_id: int,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> GroupsFollowResponse:
        """`POST /api/v1/groups/{group}/import`: follows the WhatsApp group with that `uid` (`…@g.us`)
        of a QR number (`device_id`), as importing it in the panel does: from then on its joins and
        leaves arrive by `group_participant.joined` and `group_participant.left`. Returns `{"data":
        {"uid", "name", "imported", "is_admin"}}`: `imported` is false when the group was already in
        the account, and `is_admin` says whether the number administers it (without that it cannot
        write to it). Needs **Groups and campaigns → Manage groups** (`403
        import_permission_required`); up to 5 groups per number per minute (`429
        import_rate_limited`, with `retry_after`); an official number is `422 provider_unsupported`.

        Permission: **Groups and campaigns → Manage groups**.
        """
        return cast("GroupsFollowResponse", self._request(
            "POST",
            "/api/v1/groups/{group}/import",
            path_params={"group": group_uid},
            body={"device_id": device_id},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve_action(
        self,
        action: str,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> GroupsRetrieveActionResponse:
        """`GET /api/v1/groups/actions/{action}`: where a group action, such as a message sent with
        `send_message()`, is (`queued`, `running`, `completed` or `failed`) and its `result`
        (`result.message.uid` is the id of the message in WhatsApp).

        Permission: **Groups and campaigns → View**.
        """
        return cast("GroupsRetrieveActionResponse", self._request(
            "GET",
            "/api/v1/groups/actions/{action}",
            path_params={"action": action},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Devices(Resource):
    """WhatsApp numbers of the account (accounts area). The `id` of a number is the `device_id` you
    send with.
    """

    def list(
        self,
        *,
        external_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[DeviceResource]:
        """`GET /api/v1/devices`. `external_reference` keeps only the numbers with that reference
        (exact match).

        Permission: **WhatsApp numbers → View**.
        """
        return self._paginate(
            "/api/v1/devices",
            query={"external_reference": external_reference},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def create(
        self,
        *,
        connection: Literal["qr"],
        alias: Optional[str] | NotGiven = NOT_GIVEN,
        external_reference: Optional[str] | NotGiven = NOT_GIVEN,
        same_number_as: Optional[int] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> DevicesCreateResponse:
        """`POST /api/v1/devices`: creates a number that connects by QR code (`connection="qr"`), not
        connected yet. Then show its QR with `qr()`, or send your customer a connect link
        (`connect_links.create()`). It takes a slot of the plan, with the panel's rejections (`403
        numbers_not_included`, `403 number_limit_reached`…). An account has at most one QR number
        waiting to be scanned: another one is `409 pending_number_exists`, with that number's
        `device_id` in `error.body`. `country` (two letters) is the country of the phone that will
        scan the QR.

        Permission: **WhatsApp numbers → Create, connect and delete**.
        """
        return cast("DevicesCreateResponse", self._request(
            "POST",
            "/api/v1/devices",
            body={
                "connection": connection,
                "alias": alias,
                "external_reference": external_reference,
                "same_number_as": same_number_as,
                "country": country,
            },
            idempotency_key=idempotency_key,
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        device: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> DeviceResource:
        """`GET /api/v1/devices/{device}`. `capabilities` says what the number can do by API.

        Permission: **WhatsApp numbers → View**.
        """
        return cast("DeviceResource", self._request(
            "GET",
            "/api/v1/devices/{device}",
            path_params={"device": device},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        device: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> str:
        """`DELETE /api/v1/devices/{device}`: deletes the number and frees its slot of the plan.
        Irreversible. Sends `device.deleted`.

        Permission: **WhatsApp numbers → Create, connect and delete**.

        It cannot be undone: a script or an AI agent acting on its own should ask a person to
        confirm before calling it.
        """
        return cast("str", self._request(
            "DELETE",
            "/api/v1/devices/{device}",
            path_params={"device": device},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        device: int,
        /,
        *,
        alias: Optional[str] | NotGiven = NOT_GIVEN,
        color: Optional[str] | NotGiven = NOT_GIVEN,
        image: Optional[str] | NotGiven = NOT_GIVEN,
        number: Optional[str] | NotGiven = NOT_GIVEN,
        first_conecction_at: Optional[str] | NotGiven = NOT_GIVEN,
        is_business: bool | NotGiven = NOT_GIVEN,
        phone_number_id: str | NotGiven = NOT_GIVEN,
        waba_id: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        whatsApp_business_app: bool | NotGiven = NOT_GIVEN,
        capi_consent: bool | NotGiven = NOT_GIVEN,
        external_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> DeviceResource:
        """`PUT /api/v1/devices/{device}`: also changes `external_reference`.

        Permission: **WhatsApp numbers → Edit**.
        """
        return cast("DeviceResource", self._request(
            "PUT",
            "/api/v1/devices/{device}",
            path_params={"device": device},
            body={
                "alias": alias,
                "color": color,
                "image": image,
                "number": number,
                "first_conecction_at": first_conecction_at,
                "is_business": is_business,
                "phone_number_id": phone_number_id,
                "waba_id": waba_id,
                "code": code,
                "whatsApp_business_app": whatsApp_business_app,
                "capi_consent": capi_consent,
                "external_reference": external_reference,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def qr(
        self,
        device: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> DevicesQrResponse:
        """`GET /api/v1/devices/{device}/qr`: the QR code to scan, as a PNG data URI (`qr_code`), or
        `None` once `connected`. Ask for it again every `expires_in` seconds and have it scanned
        right away: WhatsApp changes the code every few seconds, so show the latest and never store
        or forward a QR. Only for QR numbers (an official one is `422 provider_unsupported`).

        Permission: **WhatsApp numbers → Create, connect and delete**.
        """
        return cast("DevicesQrResponse", self._request(
            "GET",
            "/api/v1/devices/{device}/qr",
            path_params={"device": device},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def status(
        self,
        device: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Dict[str, Any]:
        """`GET /api/v1/devices/{device}/status`: connection status.

        Permission: **WhatsApp numbers → View**.
        """
        return cast("Dict[str, Any]", self._request(
            "GET",
            "/api/v1/devices/{device}/status",
            path_params={"device": device},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def health(
        self,
        device: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> DeviceHealthDetailResource:
        """`GET /api/v1/devices/{device}/health`.

        Permission: **WhatsApp numbers → View**.
        """
        return cast("DeviceHealthDetailResource", self._request(
            "GET",
            "/api/v1/devices/{device}/health",
            path_params={"device": device},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_connection_history(
        self,
        device: int,
        /,
        *,
        orderBy: str | NotGiven = NOT_GIVEN,
        orderByMethod: str | NotGiven = NOT_GIVEN,
        perPage: int | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[DeviceConnectionEventResource]:
        """`GET /api/v1/devices/{device}/connection-history`, paginated.

        Permission: **WhatsApp numbers → View**.
        """
        return self._paginate(
            "/api/v1/devices/{device}/connection-history",
            path_params={"device": device},
            query={"orderBy": orderBy, "orderByMethod": orderByMethod, "perPage": perPage},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )


class ConnectLinks(Resource):
    """Connect links (accounts area): a single-use page, on the Funnelchat domain, where you or your
    customer connect a WhatsApp number to your account, by QR code (`type="qr"`) or as an official
    number through Meta's sign-up (`type="meta"`, answered `503 meta_connect_disabled` in production
    for now). The number is created when the page finishes; with `device_id` the link reconnects
    that number instead.

    Reading needs **WhatsApp numbers → View**; creating and revoking, **WhatsApp numbers → Create,
    connect and delete**. The result arrives three ways: the `device.connected` webhook (with
    `connect_link_id` and `external_reference`), the `return_url`, or `get()`.
    """

    def create(
        self,
        *,
        type: Literal["meta", "qr"],
        allowed_connection_types: List[Literal["coexistence", "dedicated"]] | NotGiven = NOT_GIVEN,
        provision_us_number: bool | NotGiven = NOT_GIVEN,
        device_id: Optional[int] | NotGiven = NOT_GIVEN,
        same_number_as: Optional[int] | NotGiven = NOT_GIVEN,
        country: Optional[str] | NotGiven = NOT_GIVEN,
        external_reference: Optional[str] | NotGiven = NOT_GIVEN,
        return_url: Optional[str] | NotGiven = NOT_GIVEN,
        expires_in_minutes: Optional[int] | NotGiven = NOT_GIVEN,
        idempotency_key: Optional[str] = None,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConnectLinksCreateResponse:
        """`POST /api/v1/connect-links`: returns `{"data": link}`. `link["url"]` is the page to open:
        it carries the token and comes only in this response. `country` (only `qr`, two letters) is
        the country of the phone that will scan the QR. At most 20 links open (`429
        too_many_open_links`).

        Permission: **WhatsApp numbers → Create, connect and delete**.
        """
        return cast("ConnectLinksCreateResponse", self._request(
            "POST",
            "/api/v1/connect-links",
            body={
                "type": type,
                "allowed_connection_types": allowed_connection_types,
                "provision_us_number": provision_us_number,
                "device_id": device_id,
                "same_number_as": same_number_as,
                "country": country,
                "external_reference": external_reference,
                "return_url": return_url,
                "expires_in_minutes": expires_in_minutes,
            },
            idempotency_key=idempotency_key,
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def get(
        self,
        link: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> ConnectLinksGetResponse:
        """`GET /api/v1/connect-links/{link}`: its `status` (`pending`, `completed`, `failed`,
        `expired`, `revoked`), and `device_id` and `error_code` once it ends.

        Permission: **WhatsApp numbers → View**.
        """
        return cast("ConnectLinksGetResponse", self._request(
            "GET",
            "/api/v1/connect-links/{link}",
            path_params={"link": link},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list(
        self,
        *,
        status: Optional[Literal["pending", "completed", "failed", "expired", "revoked"]] | NotGiven = NOT_GIVEN,
        external_reference: Optional[str] | NotGiven = NOT_GIVEN,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[ConnectLinkResource]:
        """`GET /api/v1/connect-links`, paginated, newest first: filter by `status` or
        `external_reference`.

        Permission: **WhatsApp numbers → View**.
        """
        return self._paginate(
            "/api/v1/connect-links",
            query={"status": status, "external_reference": external_reference},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )

    def revoke(
        self,
        link: int,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> str:
        """`DELETE /api/v1/connect-links/{link}`: revokes a `pending` link (any other is `409
        link_not_pending`).

        Permission: **WhatsApp numbers → Create, connect and delete**.
        """
        return cast("str", self._request(
            "DELETE",
            "/api/v1/connect-links/{link}",
            path_params={"link": link},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))


class Webhooks(Resource, WebhookHelpers):
    """Webhook subscriptions (accounts area), plus `verify()` and `construct_event()` for the
    deliveries (the same functions as `funnelchat.webhooks`).

    Reading needs **Notifications (webhooks) → View** and the rest **Notifications (webhooks) →
    Manage**. A key only sees and manages subscriptions to events of the areas it can read
    (**Contacts and conversations → View**, **Groups and campaigns → View**, **WhatsApp numbers →
    View**): asking for others is a `422` on `events`. Rotating the secret is not open to API keys:
    it is done from the panel.
    """

    def events(
        self,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> WebhooksEventsResponse:
        """`GET /api/v1/webhooks/events`: the event types you can subscribe to, each with `status`.

        Permission: **WhatsApp numbers → View**.
        """
        return cast("WebhooksEventsResponse", self._request(
            "GET",
            "/api/v1/webhooks/events",
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list(
        self,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Union[List[WebhookSubscriptionResource], WebhooksListResponseVariant2]:
        """`GET /api/v1/webhooks`: every subscription of the workspace of the key (at most 50), not
        only yours.

        Permission: **Notifications (webhooks) → View**.
        """
        return cast("Union[List[WebhookSubscriptionResource], WebhooksListResponseVariant2]", self._request(
            "GET",
            "/api/v1/webhooks",
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def create(
        self,
        *,
        url: str,
        events: List[Literal["device.disconnected", "device.connected", "device.deleted", "device.health_changed", "device.quality_changed", "device.messaging_limit_changed", "device.display_name_reviewed", "billing.payment_failed", "billing.upcoming_charge", "subscription.trial_ending", "subscription.reactivated", "subscription.cancellation_confirmed", "subscription.dormant_ending", "mac.usage_80", "mac.usage_100", "mac.expiring", "account.blocked", "message.received", "flow.completed", "broadcast.finished", "contact.stage_changed", "message.status_changed", "conversation.closed", "conversation.assigned", "contact.tag_added", "broadcast.paused", "contact.tag_removed", "contact.created", "template.status_changed", "flow.failed", "whatsapp_form.completed", "contact.updated", "message.reaction_failed", "group.created", "group.invite_link_down", "group.invite_link_renewed", "group_participant.joined", "group_participant.left", "scheduled_message.group_delivery_failed", "scheduled_message.response_received", "poll.voted", "pipeline.finished", "group.blocked", "group.recovered", "campaign.status_changed", "scheduled_message.finished", "group_action.failed", "daily_report.generated", "campaign.no_groups_available", "group.full", "group_action.completed", "group.message_received", "group.reaction_added", "group_join_request.created", "group_join_request.revoked"]],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        filters: StoreWebhookSubscriptionRequestFilters2 | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> WebhookSubscriptionCreatedResource:
        """`POST /api/v1/webhooks`: the response brings `secret` once. Store it, and store the `id`.

        Permission: **Notifications (webhooks) → Manage**.
        """
        return cast("WebhookSubscriptionCreatedResource", self._request(
            "POST",
            "/api/v1/webhooks",
            body={"url": url, "description": description, "events": events, "filters": filters},
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def retrieve(
        self,
        id: str,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> WebhookSubscriptionResource:
        """`GET /api/v1/webhooks/{id}` (without the secret).

        Permission: **Notifications (webhooks) → View**.
        """
        return cast("WebhookSubscriptionResource", self._request(
            "GET",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def update(
        self,
        id: str,
        /,
        *,
        url: str,
        events: List[Literal["device.disconnected", "device.connected", "device.deleted", "device.health_changed", "device.quality_changed", "device.messaging_limit_changed", "device.display_name_reviewed", "billing.payment_failed", "billing.upcoming_charge", "subscription.trial_ending", "subscription.reactivated", "subscription.cancellation_confirmed", "subscription.dormant_ending", "mac.usage_80", "mac.usage_100", "mac.expiring", "account.blocked", "message.received", "flow.completed", "broadcast.finished", "contact.stage_changed", "message.status_changed", "conversation.closed", "conversation.assigned", "contact.tag_added", "broadcast.paused", "contact.tag_removed", "contact.created", "template.status_changed", "flow.failed", "whatsapp_form.completed", "contact.updated", "message.reaction_failed", "group.created", "group.invite_link_down", "group.invite_link_renewed", "group_participant.joined", "group_participant.left", "scheduled_message.group_delivery_failed", "scheduled_message.response_received", "poll.voted", "pipeline.finished", "group.blocked", "group.recovered", "campaign.status_changed", "scheduled_message.finished", "group_action.failed", "daily_report.generated", "campaign.no_groups_available", "group.full", "group_action.completed", "group.message_received", "group.reaction_added", "group_join_request.created", "group_join_request.revoked"]],
        description: Optional[str] | NotGiven = NOT_GIVEN,
        filters: UpdateWebhookSubscriptionRequestFilters2 | NotGiven = NOT_GIVEN,
        status: Literal["active", "paused"] | NotGiven = NOT_GIVEN,
        extra_body: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> WebhookSubscriptionResource:
        """`PUT /api/v1/webhooks/{id}`: replaces `url`, `events`, `description` and `filters`. The
        secret stays.

        Permission: **Notifications (webhooks) → Manage**.
        """
        return cast("WebhookSubscriptionResource", self._request(
            "PUT",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            body={
                "url": url,
                "description": description,
                "events": events,
                "filters": filters,
                "status": status,
            },
            extra_body=extra_body,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def delete(
        self,
        id: str,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> None:
        """`DELETE /api/v1/webhooks/{id}`.

        Permission: **Notifications (webhooks) → Manage**.
        """
        return cast("None", self._request(
            "DELETE",
            "/api/v1/webhooks/{id}",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def test(
        self,
        id: str,
        /,
        *,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> WebhooksTestResponse:
        """`POST /api/v1/webhooks/{id}/test`: delivers one signed `webhook.test` now. Check
        `succeeded`.

        Permission: **Notifications (webhooks) → Manage**.
        """
        return cast("WebhooksTestResponse", self._request(
            "POST",
            "/api/v1/webhooks/{id}/test",
            path_params={"id": id},
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        ))

    def list_deliveries(
        self,
        id: str,
        /,
        *,
        extra_query: Optional[Dict[str, Any]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        max_retries: Optional[int] = None,
    ) -> Page[WebhookSubscriptionDeliveryResource]:
        """`GET /api/v1/webhooks/{id}/deliveries`, paginated: one row per attempt, newest first.

        Permission: **Notifications (webhooks) → View**.
        """
        return self._paginate(
            "/api/v1/webhooks/{id}/deliveries",
            path_params={"id": id},
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
            max_retries=max_retries,
        )


class ClientResources:
    """The resources of `Funnelchat`, one attribute each."""

    contacts: Contacts
    conversations: Conversations
    messages: Messages
    templates: Templates
    forms: Forms
    tags: Tags
    custom_fields: CustomFields
    groups: Groups
    devices: Devices
    connect_links: ConnectLinks
    webhooks: Webhooks

    def _init_resources(self) -> None:
        client = cast("Funnelchat", self)
        self.contacts = Contacts(client)
        self.conversations = Conversations(client)
        self.messages = Messages(client)
        self.templates = Templates(client)
        self.forms = Forms(client)
        self.tags = Tags(client)
        self.custom_fields = CustomFields(client)
        self.groups = Groups(client)
        self.devices = Devices(client)
        self.connect_links = ConnectLinks(client)
        self.webhooks = Webhooks(client)

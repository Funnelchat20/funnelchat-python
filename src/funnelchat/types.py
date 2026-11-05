"""GENERATED FILE — do not edit. Run `python scripts/generate.py`.

Source: spec/funnelchat.json (sha256 0ffaad2b25733d28…) + spec/pending.json + spec/resources.json.
The shapes of what the API answers and of every webhook event, as TypedDicts: at runtime they
are plain dicts (the decoded JSON), so `message["status"]` and `json.dumps(message)` just work.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict, List, Literal, Optional, TypedDict, Union

if TYPE_CHECKING:
    from typing_extensions import NotRequired

__all__ = [
    "AccountBlockedEvent",
    "AccountBlockedEventData",
    "ActionGroupResource",
    "ActionGroupResource2",
    "ActionGroupResourceVariant2",
    "AiQuotaLowBalanceEvent",
    "AiQuotaTopupFailedEvent",
    "AiQuotaTopupSucceededEvent",
    "ApiGroupActionAcceptedResource",
    "ApiGroupDeviceRequest",
    "ApiGroupImportResource",
    "BillingPaymentFailedEvent",
    "BillingPaymentFailedEventData",
    "BillingPlanBlockedEvent",
    "BillingUpcomingChargeEvent",
    "BillingUpcomingChargeEventData",
    "BroadcastFinishedEvent",
    "BroadcastFinishedEventData",
    "BroadcastFinishedEventDataBroadcast",
    "BroadcastFinishedEventDataTotals",
    "BroadcastPausedEvent",
    "BroadcastPausedEventData",
    "BroadcastPausedEventDataBroadcast",
    "CampaignNoGroupsAvailableEvent",
    "CampaignNoGroupsAvailableEventData",
    "CampaignNoGroupsAvailableEventDataCampaign",
    "CampaignStatusChangedEvent",
    "CampaignStatusChangedEventData",
    "CampaignStatusChangedEventDataCampaign",
    "ChannelMetadataResource",
    "CommunitiesMessageResource",
    "ConnectLinkResource",
    "ConnectLinksCreateResponse",
    "ConnectLinksGetResponse",
    "ContactCreatedEvent",
    "ContactCreatedEventData",
    "ContactCreatedEventDataContact",
    "ContactCustomFieldResource",
    "ContactNoteResource",
    "ContactResource",
    "ContactResourceLastMessage",
    "ContactResourceLeadScore",
    "ContactStageChangedEvent",
    "ContactStageChangedEventData",
    "ContactStageChangedEventDataBoard",
    "ContactStageChangedEventDataContact",
    "ContactStageChangedEventDataFromStage",
    "ContactStageChangedEventDataToStage",
    "ContactTagAddedEvent",
    "ContactTagAddedEventData",
    "ContactTagAddedEventDataContact",
    "ContactTagAddedEventDataTag",
    "ContactTagRemovedEvent",
    "ContactTagRemovedEventData",
    "ContactTagRemovedEventDataContact",
    "ContactTagRemovedEventDataTag",
    "ContactTagResource",
    "ContactsAttachCustomFieldBodyItem",
    "ContactsAttachCustomFieldResponseItem",
    "ContactsAttachCustomFieldResponseItemVariant2",
    "ContactsAttachCustomFieldResponseItemVariant3",
    "ContactsDeleteBodyCustomFieldFiltersItem",
    "ContactsDeleteBodyTagFiltersItem",
    "ContactsDetachCustomFieldBodyItem",
    "ContactsDetachCustomFieldResponse",
    "ContactsListQueryCustomFieldFiltersItem",
    "ContactsListQueryTagFiltersItem",
    "ContactsMetaWindowResponse",
    "ContactsMetaWindowResponseVariant2",
    "ContactsMetaWindowResponseVariant3",
    "ConversationAssignedEvent",
    "ConversationAssignedEventData",
    "ConversationAssignedEventDataAssignee",
    "ConversationAssignedEventDataContact",
    "ConversationClosedEvent",
    "ConversationClosedEventData",
    "ConversationClosedEventDataContact",
    "ConversationsCountAllResponse",
    "ConversationsCountClosedResponse",
    "ConversationsCountOpenResponse",
    "ConversationsCountUnreadResponse",
    "ConversationsCountUnreadResponseVariant2",
    "ConversationsMarkAllReadResponse",
    "ConversationsMarkAllUnreadResponse",
    "ConversationsMessageResource",
    "ConversationsMessageResourceAiAssistant",
    "CustomFieldResource",
    "CustomFieldTypeEnum",
    "DailyReportGeneratedEvent",
    "DailyReportGeneratedEventData",
    "DailyReportGeneratedEventDataPeriod",
    "DeviceConnectedEvent",
    "DeviceConnectedEventData",
    "DeviceConnectionEventEnum",
    "DeviceConnectionEventResource",
    "DeviceDeletedEvent",
    "DeviceDeletedEventData",
    "DeviceDisconnectedEvent",
    "DeviceDisconnectedEventData",
    "DeviceDisplayNameReviewedEvent",
    "DeviceDisplayNameReviewedEventData",
    "DeviceHealthChangedEvent",
    "DeviceHealthChangedEventData",
    "DeviceHealthDetailResource",
    "DeviceHealthDetailResourceHistoryItem",
    "DeviceMessagingLimitChangedEvent",
    "DeviceMessagingLimitChangedEventData",
    "DeviceQualityChangedEvent",
    "DeviceQualityChangedEventData",
    "DeviceResource",
    "DeviceResourceAbilities",
    "DeviceResourceCapabilities",
    "DeviceResourceCapabilitiesGroups",
    "DeviceResourceCapabilitiesMessages",
    "DevicesCreateResponse",
    "DevicesMeResponse",
    "DevicesQrResponse",
    "FlowCompletedEvent",
    "FlowCompletedEventData",
    "FlowCompletedEventDataContact",
    "FlowCompletedEventDataFlow",
    "FlowFailedEvent",
    "FlowFailedEventData",
    "FlowFailedEventDataContact",
    "FlowFailedEventDataFlow",
    "FormsAddNumberResponse",
    "FormsCreateResponse",
    "FormsCreateVersionResponse",
    "FormsDefinitionResponse",
    "FormsDefinitionResponseData",
    "FormsMetricsResponse",
    "FormsNumbersResponse",
    "FormsPublishResponse",
    "FormsRemoveNumberResponse",
    "FormsRetrieveResponse",
    "FormsRetrieveResponseResponse",
    "FormsRetrieveResponseVersionsItem",
    "FormsRetryNumbersResponse",
    "FormsSyncResponse",
    "FormsTemplatesResponse",
    "FormsTemplatesResponseDataItem",
    "FormsUpdateResponse",
    "FormsVersionsResponse",
    "FormsVersionsResponseDataItem",
    "ForwardMessageRequest",
    "ForwardMessageRequestTargetsItem",
    "ForwardMessageRequestTargetsItem2",
    "GroupActionCompletedEvent",
    "GroupActionCompletedEventData",
    "GroupActionCompletedEventDataAction",
    "GroupActionCompletedEventDataCampaign",
    "GroupActionCompletedEventDataGroup",
    "GroupActionCompletedEventDataResult",
    "GroupActionCompletedEventDataResultMessage",
    "GroupActionFailedEvent",
    "GroupActionFailedEventData",
    "GroupActionFailedEventDataAction",
    "GroupActionFailedEventDataCampaign",
    "GroupActionFailedEventDataGroup",
    "GroupActionFailedEventDataPipeline",
    "GroupBlockedEvent",
    "GroupBlockedEventData",
    "GroupBlockedEventDataCampaign",
    "GroupBlockedEventDataGroup",
    "GroupCreatedEvent",
    "GroupCreatedEventData",
    "GroupCreatedEventDataCampaign",
    "GroupCreatedEventDataGroup",
    "GroupFullEvent",
    "GroupFullEventData",
    "GroupFullEventDataCampaign",
    "GroupFullEventDataGroup",
    "GroupInviteLinkDownEvent",
    "GroupInviteLinkDownEventData",
    "GroupInviteLinkDownEventDataCampaign",
    "GroupInviteLinkDownEventDataGroup",
    "GroupInviteLinkRenewedEvent",
    "GroupInviteLinkRenewedEventData",
    "GroupInviteLinkRenewedEventDataCampaign",
    "GroupInviteLinkRenewedEventDataGroup",
    "GroupJoinRequestCreatedEvent",
    "GroupJoinRequestCreatedEventData",
    "GroupJoinRequestCreatedEventDataGroup",
    "GroupJoinRequestCreatedEventDataParticipant",
    "GroupJoinRequestRevokedEvent",
    "GroupJoinRequestRevokedEventData",
    "GroupJoinRequestRevokedEventDataGroup",
    "GroupJoinRequestRevokedEventDataParticipant",
    "GroupMessageReceivedEvent",
    "GroupMessageReceivedEventData",
    "GroupMessageReceivedEventDataGroup",
    "GroupMessageReceivedEventDataMessage",
    "GroupMessageReceivedEventDataParticipant",
    "GroupMetadataResource",
    "GroupMinResource",
    "GroupParticipantJoinedEvent",
    "GroupParticipantJoinedEventData",
    "GroupParticipantJoinedEventDataCampaign",
    "GroupParticipantJoinedEventDataGroup",
    "GroupParticipantJoinedEventDataParticipant",
    "GroupParticipantLeftEvent",
    "GroupParticipantLeftEventData",
    "GroupParticipantLeftEventDataCampaign",
    "GroupParticipantLeftEventDataGroup",
    "GroupParticipantLeftEventDataParticipant",
    "GroupReactionAddedEvent",
    "GroupReactionAddedEventData",
    "GroupReactionAddedEventDataGroup",
    "GroupReactionAddedEventDataMessage",
    "GroupReactionAddedEventDataParticipant",
    "GroupRecoveredEvent",
    "GroupRecoveredEventData",
    "GroupRecoveredEventDataCampaign",
    "GroupRecoveredEventDataGroup",
    "GroupResource",
    "GroupsFollowResponse",
    "GroupsRetrieveActionResponse",
    "MacExpiringEvent",
    "MacExpiringEventData",
    "MacUsage100Event",
    "MacUsage100EventData",
    "MacUsage80Event",
    "MacUsage80EventData",
    "MessageOriginEnum",
    "MessageReceivedEvent",
    "MessageReceivedEventData",
    "MessageReceivedEventDataContact",
    "MessageReceivedEventDataMessage",
    "MessageReceivedEventDataMessageMedia",
    "MessageReceivedEventDataReceiver",
    "MessageStatusChangedEvent",
    "MessageStatusChangedEventData",
    "MessageStatusChangedEventDataError",
    "MessageStatusEnum",
    "MessageTemplateResource",
    "MessageTemplateStatusEnum",
    "MessageTemplateTypeEnum",
    "MessageTypeEnum",
    "MessagesForwardResponseItem",
    "MessagesSendContactCardResponse",
    "MessagesSendDirectResponse",
    "MessagesSendFormResponse",
    "MessagesSendResponse",
    "ParticipantEventResource",
    "ParticipantResource",
    "PendingDeviceConnection",
    "PendingDeviceQr",
    "PendingExternalReference",
    "PendingForm",
    "PendingFormLintIssue",
    "PendingFormNumber",
    "PendingGroupAction",
    "PendingGroupActionGroup",
    "PendingGroupActionResult",
    "PendingGroupActionResultGroup",
    "PendingGroupActionResultMessage",
    "PendingGroupParticipantResult",
    "PendingWebhookDevice",
    "PendingWebhookSubscriptionFilters",
    "PendingWebhookSubscriptionWithSecret",
    "PipelineFinishedEvent",
    "PipelineFinishedEventData",
    "PipelineFinishedEventDataActions",
    "PipelineFinishedEventDataCampaign",
    "PipelineFinishedEventDataPipeline",
    "PollVotedEvent",
    "PollVotedEventData",
    "PollVotedEventDataGroup",
    "PollVotedEventDataParticipant",
    "PollVotedEventDataPoll",
    "PollVotedEventDataScheduledMessage",
    "PublicMessageResource",
    "ScheduledMessageFinishedEvent",
    "ScheduledMessageFinishedEventData",
    "ScheduledMessageFinishedEventDataGroups",
    "ScheduledMessageFinishedEventDataScheduledMessage",
    "ScheduledMessageGroupDeliveryFailedEvent",
    "ScheduledMessageGroupDeliveryFailedEventData",
    "ScheduledMessageGroupDeliveryFailedEventDataGroup",
    "ScheduledMessageGroupDeliveryFailedEventDataScheduledMessage",
    "ScheduledMessageResource",
    "ScheduledMessageResponseReceivedEvent",
    "ScheduledMessageResponseReceivedEventData",
    "ScheduledMessageResponseReceivedEventDataGroup",
    "ScheduledMessageResponseReceivedEventDataParticipant",
    "ScheduledMessageResponseReceivedEventDataResponse",
    "ScheduledMessageResponseReceivedEventDataScheduledMessage",
    "SendDirectMessageRequest",
    "SendGroupMessageRequest",
    "SendMessageRequest",
    "SendMessageRequestLinkPreviewMeta",
    "SendMessageRequestLinkPreviewMeta2",
    "SendMessageRequestOptionsItem",
    "SendMessageRequestOptionsItem2",
    "SendWhatsappFormRequest",
    "StoreConnectLinkRequest",
    "StoreContactCardRequest",
    "StoreContactNoteRequest",
    "StoreContactRequest",
    "StoreDeviceRequest",
    "StoreMessageReactionRequest",
    "StoreMessageTemplateRequest",
    "StoreMessageTemplateRequestButtonsItem",
    "StoreMessageTemplateRequestButtonsItem2",
    "StoreWebhookSubscriptionRequest",
    "StoreWebhookSubscriptionRequestFilters",
    "StoreWebhookSubscriptionRequestFilters2",
    "SubscriptionCancellationConfirmedEvent",
    "SubscriptionCancellationConfirmedEventData",
    "SubscriptionDormantEndingEvent",
    "SubscriptionDormantEndingEventData",
    "SubscriptionExpiringEvent",
    "SubscriptionReactivatedEvent",
    "SubscriptionReactivatedEventData",
    "SubscriptionTrialEndingEvent",
    "SubscriptionTrialEndingEventData",
    "TagResource",
    "TemplateResource",
    "TemplateStatusChangedEvent",
    "TemplateStatusChangedEventData",
    "TemplateStatusChangedEventDataTemplate",
    "TemplatesQuickReplyButtonsResponse",
    "TemplatesSendBodyTemplateVariables",
    "TemplatesSendResponse",
    "UpdateContactRequest",
    "UpdateMessageTemplateRequest",
    "UpdateMessageTemplateRequestButtonsItem",
    "UpdateMessageTemplateRequestButtonsItem2",
    "UpdateWebhookSubscriptionRequest",
    "UpdateWebhookSubscriptionRequestFilters",
    "UpdateWebhookSubscriptionRequestFilters2",
    "WebhookEvent",
    "WebhookEventType",
    "WebhookSubscriptionCreatedResource",
    "WebhookSubscriptionDeliveryResource",
    "WebhookSubscriptionResource",
    "WebhookTestEvent",
    "WebhookTestEventData",
    "WebhooksEventsResponse",
    "WebhooksEventsResponseMeta",
    "WebhooksListResponseVariant2",
    "WebhooksListResponseVariant2Links",
    "WebhooksListResponseVariant2Meta",
    "WebhooksListResponseVariant2MetaLinksItem",
    "WebhooksTestResponse",
    "WhatsAppProviderEnum",
    "WhatsappFormCompletedEvent",
    "WhatsappFormCompletedEventData",
    "WhatsappFormCompletedEventDataAnswersItem",
    "WhatsappFormCompletedEventDataForm",
]


class ContactsListQueryTagFiltersItem(TypedDict):
    mode: Literal["all", "any", "exclude"]
    tag_ids: NotRequired[List[int]]


class ContactsListQueryCustomFieldFiltersItem(TypedDict):
    type: Literal["0", "1", "2", "3", "4"]
    mode: NotRequired[Optional[Literal["all", "any", "exclude"]]]
    value: NotRequired[Optional[str]]
    date_from: NotRequired[Optional[str]]
    date_to: NotRequired[Optional[str]]
    numeric_operator: NotRequired[Optional[Literal["lt", "eq", "gt"]]]
    numeric_value: NotRequired[Optional[float]]
    date_operator: NotRequired[Optional[Literal["lt", "gt", "eq", "period"]]]
    custom_field_ids: NotRequired[List[int]]


class ContactResource(TypedDict):
    id: int
    name: str
    email: str
    phone: str
    whatsapp_id: str
    whatsapp_username: NotRequired[Optional[str]]
    has_phone: bool
    country_code: str
    status: int
    image: str
    notes: Optional[str]
    custom_fields: NotRequired[List[ContactCustomFieldResource]]
    created_at: Optional[str]
    active_conversation: int
    favorite: int
    unread_messages: int
    manually_unread: NotRequired[bool]
    last_message: NotRequired[ContactResourceLastMessage]
    device_id: Optional[int]
    adviser_id: Optional[int]
    paused_at: Optional[str]
    mac_date: Optional[str]
    is_mac_inactive: NotRequired[bool]
    ai_assistant_name: Optional[str]
    ai_assistant_email: NotRequired[str]
    account_main_email: NotRequired[str]
    stage_since: NotRequired[str]
    is_stagnant: NotRequired[bool]
    follow_up_date: NotRequired[Optional[str]]
    lead_score: NotRequired[ContactResourceLeadScore]
    name_mismatch: NotRequired[Optional[List[Any]]]


class ContactCustomFieldResource(TypedDict):
    id: int
    name: str
    description: str
    type: str
    value: str
    created_at: str
    updated_at: str
    contact_count: str


class ContactResourceLastMessage(TypedDict):
    text: str
    file: str
    date: str
    type: str
    own: str
    deleted_at: str
    deleted_scope: str


class ContactResourceLeadScore(TypedDict):
    score: int
    signals_count: int
    category: str
    confidence: str
    disqualified: bool
    disqualified_at: Optional[str]
    updated_at: Optional[str]


class StoreContactRequest(TypedDict, total=False):
    phone: str
    whatsapp_id: str
    name: Optional[str]
    email: Optional[str]
    image: Optional[str]
    deviceId: Optional[int]


class UpdateContactRequest(TypedDict, total=False):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    notes: Optional[str]
    status: int
    adviser_id: Optional[int]
    active_conversation: bool
    favorite: bool
    fixed: bool
    image: Optional[str]
    can_execute_flows: bool
    manually_unread: bool


class ContactsDeleteBodyTagFiltersItem(TypedDict):
    tag_ids: List[int]
    mode: Literal["all", "any", "exclude"]


class ContactsDeleteBodyCustomFieldFiltersItem(TypedDict):
    custom_field_ids: List[int]
    type: Literal["0", "1", "2", "3", "4"]
    mode: NotRequired[Optional[Literal["all", "any", "exclude"]]]
    value: NotRequired[Optional[str]]
    date_from: NotRequired[Optional[str]]
    date_to: NotRequired[Optional[str]]
    numeric_operator: NotRequired[Optional[Literal["lt", "eq", "gt"]]]
    numeric_value: NotRequired[Optional[float]]
    date_operator: NotRequired[Optional[Literal["lt", "gt", "eq", "period"]]]


class ContactTagResource(TypedDict):
    id: int
    name: str
    description: str
    color: str
    created_at: Optional[str]
    updated_at: Optional[str]
    contact_count: str
    assigned_at: Optional[str]
    last_updated: Optional[str]


class ContactsAttachCustomFieldBodyItem(TypedDict):
    customFieldId: int
    contactId: int
    value: str


class ContactsAttachCustomFieldResponseItem(TypedDict):
    message: Literal["No autorizado: el campo personalizado no pertenece al usuario autenticado."]
    status: Literal[403]


class ContactsAttachCustomFieldResponseItemVariant2(TypedDict):
    message: Literal["No autorizado: el contacto no pertenece al usuario autenticado."]
    status: Literal[403]


class ContactsAttachCustomFieldResponseItemVariant3(TypedDict):
    message: Literal["Custom field value attached successfully."]
    status: Literal[201]


class ContactsDetachCustomFieldBodyItem(TypedDict):
    customFieldId: int
    contactId: int


class ContactsDetachCustomFieldResponse(TypedDict):
    messages: List[str]


class ContactsMetaWindowResponse(TypedDict):
    is_open: bool
    meta_device_id: None
    expires_at: None


class ContactsMetaWindowResponseVariant2(TypedDict):
    is_open: bool
    meta_device_id: None
    expires_at: Optional[str]


class ContactsMetaWindowResponseVariant3(TypedDict):
    is_open: bool
    meta_device_id: Any
    expires_at: Optional[str]


class ContactNoteResource(TypedDict):
    id: int
    contact_id: int
    author_id: Optional[int]
    author_name: Any
    body: str
    created_at: Optional[str]
    updated_at: Optional[str]


class StoreContactNoteRequest(TypedDict):
    body: str


class ConversationsCountUnreadResponse(TypedDict):
    count: int


class ConversationsCountUnreadResponseVariant2(TypedDict):
    count: int
    mine: int


class ConversationsCountOpenResponse(TypedDict):
    count: int


class ConversationsCountClosedResponse(TypedDict):
    count: Optional[int]


class ConversationsCountAllResponse(TypedDict):
    count: int


class ConversationsMarkAllReadResponse(TypedDict):
    message: Literal["Todas las conversaciones han sido marcadas como leídas"]
    updated_count: int


class ConversationsMarkAllUnreadResponse(TypedDict):
    message: Literal["Todas las conversaciones elegibles fueron marcadas como no leídas"]
    marked_count: int
    limit_reached: bool
    contact_ids: Dict[str, Any]


class SendMessageRequest(TypedDict):
    phone: NotRequired[str]
    whatsapp_id: NotRequired[str]
    device_id: int
    text: NotRequired[str]
    contact_id: int
    file: NotRequired[str]
    file_type: NotRequired[Optional[Literal["image", "video", "audio", "document", "sticker"]]]
    file_name: NotRequired[Optional[str]]
    temporal_uuid: NotRequired[str]
    note: NotRequired[bool]
    mentions: NotRequired[Optional[List[int]]]
    options: NotRequired[List[SendMessageRequestOptionsItem]]
    reference_message_uid: NotRequired[Optional[str]]
    client_reference: NotRequired[Optional[str]]
    link_preview: NotRequired[bool]
    link_preview_meta: NotRequired[SendMessageRequestLinkPreviewMeta]


class SendMessageRequestOptionsItem(TypedDict, total=False):
    id: str
    label: str


class SendMessageRequestLinkPreviewMeta(TypedDict, total=False):
    url: str
    title: Optional[str]
    description: Optional[str]
    image_url: Optional[str]
    domain: str


class SendMessageRequestOptionsItem2(TypedDict, total=False):
    id: str
    label: str


class SendMessageRequestLinkPreviewMeta2(TypedDict, total=False):
    url: str
    title: Optional[str]
    description: Optional[str]
    image_url: Optional[str]
    domain: str


class MessagesSendResponse(TypedDict):
    message: PublicMessageResource


class PublicMessageResource(TypedDict):
    id: int
    contact_id: Optional[int]
    device_id: Optional[int]
    direction: Literal["outbound", "inbound"]
    type: Literal["text", "image", "video", "document", "sticker", "contact", "audio", "note", "action", "invalid", "interactive", "location", "voice_call", "video_call", "event", "button", "template", "notification", "option_list", "template_button_reply", "poll", "whatsapp_form", "call_permission_request", "call_permission_reply", "request_contact_info"]
    status: Optional[Literal["sent", "delivered", "read", "failed", "queued"]]
    error: Optional[Dict[str, Any]]
    client_reference: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]


class SendDirectMessageRequest(TypedDict):
    device_id: int
    text: NotRequired[str]
    contact_id: NotRequired[Optional[int]]
    phone: NotRequired[Optional[str]]
    whatsapp_id: NotRequired[Optional[str]]
    file: NotRequired[str]
    file_type: NotRequired[Optional[Literal["image", "video", "audio", "document", "sticker"]]]
    file_name: NotRequired[Optional[str]]
    temporal_uuid: NotRequired[str]
    local_id: NotRequired[Optional[str]]
    note: NotRequired[bool]
    mentions: NotRequired[Optional[List[int]]]
    client_reference: NotRequired[Optional[str]]


class MessagesSendDirectResponse(TypedDict):
    message: PublicMessageResource


class SendWhatsappFormRequest(TypedDict):
    form_id: int
    device_id: int
    text: NotRequired[str]
    button_text: NotRequired[str]
    client_reference: NotRequired[Optional[str]]


class MessagesSendFormResponse(TypedDict):
    message: PublicMessageResource


class ConversationsMessageResource(TypedDict):
    chat_id: str
    contact_id: Union[int, Literal[""]]
    content: Union[List[Any], Dict[str, Any], str]
    device_id: Union[int, Literal[""]]
    error_code: str
    file: str
    forwarded: int
    group_id: Union[int, Literal[""]]
    id: int
    origin: Union[MessageOriginEnum, Literal[""]]
    origin_id: Union[int, Literal[""]]
    own: int
    reference_message: Optional[str]
    reference_message_uid: Optional[str]
    is_quotable: bool
    status: Optional[MessageStatusEnum]
    temporal_uuid: str
    text: str
    time: Optional[str]
    type: Optional[MessageTypeEnum]
    uid: str
    info: Union[List[Any], Literal[""]]
    user_id: int
    deleted_at: Optional[str]
    deleted_scope: Optional[str]
    deleted_by: Optional[int]
    edited_at: Optional[str]
    poll_results: NotRequired[str]
    event_rsvps: NotRequired[str]
    form_answers: NotRequired[str]
    reactions: List[Any]
    file_original_name: Optional[str]
    client_reference: Optional[str]
    scheduled: NotRequired[bool]
    ai_assistant: NotRequired[ConversationsMessageResourceAiAssistant]


class ConversationsMessageResourceAiAssistant(TypedDict):
    name: str
    email: str
    account_main_email: str


class StoreContactCardRequest(TypedDict):
    device_id: int
    contact_card_ids: List[int]
    client_reference: NotRequired[Optional[str]]


class MessagesSendContactCardResponse(TypedDict):
    messages: List[PublicMessageResource]


class ForwardMessageRequest(TypedDict):
    targets: List[ForwardMessageRequestTargetsItem]
    client_reference: NotRequired[Optional[str]]


class ForwardMessageRequestTargetsItem(TypedDict):
    contact_id: int
    device_id: int


class ForwardMessageRequestTargetsItem2(TypedDict):
    contact_id: int
    device_id: int


class MessagesForwardResponseItem(TypedDict):
    contact_id: int
    mode: Literal["internal", "native"]
    status: Literal["queued", "blocked"]
    reason: Optional[str]
    message: Optional[PublicMessageResource]


class StoreMessageReactionRequest(TypedDict):
    emoji: str


class TemplateResource(TypedDict):
    id: int
    name: str
    text: str
    header: str
    footer: str
    observation: str
    uid: str
    category: str
    type: Union[MessageTemplateTypeEnum, Literal[""]]
    status: Union[MessageTemplateStatusEnum, Literal[""]]
    language_code: str
    upload_session_id: str
    header_handle: str
    file: str
    params: Union[List[Any], Literal[""]]
    buttons: Union[List[Any], Literal[""]]
    user_id: int
    device_id: int
    created_at: Optional[str]
    recategorized_at: Optional[str]
    quick_reply_buttons: List[Any]
    waba_id: Optional[str]
    belongs_to_current_device: bool
    quality_score: str
    quality_updated_at: str
    quality: str
    available: bool


class StoreMessageTemplateRequest(TypedDict):
    name: str
    language_code: Literal["af", "sq", "ar", "ar_EG", "ar_AE", "ar_LB", "ar_MA", "ar_QA", "az", "be_BY", "bn", "bn_IN", "bg", "ca", "zh_CN", "zh_HK", "zh_TW", "hr", "cs", "da", "prs_AF", "nl", "nl_BE", "en", "en_GB", "en_US", "en_AE", "en_AU", "en_CA", "en_GH", "en_IE", "en_IN", "en_JM", "en_MY", "en_NZ", "en_QA", "en_SG", "en_UG", "en_ZA", "et", "fil", "fi", "fr", "fr_BE", "fr_CA", "fr_CH", "fr_CI", "fr_MA", "ka", "de", "de_AT", "de_CH", "el", "gu", "ha", "he", "hi", "hu", "id", "ga", "it", "ja", "kn", "kk", "rw_RW", "ko", "ky_KG", "lo", "lv", "lt", "mk", "ms", "ml", "mr", "nb", "ps_AF", "fa", "pl", "pt_BR", "pt_PT", "pa", "ro", "ru", "sr", "si_LK", "sk", "sl", "es", "es_AR", "es_CL", "es_CO", "es_CR", "es_DO", "es_EC", "es_HN", "es_MX", "es_PA", "es_PE", "es_ES", "es_UY", "sw", "sv", "ta", "te", "th", "tr", "uk", "ur", "uz", "vi", "zu"]
    category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"]
    type: Literal["text", "image", "document", "video", "location", "default"]
    header: NotRequired[Optional[str]]
    file: NotRequired[str]
    body: str
    params: NotRequired[Optional[List[str]]]
    footer: NotRequired[Optional[str]]
    buttons: NotRequired[Optional[List[StoreMessageTemplateRequestButtonsItem]]]


class StoreMessageTemplateRequestButtonsItem(TypedDict, total=False):
    text: str
    type: Literal["QUICK_REPLY", "URL", "PHONE_NUMBER"]
    url: str
    phone_number: str


class StoreMessageTemplateRequestButtonsItem2(TypedDict, total=False):
    text: str
    type: Literal["QUICK_REPLY", "URL", "PHONE_NUMBER"]
    url: str
    phone_number: str


class UpdateMessageTemplateRequest(TypedDict):
    device_id: int
    category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"]
    type: Literal["text", "image", "document", "video", "location", "default"]
    header: NotRequired[Optional[str]]
    file: NotRequired[str]
    body: str
    params: NotRequired[Optional[List[str]]]
    footer: NotRequired[Optional[str]]
    buttons: NotRequired[Optional[List[UpdateMessageTemplateRequestButtonsItem]]]


class UpdateMessageTemplateRequestButtonsItem(TypedDict, total=False):
    text: str
    type: Literal["QUICK_REPLY", "URL", "PHONE_NUMBER"]
    url: str
    phone_number: str


class UpdateMessageTemplateRequestButtonsItem2(TypedDict, total=False):
    text: str
    type: Literal["QUICK_REPLY", "URL", "PHONE_NUMBER"]
    url: str
    phone_number: str


class TemplatesQuickReplyButtonsResponse(TypedDict):
    data: List[Any]


class TemplatesSendBodyTemplateVariables(TypedDict, total=False):
    body: List[Optional[str]]


class TemplatesSendResponse(TypedDict):
    message: PublicMessageResource


class PendingForm(TypedDict):
    id: int
    family_id: int
    name: str
    label: str
    category: NotRequired[Optional[str]]
    status: Literal["draft", "published", "deprecated"]
    version: int
    definition: NotRequired[Any]
    fields: NotRequired[Any]
    mapping: NotRequired[Any]
    tag_rules: NotRequired[Any]
    has_endpoint: NotRequired[bool]
    first_screen: NotRequired[Optional[str]]
    first_screen_dynamic: NotRequired[Optional[bool]]
    lint_errors_count: NotRequired[Optional[int]]
    draft_id: NotRequired[int]
    draft_version: NotRequired[int]
    sends: NotRequired[int]
    responses: NotRequired[int]
    meta_flow_id: NotRequired[Optional[str]]
    flow_json: NotRequired[Any]
    validation_errors: NotRequired[Any]
    published_at: NotRequired[Optional[str]]
    updated_at: NotRequired[Optional[str]]


class FormsTemplatesResponse(TypedDict):
    data: List[FormsTemplatesResponseDataItem]


class FormsTemplatesResponseDataItem(TypedDict):
    key: str
    title: str
    description: NotRequired[Optional[str]]
    category: NotRequired[Optional[str]]


class FormsCreateResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]
    numbers: NotRequired[List[PendingFormNumber]]


class PendingFormLintIssue(TypedDict):
    code: str
    severity: str
    screenId: NotRequired[Optional[str]]
    itemId: NotRequired[Optional[str]]
    message: str


class PendingFormNumber(TypedDict):
    device_id: Optional[int]
    primary: bool
    status: Literal["draft", "publishing", "published", "failed"]
    error: Optional[str]


class FormsRetrieveResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]
    versions: NotRequired[List[FormsRetrieveResponseVersionsItem]]
    numbers: NotRequired[List[PendingFormNumber]]


class FormsRetrieveResponseVersionsItem(TypedDict, total=False):
    id: int
    version: int
    status: str
    published_at: Optional[str]


class FormsUpdateResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]


class FormsCreateVersionResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]
    created: NotRequired[bool]
    numbers: NotRequired[List[PendingFormNumber]]


class FormsSyncResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]
    numbers: NotRequired[List[PendingFormNumber]]


class FormsPublishResponse(TypedDict):
    data: PendingForm
    lint: NotRequired[List[PendingFormLintIssue]]
    numbers: NotRequired[List[PendingFormNumber]]


class FormsNumbersResponse(TypedDict):
    numbers: List[PendingFormNumber]


class FormsAddNumberResponse(TypedDict):
    numbers: List[PendingFormNumber]


class FormsRemoveNumberResponse(TypedDict):
    numbers: List[PendingFormNumber]


class FormsRetryNumbersResponse(TypedDict):
    numbers: List[PendingFormNumber]


class FormsDefinitionResponse(TypedDict):
    data: Optional[FormsDefinitionResponseData]


class FormsDefinitionResponseData(TypedDict, total=False):
    family_id: int
    form_id: int
    name: str
    status: str
    version: int
    definition: Any


class FormsVersionsResponse(TypedDict):
    data: List[FormsVersionsResponseDataItem]


class FormsVersionsResponseDataItem(TypedDict, total=False):
    id: int
    version: int
    name: str
    status: str
    is_current: bool
    published_at: Optional[str]
    deprecated_at: Optional[str]
    meta_flow_id: Optional[str]
    retained_reason: Optional[str]
    responses: int
    templates: Any


class FormsRetrieveResponseResponse(TypedDict):
    data: Any


class FormsMetricsResponse(TypedDict):
    data: Any


class TagResource(TypedDict):
    id: int
    name: str
    description: str
    color: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    contact_count: Union[str, int]


class CustomFieldResource(TypedDict):
    id: int
    name: str
    type: CustomFieldTypeEnum
    description: Optional[str]
    contact_count: NotRequired[int]
    created_at: Optional[str]


class GroupResource(TypedDict):
    id: Any
    admins_numbers: Any
    admins: Any
    admins_count: Any
    owner: Any
    owner_display_phone: Any
    owner_connected: Any
    clicks: Any
    communityUid: Any
    newsletterUid: Any
    description: Any
    deviceId: Any
    image: Any
    isFull: Any
    isApi: Any
    link: str
    campaign_link: str
    campaign_custom_domain: Optional[str]
    name: str
    order: str
    participants_numbers: str
    participants_count: str
    read_rate: Optional[int]
    read_rate_messages_count: int
    status: str
    uid: str
    updatedAt: str
    createdAt: str
    scheduled_message_count: Union[str, Literal[0]]
    type: str
    manual_import: bool
    participantMode: bool
    ownNumbers: Optional[str]
    adminOnlyMessage: Optional[bool]
    origin: Literal[1, 0]
    lastSyncAt: Optional[str]


class GroupMinResource(TypedDict):
    uid: str
    name: str
    description: str
    device_id: str
    alias: str
    number: str
    communityUid: str


class GroupMetadataResource(TypedDict):
    name: str
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
    admins_numbers: List[str]
    participants_numbers: List[str]
    verified_admin: bool
    membership: str
    subscribers_count: int
    participants: List[Any]
    owner: Optional[str]


class ChannelMetadataResource(TypedDict):
    name: Optional[str]
    description: Optional[str]
    image: Optional[str]
    link: Optional[str]
    admins_numbers: List[str]
    participants_numbers: List[str]
    verified_admin: bool
    subscribers_count: Union[str, Literal[0]]
    participants: List[str]


class ParticipantResource(TypedDict):
    id: str
    phone: str
    action: str
    isAdmin: str
    created_at: str


class ParticipantEventResource(TypedDict):
    phone: str
    whatsapp_id: str
    event_type: Literal["join", "leave"]
    event_at: Optional[str]
    group_id: int
    group_name: str
    country_code: str
    country_name: str


class CommunitiesMessageResource(TypedDict):
    id: str
    uid: str
    type: str
    value: Any
    scheduledMessage: ScheduledMessageResource


class ScheduledMessageResource(TypedDict):
    id: str
    name: str
    send_at: str
    status: str
    type: str
    audience: str
    total_readed: str
    total_played: str
    campaigns: str
    groups: str
    total_groups: str
    messages: List[MessageTemplateResource]


class MessageTemplateResource(TypedDict):
    id: str
    type: str
    value: str
    metrics: str
    reactions: str
    votes: str
    event_responses: str
    shipping_order: str


class ActionGroupResource2(TypedDict):
    id: str
    name: str
    status: str
    info: Any
    action_name: str
    action_label: Optional[str]
    executed_at: Optional[str]
    executed_by: Optional[str]
    groups: Union[str, List[str]]


class ActionGroupResourceVariant2(TypedDict):
    id: str
    name: Optional[str]
    status: str
    info: Any
    action_name: Optional[str]
    action_label: Optional[str]
    executed_at: Optional[str]
    executed_by: Optional[str]
    groups: Union[List[Any], List[str]]


class SendGroupMessageRequest(TypedDict):
    device_id: int
    type: Literal["text", "image", "video", "audio", "document"]
    text: NotRequired[str]
    media_url: NotRequired[str]
    caption: NotRequired[str]
    file_name: NotRequired[str]


class ApiGroupActionAcceptedResource(TypedDict):
    action_id: str
    status: Literal["queued"]


class ApiGroupDeviceRequest(TypedDict):
    device_id: int


class GroupsFollowResponse(TypedDict):
    data: ApiGroupImportResource


class ApiGroupImportResource(TypedDict):
    uid: str
    name: Optional[str]
    imported: bool
    is_admin: bool


class GroupsRetrieveActionResponse(TypedDict):
    data: PendingGroupAction


class PendingGroupAction(TypedDict):
    action_id: str
    type: str
    status: Literal["queued", "running", "completed", "failed"]
    device_id: Optional[int]
    group: Optional[PendingGroupActionGroup]
    result: Optional[PendingGroupActionResult]
    reason: Optional[str]
    created_at: Optional[str]
    started_at: Optional[str]
    completed_at: Optional[str]
    failed_at: Optional[str]


class PendingGroupActionGroup(TypedDict):
    uid: str
    name: Optional[str]


class PendingGroupActionResult(TypedDict, total=False):
    message: PendingGroupActionResultMessage
    participants: List[PendingGroupParticipantResult]
    invite_link: str
    group: PendingGroupActionResultGroup


class PendingGroupActionResultMessage(TypedDict, total=False):
    uid: str


class PendingGroupParticipantResult(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    status: Literal["added", "invited", "removed", "promoted", "demoted", "approved", "rejected", "failed"]
    reason: Optional[str]


class PendingGroupActionResultGroup(TypedDict, total=False):
    uid: str
    name: Optional[str]


class DeviceResource(TypedDict):
    id: int
    alias: str
    image: str
    color: str
    number: str
    normalized_number: str
    first_conecction_at: str
    user_id: int
    provider: WhatsAppProviderEnum
    waba_id: str
    whatsapp_username: Optional[str]
    is_business: int
    connected: int
    active: Optional[int]
    health: str
    number_key: Optional[str]
    number_key_confirmed: str
    is_coexistence: bool
    slot_state: str
    pool_suspended: bool
    pool_suspension_reason: Optional[str]
    pool_keep: bool
    qr_allowed: bool
    can_change_to_meta: bool
    connected_by_user_id: Optional[int]
    connected_by_name: Optional[str]
    abilities: DeviceResourceAbilities
    capabilities: DeviceResourceCapabilities
    connection: Optional[Literal["qr", "coexistence", "dedicated"]]
    external_reference: Optional[str]
    overloaded: bool
    overloaded_computed_at: Optional[str]
    overloaded_groups_count: Optional[int]
    overloaded_one_to_one_count: Optional[int]
    overloaded_has_pending_broadcast: bool
    overloaded_has_active_flow: bool
    overloaded_has_active_ai_agent: bool
    overloaded_alert_level: str
    overloaded_dismissed_at: Optional[str]
    sync_all_groups: bool


class DeviceResourceAbilities(TypedDict):
    connect: bool
    disconnect: bool
    delete: bool
    update: bool


class DeviceResourceCapabilities(TypedDict):
    messages: DeviceResourceCapabilitiesMessages
    groups: DeviceResourceCapabilitiesGroups
    statuses: List[str]


class DeviceResourceCapabilitiesMessages(TypedDict):
    text: bool
    media: bool
    buttons: bool
    lists: bool
    templates: bool
    location: bool
    voice_note: bool
    polls: bool
    events: bool
    contact_card: bool
    reactions: bool


class DeviceResourceCapabilitiesGroups(TypedDict):
    create: bool
    add_participants: Union[bool, Literal["direct", "invite"]]
    remove_participants: bool
    admins: bool
    photo: bool
    settings: bool
    invite_link: bool
    send: bool
    join_requests: Union[bool, Literal["list", "list_and_decide"]]


class StoreDeviceRequest(TypedDict):
    connection: Literal["qr"]
    alias: NotRequired[Optional[str]]
    external_reference: NotRequired[Optional[str]]
    same_number_as: NotRequired[Optional[int]]
    country: NotRequired[Optional[str]]


class DevicesCreateResponse(TypedDict):
    data: DeviceResource


class DevicesQrResponse(TypedDict):
    data: PendingDeviceQr


class PendingDeviceQr(TypedDict):
    connected: bool
    qr_code: Optional[str]
    expires_in: int


class DeviceHealthDetailResource(TypedDict):
    health: str
    identity: str
    entities: str
    throughput_level: str
    history: List[DeviceHealthDetailResourceHistoryItem]
    meta_billing: Optional[Dict[str, Any]]


class DeviceHealthDetailResourceHistoryItem(TypedDict):
    field: str
    previous_value: str
    new_value: str
    detail: Optional[str]
    source: str
    occurred_at: str


class DevicesMeResponse(TypedDict):
    phone: str
    locale: Literal[""]
    name: str
    avatar: str
    isBusiness: bool
    about: Literal[""]


class DeviceConnectionEventResource(TypedDict):
    id: int
    phone: Optional[str]
    event: DeviceConnectionEventEnum
    created_at: str


class StoreConnectLinkRequest(TypedDict):
    type: Literal["meta", "qr"]
    allowed_connection_types: NotRequired[List[Literal["coexistence", "dedicated"]]]
    provision_us_number: NotRequired[bool]
    device_id: NotRequired[Optional[int]]
    same_number_as: NotRequired[Optional[int]]
    country: NotRequired[Optional[str]]
    external_reference: NotRequired[Optional[str]]
    return_url: NotRequired[Optional[str]]
    expires_in_minutes: NotRequired[Optional[int]]


class ConnectLinksCreateResponse(TypedDict):
    data: ConnectLinkResource


class ConnectLinkResource(TypedDict):
    id: int
    type: str
    status: str
    url: str
    expires_at: str
    allowed_connection_types: Optional[List[str]]
    provision_us_number: bool
    country: Optional[str]
    device_id: Optional[int]
    external_reference: Optional[str]
    return_url: Optional[str]
    error_code: Optional[str]
    created_at: Optional[str]
    completed_at: Optional[str]


class ConnectLinksGetResponse(TypedDict):
    data: ConnectLinkResource


class WebhooksEventsResponse(TypedDict):
    data: List[Any]
    meta: WebhooksEventsResponseMeta


class WebhooksEventsResponseMeta(TypedDict):
    total: int
    active: int
    envelope_version: Literal["v1"]
    signature_header: Literal["X-Funnelchat-Signature"]
    signature_format: Literal["t=<unix>,v1=<hex hmac-sha256 de \"<t>.<cuerpo crudo>\" con el secreto del endpoint>"]


class WebhookSubscriptionResource(TypedDict):
    id: str
    url: str
    description: Optional[str]
    events: NotRequired[List[str]]
    filters: Optional[Dict[str, Any]]
    status: str
    disabled_reason: Optional[str]
    last_delivery_at: Optional[str]
    last_success_at: Optional[str]
    secret_rotated_at: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    migration: Optional[Dict[str, Any]]


class WebhooksListResponseVariant2(TypedDict):
    data: List[WebhookSubscriptionResource]
    links: WebhooksListResponseVariant2Links
    meta: WebhooksListResponseVariant2Meta


class WebhooksListResponseVariant2Links(TypedDict):
    first: Optional[str]
    last: Optional[str]
    prev: Optional[str]
    next: Optional[str]


WebhooksListResponseVariant2Meta = TypedDict("WebhooksListResponseVariant2Meta", {"current_page": int, "from": Optional[int], "last_page": int, "links": List["WebhooksListResponseVariant2MetaLinksItem"], "path": Optional[str], "per_page": int, "to": Optional[int], "total": int}, total=True)


class WebhooksListResponseVariant2MetaLinksItem(TypedDict):
    url: Optional[str]
    label: str
    active: bool


class StoreWebhookSubscriptionRequest(TypedDict):
    url: str
    description: NotRequired[Optional[str]]
    events: List[Literal["device.disconnected", "device.connected", "device.deleted", "device.health_changed", "device.quality_changed", "device.messaging_limit_changed", "device.display_name_reviewed", "billing.payment_failed", "billing.plan_blocked", "billing.upcoming_charge", "subscription.expiring", "subscription.trial_ending", "subscription.reactivated", "subscription.cancellation_confirmed", "subscription.dormant_ending", "ai_quota.low_balance", "ai_quota.topup_succeeded", "ai_quota.topup_failed", "mac.usage_80", "mac.usage_100", "mac.expiring", "account.blocked", "message.received", "flow.completed", "broadcast.finished", "contact.stage_changed", "message.status_changed", "conversation.closed", "conversation.assigned", "contact.tag_added", "broadcast.paused", "contact.tag_removed", "contact.created", "template.status_changed", "flow.failed", "whatsapp_form.completed", "group.created", "group.invite_link_down", "group.invite_link_renewed", "group_participant.joined", "group_participant.left", "scheduled_message.group_delivery_failed", "scheduled_message.response_received", "poll.voted", "pipeline.finished", "group.blocked", "group.recovered", "campaign.status_changed", "scheduled_message.finished", "group_action.failed", "daily_report.generated", "campaign.no_groups_available", "group.full", "group_action.completed", "group.message_received", "group.reaction_added", "group_join_request.created", "group_join_request.revoked"]]
    filters: NotRequired[StoreWebhookSubscriptionRequestFilters]


class StoreWebhookSubscriptionRequestFilters(TypedDict, total=False):
    campaign_ids: Optional[List[str]]


class StoreWebhookSubscriptionRequestFilters2(TypedDict, total=False):
    campaign_ids: Optional[List[str]]


class WebhookSubscriptionCreatedResource(TypedDict):
    id: str
    url: str
    description: Optional[str]
    events: NotRequired[List[str]]
    filters: Optional[Dict[str, Any]]
    status: str
    disabled_reason: Optional[str]
    last_delivery_at: Optional[str]
    last_success_at: Optional[str]
    secret_rotated_at: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    migration: Optional[Dict[str, Any]]
    secret: str
    secret_notice: Literal["Guarda este secreto ahora: es la única vez que se muestra. Con él validas la firma del header de cada entrega."]


class UpdateWebhookSubscriptionRequest(TypedDict):
    url: str
    description: NotRequired[Optional[str]]
    events: List[Literal["device.disconnected", "device.connected", "device.deleted", "device.health_changed", "device.quality_changed", "device.messaging_limit_changed", "device.display_name_reviewed", "billing.payment_failed", "billing.plan_blocked", "billing.upcoming_charge", "subscription.expiring", "subscription.trial_ending", "subscription.reactivated", "subscription.cancellation_confirmed", "subscription.dormant_ending", "ai_quota.low_balance", "ai_quota.topup_succeeded", "ai_quota.topup_failed", "mac.usage_80", "mac.usage_100", "mac.expiring", "account.blocked", "message.received", "flow.completed", "broadcast.finished", "contact.stage_changed", "message.status_changed", "conversation.closed", "conversation.assigned", "contact.tag_added", "broadcast.paused", "contact.tag_removed", "contact.created", "template.status_changed", "flow.failed", "whatsapp_form.completed", "group.created", "group.invite_link_down", "group.invite_link_renewed", "group_participant.joined", "group_participant.left", "scheduled_message.group_delivery_failed", "scheduled_message.response_received", "poll.voted", "pipeline.finished", "group.blocked", "group.recovered", "campaign.status_changed", "scheduled_message.finished", "group_action.failed", "daily_report.generated", "campaign.no_groups_available", "group.full", "group_action.completed", "group.message_received", "group.reaction_added", "group_join_request.created", "group_join_request.revoked"]]
    filters: NotRequired[UpdateWebhookSubscriptionRequestFilters]
    status: NotRequired[Literal["active", "paused"]]


class UpdateWebhookSubscriptionRequestFilters(TypedDict, total=False):
    campaign_ids: Optional[List[str]]


class UpdateWebhookSubscriptionRequestFilters2(TypedDict, total=False):
    campaign_ids: Optional[List[str]]


class PendingWebhookSubscriptionWithSecret(TypedDict):
    id: str
    url: str
    description: Optional[str]
    events: List[str]
    filters: PendingWebhookSubscriptionFilters
    status: Literal["active", "paused", "disabled"]
    disabled_reason: Optional[Literal["too_many_failures", "key_revoked"]]
    last_delivery_at: Optional[str]
    last_success_at: Optional[str]
    secret_rotated_at: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    migration: Optional[Dict[str, Any]]
    secret: str
    secret_notice: str


class PendingWebhookSubscriptionFilters(TypedDict, total=False):
    campaign_ids: List[str]


class WebhooksTestResponse(TypedDict):
    succeeded: bool
    response_status: Optional[int]
    error: Optional[Literal["non_2xx", "internal_error", "timeout", "connection_failed", "tls_error", "destination_not_allowed", "secret_unreadable"]]
    duration_ms: Optional[int]
    delivery_id: int


class WebhookSubscriptionDeliveryResource(TypedDict):
    id: int
    event_id: str
    event_type: str
    attempt: int
    url: str
    response_status: Optional[int]
    succeeded: bool
    error: Optional[str]
    duration_ms: Optional[int]
    attempted_at: str


class AccountBlockedEventData(TypedDict):
    reason: str
    grace_started_at: str
    grace_expired_at: str
    workspace_id: Optional[int]


class AccountBlockedEvent(TypedDict):
    id: str
    type: Literal["account.blocked"]
    version: int
    occurred_at: str
    data: AccountBlockedEventData


class AiQuotaLowBalanceEvent(TypedDict):
    id: str
    type: Literal["ai_quota.low_balance"]
    version: int
    occurred_at: str
    data: Dict[str, Any]


class AiQuotaTopupFailedEvent(TypedDict):
    id: str
    type: Literal["ai_quota.topup_failed"]
    version: int
    occurred_at: str
    data: Dict[str, Any]


class AiQuotaTopupSucceededEvent(TypedDict):
    id: str
    type: Literal["ai_quota.topup_succeeded"]
    version: int
    occurred_at: str
    data: Dict[str, Any]


class BillingPaymentFailedEventData(TypedDict):
    amount_cents: int
    currency: str
    workspace_id: Optional[int]


class BillingPaymentFailedEvent(TypedDict):
    id: str
    type: Literal["billing.payment_failed"]
    version: int
    occurred_at: str
    data: BillingPaymentFailedEventData


class BillingPlanBlockedEvent(TypedDict):
    id: str
    type: Literal["billing.plan_blocked"]
    version: int
    occurred_at: str
    data: Dict[str, Any]


class BillingUpcomingChargeEventData(TypedDict):
    charge_date: str
    amount_cents: int
    currency: str
    workspace_id: Optional[int]


class BillingUpcomingChargeEvent(TypedDict):
    id: str
    type: Literal["billing.upcoming_charge"]
    version: int
    occurred_at: str
    data: BillingUpcomingChargeEventData


class BroadcastFinishedEventData(TypedDict):
    broadcast: BroadcastFinishedEventDataBroadcast
    status: str
    reason: str
    totals: BroadcastFinishedEventDataTotals
    workspace_id: Optional[int]


class BroadcastFinishedEventDataBroadcast(TypedDict):
    id: int
    name: str


class BroadcastFinishedEventDataTotals(TypedDict):
    processed: int
    failed: int
    skipped_unreachable: int


class BroadcastFinishedEvent(TypedDict):
    id: str
    type: Literal["broadcast.finished"]
    version: int
    occurred_at: str
    data: BroadcastFinishedEventData


class BroadcastPausedEventData(TypedDict):
    broadcast: BroadcastPausedEventDataBroadcast
    reason: str
    quality: str
    quality_baseline: str
    template: Any
    workspace_id: Optional[int]


class BroadcastPausedEventDataBroadcast(TypedDict):
    id: int
    name: str


class BroadcastPausedEvent(TypedDict):
    id: str
    type: Literal["broadcast.paused"]
    version: int
    occurred_at: str
    data: BroadcastPausedEventData


class CampaignNoGroupsAvailableEventData(TypedDict):
    campaign: CampaignNoGroupsAvailableEventDataCampaign
    reason: str
    workspace_id: Optional[int]


class CampaignNoGroupsAvailableEventDataCampaign(TypedDict):
    uuid: str
    name: str


class CampaignNoGroupsAvailableEvent(TypedDict):
    id: str
    type: Literal["campaign.no_groups_available"]
    version: int
    occurred_at: str
    data: CampaignNoGroupsAvailableEventData


CampaignStatusChangedEventData = TypedDict("CampaignStatusChangedEventData", {"campaign": "CampaignStatusChangedEventDataCampaign", "from": str, "to": str}, total=True)


class CampaignStatusChangedEventDataCampaign(TypedDict):
    uuid: str
    name: str


class CampaignStatusChangedEvent(TypedDict):
    id: str
    type: Literal["campaign.status_changed"]
    version: int
    occurred_at: str
    data: CampaignStatusChangedEventData


class ContactCreatedEventData(TypedDict):
    contact: ContactCreatedEventDataContact
    workspace_id: Optional[int]


class ContactCreatedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str
    email: str


class ContactCreatedEvent(TypedDict):
    id: str
    type: Literal["contact.created"]
    version: int
    occurred_at: str
    data: ContactCreatedEventData


class ContactStageChangedEventData(TypedDict):
    contact: ContactStageChangedEventDataContact
    board: ContactStageChangedEventDataBoard
    kind: str
    from_stage: ContactStageChangedEventDataFromStage
    to_stage: ContactStageChangedEventDataToStage
    workspace_id: Optional[int]


class ContactStageChangedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class ContactStageChangedEventDataBoard(TypedDict):
    id: int
    name: str


class ContactStageChangedEventDataFromStage(TypedDict):
    id: int
    name: str
    position: int


class ContactStageChangedEventDataToStage(TypedDict):
    id: int
    name: str
    position: int


class ContactStageChangedEvent(TypedDict):
    id: str
    type: Literal["contact.stage_changed"]
    version: int
    occurred_at: str
    data: ContactStageChangedEventData


class ContactTagAddedEventData(TypedDict):
    contact: ContactTagAddedEventDataContact
    tag: ContactTagAddedEventDataTag
    source: str
    workspace_id: Optional[int]


class ContactTagAddedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class ContactTagAddedEventDataTag(TypedDict):
    id: int
    name: str


class ContactTagAddedEvent(TypedDict):
    id: str
    type: Literal["contact.tag_added"]
    version: int
    occurred_at: str
    data: ContactTagAddedEventData


class ContactTagRemovedEventData(TypedDict):
    contact: ContactTagRemovedEventDataContact
    tag: ContactTagRemovedEventDataTag
    source: str
    workspace_id: Optional[int]


class ContactTagRemovedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class ContactTagRemovedEventDataTag(TypedDict):
    id: int
    name: str


class ContactTagRemovedEvent(TypedDict):
    id: str
    type: Literal["contact.tag_removed"]
    version: int
    occurred_at: str
    data: ContactTagRemovedEventData


class ConversationAssignedEventData(TypedDict):
    contact: ConversationAssignedEventDataContact
    assignee: ConversationAssignedEventDataAssignee
    workspace_id: Optional[int]


class ConversationAssignedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class ConversationAssignedEventDataAssignee(TypedDict):
    type: str
    name: str


class ConversationAssignedEvent(TypedDict):
    id: str
    type: Literal["conversation.assigned"]
    version: int
    occurred_at: str
    data: ConversationAssignedEventData


class ConversationClosedEventData(TypedDict):
    contact: ConversationClosedEventDataContact
    workspace_id: Optional[int]


class ConversationClosedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class ConversationClosedEvent(TypedDict):
    id: str
    type: Literal["conversation.closed"]
    version: int
    occurred_at: str
    data: ConversationClosedEventData


class DailyReportGeneratedEventData(TypedDict):
    period: DailyReportGeneratedEventDataPeriod
    clicks: int
    joins: int
    leaves: int
    conversion_rate: float
    workspace_id: Optional[int]


class DailyReportGeneratedEventDataPeriod(TypedDict):
    date: str
    timezone: str


class DailyReportGeneratedEvent(TypedDict):
    id: str
    type: Literal["daily_report.generated"]
    version: int
    occurred_at: str
    data: DailyReportGeneratedEventData


class DeviceConnectedEventData(TypedDict):
    device: PendingWebhookDevice
    connected_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class PendingWebhookDevice(TypedDict):
    id: int
    name: Optional[str]
    number: Optional[str]
    connection: PendingDeviceConnection
    external_reference: PendingExternalReference


class DeviceConnectedEvent(TypedDict):
    id: str
    type: Literal["device.connected"]
    version: int
    occurred_at: str
    data: DeviceConnectedEventData


class DeviceDeletedEventData(TypedDict):
    device: PendingWebhookDevice
    deleted_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceDeletedEvent(TypedDict):
    id: str
    type: Literal["device.deleted"]
    version: int
    occurred_at: str
    data: DeviceDeletedEventData


class DeviceDisconnectedEventData(TypedDict):
    device: PendingWebhookDevice
    disconnected_at: str
    reason: Literal["qr_logged_out", "meta_account_not_registered", "shadow_ban_protection", "provider_error", "unknown", "disconnected_by_user"]
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceDisconnectedEvent(TypedDict):
    id: str
    type: Literal["device.disconnected"]
    version: int
    occurred_at: str
    data: DeviceDisconnectedEventData


class DeviceDisplayNameReviewedEventData(TypedDict):
    device: PendingWebhookDevice
    decision: Literal["approved", "rejected"]
    previous_status: str
    status: str
    verified_name: Optional[str]
    rejection_reason: Optional[str]
    reviewed_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceDisplayNameReviewedEvent(TypedDict):
    id: str
    type: Literal["device.display_name_reviewed"]
    version: int
    occurred_at: str
    data: DeviceDisplayNameReviewedEventData


class DeviceHealthChangedEventData(TypedDict):
    device: PendingWebhookDevice
    previous_state: Literal["available", "limited", "blocked", "unknown"]
    state: Literal["available", "limited", "blocked", "unknown"]
    changed_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceHealthChangedEvent(TypedDict):
    id: str
    type: Literal["device.health_changed"]
    version: int
    occurred_at: str
    data: DeviceHealthChangedEventData


class DeviceMessagingLimitChangedEventData(TypedDict):
    device: PendingWebhookDevice
    previous: str
    current: str
    changed_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceMessagingLimitChangedEvent(TypedDict):
    id: str
    type: Literal["device.messaging_limit_changed"]
    version: int
    occurred_at: str
    data: DeviceMessagingLimitChangedEventData


class DeviceQualityChangedEventData(TypedDict):
    device: PendingWebhookDevice
    previous: str
    current: str
    changed_at: str
    connect_link_id: Optional[int]
    workspace_id: Optional[int]


class DeviceQualityChangedEvent(TypedDict):
    id: str
    type: Literal["device.quality_changed"]
    version: int
    occurred_at: str
    data: DeviceQualityChangedEventData


class FlowCompletedEventData(TypedDict):
    flow: FlowCompletedEventDataFlow
    contact: FlowCompletedEventDataContact
    workspace_id: Optional[int]


class FlowCompletedEventDataFlow(TypedDict):
    id: int
    name: str


class FlowCompletedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class FlowCompletedEvent(TypedDict):
    id: str
    type: Literal["flow.completed"]
    version: int
    occurred_at: str
    data: FlowCompletedEventData


class FlowFailedEventData(TypedDict):
    flow: FlowFailedEventDataFlow
    contact: FlowFailedEventDataContact
    reason: str
    workspace_id: Optional[int]


class FlowFailedEventDataFlow(TypedDict):
    id: int
    name: str


class FlowFailedEventDataContact(TypedDict):
    id: int
    name: str
    phone: str


class FlowFailedEvent(TypedDict):
    id: str
    type: Literal["flow.failed"]
    version: int
    occurred_at: str
    data: FlowFailedEventData


class GroupBlockedEventData(TypedDict):
    group: GroupBlockedEventDataGroup
    campaign: GroupBlockedEventDataCampaign
    reason: str
    workspace_id: Optional[int]


class GroupBlockedEventDataGroup(TypedDict):
    uid: str
    name: str


class GroupBlockedEventDataCampaign(TypedDict):
    uuid: str


class GroupBlockedEvent(TypedDict):
    id: str
    type: Literal["group.blocked"]
    version: int
    occurred_at: str
    data: GroupBlockedEventData


class GroupCreatedEventData(TypedDict):
    group: GroupCreatedEventDataGroup
    campaign: GroupCreatedEventDataCampaign
    source: str
    workspace_id: Optional[int]


class GroupCreatedEventDataGroup(TypedDict):
    uid: str
    name: str
    type: str


class GroupCreatedEventDataCampaign(TypedDict):
    uuid: str
    name: str


class GroupCreatedEvent(TypedDict):
    id: str
    type: Literal["group.created"]
    version: int
    occurred_at: str
    data: GroupCreatedEventData


class GroupFullEventData(TypedDict):
    group: GroupFullEventDataGroup
    campaign: GroupFullEventDataCampaign
    trigger: str
    participants: int
    workspace_id: Optional[int]


class GroupFullEventDataGroup(TypedDict):
    uid: str
    name: str
    type: str


class GroupFullEventDataCampaign(TypedDict):
    uuid: str
    name: str


class GroupFullEvent(TypedDict):
    id: str
    type: Literal["group.full"]
    version: int
    occurred_at: str
    data: GroupFullEventData


class GroupInviteLinkDownEventData(TypedDict):
    group: GroupInviteLinkDownEventDataGroup
    campaign: GroupInviteLinkDownEventDataCampaign
    reason: str
    renewal_attempted: bool
    workspace_id: Optional[int]


class GroupInviteLinkDownEventDataGroup(TypedDict):
    uid: str
    name: str
    type: str


class GroupInviteLinkDownEventDataCampaign(TypedDict):
    uuid: str
    name: str


class GroupInviteLinkDownEvent(TypedDict):
    id: str
    type: Literal["group.invite_link_down"]
    version: int
    occurred_at: str
    data: GroupInviteLinkDownEventData


class GroupInviteLinkRenewedEventData(TypedDict):
    group: GroupInviteLinkRenewedEventDataGroup
    campaign: GroupInviteLinkRenewedEventDataCampaign
    invite_link: str
    previous_invite_link: str
    trigger: str
    recovered: bool
    workspace_id: Optional[int]


class GroupInviteLinkRenewedEventDataGroup(TypedDict):
    uid: str
    name: str
    type: str


class GroupInviteLinkRenewedEventDataCampaign(TypedDict):
    uuid: str
    name: str


class GroupInviteLinkRenewedEvent(TypedDict):
    id: str
    type: Literal["group.invite_link_renewed"]
    version: int
    occurred_at: str
    data: GroupInviteLinkRenewedEventData


class GroupMessageReceivedEventData(TypedDict):
    group: GroupMessageReceivedEventDataGroup
    message: GroupMessageReceivedEventDataMessage
    participant: GroupMessageReceivedEventDataParticipant
    workspace_id: Optional[int]


class GroupMessageReceivedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupMessageReceivedEventDataMessage(TypedDict):
    uid: str
    type: str
    text: Optional[str]
    caption: Optional[str]
    media_url: Optional[str]
    mime_type: Optional[str]
    file_name: Optional[str]
    quoted_uid: Optional[str]


class GroupMessageReceivedEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupMessageReceivedEvent(TypedDict):
    id: str
    type: Literal["group.message_received"]
    version: int
    occurred_at: str
    data: GroupMessageReceivedEventData


class GroupReactionAddedEventData(TypedDict):
    group: GroupReactionAddedEventDataGroup
    message: GroupReactionAddedEventDataMessage
    participant: GroupReactionAddedEventDataParticipant
    reaction: str
    workspace_id: Optional[int]


class GroupReactionAddedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupReactionAddedEventDataMessage(TypedDict):
    uid: str


class GroupReactionAddedEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupReactionAddedEvent(TypedDict):
    id: str
    type: Literal["group.reaction_added"]
    version: int
    occurred_at: str
    data: GroupReactionAddedEventData


class GroupRecoveredEventData(TypedDict):
    group: GroupRecoveredEventDataGroup
    campaign: GroupRecoveredEventDataCampaign
    reason: str
    workspace_id: Optional[int]


class GroupRecoveredEventDataGroup(TypedDict):
    uid: str
    name: str


class GroupRecoveredEventDataCampaign(TypedDict):
    uuid: str


class GroupRecoveredEvent(TypedDict):
    id: str
    type: Literal["group.recovered"]
    version: int
    occurred_at: str
    data: GroupRecoveredEventData


class GroupActionCompletedEventData(TypedDict):
    action: GroupActionCompletedEventDataAction
    group: Optional[GroupActionCompletedEventDataGroup]
    campaign: Optional[GroupActionCompletedEventDataCampaign]
    result: GroupActionCompletedEventDataResult
    workspace_id: Optional[int]


class GroupActionCompletedEventDataAction(TypedDict):
    uuid: str
    type: str


class GroupActionCompletedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupActionCompletedEventDataCampaign(TypedDict):
    uuid: str
    name: Optional[str]


class GroupActionCompletedEventDataResult(TypedDict, total=False):
    message: GroupActionCompletedEventDataResultMessage
    participants: List[PendingGroupParticipantResult]
    invite_link: str


class GroupActionCompletedEventDataResultMessage(TypedDict, total=False):
    uid: str


class GroupActionCompletedEvent(TypedDict):
    id: str
    type: Literal["group_action.completed"]
    version: int
    occurred_at: str
    data: GroupActionCompletedEventData


class GroupActionFailedEventData(TypedDict):
    campaign: Optional[GroupActionFailedEventDataCampaign]
    pipeline: Optional[GroupActionFailedEventDataPipeline]
    group: Optional[GroupActionFailedEventDataGroup]
    action: GroupActionFailedEventDataAction
    reason: str
    workspace_id: Optional[int]


class GroupActionFailedEventDataCampaign(TypedDict):
    uuid: str
    name: Optional[str]


class GroupActionFailedEventDataPipeline(TypedDict):
    uuid: str
    name: Optional[str]


class GroupActionFailedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupActionFailedEventDataAction(TypedDict):
    uuid: Optional[str]
    type: str


class GroupActionFailedEvent(TypedDict):
    id: str
    type: Literal["group_action.failed"]
    version: int
    occurred_at: str
    data: GroupActionFailedEventData


class GroupJoinRequestCreatedEventData(TypedDict):
    group: GroupJoinRequestCreatedEventDataGroup
    participant: GroupJoinRequestCreatedEventDataParticipant
    workspace_id: Optional[int]


class GroupJoinRequestCreatedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupJoinRequestCreatedEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupJoinRequestCreatedEvent(TypedDict):
    id: str
    type: Literal["group_join_request.created"]
    version: int
    occurred_at: str
    data: GroupJoinRequestCreatedEventData


class GroupJoinRequestRevokedEventData(TypedDict):
    group: GroupJoinRequestRevokedEventDataGroup
    participant: GroupJoinRequestRevokedEventDataParticipant
    workspace_id: Optional[int]


class GroupJoinRequestRevokedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupJoinRequestRevokedEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupJoinRequestRevokedEvent(TypedDict):
    id: str
    type: Literal["group_join_request.revoked"]
    version: int
    occurred_at: str
    data: GroupJoinRequestRevokedEventData


class GroupParticipantJoinedEventData(TypedDict):
    group: GroupParticipantJoinedEventDataGroup
    campaign: Optional[GroupParticipantJoinedEventDataCampaign]
    participant: GroupParticipantJoinedEventDataParticipant
    workspace_id: Optional[int]


class GroupParticipantJoinedEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupParticipantJoinedEventDataCampaign(TypedDict):
    uuid: str


class GroupParticipantJoinedEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupParticipantJoinedEvent(TypedDict):
    id: str
    type: Literal["group_participant.joined"]
    version: int
    occurred_at: str
    data: GroupParticipantJoinedEventData


class GroupParticipantLeftEventData(TypedDict):
    group: GroupParticipantLeftEventDataGroup
    campaign: Optional[GroupParticipantLeftEventDataCampaign]
    participant: GroupParticipantLeftEventDataParticipant
    workspace_id: Optional[int]


class GroupParticipantLeftEventDataGroup(TypedDict):
    uid: str
    name: Optional[str]


class GroupParticipantLeftEventDataCampaign(TypedDict):
    uuid: str


class GroupParticipantLeftEventDataParticipant(TypedDict):
    identity: str
    identity_type: Literal["phone", "whatsapp_user"]
    name: Optional[str]


class GroupParticipantLeftEvent(TypedDict):
    id: str
    type: Literal["group_participant.left"]
    version: int
    occurred_at: str
    data: GroupParticipantLeftEventData


class MacExpiringEventData(TypedDict):
    contacts_expiring: int
    expires_at: str
    workspace_id: Optional[int]


class MacExpiringEvent(TypedDict):
    id: str
    type: Literal["mac.expiring"]
    version: int
    occurred_at: str
    data: MacExpiringEventData


class MacUsage100EventData(TypedDict):
    used: int
    limit: int
    percentage: int
    cycle_started_at: str
    grace_expires_at: str
    workspace_id: Optional[int]


class MacUsage100Event(TypedDict):
    id: str
    type: Literal["mac.usage_100"]
    version: int
    occurred_at: str
    data: MacUsage100EventData


class MacUsage80EventData(TypedDict):
    used: int
    limit: int
    percentage: int
    cycle_started_at: str
    workspace_id: Optional[int]


class MacUsage80Event(TypedDict):
    id: str
    type: Literal["mac.usage_80"]
    version: int
    occurred_at: str
    data: MacUsage80EventData


class MessageReceivedEventData(TypedDict):
    message: MessageReceivedEventDataMessage
    contact: MessageReceivedEventDataContact
    receiver: MessageReceivedEventDataReceiver
    device_id: Optional[int]
    workspace_id: Optional[int]


class MessageReceivedEventDataMessage(TypedDict):
    id: int
    type: Literal["text", "image", "video", "document", "sticker", "contact", "audio", "note", "action", "invalid", "interactive", "location", "voice_call", "video_call", "event", "button", "template", "notification", "option_list", "template_button_reply", "poll", "whatsapp_form", "call_permission_request", "call_permission_reply", "request_contact_info"]
    text: Optional[str]
    media: Optional[MessageReceivedEventDataMessageMedia]


class MessageReceivedEventDataMessageMedia(TypedDict):
    file: str


class MessageReceivedEventDataContact(TypedDict):
    id: Optional[int]
    name: Optional[str]
    phone: Optional[str]


class MessageReceivedEventDataReceiver(TypedDict):
    phone: Optional[str]


class MessageReceivedEvent(TypedDict):
    id: str
    type: Literal["message.received"]
    version: int
    occurred_at: str
    data: MessageReceivedEventData


class MessageStatusChangedEventData(TypedDict):
    message_id: int
    contact_id: int
    device_id: Optional[int]
    status: Literal["sent", "delivered", "read", "failed"]
    previous_status: Optional[Literal["sent", "delivered", "read", "failed"]]
    error: NotRequired[MessageStatusChangedEventDataError]
    occurred_at: str
    client_reference: Optional[str]
    workspace_id: Optional[int]


class MessageStatusChangedEventDataError(TypedDict):
    code: Optional[int]
    title: Optional[str]
    reason: Optional[Literal["device_unavailable", "insufficient_balance", "window_closed", "recipient_unreachable", "template_not_found", "template_unresolved_placeholder", "not_queued", "not_sent"]]


class MessageStatusChangedEvent(TypedDict):
    id: str
    type: Literal["message.status_changed"]
    version: int
    occurred_at: str
    data: MessageStatusChangedEventData


class PipelineFinishedEventData(TypedDict):
    campaign: PipelineFinishedEventDataCampaign
    pipeline: PipelineFinishedEventDataPipeline
    outcome: str
    actions: PipelineFinishedEventDataActions
    idempotency_key: str
    workspace_id: Optional[int]


class PipelineFinishedEventDataCampaign(TypedDict):
    uuid: str


class PipelineFinishedEventDataPipeline(TypedDict):
    uuid: str
    name: str


class PipelineFinishedEventDataActions(TypedDict):
    total: int
    succeeded: int
    failed: int
    skipped: int
    cancelled: int


class PipelineFinishedEvent(TypedDict):
    id: str
    type: Literal["pipeline.finished"]
    version: int
    occurred_at: str
    data: PipelineFinishedEventData


class PollVotedEventData(TypedDict):
    poll: PollVotedEventDataPoll
    group: PollVotedEventDataGroup
    scheduled_message: PollVotedEventDataScheduledMessage
    participant: PollVotedEventDataParticipant
    options: List[str]
    workspace_id: Optional[int]


class PollVotedEventDataPoll(TypedDict):
    uid: str


class PollVotedEventDataGroup(TypedDict):
    uid: str


class PollVotedEventDataScheduledMessage(TypedDict):
    uuid: str


class PollVotedEventDataParticipant(TypedDict):
    identity: str
    identity_type: str
    name: Any


class PollVotedEvent(TypedDict):
    id: str
    type: Literal["poll.voted"]
    version: int
    occurred_at: str
    data: PollVotedEventData


class ScheduledMessageFinishedEventData(TypedDict):
    scheduled_message: ScheduledMessageFinishedEventDataScheduledMessage
    outcome: str
    groups: ScheduledMessageFinishedEventDataGroups
    occurrence: int
    workspace_id: Optional[int]


class ScheduledMessageFinishedEventDataScheduledMessage(TypedDict):
    uuid: str
    name: str


class ScheduledMessageFinishedEventDataGroups(TypedDict):
    total: int
    failed: int
    partially_failed: int


class ScheduledMessageFinishedEvent(TypedDict):
    id: str
    type: Literal["scheduled_message.finished"]
    version: int
    occurred_at: str
    data: ScheduledMessageFinishedEventData


class ScheduledMessageGroupDeliveryFailedEventData(TypedDict):
    scheduled_message: ScheduledMessageGroupDeliveryFailedEventDataScheduledMessage
    group: ScheduledMessageGroupDeliveryFailedEventDataGroup
    reason: str
    partial: bool
    occurrence: int
    workspace_id: Optional[int]


class ScheduledMessageGroupDeliveryFailedEventDataScheduledMessage(TypedDict):
    uuid: str


class ScheduledMessageGroupDeliveryFailedEventDataGroup(TypedDict):
    uid: str
    name: str


class ScheduledMessageGroupDeliveryFailedEvent(TypedDict):
    id: str
    type: Literal["scheduled_message.group_delivery_failed"]
    version: int
    occurred_at: str
    data: ScheduledMessageGroupDeliveryFailedEventData


class ScheduledMessageResponseReceivedEventData(TypedDict):
    scheduled_message: ScheduledMessageResponseReceivedEventDataScheduledMessage
    group: ScheduledMessageResponseReceivedEventDataGroup
    participant: ScheduledMessageResponseReceivedEventDataParticipant
    response: ScheduledMessageResponseReceivedEventDataResponse
    workspace_id: Optional[int]


class ScheduledMessageResponseReceivedEventDataScheduledMessage(TypedDict):
    uuid: str


class ScheduledMessageResponseReceivedEventDataGroup(TypedDict):
    uid: str


class ScheduledMessageResponseReceivedEventDataParticipant(TypedDict):
    identity: str
    identity_type: str
    name: str


class ScheduledMessageResponseReceivedEventDataResponse(TypedDict):
    type: str
    options: List[str]
    rsvp: Any


class ScheduledMessageResponseReceivedEvent(TypedDict):
    id: str
    type: Literal["scheduled_message.response_received"]
    version: int
    occurred_at: str
    data: ScheduledMessageResponseReceivedEventData


class SubscriptionCancellationConfirmedEventData(TypedDict):
    access_until: str
    workspace_id: Optional[int]


class SubscriptionCancellationConfirmedEvent(TypedDict):
    id: str
    type: Literal["subscription.cancellation_confirmed"]
    version: int
    occurred_at: str
    data: SubscriptionCancellationConfirmedEventData


class SubscriptionDormantEndingEventData(TypedDict):
    charge_date: str
    amount_cents: int
    currency: str
    workspace_id: Optional[int]


class SubscriptionDormantEndingEvent(TypedDict):
    id: str
    type: Literal["subscription.dormant_ending"]
    version: int
    occurred_at: str
    data: SubscriptionDormantEndingEventData


class SubscriptionExpiringEvent(TypedDict):
    id: str
    type: Literal["subscription.expiring"]
    version: int
    occurred_at: str
    data: Dict[str, Any]


class SubscriptionReactivatedEventData(TypedDict):
    renews_at: str
    workspace_id: Optional[int]


class SubscriptionReactivatedEvent(TypedDict):
    id: str
    type: Literal["subscription.reactivated"]
    version: int
    occurred_at: str
    data: SubscriptionReactivatedEventData


class SubscriptionTrialEndingEventData(TypedDict):
    trial_ends_at: str
    workspace_id: Optional[int]


class SubscriptionTrialEndingEvent(TypedDict):
    id: str
    type: Literal["subscription.trial_ending"]
    version: int
    occurred_at: str
    data: SubscriptionTrialEndingEventData


class TemplateStatusChangedEventData(TypedDict):
    template: TemplateStatusChangedEventDataTemplate
    previous_status: str
    status: str
    reason: Any
    workspace_id: Optional[int]


class TemplateStatusChangedEventDataTemplate(TypedDict):
    id: int
    uid: str
    name: str
    category: str


class TemplateStatusChangedEvent(TypedDict):
    id: str
    type: Literal["template.status_changed"]
    version: int
    occurred_at: str
    data: TemplateStatusChangedEventData


class WebhookTestEventData(TypedDict):
    subscription: str
    sent_at: str
    workspace_id: Optional[int]


class WebhookTestEvent(TypedDict):
    id: str
    type: Literal["webhook.test"]
    version: int
    occurred_at: str
    data: WebhookTestEventData


class WhatsappFormCompletedEventData(TypedDict):
    form: WhatsappFormCompletedEventDataForm
    message_id: Optional[int]
    contact_id: Optional[int]
    device_id: Optional[int]
    answers: List[WhatsappFormCompletedEventDataAnswersItem]
    occurred_at: str
    workspace_id: Optional[int]


class WhatsappFormCompletedEventDataForm(TypedDict):
    id: int
    name: str
    version_id: int


class WhatsappFormCompletedEventDataAnswersItem(TypedDict):
    key: str
    label: Optional[str]
    value: Union[bool, float, str, List[str], None]


class WhatsappFormCompletedEvent(TypedDict):
    id: str
    type: Literal["whatsapp_form.completed"]
    version: int
    occurred_at: str
    data: WhatsappFormCompletedEventData


MessageOriginEnum = Literal[0, 1, 2, 3]


MessageStatusEnum = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


MessageTypeEnum = Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


MessageTemplateTypeEnum = Literal["text", "image", "document", "video", "location", "default"]


MessageTemplateStatusEnum = Literal["PENDING", "APPROVED", "REJECTED", "PENDING_DELETION", "PAUSED", "DISABLED", "ARCHIVED"]


CustomFieldTypeEnum = Literal[0, 1, 2, 3, 4]


ActionGroupResource = Union["ActionGroupResource2", "ActionGroupResourceVariant2"]


WhatsAppProviderEnum = Literal[1, 2, 3, 4]


DeviceConnectionEventEnum = Literal[0, 1]


PendingDeviceConnection = Optional[Literal["qr", "coexistence", "dedicated"]]


PendingExternalReference = Optional[str]


#: Every webhook event type the spec knows.
WebhookEventType = Literal[
    "account.blocked",
    "ai_quota.low_balance",
    "ai_quota.topup_failed",
    "ai_quota.topup_succeeded",
    "billing.payment_failed",
    "billing.plan_blocked",
    "billing.upcoming_charge",
    "broadcast.finished",
    "broadcast.paused",
    "campaign.no_groups_available",
    "campaign.status_changed",
    "contact.created",
    "contact.stage_changed",
    "contact.tag_added",
    "contact.tag_removed",
    "conversation.assigned",
    "conversation.closed",
    "daily_report.generated",
    "device.connected",
    "device.deleted",
    "device.disconnected",
    "device.display_name_reviewed",
    "device.health_changed",
    "device.messaging_limit_changed",
    "device.quality_changed",
    "flow.completed",
    "flow.failed",
    "group.blocked",
    "group.created",
    "group.full",
    "group.invite_link_down",
    "group.invite_link_renewed",
    "group.message_received",
    "group.reaction_added",
    "group.recovered",
    "group_action.completed",
    "group_action.failed",
    "group_join_request.created",
    "group_join_request.revoked",
    "group_participant.joined",
    "group_participant.left",
    "mac.expiring",
    "mac.usage_100",
    "mac.usage_80",
    "message.received",
    "message.status_changed",
    "pipeline.finished",
    "poll.voted",
    "scheduled_message.finished",
    "scheduled_message.group_delivery_failed",
    "scheduled_message.response_received",
    "subscription.cancellation_confirmed",
    "subscription.dormant_ending",
    "subscription.expiring",
    "subscription.reactivated",
    "subscription.trial_ending",
    "template.status_changed",
    "webhook.test",
    "whatsapp_form.completed",
]

#: A verified webhook event, discriminated by `type`. New types can arrive before this SDK
#: knows them: answer 2xx to the ones you do not handle.
WebhookEvent = Union[
    "AccountBlockedEvent",
    "AiQuotaLowBalanceEvent",
    "AiQuotaTopupFailedEvent",
    "AiQuotaTopupSucceededEvent",
    "BillingPaymentFailedEvent",
    "BillingPlanBlockedEvent",
    "BillingUpcomingChargeEvent",
    "BroadcastFinishedEvent",
    "BroadcastPausedEvent",
    "CampaignNoGroupsAvailableEvent",
    "CampaignStatusChangedEvent",
    "ContactCreatedEvent",
    "ContactStageChangedEvent",
    "ContactTagAddedEvent",
    "ContactTagRemovedEvent",
    "ConversationAssignedEvent",
    "ConversationClosedEvent",
    "DailyReportGeneratedEvent",
    "DeviceConnectedEvent",
    "DeviceDeletedEvent",
    "DeviceDisconnectedEvent",
    "DeviceDisplayNameReviewedEvent",
    "DeviceHealthChangedEvent",
    "DeviceMessagingLimitChangedEvent",
    "DeviceQualityChangedEvent",
    "FlowCompletedEvent",
    "FlowFailedEvent",
    "GroupBlockedEvent",
    "GroupCreatedEvent",
    "GroupFullEvent",
    "GroupInviteLinkDownEvent",
    "GroupInviteLinkRenewedEvent",
    "GroupMessageReceivedEvent",
    "GroupReactionAddedEvent",
    "GroupRecoveredEvent",
    "GroupActionCompletedEvent",
    "GroupActionFailedEvent",
    "GroupJoinRequestCreatedEvent",
    "GroupJoinRequestRevokedEvent",
    "GroupParticipantJoinedEvent",
    "GroupParticipantLeftEvent",
    "MacExpiringEvent",
    "MacUsage100Event",
    "MacUsage80Event",
    "MessageReceivedEvent",
    "MessageStatusChangedEvent",
    "PipelineFinishedEvent",
    "PollVotedEvent",
    "ScheduledMessageFinishedEvent",
    "ScheduledMessageGroupDeliveryFailedEvent",
    "ScheduledMessageResponseReceivedEvent",
    "SubscriptionCancellationConfirmedEvent",
    "SubscriptionDormantEndingEvent",
    "SubscriptionExpiringEvent",
    "SubscriptionReactivatedEvent",
    "SubscriptionTrialEndingEvent",
    "TemplateStatusChangedEvent",
    "WebhookTestEvent",
    "WhatsappFormCompletedEvent",
]

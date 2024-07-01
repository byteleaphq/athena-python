# CreateNewChatResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `http_meta`                                                        | [components.HTTPMetadata](../../models/components/httpmetadata.md) | :heavy_check_mark:                                                 | N/A                                                                |
| `headers`                                                          | Dict[str, List[*str*]]                                             | :heavy_check_mark:                                                 | N/A                                                                |
| `chats`                                                            | List[[components.Chat](../../models/components/chat.md)]           | :heavy_minus_sign:                                                 | OK                                                                 |
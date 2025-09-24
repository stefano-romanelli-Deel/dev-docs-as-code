---
title: "Get started with webhooks"
slug: "webhooks-get-started"
excerpt: ""
hidden: false
createdAt: "Fri Feb 28 2025 14:56:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 30 2025 10:15:05 GMT+0000 (Coordinated Universal Time)"
---
## Prerequisites

- A Deel account with API access
- Basic familiarity with webhook concepts
- A secure HTTPS endpoint to receive events

## Webhooks API

You can use the webhook API to manage your webhooks. The following endpoints are available:

- [List webhook event types](https://developer.deel.com/reference/getallwebhookeventtypes)
- [Create a webhook](https://developer.deel.com/v2.1.51/reference/createwebhook)
- [List webhook subscriptions](https://developer.deel.com/v2.1.51/reference/getallwebhooks)
- [Retrieve a single webhook](https://developer.deel.com/v2.1.51/reference/webhookcontroller_getbyid)
- [Edit a webhook](https://developer.deel.com/v2.1.51/reference/webhookcontroller_editbyid)
- [Delete a webhook](https://developer.deel.com/v2.1.51/reference/webhookcontroller_deletebyid)

> 📘 Webhooks API scopes
> 
> Unlike Other API endpoints, webhook subscription endpoints do not require specific scopes.

## Webhook structure

### Webhook headers

In addition to the message payload, each webhook message has a variety of headers containing additional context.

```yaml
x-deel-signature: e4fce40e4a4aa76156f8846e93193b2de5649eed7aeedf4f53abd86113c91744
x-deel-hmac-label: New Webhook
x-deel-webhook-version: 1.0.0
```

The following header fields are used:

| Field                  | Use                                                                                                                       |
| :--------------------- | :------------------------------------------------------------------------------------------------------------------------ |
| x-deel-signature       | [Learn more](#security).                                                                                                  |
| x-deel-hmac-label      | HMAC signing key label. If you have multiple subscriptions, you can use the label to identify the signing key signatures. |
| x-deel-webhook-version | Specifies what version of the Deel API was used to serialize the webhook event payload.                                   |

### Webhook payload body

The webhook payload body includes a `data` object with event information and a `timestamp` for when the event occurred.

#### Webhook payload example

The `payload_example` shows what your webhook endpoint receives when the event occurs. This example shows a `tax.document.available` event triggered when a W-9 tax document is published for a US-based contract. The payload includes:

- [Meta information](#meta-object)
- [Resource data](#resource-object)
- [Timestamp](#timestamp-property)

The resource array can contain multiple items if the event affects multiple documents or contracts simultaneously.

```json
"data": {
    "meta": {
      "event_type": "tax.document.available",
      "event_type_id": "3455d332-0c09-4a62-a69f-b6cd0c56a596",
      "organization_id": "c2f26732-e747-4776-8a21-b31c379f2356",
      "organization_name": "Deel",
      "tracking_id": "d09a72b0002191b65de3a453d187f1a7"
    },
    "resource": [
      {
        "contract_oid": "123abc1",
        "country": "US",
        "id": 434078,
        "month": null,
        "status": "PUBLISHED",
        "document_type": "W-9",
        "year": 2024
      }
    ]
  },
"timestamp": "2025-02-05T15:39:38.070Z"
```

#### Meta object

The meta object includes the metadata for the webhook. The following fields are in the meta object:

| Field               | Description                                          | Example                                |
| ------------------- | ---------------------------------------------------- | -------------------------------------- |
| `event_type`        | Type of webhook event                                | `tax.document.available`               |
| `event_type_id`     | Unique identifier for this specific event occurrence | `3455d332-0c09-4a62-a69f-b6cd0c56a596` |
| `organization_id`   | ID of your Deel organization                         | `c2f26732-e747-4776-8a21-b31c379f2356` |
| `organization_name` | Name of your Deel organization                       | `Deel`                                 |
| `tracking_id`       | Unique tracking ID for support requests              | `d09a72b0002191b65de3a453d187f1a7`     |

#### Resource object

The `resource` object contains the actual data for the webhook event. The structure, format, and complexity of this object varies depending on the event type. Use the [List of webhook event types](https://developer.deel.com/reference/getallwebhookeventtypes) endpoint to explore the available event types and view different resource data examples.

Following the example above, a `tax.document.available` event contains specific information about the published tax document, including the contract, document type, and status.

#### Timestamp property

Defines the timestamp when the webhook was created.

## Security

Deel secures webhook notifications by signing each payload with an HMAC generated using SHA256 and a unique secret key that you receive when you create a webhook subscription.

Here’s how it works:

1. **Signature generation**: When a webhook event is triggered, Deel uses your secret key and the SHA256 algorithm to compute a digital signature of the payload. The full raw body of the request is used, and Deel prepends it with the string `POST` before hashing. This signature is then included in the `x-deel-signature` [header of the webhook](#webhook-headers) request.
2. **Signature verification**: On your side, calculate the HMAC of the exact raw payload (with the `POST` prefix), using the same secret key and SHA256 algorithm. Compare it with the signature provided in the `x-deel-signature` header using a secure, constant-time comparison function. If they match, the webhook is verified as authentic.

![](https://files.readme.io/99a9c998b9a01115b86754aba18ce6d1b1cdb58e8ef7b2108dd03e5a494674ef-webhook-sha-diagram.png)


### Verifying the webhook signature

Here is a high-level outline that applies to most languages and frameworks:

```txt
signature_from_header = request.headers['x-deel-signature']
raw_payload = get_raw_request_body()  // Ensure you're using the exact body of the request before any parsing or decoding
signing_key = 'your_webhook_signing_key'

expected_signature = HMAC_SHA256(signing_key, 'POST' + raw_payload) // Ensure you're including the 'POST' prefix when computing the HMAC
if constant_time_equals(signature_from_header, expected_signature):
    accept_request()
else:
    reject_request()
```

Additionally, you can find language-specific examples in the [Webhook verification examples](/docs/webhook-verification-examples) .

> 🚧 Common pitfalls
> 
> Some frameworks parse or consume the body before you can access it, such as `request.body.read()` in Python or standard `req.body` in JavaScript frameworks. Always make sure to:
> 
> - Capture the raw body. For example, you can use `request.get_data(as_text=True)` in Python or `req.rawBody` in JavaScript.
> - Prefix the body with `"POST"` before hashing.
> - Use hex encoding to compare the signatures. For example, you can use `hexdigest()` in Python or `digest('hex')` in Node.js.
> - Use a constant-time comparison to prevent timing attacks.

## Event types

We maintain a list of webhook event types in our developer portal, but you can also access the available endpoints using the API. Pick the one that best suits your needs:

- [Article with all webhook event types](https://developer.deel.com/docs/webhook-event-types)
- [Get all webhook event types](https://developer.deel.com/reference/getallwebhookeventtypes) API endpoint

## Testing webhooks

You can also test your webhooks locally using tools that forward webhooks to your local server. While we're not affiliated to any of them, here's some tools you can use:

- [Hookdeck](https://hookdeck.com/)
- [Smee](https://smee.io/)

## Best Practices

When using webhooks, it's important to follow some best practices:

- [Respond fast](#respond-fast)
- [Ignore duplicates](#ignore-duplicates)
- [Stick to your needs](#stick-to-your-needs)
- [Implement reconciliation jobs](#implement-reconciliation-jobs)

### Respond fast

By ensuring your webhook receiving mechanism reliably returns a 2xx response, you can avoid delivery failures and the subsequent disabling of your webhook subscription.

Non-delivered webhook messages are stored in a message queue and retried later. Responding promptly reduces the chances of requests timing out and delivery failures. For more information, see [Retry mechanism](#retry-mechanism).

### Ignore duplicates

Webhook endpoints may occasionally receive the same event more than once. You are advised to guard against duplicated event receipts by making your event processing idempotent. You can do this by logging the events you’ve processed and not processing the already-logged events.

### Stick to your needs

Only subscribe to the event you are using. For example, if you only need to know if the contract has been created, subscribe to that event only. You should make judicious use of the services.

### Implement reconciliation jobs

You shouldn’t rely solely on receiving data from the webhooks, as delivery isn’t always guaranteed. We recommend that you also implement reconciliation jobs to fetch data from Deel periodically. For example, if you are awaiting contract status updates, you should also implement a reconciliation job that pulls data from Deel API periodically to ensure that you are getting all the updates correctly.

## Retry mechanism

If a webhook delivery fails—that is, if your webhook URL responds with a non-`2xx` HTTP status—the message is not immediately discarded. Instead, it’s queued for a series of 9 automated retries using an exponential backoff schedule.

After the 9th retry, which is the 10th attempt in total, the webhook is marked as disabled and no further events will be sent.

When a webhook is disabled, we send an email notification to the organization admin.

You can re-enable the webhook if you need, but keep in mind that [URLs cannot be edited](#unique-webhook-urls).

### Retry schedule

 For example, the retry delays are typically set as follows:

| Attempt | Delay after failed attempt |
| ------- | -------------------------- |
| 1       | 1 minute                   |
| 2       | 5 minutes                  |
| 3       | 15 minutes                 |
| 4       | 30 minutes                 |
| 5       | 1 hour                     |
| 6       | 2 hours                    |
| 7       | 4 hours                    |
| 8       | 8 hours                    |
| 9       | 16 hours                   |
| 10      | Webhook disabled           |

> 📘 A background cron job runs every 10 minutes to process these retries, so actual retry times might be adjusted to the next cron execution.

## Unique webhook URLs

If the webhook URL itself is no longer valid or has permanently changed, you cannot update the URL of an existing subscription. In that case, you must create a new webhook subscription. For more information, visit [Managing webhooks](https://developer.deel.com/docs/webhook-manage).

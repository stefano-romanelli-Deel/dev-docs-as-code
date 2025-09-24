---
title: "Managing webhooks"
slug: "webhooks-manage"
excerpt: "Learn how to manage webhook subscriptions in the UI and with the API."
hidden: false
createdAt: "Fri Feb 28 2025 15:08:23 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 30 2025 10:12:39 GMT+0000 (Coordinated Universal Time)"
---
## Before you begin

Make sure to review the following articles before creating or managing webhook subscriptions. They explain how webhooks work and how to use them.

- [Webhooks overview](https://developer.deel.com/docs/webhooks)
- [Get started with webhooks](https://developer.deel.com/docs/webhooks-get-started)

## Explore event types and payload examples

This section explains how to list the available webhooks and their payload details. You can do this in two ways:

- [List available event types with the API](#list-available-event-types-with-the-api)
- [List available event types in the UI](#list-available-event-types-in-the-ui)

### List available event types with the API

The [List of webhook event types](https://developer.deel.com/reference/getallwebhookeventtypes) endpoint returns information about the available event types and examples of their payloads. You can retrieve them by sending a GET request to the endpoint.

Here's an example of the webhook event type information returned by the endpoint:

```json
    {
      "id": "c7d1be74-efd9-4555-b3f0-80ae9031963f",
      "module_name": "verifications",
      "module_label": "Verifications",
      "name": "bgcheck.result.available",
      "description": "Triggered when background check result is available",
      "payload_example": {
        "data": {
          "meta": {
            "event_type": "bgcheck.result.available",
            "event_type_id": "af7ce5be-d404-4788-aed5-9a5fce1b66c8",
            "organization_id": "987deccd-cef2-4c0f-a068-7cb07971bcfe",
            "organization_name": "Deel",
            "tracking_id": "q8tVRj_Je00wJLY2GriqT10nUjBZ"
          },
          "resource": {
            "candidate_email": "john.doet@deel.com",
            "completed_at": "2024-09-05T08:32:51. 658Z",
            "contract_id": "3072cm7",
            "created_at": "2024-09-05T08:28:24.394Z",
            "id": "d1f5e39c-fcfd-4f08-b5fa-66ce7112ffef",
            "is_complete": true,
            "name": "Softcheck",
            "package": null,
            "result": "CLEARED",
            "status": "COMPLETE",
            "third party_name": "request softcheck"
          }
        },
        "timestamp": "2024-09-05T08:32:52. 119Z"
      },
      "created_at": "2024-08-28T10:51:50.868Z",
      "updated_at": "2024-08-28T10:51:50.868Z"
    }
```

A detailed explanation of a webhook payload structure is available in [Get started with webhooks](webhooks-get-started.md#webhook-structure).

### List available event types in the UI

The list of available event types is also available from the [Developer Center](https://app.deel.com/developer-center) in the UI. To see the available event types:

1. Go to **More** > **Developer** and go to the **Webhooks** tab.
2. Click **Event payload**.

![](https://files.readme.io/3cefb18592252a1f2244da284f32a685c5d5db775f598ee4be09b41b8ef7dbf4-webhook-ui-payload.png)


3. Browse the available payloads in the resulting screen.

![](https://files.readme.io/4894dff7a3295edd54fc6c60a60ba25e6e76ca50eafefff434f271aeeec30d2d-webhook-ui-payload-example.png)


## Subscribe to a webhook

You can register your endpoint via the API or directly in the Developer Center. This section explains how to do that.

- [Subscribe to a webhook with the API](#subscribe-to-a-webhook-with-the-api)
- [Subscribe to a webhook in the UI](#subscribe-to-a-webhook-in-the-ui)

### Subscribe to a webhook with the API

You can use the dedicated [Create a webhook](https://developer.deel.com/reference/createwebhook) endpoint to subscribe to a webhook. Following is an example of the request, for more information, refer to the API reference.

```bash
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/webhooks \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {token}' \
     --header 'content-type: application/json' \
     --data '
{
  "status": "enabled",
  "api_version": "v2",
  "name": "Demo webhook",
  "description": "My webhook description",
  "url": "https://webhook.site/d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
  "events": [
    "contract.created"
  ]
}
'
```

### Subscribe to a webhook in the UI

To subscribe to a webhook in the UI:

1. Go to **More** > **Developer** and go to the **Webhooks** tab.
2. Click **Add webhook**.
3. ![](https://files.readme.io/2c27b1c0ed02d55138c34a952a6a64daf3a73385c1f0fa93e7e142f0a20a5131-webhook-ui-add.png)
4. Enter the webhook details, then click **Continue**.

   ![](https://files.readme.io/641ec8157553e651913b139c71ba51f306ca8f88f7042d490c5269afeb8e56d3-webhook-ui-details.png)
5. Select the events you want to subscribe to, then click **Continue**.
6. Review your settings and click **Finalize Webhook**.

   ![](https://files.readme.io/ecbeedae3c9b4b7d4b0f5151ebaca6505e2e33fd0afe33446a323ca25fbc331e-webhook-ui-finalize.png)

## Disabling webhook subscriptions

You can disable an existing webhook using either of the following methods:

- [Disable a webhook subscription with the API](#disable-a-webhook-subscription-with-the-api)
- [Disable a webhook subscription in the UI](#disable-a-webhook-subscription-in-the-ui)

### Disable a webhook subscription with the API

To disable a webhook subscription, use the dedicated [Edit a webhook](https://developer.deel.com/reference/webhookcontroller_editbyid) endpoint and set the `status` parameter to `disabled`. For more information, refer to the API reference.

### Disable a webhook subscription in the UI

To disable a webhook subscription in the UI:

1. Go to **More** > **Developer** and go to the **Webhooks** tab.
2. Locate the webhook you want to disable, click the ellipsis (three dots), then select **Disable**.

![](https://files.readme.io/ad6de8bcde4b9fb0a9f129b36e7aed38601ce4b3d1adc2e77486f8e6d60eab6d-webhook-ui-disable.png)


## Delete webhook subscriptions

When you no longer need a webhook subscription, or if you need to change aspects of the subscription that cannot be edited, such as the URL, you may delete the subscription. You can do so from the API or the UI.

Before deleting a webhook, consider that events will no longer be notified to your endpoint after the webhook is deleted.

You can delete a webhook using either of the following methods:

- [Delete a webhook subscription with the API](#delete-a-webhook-subscription-with-the-api)
- [Delete a webhook subscription in the UI](#delete-a-webhook-subscription-in-the-ui)

### Delete a webhook subscription with the API

To delete a webhook subscription, use the dedicated [Delete a webhook](https://developer.deel.com/reference/webhookcontroller_deletebyid) endpoint. For more information, refer to the API reference.

### Delete a webhook subscription in the UI

To delete a webhook subscription in the UI:

1. Go to **More** > **Developer** and go to the **Webhooks** tab.
2. Locate the webhook you want to delete, click the ellipsis (three dots), then select **Delete**.
3. ![](https://files.readme.io/f872067b30c2f18a9b6c1cd6db03080fa86f07c889c1c2fe39599d533f96abef-webhook-ui-delete.png)
4. On the confirmation dialog, click **Delete**.

## Monitor webhook events

You can also monitor the delivery of webhook events from the UI, without having to rely on raw logs or technical support to track the overall health of your webhooks and any failed deliveries.

For each webhook event, you'll be able to view:

- The event type
- The event payload
- The event timestamp
- The response status
- The URL where the event was sent
- The retry history

To monitor the delivery of webhook events:

1. Go to **More** > **Developer** and select the **Webhooks** tab.

![](https://files.readme.io/eade34f3d6425fc5dff39ccb9e250fdd9f84e8037f68c250cb3fc29ebc15fe84-webhooks-tab.png)


2. In the list of webhooks, click the ellipsis (three dots), then select **See attempts** next to the webhook subscription you want to monitor.

![](https://files.readme.io/5ba9480acc6a6a3c56b3e5c41937bc8c40cdbd821008314fd2707fa36e1ea35b-webhooks-see-attempts.png)


3. Click on the attempt you want to view to see and analyze its details.

![](https://files.readme.io/ad52db7375d1273168476e3ef3041dc466b8749fec1aa2e58a6bec4806bdf5f0-webhook-details.png)

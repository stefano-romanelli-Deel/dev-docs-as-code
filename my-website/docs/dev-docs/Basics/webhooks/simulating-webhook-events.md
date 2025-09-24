---
title: "Simulating webhook events"
slug: "simulating-webhook-events"
excerpt: "This article explains how to use webhook simulation in Deel to safely test integrations."
hidden: false
createdAt: "Fri Aug 29 2025 15:46:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Aug 29 2025 15:51:00 GMT+0000 (Coordinated Universal Time)"
---
Webhook simulation lets you test integrations without triggering real business processes. You can send predefined test payloads to your registered webhook endpoints directly from the webhook management interface. These test events behave like production events, but are only simulated.

The benefits of webhook simulation are:

- Validate configurations before going live without affecting live data.
- Troubleshoot safely by reproducing events without triggering actual workflows.
- Ensure consistency since simulated events use the same authentication, timeout, and retry logic as production.
- Maintain transparency because test events are logged and marked with `is_simulation`.

## Before you begin

Review the [Getting started with webhooks](https://developer.deel.com/docs/webhooks-get-started) guide to ensure you have the necessary requirements.

## How webhook simulation works

When you simulate an event, Deel sends a test payload to your configured endpoint. The request uses the same infrastructure as production events, including authentication headers and retry policies. The only difference is that the payload includes `"is_simulation": true` so your system can distinguish it from real activity.

![](https://files.readme.io/98d07aa97e9ae97c3dfdff4424be1fe12fe5f57b019d1e534bf00927a26b3540-webhook-simulation-diagram.png)


> 📘 Simulation attempts are rate-limited to 10 per webhook per hour.

## Using webhook simulation

1. Go to **More** > **Developer** and go to the **Webhooks** tab.
2. Select the webhook you want to simulate.
3. On the **Events** card, select the number of events the webhook is listening for.  
   ![](https://files.readme.io/a2616d66f6095253d3dbc6292628f890b57b19852810cc8745498abdb0ce40d1-webhook-ui.png)
4. Expand the event type and click **Simulate** next to the event you want to test. A dialog appears confirming that the event simulation was successful.  
   ![](https://files.readme.io/4d5db262d02f12e70e4f8b9ab7588c7b4b4df2d4459fbdfcc820c260be339676-webhook-events-to-simulate.png)
5. Confirm the simulation in your configured endpoint.

## Example payload

Here’s an example of a simulated `contract.created` event. To learn more about webhook payloads and their structure, see [Getting started with webhooks](https://developer.deel.com/docs/webhooks-get-started).  
:

```json
{
  "data": {
    "meta": {
      "event_type": "contract.created",
      "event_type_id": "a3271a64-092c-45a6-bcb9-1677c441b4fd",
      "is_simulation": true,
      "organization_id": "3e214829-9ad4-4a5a-81f8-491a2a79b6e4",
      "organization_name": "White Label Demo",
      "tracking_id": "0b39d6e2-84eb-4ad5-ac31-137c4b0993ae"
    },
    "resource": {
      "client": {
        "legal_entity": {
          "email": "",
          "name": "",
          "registration_number": "",
          "subtype": "",
          "type": "company",
          "vat_number": ""
        }
      },
      "compensation_details": {
        "currency_code": "USD",
        "first_payment": "",
        "first_payment_date": "",
        "frequency": "",
        "gross_annual_salary": "",
        "gross_signing_bonus": "",
        "gross_variable_bonus": "",
        "scale": ""
      },
      "created_at": "2025-02-05T10:10:39.723Z",
      "employment_details": {
        "days_per_week": 0,
        "hours_per_day": 0,
        "paid_vacation_days": 0,
        "probation_period": 0,
        "type": "ongoing_time_based"
      },
      "id": "3072cm7",
      "invitations": {
        "client_email": "",
        "worker_email": ""
      },
      "is_archived": false,
      "notice_period": 10,
      "signatures": {
        "client_signature": "",
        "client_signed_at": "",
        "signed_at": "",
        "worker_signature": "",
        "worker_signed_at": ""
      },
      "special_clause": "",
      "start_date": "2025-02-04T21:00:00.000Z",
      "status": "waiting_for_client_sign",
      "termination_date": "",
      "title": "Software Engineer",
      "type": "ongoing_time_based",
      "worker": {
        "expected_email": "john.doe@gmail.com",
        "first_name": "John",
        "last_name": "Doe"
      }
    }
  },
  "timestamp": "2025-08-29T14:30:00.029Z"
}
```

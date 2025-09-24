---
title: "Getting Started"
slug: "getting-started-adjustments-api"
excerpt: ""
hidden: false
createdAt: "Thu Feb 15 2024 09:06:34 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Sep 17 2025 14:54:47 GMT+0000 (Coordinated Universal Time)"
---
# Introduction

The Adjustments API is a powerful tool designed to streamline the process of managing payroll adjustments such as expenses, bonuses, and other modifications. This article serves as a step-by-step guide to help you get started with the Adjustments API.

# Step 1: Understand Adjustments in Deel

Before diving in, familiarize yourself with what payroll adjustments are and how they impact employee payroll. Adjustments can be additions or deductions like bonuses, expenses, or custom adjustments specific to your organization.

We recommend exploring Deel in your sandbox to familiarize yourself with adjustments. 

# Step 2: Set Up Your Sandbox

Ensure your sandbox environment is ready. Follow [this guide](https://developer.deel.com/docs/sandbox) to create your Deel Sandbox.

# Step 3: Authentication

It's required to authenticate your API requests. You can do this by obtaining an API key or by integrating OAuth 2.0. 

For an API key, refer to our [detailed guide](https://developer.deel.com/docs/api-tokens-1) on API Token Generation which will walk you through the process of obtaining and using your unique key. 

If you prefer OAuth 2.0, our [OAuth 2.0 Integration Guide](https://developer.deel.com/docs/oauth2) provides comprehensive instructions on setting up and using OAuth 2.0 with the Adjustments API. 

Both methods ensure secure and authenticated access to the API functionalities.

# Step 4: Create a test Adjustment

Start by creating a simple adjustment. The following code block show how to create an adjustment using the API.

```curl Request payload
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/adjustments \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {token}' \
     --header 'content-type: multipart/form-data' \
     --form 'file={file_name}' \
     --form date_of_adjustment=2024-01-24 \
     --form title=Keyboard \
     --form amount=80 \
     --form 'vendor=Keyboards Company' \
     --form country=US \
     --form contract_id=v8k78yg \
     --form 'description=I bought a keyboard' \
     --form adjustment_category_id=c6816f1bad6384ada82bf4e41de469 \
     --form move_next_cycle=true \
     --form cycle_reference=my_cycle_reference
```
```json Response payload
{
  "data": {
    "title": "Keyboard",
    "description": "I bought a keyboard",
    "status": "OPEN",
    "cycle_reference": "my_cycle_reference",
    "move_next_cycle": true,
    "created_at": "2025-09-17T14:54:25.055Z",
    "updated_at": "2025-09-17T14:54:25.056Z",
    "file": null,
    "id": "c209efd2-1122-48cf-b493-f0ec9db5628f",
    "contract_id": "v8k78yg",
    "amount": "80.00",
    "actual_start_cycle_date": "2025-08-01T00:00:00.000Z",
    "actual_end_cycle_date": "2025-08-31T00:00:00.000Z",
    "date_of_adjustment": "2024-01-24T00:00:00.000Z",
    "adjustment_category_id": "clst31ugz099ps901ixhfiu7q"
  }
}
```

Where:

| Name                     | Required | Type          | Format | Description                                                                | Example                          |
| ------------------------ | -------- | ------------- | ------ | -------------------------------------------------------------------------- | -------------------------------- |
| `file`                   | true     | file          | -      | A file to upload as supporting evidence for the adjustment.                | `receipt.pdf`                    |
| `date_of_adjustment`     | true     | string        | date   | The date of the adjustment. Use the ISO-8601 short date format YYYY-MM-DD. | `2024-01-24`                     |
| `title`                  | true     | string        | -      | The title or short name of the adjustment.                                 | `Keyboard`                       |
| `amount`                 | true     | number/string | -      | The adjustment amount.                                                     | `80`                             |
| `vendor`                 | true     | string        | -      | The name of the vendor associated with the adjustment.                     | `Keyboards Company`              |
| `country`                | true     | string        | -      | The country where the adjustment applies. Use the ISO 3166-1 alpha-2 code. | `US`                             |
| `contract_id`            | true     | string        | -      | The identifier of the contract associated with the adjustment.             | `v8k78yg`                        |
| `description`            | true     | string        | -      | A description of the adjustment.                                           | `I bought a keyboard`            |
| `adjustment_category_id` | true     | string        | -      | The identifier of the adjustment category.                                 | `c6816f1bad6384ada82bf4e41de469` |
| `move_next_cycle`        | false    | boolean       | -      | If true, the adjustment will be applied to the next cycle.                 | `true`                           |
| `cycle_reference`        | false    | string        | -      | A reference identifier for the payroll cycle.                              | `my_cycle_reference`             |

<iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FcEqZVcS992A%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DcEqZVcS992A&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FcEqZVcS992A%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube" width="854" height="480" scrolling="no" title="YouTube embed" frameborder="0" allow="autoplay; fullscreen; encrypted-media; picture-in-picture;" allowfullscreen="true"></iframe>


# Step 7: Explore API Reference

Each API has unique features and limitations. Read the Adjustments API documentation thoroughly. It's your best resource for understanding specific endpoints.

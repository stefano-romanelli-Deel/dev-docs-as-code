---
title: "Request background checks"
slug: "request-background-checks"
excerpt: "Learn how to see the available background checks by country and how to request a background check for an existing contract"
hidden: false
createdAt: "Wed Aug 14 2024 09:18:17 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 06 2024 15:26:49 GMT+0000 (Coordinated Universal Time)"
---
Deel offers the possibility to request background checks on employees leveraging [Certn](https://certn.co/about-certn/), a third-party background check provider.

This guide explains how to request background checks on employees using the API.

## Before you begin

To request background checks using the API, you'll need:

- An active Certn account created from the Deel UI. Instructions on how to create one are available on the [Help Center](https://help.letsdeel.com/hc/en-gb/articles/8109759731985-How-to-Run-a-Background-Check-on-Deel#h_01G9HB7088AZ92CBQWCKA2S5TW).
- An existing contract for which the background check is requested.
- The country of residence of the worker must be declared in the contract, because the availability of background checks depends on the country.

Before starting to request background checks from the API, we recommend reading the [dedicated Help Center article](https://help.letsdeel.com/hc/en-gb/articles/8109759731985-How-to-Run-a-Background-Check-on-Deel).

> 📘 Currently, requesting background checks when there's no active contract for a worker is only supported from the UI.

## Retrieve the available background checks

Before requesting a background check, you need to understand which background check you want to request for the worker.

Background checks are available for all countries. However, their availability varies for each country. This is why the endpoint to get the list of available background checks offers the possibility to filter the results by country.

You can also retrieve the background checks price so that the cost of performing a background check is transparent at all times.

The available background checks are retrieved by making a `GET` request to the [List background checks](https://developer.deel.com/reference/getbackgroundchecksoptions) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/background-checks/options?country=ES&prices=true' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the query:

| Name      | Required | Type    | Format                                      | Description                                                                                                                                                                                                                                                                                                                                                                          | Example |
| --------- | -------- | ------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `country` | false    | string  | ISO 3166-1 alpha-2 code in capital letters. | The country where you want to check the availability. Adding this parameter will result in the boolean flag `isAvailable` to be returned in the response. A list of the available country codes can be found on our [Help Center](https://help.letsdeel.com/hc/en-gb/articles/15021126310161-How-To-Troubleshoot-Issues-When-Mass-Importing-Employees#h_01GZJS969FZY3K2K4V8YGRNEGJ). | `US`    |
| `prices`  | false    | boolean | -                                           | Whether to include the price of the background check.                                                                                                                                                                                                                                                                                                                                | `true`  |

A successful response will return the list of available background checks and, optionally, their availability and price.

Note down the `id` of the background checks you're interested in. IDs are needed to request the background checks.

> 📘 Individual checks and packages
> 
> Checks can be requested individually or as packages. As the word suggests, packages are a collection of checks that can be requested together.
> 
> - Individual checks are listed within the `individual_checks` object in the response.
> - Packages are listed within the `packages` object in the response. Each package also contains the IDs of the individual checks that comprise it.

```json
{
  "data": {
    "individual_checks": [
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Softcheck",
        "third_party_name": "request_softcheck",
        "is_available": true,
        "currency": "USD",
        "price": 49
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Education Verification",
        "third_party_name": "request_education_verification",
        "is_available": true,
        "currency": "USD",
        "price": 65
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Employment Verification",
        "third_party_name": "request_employment_verification",
        "is_available": true,
        "currency": "USD",
        "price": 52
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Credential Verification",
        "third_party_name": "request_credential_verification",
        "is_available": true,
        "currency": "USD",
        "price": 48
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "International Criminal Check",
        "third_party_name": "request_international_criminal_record_check",
        "is_available": true,
        "currency": "USD",
        "price": 103
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Canadian Criminal Check",
        "third_party_name": "request_criminal_record_check",
        "is_available": false,
        "currency": "USD",
        "price": 0
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "US criminal check",
        "third_party_name": "request_us_criminal_record_check_tier_1",
        "is_available": false,
        "currency": "USD",
        "price": 0
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "US criminal and court check",
        "third_party_name": "request_us_criminal_record_check_tier_3",
        "is_available": false,
        "currency": "USD",
        "price": 0
      }
    ],
    "packages": [
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Standard Employment Check",
        "checks": [
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
        ],
        "is_available": true,
        "currency": "USD",
        "price": 101
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Pro Employment Check",
        "checks": [
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
        ],
        "is_available": true,
        "currency": "USD",
        "price": 166
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Pro International Criminal Check",
        "checks": [
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
        ],
        "is_available": true,
        "currency": "USD",
        "price": 220
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Pro US Criminal Check",
        "checks": [
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
        ],
        "is_available": false,
        "currency": "USD",
        "price": 117
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Standard US Criminal Check",
        "checks": [
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
        ],
        "is_available": false,
        "currency": "USD",
        "price": 52
      }
    ]
  }
}
```

## Request a background check

Once you have the IDs of the background checks you want to request, you are ready to request them.

Background checks are requested by making a `POST` request to the [Create background check](https://developer.deel.com/reference/createbackgroundcheckforcontracts) endpoint.

As seen in the previous steps, background checks can be requested as individual checks or as packages. It's not possible to mix individual checks and packages in one request.

### Request individual background checks

To request individual background checks, include one or more IDs of the checks in the `individual_check_ids` array in the request body when making the request.

> 👍 Multiple individual checks can be requested at once

```curl
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/background-checks/regular \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "contract_ids": [
      "dd3m0000"
    ],
    "individual_check_ids": [
      "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
    ],
  }
}
'
```

A successful response (`201`) will return a confirmation that the background checks have been requested.

```json
{
  "data": {
    "created": true
  }
}
```

### Request a background check package

To request a background check package, include the ID of the package in the `package_id` field in the request body when making the request.

> 📘 It's not possible to request multiple background check packages in one request.

```curl
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/background-checks/regular \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "contract_ids": [
      "dd3m0000"
    ],
    "package_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
  }
}
'
```

A successful response (`201`) will return a confirmation that the background checks have been requested.

```json
{
  "data": {
    "created": true
  }
}
```

## Stay updated on the status of a background check

When the request is created, the worker is notified that a background check is being initiated for them. In some cases they may be asked to provide additional information. Once Certn has completed the background check, the report will become available on Deel within 24 hours.

There are 2 ways to stay updated on the status of a background check:

- [By querying the List background checks by contract ID endpoint](#view-the-status-of-a-background-check-using-an-endpoint)
- [By receiving updates from a webhook](#receive-background-check-status-updates-via-webhooks)

> 👍 There's also the UI
> 
> You can always check the status of the background check from the Deel UI by going to the **Background checks** section and selecting **View workers** next to the specific check type.  
> ![Screenshot showing the background checks section with the view workers button highlighted](https://help.letsdeel.com/hc/article_attachments/27191912165777 "The view workers button allows to view the workers for which a specific background check type is active")

### View the status of a background check using an endpoint

You can view the status of a background check that was requested for a contract by making a `GET` request to the [List background checks by contract ID](https://developer.deel.com/reference/getbackgroundchecksbycontractid) endpoint and indicating the contract ID in the request.

```curl
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/background-checks/{contract_id} \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the path:

| Name          | Required | Type   | Format | Description             | Example   |
| ------------- | -------- | ------ | ------ | ----------------------- | --------- |
| `contract_id` | true     | string | -      | The ID of the contract. | `d33m000` |

A successful response (`200`) will return the list of the background check requested for the contract and their status.

```json
{
  "data": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "name": "International Criminal Check",
      "third_party_name": "request_international_criminal_record_check",
      "status": "REQUESTED",
      "is_complete": false,
      "created_at": "2024-08-27T14:51:51.304Z",
      "completed_at": null,
      "package": null
    },
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "name": "Education Verification",
      "third_party_name": "request_education_verification",
      "status": "REQUESTED",
      "is_complete": false,
      "created_at": "2024-08-30T12:33:46.739Z",
      "completed_at": null,
      "package": {
        "name": "Pro Employment Check"
      }
    },
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "name": "Employment Verification",
      "third_party_name": "request_employment_verification",
      "status": "REQUESTED",
      "is_complete": false,
      "created_at": "2024-08-30T12:33:46.739Z",
      "completed_at": null,
      "package": {
        "name": "Pro Employment Check"
      }
    },
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "name": "Softcheck",
      "third_party_name": "request_softcheck",
      "status": "COMPLETE",
      "is_complete": true,
      "created_at": "2024-08-30T12:33:46.739Z",
      "completed_at": "2024-08-30T12:37:20.228Z",
      "package": {
        "name": "Pro Employment Check"
      }
    }
  ]
}
```

Where:

| Name               | Type    | Format | Description                                                                                                                                                                    | Example                                       |
| ------------------ | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| `id`               | string  | -      | The ID of the background check.                                                                                                                                                | `0f354711-1398-44cd-95d5-e433b6fd439d`        |
| `name`             | string  | -      | The name of the background check.                                                                                                                                              | `International Criminal Check`                |
| `third_party_name` | string  | -      | The name of the third party.                                                                                                                                                   | `request_international_criminal_record_check` |
| `status`           | string  | -      | The status of the background check. Possible values are `WAITING_CONTRACTOR_SIGNATURE`, `READY_TO_BE_REQUESTED`, `REQUESTED`, `IN_PROGRESS`, `DRAFT`, `COMPLETE`, `CANCELLED`. | `REQUESTED`                                   |
| `is_complete`      | boolean | -      | Whether the background check is complete.                                                                                                                                      | `true`                                        |
| `created_at`       | string  | -      | The date and time when the background check was created.                                                                                                                       | `2024-08-27T14:51:51.304Z`                    |
| `completed_at`     | string  | -      | The date and time when the background check was completed.                                                                                                                     | `2024-08-30T12:37:20.228Z`                    |
| `package.name`     | string  | -      | If the background check is part of a package, indicates the name of the package.                                                                                               | `Pro Employment Check`                        |

### Receive background check status updates via webhooks

It's also possible to know when a background check has been completed subscribing to the dedicated webhook event `bgcheck.result.available`.

- Instructions on how to create a webhook subscription are available at [Create a webhook subscription](https://developer.deel.com/docs/getting-started-2#create-a-webhook-subscription)
- Information on the payload sent by the webhook is available at [bgcheck.result.available](https://developer.deel.com/docs/event-payload-examples#bgcheckresultavailable)

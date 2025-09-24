---
title: "Creating an EOR contract"
slug: "creating-an-eor-contract"
excerpt: "Learn how to gather requirements, create the contract, and receive a quote when hiring an EOR employee via API"
hidden: true
createdAt: "Fri Jun 20 2025 13:55:43 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jun 20 2025 13:57:40 GMT+0000 (Coordinated Universal Time)"
---
Hiring an EOR employee requires going through several steps.

In this guide, we'll walk you through the first phase of the hiring process, which consists in creating the contract and receiving a quote from Deel.

## Step 1: Understand the required information to create the contract

The first step consists in retrieving the information to create the contract using the the [Fetch EOR contract form](https://developer.deel.com/reference/fetcheorcontractform).

The information you must input to create the contract depends on a combination of the country and other employment parameters, such as the contract duration and hours worked. By adding this information to the contract payload, the API will return the list of required for the contract creation. The response simulates the structure of the contract creation form that you'd see in the UI, and describes all necessary fields, validation rules, and the additional endpoints you’ll need to query to populate your contract payload.

Here's a sample request that retrieves the required information to create a contract for a US employee in Washington, working 40 hours per week for 300 days.

```bash
curl --request GET \
     --url 'https://api-sandbox.demo.deel.com/rest/v2/forms/eor/create-contract/US?state=WA&start_date=2025-06-25&work_hours_per_week=40&contract_duration_in_days=300' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {token}'
```

Just like a UI wizard, the response is organized in `pages` > `sections` > `questions`. For each question, when available, the `source` field contains the endpoint to query to retrieve the necessary information. Additionally, by looking at the `rules` object for each question, you can understand the expected format and constraints for the field.

```json
{
  "data": {
    "pages": [
      {
        "title": "Personal details",
        "sections": [
          {
            "title": "Employee Info",
            "questions": [
              {
                "key": "employee.first_name",
                "title": "First name",
                "type": "FreeText",
                "is_required": true
              },
              {
                "key": "employment.country",
                "title": "Employment country",
                "type": "PresetDropdown",
                "is_required": true,
                "source": {
                  "url": "/rest/v2/lookups/countries"
                }
              },
              {
                "key": "employment.work_visa_required",
                "title": "Work visa required",
                "type": "SingleSelection",
                "is_required": true,
                "options": [
                  { "title": "Yes", "value": "true" },
                  { "title": "No", "value": "false" }
                ],
                "rules": [
                  {
                    "requires": [
                      {
                        "key": "employee.nationality",
                        "compare_key": "employment.country",
                        "operator": "ne"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "title": "Job",
        "sections": [
          {
            "title": "Details",
            "questions": [
              {
                "key": "job_title",
                "title": "Job title",
                "type": "FreeText",
                "is_required": true
              }
            ]
          }
        ]
      },
      {
        "title": "Compensation",
        "sections": [
          {
            "title": "Salary",
            "questions": [
              {
                "key": "compensation_details.salary",
                "title": "Salary",
                "type": "Number",
                "is_required": true,
                "rules": [
                  {
                    "min_value": 30000,
                    "requires": [
                      {
                        "key": "employment.type",
                        "operator": "eq",
                        "value": "Full-time"
                      }
                    ]
                  }
                ]
              }
            ]
          }
        ]
      },
      {
        "title": "Benefits",
        "sections": [
          {
            "title": "Healthcare",
            "questions": [
              {
                "key": "benefits.[].plan_id",
                "title": "Healthcare Plan",
                "type": "CustomDropdown",
                "is_required": true,
                "source": {
                  "url": "/rest/v2/eor/benefits"
                }
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## Step 2: Collect the information to create the contract

With the response given in the previous step, you are now ready to retrieve the information necessary for the contract creation payload. Scan the payload from the previous step to see which fields you need to retrieve, and query the respective endpoints:

1. Iterate through `pages` > `sections` > `questions` from the response payload.
2. For every question that has a source, retrieve the required data using the provided definition URL.
3. Collect the desired values for the contract creation payload.

Here's a list of common endpoints you'll need to query to retrieve the information you need. This is not a complete list, always use the response payload as the source of truth for which fields you need to retrieve.

- Entity and organization info
  - [Legal entities](https://developer.deel.com/reference/getlegalentitylist)
  - [Teams](https://developer.deel.com/reference/getteams)
- Employment and compliance
  - [Countries and states](https://developer.deel.com/reference/getcountries)
  - [Job titles](https://developer.deel.com/reference/getjobtitlelist)
  - [Seniorities](https://developer.deel.com/reference/getsenioritylist)
  - [Currencies](https://developer.deel.com/reference/getcurrencies)
- Benefits and allowances
  - [Benefits by country](https://developer.deel.com/reference/retrievebenefitsbycountry)
  - [Fixed allowances](https://developer.deel.com/reference/geteoradditionalcosts)

> 📘 New job scopes must be validated
> 
> If you want to create a contract for a different scope than the default ones, you must first validate the job scope to ensure that the job description is compliant with local laws and regulations. You can use the [Request job scope validation](https://developer.deel.com/reference/requestjobscopevalidation) to validate a scope.

## Step 3: Create the contract

Once you’ve assembled all required data, use the [Create an EOR contract](https://developer.deel.com/reference/createaneorcontract) endpoint to create the contract.

> 👍 Always ensure you apply the field-level rules defined in the form (like min/max values, required flags, or conditional logic). This helps prevent 400 errors when submitting the contract payload.

```json
{
  "data": {
    "client": {
      "team": { "id": "..." },
      "legal_entity": { "id": "..." }
    },
    "employee": {
      "email": "m.scott@dundermifflin.com",
      "first_name": "Michael",
      "last_name": "Scott",
      "address": {
        "country": "US",
        "city": "Scranton"
      }
    },
    "employment": {
      "type": "Full-time",
      "country": "US",
      "start_date": "2025-02-13",
      "scope_of_work": "Overseeing the Scranton branch"
    },
    "compensation_details": {
      "salary": 300000,
      "currency": "USD",
      ...
    },
    "job_title": "Regional manager"
  }
}
```

Creating a contract triggers a quote request for us. Learn how to receive the quote in the next section.

## Step 3: Review the quote from Deel

Since Deel becomes the formal employer of the worker you're hiring, we will issue a quote for the new contract being created. You must approve the quote to proceed with the contract creation.

The time it takes to issue the quote depends on the possibility to automate the quote issuance on our end.

- If the quote can be issued automatically, you'll receive it within a few minutes
- If the quote must be issued manually, it takes up to 24 hours to receive the quote

There are 2 ways to review the quote:

- By [subscribing to the EOR quote created webhook](#subscribe-to-the-eor-quote-created-webhook)
- [From the UI](#review-the-quote-from-the-ui)

### Subscribe to the EOR quote created webhook

The EOR quote created webhook is triggered when a quote is issued for an EOR contract. You can subscribe to the `eor.quote.created` webhook to receive the quote when it's issued.

You can subscribe to the webhook using the [Create webhook endpoint](https://developer.deel.com/reference/createwebhook).

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/webhooks \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "status": "enabled",
    "api_version": "v2",
    "name": "EOR contract quote ready",
    "description": "Triggered when a new quote for a EOR contract becomes available",
    "url": "https://mywebhook.com/listening",
    "signing_key": "{YOUR_SIGNING_KEY}",
    "events": [
      "eor.quote.created"
    ]
  }
}
'
```

You'll receive a `201` response with the content of the newly created webhook.

```json
{
  "data": {
    "id": "00000000-0000-0000-0000-000000000000",
    "name": "EOR contract quote ready",
    "description": "Triggered when a new quote for a EOR contract becomes available",
    "status": "enabled",
    "url": "https://mywebhook.com/listening",
    "signing_key": null,
    "api_version": "v2",
    "events": [
      "eor.quote.created"
    ],
    "created_at": "2020-01-01T00:00:00.000Z",
    "updated_at": "2020-01-01T00:00:00.000Z",
    "hidden": false,
    "internal": true,
    "deleted_at": "string"
  }
}
```

Here's a sample payload that contains the quote information received through the newly created webhook.

```json
{
  "data": {
    "resource": {
      "contract_name": "Michael Scott - Regional Manager",
      "annual_salary": "300000.00",
      "monthly_cost_total": "68636.66",
      "platform_fee_total": "40644.99",
      "country_name": "USA"
    }
  }
}
```

### Review the quote from the UI

Alternatively, you can review a quote from the Deel UI.

For detailed instructions on how to review a quote from the UI, visit [How to review your quote](https://help.letsdeel.com/hc/en-gb/articles/4407737640849-How-to-review-your-quote).

## Signing the contract

If you agree with the quote received, you can proceed to signing the contract. Signing a contract counts as accepting the quote.

Visit [Signing the contract](https://developer.deel.com/docs/eor-sign-contract) for a step-by-tep guide on signing the contract.

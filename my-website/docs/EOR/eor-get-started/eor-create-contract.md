---
title: "Creating an EOR contract"
slug: "eor-create-contract"
excerpt: "Learn how to gather requirements, create the contract, and receive a quote when hiring an EOR employee via API"
hidden: false
createdAt: "Wed Jul 09 2025 13:35:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 09 2025 19:20:00 GMT+0000 (Coordinated Universal Time)"
---
Hiring an EOR employee requires going through several steps.

This guide walks you through the first phase of hiring, which consists in creating the contract and receiving a quote from Deel.

![](https://files.readme.io/778524d138b07c74a1c3dccad8968728914a011e56be0949b21e600fcece4f9c-eor-create-contract-diagram.png)


## Before you begin

Before you begin, make sure that:

- You're equipped to authenticate your requests with a valid [API token](https://developer.deel.com/docs/api-tokens-1).

## Step 1. Understand the required information to create the contract

The first step consists in retrieving the information to create the contract using the the [Fetch EOR contract form](https://developer.deel.com/reference/fetcheorcontractform).

The information you must input to create the contract depends on a combination of the country and other employment parameters, such as the contract duration and hours worked. By adding this information to the contract payload, the API will return the list of required fields for the contract creation, along with references of the endpoints to retrieve them. The response simulates the structure of the contract creation form that you'd see in the UI, and describes all necessary fields, validation rules, and the additional endpoints you’ll need to query to populate your contract payload.

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

## Step 2. Define the job scope

Each contract must be associated to a job scope, where the job is described. A job scope must be validated by our team before it can be used in a contract. This ensures that the job description is compliant with local laws and regulations.

In regards to job scopes, you have 3 alternatives, each one with its tradeoffs to consider, related to the time it takes to create the contract and the level of customization available.

| Option                                                                                                                                                   | Requires validation                                                                           | Customizable | When to use it                                                                                                        | Passed as                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| [Use a pre-defined job scope template](#option-1-use-a-pre-defined-job-scope-template)                                                                   | No                                                                                            | No           | If you don't need a custom job scope and want to create the contract without delay                                    | `scope_template_id`        |
| [Create a new job scope and validate it before you create the contract](#option-2-create-a-new-job-scope-and-validate-it-before-you-create-the-contract) | Only if the automatic validation done when submitting the job scope returns errors (24 hours) | Yes          | If you want to use a custom job scope and can validate it ahead of time                                               | `scope_validation_id`      |
| [Create a new job scope as you create the contract](#option-3-create-a-new-job-scope-as-you-create-the-contract)                                         | Yes (up to 24 hours)                                                                          | Yes          | If you want a custom scope and can't plan validation ahead. Contract won't progress until scope is manually validated | Inline in contract payload |

In all cases, the job scope is passed when [creating the contract](#step-4-create-the-contract), either as a pre-defined job scope template or as a new job scope.

### Option 1: Use a pre-defined job scope template

Using one of the pre-defined job scope templates is the most common option for creating contracts, because job scopes don't require extra time to validate and the contract can move automatically to the next stage.

If you want to use a pre-defined job scope template, you can pass the template ID (`scope_template_id`) you want to use when you [create the contract](#step-4-create-the-contract).

```json
{
  "data": {
    "employment": {
      ...
      "scope_of_work": {
        "scope_template_id": "00000000-0000-0000-0000-000000000000"
      }
    }
  }
}
```

You can retrieve template IDs from the the [Retrieve contract templates](https://developer.deel.com/reference/getcontracttemplates) endpoint.

```bash
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/contract-templates \
     --header 'accept: application/json'
```

A successful response will contain an array of templates. Note down the ID you want to use for your contract.

```json
{
  "data": [
    {
      "id": "12345",
      "title": "Standard Employment Contract"
    },
    {
      "id": "67890",
      "title": "Non-Disclosure Agreement"
    }
  ]
}
```

### Option 2: Create a new job scope and validate it before you create the contract

This option is useful if you want to have more control over the job scope and if you can plan ahead for the validation of the newly-created job scope to happen before creating the contract.

> 📘 Validating a job scope can take up to 24 hours.

To create and validate a new job scope, you can use the [Request job scope validation](https://developer.deel.com/reference/requestjobscopevalidation) endpoint, passing the team ID and the legal entity ID, along with other parameters in the body.

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor/job-scopes/validate \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "team_id": "123e4567-e89b-12d3-a456-426614174000",
    "job_scope": "Sample job description here",
    "job_title": "Regional Manager",
    "work_visa": false,
    "employee_name": "Michael Scott",
    "employment_state": null,
    "employment_country": "US",
    "employee_nationality": "US"
  }
}
'
```

A successful response (`200`), returns a confirmation that the job scope has been validated, along with its ID in the `quote_validation_log_public_id` field. You can use that ID and place it in the `scope_validation_id` field when you [create the contract](#step-4-create-the-contract).

```json
{
    "errors": [],
    "quote_validation_log_public_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "data_for_corrected_job_scope_endpoint": {
        "anonymized_job_scope": null,
        "must_create_correct_job_scope": false,
        "errors_for_correct_job_scope": []
    }
}
```

### Option 3: Create a new job scope as you create the contract

You also have the option to create a new job scope as you create the contract. This option is useful if you want to have more control over the job scope and if you cannot plan the validation ahead of time. However, in this case, the validation is manually by our team, which will inevitably delay the contract movement to the next stage.

To create a new job scope, add the new job description in the contract creation payload when creating a contract. Following is an excerpt of the contract creation payload to show how to do it.

For the full payload, visit [Step 4: Create the contract](#step-4-create-the-contract).

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    ...,
    "employment": {
      ...
      "scope_of_work": "New job description goes here."
    },
    ...
  }
}
'
```

## Step 3. Collect the information to create the contract

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

## Step 4. Create the contract

Once you’ve assembled all required data, use the [Create an EOR contract](https://developer.deel.com/reference/createaneorcontract) endpoint to create the contract.

> 👍 Always ensure you apply the field-level rules defined in the form (like min/max values, required flags, or conditional logic). This helps prevent 400 errors when submitting the contract payload.

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {TOKEN}' \
     --data '
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

A successful response returns the contract details, with some interesting parameters to note down for future use:

- The `contract_id`, that you'll use as a reference for any other contract-related requests.
- Creating a contract triggers a quote creation request for us. If the quote can be issued automatically, it'll be in the `costs` object of the response. For more information, see [Check the contract creation response](#check-the-contract-creation-response)
- The `status` field, which can be used to monitor the status of the contract. As the contract moves through its various stages, the `status` reflects the current state of the contract.
- The `scope_of_work` field, which links a contract to a job description as explained in [Step 2: Define the job scope](#step-2-define-the-job-scope).

The full breakdown of the response is available in the [Create an EOR contract](https://developer.deel.com/reference/createaneorcontract) documentation.

```json
{
  "data": {
    "id": "38j84xg",
    "type": "ongoing_time_based",
    "costs": {
      "summary": {
        "salary": "700,000.00",
        "currency": "EUR",
        "exchange_rate": "0.92",
        "totals_formatted": [
          {
            "title": "Monthly total",
            "total": "61,613.86",
            "frequency": "monthly",
            "total_supporting": "67,116.35"
          }
        ],
        "supporting_currency": "USD"
      },
      "sections": [
        {
          "name": "MONTHLY_EMPLOYMENT_BREAKDOWN",
          "label": "Monthly employment breakdown",
          "groups": [
            {
              "name": "GROSS_MONTHLY_SALARY",
              "costs": [
                {
                  "label": "Salary",
                  "totals": [
                    {
                      "total": "58,333.33",
                      "frequency": "monthly",
                      "total_supporting": "63,542.84"
                    }
                  ]
                }
              ],
              "label": "Gross salary",
              "totals": [
                {
                  "total": "58,633.33",
                  "frequency": "monthly",
                  "total_supporting": "63,869.63"
                }
              ],
              "has_breakdown": true
            }
          ],
          "totals": [
            {
              "total": "61,613.86",
              "frequency": "monthly",
              "total_supporting": "67,116.35"
            }
          ],
          "is_summarized": true,
          "standalone_items": [
            {
              "name": "One off payment",
              "label": "Printed Agreement handling fee",
              "totals": [
                {
                  "total": "73.44",
                  "frequency": "monthly",
                  "total_supporting": "80.00"
                }
              ]
            }
          ]
        }
      ],
      "additional_data": {
        "annual_notes": [],
        "monthly_notes": [],
        "once_off_notes": [],
        "additional_notes": [
          "Kindly note that the onboarding process for employees in this country requires the completion of a QES (Qualified Electronic Signature) process, which carries a fee of $80 USD. This fee is designed to cover the additional administrative expenses associated with the QES process. In the event that the QES option is not available, an alternative would be to proceed with a printed agreement signature process, incurring costs of $80 USD. These costs include expenses for printing, shipping, and handling related to the signing of the printed agreement.",
          "Deel can countersign the employment agreement once you provide a Qualifying Electronic Signature (QES). After the employee registers on the Deel platform, we will notify and invite you to sign the Scope of Work, through the QES process. Please note that we are unable to proceed with your employee full onboarding until you complete this QES signing step."
        ]
      }
    },
    "client": {
      "legal_entity": {
        "name": "string"
      }
    },
    "status": "new",
    "employee": {
      "email": "string",
      "last_name": "string",
      "first_name": "string",
      "legal_name": "string"
    },
    "job_title": "string",
    "seniority": {
      "id": 0,
      "name": "string"
    },
    "created_at": "2025-06-26T14:42:58.458Z",
    "employment": {
      "state": "string",
      "country": "string",
      "end_date": "2025-06-26",
      "start_date": "2025-06-26",
      "scope_of_work": "string",
      "time_off_type": "string",
      "probation_period": 0,
      "work_visa_required": true,
      "calculated_holidays": 0
    },
    "health_plan": {
      "id": "string",
      "name": "string"
    },
    "compensation_details": {
      "salary": 0,
      "currency": "string",
      "variable_compensation": "string",
      "variable_compensation_type": "string"
    }
  }
}
```

Once the contract is created, the next step is to review the quote once it's issued.

## Step 5: Review the quote from Deel

Since Deel becomes the formal employer of the worker you're hiring, we will issue a quote for the new contract being created. You must approve the quote to proceed with the contract creation.

Depending on the country where of the contract, the quote can be issued automatically or manually.

- If the quote can be issued automatically, you'll receive immediately
- If the quote must be issued manually, it takes up to 24 hours to receive the quote

There are a few ways to check for the quote:

- In the [response when creating the contract](#check-the-contract-creation-response)
- By [subscribing to the EOR quote created webhook](#subscribe-to-the-eor-quote-created-webhook)
- [Using the Retrieve EOR contract details endpoint](#check-the-quote-status-using-the-retrieve-eor-contract-details-endpoint)
- [From the UI](#review-the-quote-from-the-ui)

### Check the contract creation response

If the quote can be issued automatically, the response will contain the quote in the `costs` object. Here's how you can interpret the response:

```json
    "costs": {
      "summary": {
        "salary": "700,000.00",
        "currency": "EUR",
        "exchange_rate": "0.92",
        "totals_formatted": [
          {
            "title": "Monthly total",
            "total": "61,613.86",
            "frequency": "monthly",
            "total_supporting": "67,116.35"
          }
        ],
        "supporting_currency": "USD"
      },
      "sections": [
        {
          "name": "MONTHLY_EMPLOYMENT_BREAKDOWN",
          "label": "Monthly employment breakdown",
          "groups": [
            {
              "name": "GROSS_MONTHLY_SALARY",
              "costs": [
                {
                  "label": "Salary",
                  "totals": [
                    {
                      "total": "58,333.33",
                      "frequency": "monthly",
                      "total_supporting": "63,542.84"
                    }
                  ]
                }
              ],
              "label": "Gross salary",
              "totals": [
                {
                  "total": "58,633.33",
                  "frequency": "monthly",
                  "total_supporting": "63,869.63"
                }
              ],
              "has_breakdown": true
            }
          ],
          "totals": [
            {
              "total": "61,613.86",
              "frequency": "monthly",
              "total_supporting": "67,116.35"
            }
          ],
          "is_summarized": true,
          "standalone_items": [
            {
              "name": "One off payment",
              "label": "Printed Agreement handling fee",
              "totals": [
                {
                  "total": "73.44",
                  "frequency": "monthly",
                  "total_supporting": "80.00"
                }
              ]
            }
          ]
        }
      ],
      "additional_data": {
        "annual_notes": [],
        "monthly_notes": [],
        "once_off_notes": [],
        "additional_notes": [
          "Kindly note that the onboarding process for employees in this country requires the completion of a QES (Qualified Electronic Signature) process, which carries a fee of $80 USD. This fee is designed to cover the additional administrative expenses associated with the QES process. In the event that the QES option is not available, an alternative would be to proceed with a printed agreement signature process, incurring costs of $80 USD. These costs include expenses for printing, shipping, and handling related to the signing of the printed agreement.",
          "Deel can countersign the employment agreement once you provide a Qualifying Electronic Signature (QES). After the employee registers on the Deel platform, we will notify and invite you to sign the Scope of Work, through the QES process. Please note that we are unable to proceed with your employee full onboarding until you complete this QES signing step."
        ]
      }
    }
```

| Field                                            | Description                                                                 |
| ------------------------------------------------ | --------------------------------------------------------------------------- |
| `costs.summary.totals_formatted[]`               | Precomputed totals (monthly or annual)                                      |
| `costs.summary.salary`                           | Annual gross salary in local currency                                       |
| `costs.summary.currency` / `supporting_currency` | Local and supporting (usually USD) currencies                               |
| `costs.summary.exchange_rate`                    | FX rate used to calculate supporting totals                                 |
| `costs.sections[]`                               | Main breakdown by category                                                  |
| `sections[].groups[]`                            | Sub-categories like salary, taxes, management fees                          |
| `groups[].label`                                 | Label for cost group (e.g. "Gross Salary", "Employer Cost", "Monthly Fees") |
| `groups[].costs[]`                               | Individual cost items (e.g. "Salary", "National Insurance", etc.)           |
| `groups[].totals[]`                              | Group-level monthly/annual totals                                           |
| `sections[].totals[]`                            | Section-level total (e.g., total monthly employment cost)                   |
| `sections[].standalone_items[]`                  | One-off costs (e.g. printed agreement fees). Not included in main totals.   |
| `costs.additional_data.additional_notes[]`       | Contextual notes (e.g. QES process, post-enrollment benefit costs)          |
| `monthly_eor_management_fee_usd`                 | Deel platform fee; also found in `MONTHLY_FEES` group                       |

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

### Check the quote status using the Retrieve EOR contract details endpoint

When a quote cannot be issued automatically upon contract creation, the status of the contract will change to `under_review` after its creation, and the `costs` object will be `null`.

You can keep monitoring the status of the contract using the [Retrieve EOR contract details endpoint](https://developer.deel.com/reference/retrieveeorcontractdetails) endpoint.

When the quote becomes available, the contract status changes to `waiting_for_client_sign` and the `costs` object is populated.

Include the `contract_id` obtained when [creating the contract](#step-4-create-the-contract) in your request:

```bash
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/eor/contracts/{contract_id}/details \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}'
```

The `costs` object returned in the response has the same structure as the one returned when creating the contract. For a detailed breakdown, refer to [Check the contract](#check-the-contract-creation-response).

### Review the quote from the UI

Alternatively, you can review a quote from the Deel UI.

For detailed instructions on how to review a quote from the UI, visit [How to review your quote](https://help.letsdeel.com/hc/en-gb/articles/4407737640849-How-to-review-your-quote).

## Signing the contract

If you agree with the quote received, you can proceed to signing the contract. Signing a contract counts as accepting the quote.

Visit [Signing the contract](https://developer.deel.com/docs/eor-sign-contract) for a step-by-tep guide on signing the contract.

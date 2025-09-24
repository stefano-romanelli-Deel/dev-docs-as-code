---
title: "Create a milestone based contract"
slug: "create-contract-milestone"
excerpt: "Learn how to create contracts where the contractor is paid based on milestones"
hidden: false
createdAt: "Wed Aug 14 2024 10:26:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 25 2025 14:33:12 GMT+0000 (Coordinated Universal Time)"
---
Milestone contracts are suited for projects with defined goals and deliverables. The independent contractor’s payment is tied to each milestone rather than the contract itself. Because of this, many compensation fields are not required when creating the contract.

This guide explains how to create a milestone based contract with the API. It mirrors the Milestone contract type available in the Deel UI.

In the UI, at least one milestone must be added during contract creation. With the API, milestones are created separately after the contract is signed and then linked to it. For more information on the UI process, visit [How To Create A Milestone Contract On Deel](https://help.letsdeel.com/hc/en-gb/articles/4407745475857-How-To-Create-A-Milestone-Contract-On-Deel) on the Help Center.

> 👍 Configure who can submit work from the UI
> 
> Either you, the contractor, or both can submit work on milestone contracts. Visit the [Help Center](https://help.letsdeel.com/hc/en-gb/articles/4407737743505-How-To-Create-A-Pay-As-You-Go-Contract-On-Deel) for more information on how to configure who can submit work.

## Before you begin

Use the [Create contract](https://developer.deel.com/reference/createanewcontract) endpoint to set up any contracts. This guide focuses on the fields specific to milestone contracts, and assumes that you are familiar with the endpoint and the data structure. These are explained in [Create a contract](https://developer.deel.com/docs/create-contract).

## 1. Add generic details

Start filling the `data` object with the payload top-level contract details.

For the `contract_template_id`, use the [Retrieve contract templates](https://developer.deel.com/reference/getcontracttemplates) endpoint.

```json
{
  "data": {
    "country_code": "US",
    "external_id": "11001100110",
    "notice_period": 15,
    "scope_of_work": "Lorem ipsum dolor sit amet.",
    "special_clause": "Lorem ipsum dolor sit amet.",
    "start_date": "2024-08-01",
    "state_code": "IL",
    "termination_date": "2025-08-31",
    "title": "Engineer",
    "type": "payg_milestones"
    "contract_template_id": "00000000-0000-0000-0000-000000000000",
    …
  }
}
```

Where:

| Name                   | Required | Type   | Format | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example                                |
| ---------------------- | -------- | ------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `start_date`           | true     | string | date   | The start date of the contract. Use the ISO-8601 short date format YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                                                                              | `2024-08-01`                           |
| `title`                | true     | string | -      | The name of the contract.                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `Engineer`                             |
| `type`                 | true     | string | enum   | Determines the contract type. For a task-based pay-as-you-go contract, the type must be set to `payg_tasks`.                                                                                                                                                                                                                                                                                                                                                                | `payg_tasks`                           |
| `country_code`         | false    | string | -      | The code of the country of the contractor's tax residence. Leave it blank to use the country indicated by the contractor when they create their profile. Use the ISO 3166-1 alpha-2 code in capital letters for the residence of the contractor. A list of the available country codes can be found on our [Help Center](https://help.letsdeel.com/hc/en-gb/articles/15021126310161-How-To-Troubleshoot-Issues-When-Mass-Importing-Employees#h_01GZJS969FZY3K2K4V8YGRNEGJ). | `US`                                   |
| `external_id`          | false    | string | -      | Can be used to link the ID of the worker from third-party system or platform.                                                                                                                                                                                                                                                                                                                                                                                               | `11001100110`                          |
| `notice_period`        | false    | number | -      | The number of days of notice required to terminate the contract.                                                                                                                                                                                                                                                                                                                                                                                                            | `10`                                   |
| `scope_of_work`        | false    | string | -      | Fill it with a job description or a summary of the roles and responsibilities of the worker.                                                                                                                                                                                                                                                                                                                                                                                | `Lorem ipsum dolor sit amet.`          |
| `special_clause`       | false    | string | -      | Fill it with any special clauses to be included in the contract.                                                                                                                                                                                                                                                                                                                                                                                                            | `Lorem ipsum dolor sit amet.`          |
| `state_code`           | false    | string | -      | If the `country_code` parameter is set to `US`, indicates the state code of the contract.                                                                                                                                                                                                                                                                                                                                                                                   | `IL`                                   |
| `termination_date`     | false    | string | date   | The termination date of the contract. Use the ISO-8601 short date format YYYY-MM-DD.                                                                                                                                                                                                                                                                                                                                                                                        | `2025-08-31`                           |
| `contract_template_id` | false    | string | -      | The contract template identifier to use when creating a contract.                                                                                                                                                                                                                                                                                                                                                                                                           | `00000000-0000-0000-0000-000000000000` |

## 2. Add client information

Each contract must be associated with a legal entity and a team (group), that are client-specific information. The `client` object allows to associate the contract being created to existing legal entities and teams using their IDs. You can retrieve the IDs using the following endpoints:

- For the legal entity ID, use the [Get list of legal entities](https://developer.deel.com/reference/getlegalentitylist) endpoint
- For the team ID, use the [Get team list](https://developer.deel.com/reference/getteams) endpoint

> 👍 New legal entities and teams (groups) can be created using the [POST create legal entity](https://developer.deel.com/reference/createlegalentity) and the [POST create group](https://developer.deel.com/reference/creategroup-1) endpoints respectively.

```json
{
  "data": {
    …,
    "client": {
      "legal_entity": {
        "id": "00000000-0000-0000-0000-000000000000"
      },
      "team": {
        "id": "00000000-0000-0000-0000-000000000000"
      }
    }
  }
}
```

Where:

| Name                     | Required | Type   | Format | Description                 | Example                                |
| ------------------------ | -------- | ------ | ------ | --------------------------- | -------------------------------------- |
| `client.legal_entity.id` | true     | string | UUID   | The ID of the legal entity. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `client.team.id`         | true     | string | UUID   | The ID of the team (group). | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

## 3. Add worker's personal information

The `worker` object contains the worker's personal information. The email must be unique in your organization. If the email already exists, the contract will be connected to the worker's existing profile.

> 👍 Use the worker's personal email
> 
> This way they can access their account and contract even after the contract has ended.

```json
{
  "data": {
    …,
    "worker": {
      "expected_email": "demo@email.com",
      "first_name": "John",
      "last_name": "Doe"
    }
  }
}
```

Where:

| Name                    | Required | Type   | Format | Description                      | Example          |
| ----------------------- | -------- | ------ | ------ | -------------------------------- | ---------------- |
| `worker.expected_email` | true     | string | email  | The email of the contractor      | `demo@email.com` |
| `worker.first_name`     | true     | string | -      | The first name of the contractor | `John`           |
| `worker.last_name`      | false    | string | -      | The last name of the contractor  | `Doe`            |

## 4. Add job title and seniority

Optionally, a job title and a seniority level can be associated to the contract using the `job_title` and `seniority` objects. You can retrieve the job title and seniority level IDs from the following endpoints:

- For the job title ID, use the [GET job title list](https://developer.deel.com/reference/getjobtitlelist) endpoint
- For the seniority ID, use the [GET seniority levels](https://developer.deel.com/reference/retrievesenioritylevels) endpoint

> 👍 Creating new job titles
> 
> New job titles can be created by replacing the `job_title.id` with `job_title.name`, containing the name of the new job title. For example:
> 
> ```json
>     "job_title": {
>       "name": "Director"
>     },
> ```

```json
{
  "data": {
    …,
    "job_title": {
      "id": "12345"
    },
    "seniority": {
      "id": "12345"
    }
  }
}
```

Where:

| Name           | Required | Type   | Format | Description                   | Example |
| -------------- | -------- | ------ | ------ | ----------------------------- | ------- |
| `job_title.id` | true     | number | ID     | The ID of the job title       | `12345` |
| `seniority.id` | false    | number | ID     | The ID of the seniority level | `12345` |

## 5. Add meta information

The `meta` object allows to adjust additional settings of the contract, such as requiring the contractor to provide additional compliance documents as per their country's local laws.

> 👍 Recommendation
> 
> Request these documents to meet compliance obligations.

```json
{
  "data": {
    …,
    "meta": {
      "documents_required": true,
      "is_main_income": true
    }
  }
}
```

Where:

| Name                 | Required | Type    | Format | Description                                                                                                                                                                                                                                                                 | Example |
| :------------------- | :------- | :------ | :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `documents_required` | true     | boolean | -      | Determines whether contractors must provide [additional compliance documents](https://help.letsdeel.com/hc/en-gb/articles/4407745411217-What-compliance-documents-will-contractors-need-to-upload). We recommend requesting these documents to meet compliance obligations. | true    |
| `is_main_income`     | flase    | boolean | -      | Indicates whether the contract is the contractor’s primary source of income.                                                                                                                                                                                                | true    |

## 6. Add compensation details

How much the contractor will be compensated and when can be defined in the `compensation_details` object.

```json
{
  "data": {
    …,
    "compensation_details": {
      "amount": 100,
      "currency_code": "USD",
      "cycle_end": 30,
      "cycle_end_type": "DAY_OF_MONTH",
      "first_payment": 0,
      "first_payment_date": "2024-09-05",
      "frequency": "weekly",
      "notice_period": 15,
      "pay_before_weekends": true,
      "payment_due_days": 5,
      "payment_due_type": "REGULAR",
    }
  }
}
```

Where:

| Name | Required | Type | Format | Description | Example |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `compensation_details.currency_code` | true | string | - | Indicates the currency code of the compensation following the 3-digit ISO 4217 format. Visit the [Help center](https://help.letsdeel.com/hc/en-gb/articles/4407737591953-In-What-Currencies-Can-I-Create-A-Contractor-Contract) for a list of supported currencies. | `USD` |
| `compensation_details.cycle_end` | true | number | - | Indicates the day when the invoicing cycle ends, based on what's set in the `cycle_end_type` parameter. For example, use 7 for a Sunday or use 30 for the 30th of the month. If the month is shorter than the number indicated, the cycle ends on the last day of the month. | 30 |
| `compensation_details.cycle_end_type` | true | string | enum | Together with the `cycle_end` parameter, determines when the compensation cycle ends. Available values are:<br/>- `DAY_OF_MONTH` for the calendar day of the month<br/>- `DAY_OF_WEEK` for the week day in weekly payments<br/>- `DAY_OF_LAST_WEEK` for the last week day of the month | `DAY_OF_MONTH` |
| `compensation_details.frequency` | true | string | enum | Determines how often the compensation is paid to the contractor. The available values are `monthly`, `weekly`, `biweekly`, `semimonthly`, and `calendar_month`. | `weekly` |
| `compensation_details.amount` | false | number | - | The amount of the compensation to be paid to the contractor. How frequently the compensation is determined by the `frequency` parameter. | 100 |
| `compensation_details.first_payment` | false | number | - | Determines the amount of the first payment, based on the invoicing cycle. | `1000` |
| `compensation_details.first_payment_date` | false | string | date | Can be used to force the date of the first payment when the date falls outside of the invoicing cycle. Use the ISO-8601 short date format YYYY-MM-DD. | `2024-09-05` |
| `compensation_details.notice_period` | false | number | - | Determines the days of notice that each party must give to end the contract. | `15` |
| `compensation_details.pay_before_weekends` | false | boolean | - | When set to `true`, if the pay day falls on a weekend, the compensation payment will be anticipated to the last working day of the week. | `true` |
| `compensation_details.payment_due_days` | false | number | - | When the `payment_due_type` parameter is set to `REGULAR`, this parameter determines the offset of days for the payment to be due. For example, set it to 5 if you want the payment to be due 5 days after the last day of the invoicing cycle. | `0` |
| `compensation_details.payment_due_type` | false | string | enum | Determines when the payment is due. If you select `REGULAR`, the payment is determined by the `payment_due_days` parameter. If you select `WITHIN_MONTH` the payment is due on the last day of the invoicing cycle. | `WITHIN_MONTH` |


## 7. Make the API request

Now that all the contract information is set, it's time to make the API request. Here's how the request should look like.

A successful response returns a `200` status code and includes the contract ID and details in the payload. Save the `id` parameter at the top of the response, you need it for the next step: signing the contract.

```curl Request payload
curl --request POST \
     --url 'https://api.letsdeel.com/rest/v2/contracts' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data-raw '
{
  "data": {
    "country_code": "US",
    "external_id": "11001100110",
    "notice_period": 10,
    "scope_of_work": "Lorem ipsum dolor sit amet.",
    "special_clause": "Lorem ipsum dolor sit amet.",
    "start_date": "2024-08-01",
    "state_code": "IL",
    "termination_date": "2024-08-31",
    "title": "Contract",
    "type": "payg_milestones",
    "client": {
      "legal_entity": {
        "id": "00000000-0000-0000-0000-000000000000"
      },
      "team": {
        "id": "00000000-0000-0000-0000-000000000000"
      }
    },
    "worker": {
      "expected_email": "demo@email.com",
      "first_name": "John",
      "last_name": "Doe"
    },
    "job_title": {
      "id": "12345"
    },
    "seniority": {
      "id": "12345"
    },
    "meta": {
      "documents_required": true
    },
    "compensation_details": {
      "amount": 100,
      "currency_code": "USD",
      "cycle_end": 30,
      "cycle_end_type": "DAY_OF_MONTH",
      "first_payment": 0,
      "first_payment_date": "2024-09-05",
      "frequency": "weekly",
      "notice_period": 0,
      "pay_before_weekends": true,
      "payment_due_days": 5,
      "payment_due_type": "REGULAR"
    }    
  }
}'
```
```json Response payload
{
    "data": {
        "id": "8e9vjjd",
        "title": "Contract",
        "type": "payg_milestones",
        "status": "waiting_for_client_sign",
        "created_at": "2025-08-21T09:17:31.792Z",
        "client": {
            "team": {
                "id": "39065a83-b18c-482e-95bf-bd6a2940cdb6",
                "name": "Wayne Enterprise UK"
            },
            "legal_entity": {
                "id": "8dc7e92a-ccff-457d-9995-fd4ae9f0e757",
                "name": "Wayne Enterprise Global",
                "email": "",
                "type": "company",
                "subtype": "general-partnership",
                "registration_number": "987654321",
                "vat_number": "123456789"
            }
        },
        "worker": {
            "id": "4ce38570-f263-4f1c-a848-571f8e06e5da",
            "expected_email": "demo@email.com",
            "first_name": "John",
            "last_name": "Doe"
        },
        "invitations": {
            "client_email": "",
            "worker_email": ""
        },
        "signatures": {
            "client_signature": "",
            "client_signed_at": null,
            "worker_signature": "",
            "worker_signed_at": null,
            "signed_at": null
        },
        "compensation_details": {
            "currency_code": "USD",
            "amount": null,
            "scale": "",
            "frequency": "",
            "first_payment": "",
            "first_payment_date": "",
            "gross_annual_salary": "",
            "gross_signing_bonus": "",
            "gross_variable_bonus": "",
            "variable_compensations": null,
            "cycle_end": null,
            "cycle_end_type": null
        },
        "contract_template": null,
        "employment_details": {
            "type": "payg_milestones",
            "days_per_week": 0,
            "hours_per_day": 0,
            "probation_period": 0,
            "paid_vacation_days": 0
        },
        "job_title": "Engineer",
        "scope_of_work": "Lorem ipsum dolor sit amet.",
        "seniority": {
            "id": 3,
            "name": "Senior (Individual Contributor Level 3)",
            "level": 3
        },
        "special_clause": "Lorem ipsum dolor sit amet.",
        "start_date": "2024-07-31T16:00:00.000Z",
        "termination_date": "2024-08-31T15:59:59.999Z",
        "is_archived": false,
        "notice_period": 10,
        "custom_fields": [],
        "external_id": "11001100110",
        "employment_type": null,
        "work_schedule": null
    }
}
```

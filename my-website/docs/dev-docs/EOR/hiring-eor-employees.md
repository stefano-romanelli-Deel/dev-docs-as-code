---
title: "Hiring EOR employees"
slug: "hiring-eor-employees"
excerpt: "Learn how to create EOR contracts, sign them, and invite workers using the Deel API"
hidden: false
createdAt: "Wed Feb 12 2025 16:25:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 25 2025 13:40:42 GMT+0000 (Coordinated Universal Time)"
---
When you want to hire workers in a country where you don't have a business, you can use our EOR. With the EOR service, workers are hired using one of Deel's legal entities in 150+ countries.  
Using EOR allows you to stay compliant when it comes to contracts, minimum wage, terminations, and other local laws, without the need to set up a local legal entity in the country you want to hire.

This guide explains how to create EOR contracts, sign them, and invite workers using the Deel API.

## In this guide

- [Part 1: Retrieve information to create the contract](#part-1-retrieve-information-to-create-the-contract)
- [Part 2: Create the contract](#part-2-create-the-contract)
- [Part 3: Receive a quote from Deel](#part-3-receive-a-quote-from-deel)
- [Part 4: Sign the contract](#part-4-sign-the-contract)
- [Part 5: The worker signs the contract](#part-5-the-worker-signs-the-contract)

## Part 1: Retrieve information to create the contract

The first part of the hiring flow is to retrieve information to create the contract.

![](https://files.readme.io/b0d878210a73c325c9016d3f5bf5d8db9aabcafab2863e3bb10686a899620831-eor-hiring-flow-diagram-part1.png)


### Step 1. Retrieve country-specific information

EOR workers are subject to laws and regulation of the country they are hired in. To understand the requirements for hiring an EOR worker in a particular country, you can retrieve country-specific information.

The [Retrieve detailed hiring guide for a country](https://developer.deel.com/reference/geteorcountryvalidations) endpoint returns information about hiring in each country, so that you can understand requirements, such as holidays, sick leave, minimum salary, probation period, pension, available insurance providers, and so on.

You need the information retrieved with this endpoint to fill the details of the contract you want to create.

Below you will find an example of what the response looks like:

```json
{
  "data": {
    "holiday": {
      "min": "23",
      "max": null,
      "mostCommon": "25"
    },
    "part_time_holiday": {
      "type": "STANDARD",
      "min": "23"
    },
    "sick_days": {
      "min": "0",
      "max": "365"
    },
    "salary": {
      "min": "15120.00",
      "max": "800000.00",
      "frequency": "monthly"
    },
    "probation": {
      "min": null,
      "max": 180
    },
    "part_time_probation": {
      "min": null,
      "max": 180
    },
    "work_schedule": {
      "days": {
        "max": null,
        "min": "5.0000"
      },
      "hours": {
        "max": null,
        "min": "8.0000"
      }
    },
    "currency": "EUR",
    "hiring_guide_country_name": "spain",
    "start_date_buffer": 3,
    "definite_contract": {
      "type": "NOT_ALLOWED",
      "maximum_limitation": null
    },
    "adjustments_information_box": "For reimbursable costs connected to carrying out work, choose \"expenses\".\nFor fixed or recurring amounts provided as a benefit to employee, choose \"allowances\".",
    "health_insurance": {
      "status": "ENABLED",
      "providers": [
         …
      ]
    },
    "pension": {
      "status": "REQUIRED",
      "providers": [
        {
          "id": "c1631641-1d6e-41ad-bc0c-cbbbe3f565ca",
          "name": "Fidelity",
          "home_page_url": "https://www.fidelity.com/",
          "contribution": {
            "type": "PERCENTAGE",
            "minimum": "2.00",
            "maximum": "2.00"
          }
        }
      ]
    },
    "mandatory_fields": [
      …
    ]
  }
}
```

### Step 2: Retrieve other information

Filling the payload to create a contract requires information that you can retrieve using other endpoints. Here's a list of the info you will need and the respective endpoints:

| Info            | Endpoint                                                                           |
| --------------- | ---------------------------------------------------------------------------------- |
| Legal entity ID | [List of legal entities](https://developer.deel.com/reference/getlegalentities)    |
| Team ID         | [Get team list](https://developer.deel.com/reference/getteams)                     |
| Seniority level | [Retrieve seniority levels](https://developer.deel.com/reference/getsenioritylist) |

## Part 2: Create the contract

After [retrieving the information to create the contract](#part-1-retrieve-information-to-create-the-contract), you can create it using the [Create EOR contract](https://developer.deel.com/reference/createeorcontract) endpoint.

![](https://files.readme.io/4d16b2433c1efef063aa6dce6b383287bb01e1d73fb57789ce2a576894131cb0-eor-hiring-flow-diagram-part2.png)


Following is a sample request for your reference:

```curl
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor \
     --header 'accept: application/json' \
     --header 'authorization: Bearer Token' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "client": {
      "team": {
        "id": "0c7012ce-2843-4b59-85b0-21c8dfa5fc5b"
      },
      "legal_entity": {
        "id": "0a71b451-4979-490b-b0be-1461f81bf994"
      }
    },
    "employee": {
      "address": {
        "zip": "18509",
        "city": "Scranton",
        "state": "PA",
        "street": "1725 Slough Avenue",
        "country": "US"
      },
      "email": "m.scott@dundermifflin.com",
      "last_name": "Scott",
      "first_name": "Michael",
      "nationality": "US"
    },
    "seniority": {
      "id": "6"
    },
    "employment": {
      "work_visa_required": false,
      "type": "Full-time",
      "country": "US",
      "start_date": "2025-02-13",
      "scope_of_work": "Overseeing the Scranton branch for Dunder Mifflin",
      "time_off_type": "STANDARD"
    },
    "compensation_details": {
      "salary": 300000,
      "currency": "US"
    },
    "job_title": "Regional manager"
  }
}
'
```

## Part 3: Receive a quote from Deel

Since we're the formal employers of the worker you're hiring, we will issue a quote for the new contract being created.

![](https://files.readme.io/11bc480d6066e7c5279646b1293474fccb91dd2308855e7eb9512bea2a6716d4-eor-hiring-flow-diagram-part3.png)


> 📘 Quote issuance timeline
> 
> The time it takes to receive the quote depends on the possibility to automate the quote issuance on our end.
> 
> - If the quote can be issued automatically, you'll receive it within a few minutes
> - If the quote must be issued manually, it takes up to 24 hours to receive the quote

You can review the quote by subscribing to the dedicated `eor.quote.created` webhook. You can subscribe to webhooks using the [Create a webhook](https://developer.deel.com/reference/createwebhook) endpoint.

For more information on how to subscribe to a webhook, visit [Getting started with webhooks](https://developer.deel.com/docs/getting-started-2).

If you accept the quote, you can proceed to signing the contract, and it will count as accepting the quote. In the same way, not signing the contract will count as rejecting the quote.

Following is a sample webhook payload emitted when the quote is available:

```json
{
    "data": {
        "meta": {
            "event_type": "eor.quote.created",
            "event_type_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
            "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
            "organization_name": "API Integration Account",
            "tracking_id": "abcdefg1234567890abdcefg1234567"
        },
        "resource": {
            "annual_salary": "300000.00",
            "breakdown_costs": {
                "monthly": {
                    "costs": [
                        {
                            "currency": "INR",
                            "name": "Employees' Deposit Linked Insurance (EDLI)",
                            "total": "75.00",
                            "total_usd": "0.91"
                        },
                        {
                            "currency": "INR",
                            "name": "Employee's Provident Fund (EPF)",
                            "total": "1800.00",
                            "total_usd": "21.74"
                        },
                        {
                            "currency": "INR",
                            "name": "Provident Fund Office EPF Admin Fee",
                            "total": "75.00",
                            "total_usd": "0.91"
                        }
                    ],
                    "total": "1950.00",
                    "total_usd": "23.56"
                }
            },
            "cba_total": "0.00",
            "cba_total_usd": "0.00",
            "contract_id": "d3m0d3m",
            "contract_name": "Michael Scott - Regional Manager",
            "country_name": "India",
            "created_at": "2024-11-07T13:16:25.747Z",
            "currency": "INR",
            "employer_cost_total": "1950.00",
            "employer_cost_total_usd": "23.56",
            "gross_salary_total": null,
            "gross_salary_total_usd": "25000.00",
            "mobility_fee_total": null,
            "mobility_fee_total_usd": null,
            "monthly_cost_total": "68636.66",
            "monthly_cost_total_usd": "829.15",
            "platform_fee_total": "40644.99",
            "platform_fee_total_usd": "491.00",
            "recurring_allowance_total": "0.00",
            "recurring_allowance_total_usd": "0.00",
            "salary_total": "25000.00",
            "salary_total_usd": "302.01",
            "severance_accrual_total": "1041.67",
            "severance_accrual_total_usd": "0.00",
            "updated_at": "2024-11-07T13:16:25.747Z"
        }
    },
    "timestamp": "2024-11-07T13:22:47.823Z"
}
```

> 👍 You can also review the quote from the UI
> 
> For more information, visit [How to create an Employer of Record (EOR) contract](https://help.letsdeel.com/hc/en-gb/articles/4407745374353-How-to-Create-an-Employer-Of-Record-EOR-Contract#h_01GP882AADCXR6DX53BDTKM2NH) and [How to review your quote](https://help.letsdeel.com/hc/en-gb/articles/4407737640849-How-to-review-your-quote) in our Help Center.

## Part 4: Sign the contract

If you [agree with the quote](#part-3-receive-a-quote-from-deel) for the contract, you can go ahead and sign it and it will be automatically accepted.

![](https://files.readme.io/fb2b1ad12acb753b9fed5518b12a58f48c0554e50125af3398f84375f7c88577-eor-hiring-flow-diagram-part4.png)


To sign a contract, you can use the Sign a contract endpoint. For more information, visit the [Sign a contract endpoint reference](https://developer.deel.com/reference/signcontract).

## Part 5: The worker signs the contract

Once you sign the contract, the worker receives an invitation email to create their Deel account and sign the contract.

![](https://files.readme.io/081060c4151d1716cb2d94a9ccc10121bb679e694008f5b1f2ff5dd3cbddb1c8-eor-hiring-flow-diagram-part5.png)


You can also monitor the contract status by [subscribing](https://developer.deel.com/reference/createwebhook) to the dedicated [`contract.status.updated`](https://developer.deel.com/docs/event-payload-examples#contractstatusupdated) webhook. review the quote by subscribing to the dedicated `eor.quote.created` webhook.

For more information on how to subscribe to a webhook, visit [Getting started with webhooks](https://developer.deel.com/docs/getting-started-2).

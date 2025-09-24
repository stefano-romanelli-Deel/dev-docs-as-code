---
title: "Hire EOR employees"
slug: "hire-eor-employees"
excerpt: "Learn how to create EOR contracts, sign them, and complete worker onboarding using the Deel API"
hidden: true
createdAt: "Wed May 07 2025 10:13:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 07 2025 10:13:21 GMT+0000 (Coordinated Universal Time)"
---
When you want to hire workers in a country where you don't have a business, you can use our EOR. With the EOR service, workers are hired using one of Deel's legal entities in 150+ countries. Using EOR allows you to stay compliant when it comes to contracts, minimum wage, terminations, and other local laws, without the need to set up a local legal entity in the country you want to hire.

This guide explains how to create EOR contracts, sign them, invite workers, and complete their onboarding using the Deel API.

## In this guide

- [Part 1: Retrieve information to create the contract](#part-1-retrieve-information-to-create-the-contract)
- [Part 2: Create the contract](#part-2-create-the-contract)
- [Part 3: Receive a quote from Deel](#part-3-receive-a-quote-from-deel)
- [Part 4: Sign the contract](#part-4-sign-the-contract)
- [Part 5: The worker signs the contract](#part-5-the-worker-signs-the-contract)
- [Part 6: Complete worker onboarding](#part-6-complete-worker-onboarding)0

## Before you begin

Creating an EOR contract involves a through understanding of country-specific requirements and querying many endpoints to retrieve information that's needed for the creation request payload and subsequent steps. Make sure to read the [Get started with EOR contracts](https://developer.deel.com/docs/eor-get-started) before following the instructions in this guide.

## Part 1: Retrieve information to create the contract

The first part of the hiring flow is to retrieve information to create the contract.

![](https://files.readme.io/513f4d6e4468a6552dfa2f7bae081aace08005f8e1acfbc0a24577b4be60c359-eor-hiring-flow-diagram-part1.png)


### Step 1. Retrieve country-specific hiring requirements

EOR workers are subject to the laws and regulations of the country they are hired in. To ensure the contract complies with local requirements, you can use the [Retrieve detailed hiring guide for a country](https://developer.deel.com/reference/geteorcountryvalidations) endpoint. This returns information such as:

- Minimum salary
- Work schedules
- Probation periods
- Paid leave policies
- Statuatory benefits

### Step 2: Retrieve applicable benefits

Benefits vary based on the legal entity, team, visa status, and employment type. Use the [Retrieve benefits by country](https://developer.deel.com/reference/retrievebenefitsbycountry) endpoint to get real-time, applicable benefits based on:

- Legal entity and team
- Contract type and hours per week
- Visa status (if applicable)

This helps ensure you offer compliant and non-discriminatory benefits to your workers.

### Step 3: Retrieve required fields for the contract

Filling the payload to create a contract requires information that you can retrieve using other endpoints. Here's a list of the info you will need and the respective endpoints:

- The [Fetch EOR contract form](https://developer.deel.com/reference/fetcheorcontractform) endpoint returns required fields and where to retrieve them.
- The [Get worker additional fields for EOR](https://developer.deel.com/reference/getworkeradditionalfieldsforeor) endpoint returns the country-specific fields necessary for contract creation.

## Part 2: Create the contract

After [retrieving the information to create the contract](#part-1-retrieve-information-to-create-the-contract), you can create it using the [Create EOR contract](https://developer.deel.com/reference/createeorcontract) endpoint.

![](https://files.readme.io/941050dc888c7750a1e1e3ccba4f4cdbee4ce9152a0890cf5d7e493431acd9be-eor-hiring-flow-diagram-part2.png)


> 📘 New job scopes must be validated
> 
> If you want to use a different scope than the default ones, use [Request job scope validation](https://developer.deel.com/reference/requestjobscopevalidation) to validate the scope. The validation process ensures that the job description is compliant with local laws and regulations.

Following is a sample request for your reference:

```curl
curl --request POST \
     --url https://api.deel.com/rest/v2/eor \
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

Since Deel becomes the formal employer of the worker you're hiring, we will issue a quote for the new contract being created.

![](https://files.readme.io/b11eece2c755cbaf2f32c7f53b54f783448d3755a331b5fa83a44f6e7138eaeb-eor-hiring-flow-diagram-part3.png)


> 📘 Quote issuance timeline
> 
> The time it takes to receive the quote depends on the possibility to automate the quote issuance on our end.
> 
> - If the quote can be issued automatically, you'll receive it within a few minutes
> - If the quote must be issued manually, it takes up to 24 hours to receive the quote

You can [subscribe](https://developer.deel.com/reference/createwebhook) to the dedicated `eor.quote.created` webhook to receive the quote once ready. For more information on how to subscribe to a webhook, visit [Getting started with webhooks](https://developer.deel.com/docs/webhooks-get-started).

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

If you [agree w¡th the quote](#part-3-receive-a-quote-from-deel) for the contract, you can go ahead and sign it and it will be automatically accepted.

![](https://files.readme.io/2ca6103cd4f477e05271cfdf9d36e5328797acef6ee728d94dbc57fa3c96a0ab-eor-hiring-flow-diagram-part4.png)


To sign a contract, you can use the [Sign a contract endpoint](https://developer.deel.com/reference/signcontract).

## Part 5: The worker signs the contract

Once you sign the contract, the worker receives an invitation email to create their Deel account and sign the contract.

![](https://files.readme.io/f9cec7ca80cd9be4b3dacc5738a3851443d3b62e7127cb502e9518f96a4ec711-eor-hiring-flow-diagram-part5.png)


You can also monitor the contract status by [subscribing](https://developer.deel.com/reference/createwebhook) to the dedicated [`contract.status.updated`](https://developer.deel.com/docs/event-payload-examples#contractstatusupdated) webhook. For more information on how to subscribe to a webhook, visit [Getting started with webhooks](https://developer.deel.com/docs/webhooks-get-started).

## Part 6: Complete worker onboarding

After the worker signs the contract, they must be onboarded. Onboarding consists in collecting additional country-specific information, compliance documents, and verifying the worker's identity. While the steps listed in this section don't have to be completed in the exact order, onboarding is only considered completed only after they have all been completed successfully.

![](https://files.readme.io/b2ce8437015dae48695fe8fdef820bd42ba0409b5ca0944dcfeb50d22ff8a4ac-eor-hiring-flow-diagram-part6.png)


### Step 1. Retrieve required additional information

Use the [Get worker additional fields for EOR](https://developer.deel.com/reference/getworkeradditionalfieldsforeor) endpoint to retrieve country-specific fields required for onboarding, such as Tax ID or marital status.

### Step 2. Submit additional information

Use the [Add EOR worker additional information](https://developer.deel.com/reference/addeorworkeradditionalinformation) endpoint to submit the additional information required.

### Step 3. Handle compliance documents

To fulfill compliance obligations:

1. Use [Get EOR employee compliance documents](https://developer.deel.com/reference/geteoremployeecompliancedocuments) to retrieve required documents.
2. For each document, use [Get template](https://developer.deel.com/reference/geteoremployeecompliancedocumenttemplate) if a template is needed.
3. Upload the filled document using [Upload employee compliance document](https://developer.deel.com/reference/uploademployeecompliancedocument).

### Step 4. Verify the worker's identity

Depending on the country and case, one of the following verification flows must be used:

- [Create Veriff session](https://developer.deel.com/reference/createveriffsession) (automated identity verification)
- [Create manual verification screening](https://developer.deel.com/reference/createmanualverificationscreening) (alternative to Veriff)

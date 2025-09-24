---
title: "Get started with EOR contracts"
slug: "eor-get-started"
excerpt: ""
hidden: false
createdAt: "Wed May 07 2025 09:44:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 09 2025 13:38:25 GMT+0000 (Coordinated Universal Time)"
---
The [Employer of Record (EOR)](https://www.deel.com/glossary/employer-of-record/) APIs allow you to hire full-time employees in countries where you don't have a legal entity. This set of endpoints helps you streamline and automate every step of the hiring and onboarding flow—from understanding local regulations to signing the final contract and submitting compliance documentation.

This guide walks you through everything you need before making your first API call to hire an EOR employee.

## Overview of the EOR hiring flow

Hiring an EOR employee involves 3 main milestones, and some optional steps:

1. [Creating the contract](https://developer.deel.com/docs/eor-create-contract)
2. [Signing the contract](https://developer.deel.com/docs/eor-sign-contract)
3. [Worker onboarding](https://developer.deel.com/docs/eor-worker-onboarding)

![](https://files.readme.io/8dfeca0edb165e0ab243db684c727ee247c4afc54ee684e03722dae3aaae1ca1-eor-get-started-diagram.png)


Each milestone consists of one or more steps, and may require you to interact with multiple endpoints depending on your use case and the country where you're hiring.

Before getting into the details of hiring an EOR worker, let's take a look at some preliminary steps that can help you navigate the hiring process.

## Estimating hiring costs (optional)

If you want to estimate employment costs before creating a contract, the following endpoints are available:

- [Calculate employee costs globally](https://developer.deel.com/reference/calculateemploymentcostforeor): gives a cost estimate based on base salary, country, and other parameters.
- [Get EOR additional costs](https://developer.deel.com/reference/geteoradditionalcosts): returns a breakdown of non-statuatory allowances and benefits.

While this step is optional, it can help with budgeting and comparing countries.

## Visas and background checks (optional)

If the employee requires a visa or you want to perform a background check, Deel provides API endpoints for that too:

- [Create background check](https://developer.deel.com/reference/createbackgroundcheckforcontracts)
- [Create an immigration case](https://developer.deel.com/reference/createcase)

For more information, visit the [Immigration API guide](https://developer.deel.com/docs/immigration-api).

## Understanding what’s required

Before creating a contract, you must understand the requirements for employing a worker in a specific country. These include:

- Local compliance constraints
- Required fields and formats
- Available benefits
- Visa needs or employment eligibility

Rather than retrieving this information from multiple endpoints, you can now use the [Fetch EOR contract form](https://developer.deel.com/reference/fetcheorcontractform) to retrieve all the required fields in one call.

This endpoint simulates Deel’s UI wizard and returns a structured payload with:

- All the questions and required values for contract creation
- Validation rules for each field (e.g., min/max values, dependencies)
- Source URLs to retrieve dropdown options (e.g., job titles, countries, currencies)
- Indicators of whether additional steps are needed, such as job scope validation

This is the source of truth for contract creation data and will be your first step when [creating a contract](https://developer.deel.com/docs/eor-create-contract).

## Next steps

Once you’ve used the [Fetch EOR contract form](https://developer.deel.com/reference/fetcheorcontractform) to gather the required information, you're ready to move through the rest of the hiring flow:

1. [Create the contract](https://developer.deel.com/docs/eor-create-contract)
2. [Sign the contract](https://developer.deel.com/docs/eor-sign-contract)
3. [Onboard the worker](https://developer.deel.com/docs/eor-worker-onboarding)

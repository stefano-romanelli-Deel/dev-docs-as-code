---
title: "Immigration API"
slug: "immigration-api"
excerpt: "Learn how to use the immigration API to manage your workforce's immigration processes"
hidden: false
createdAt: "Fri Dec 13 2024 10:24:02 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 07 2025 10:20:24 GMT+0000 (Coordinated Universal Time)"
---
Immigration cases in Deel represent the suite of visa and immigration support services offered to clients and workers through the platform. These cases help businesses manage compliance, workforce mobility, and hiring in global markets.

## What Deel immigration cases cover

Deel supports a variety of immigration-related workflows for both sponsored and self-sponsored scenarios. These include:

### Visa applications

- **EOR Visa Applications**: Sponsored by Deel, for employees hired under the Employer of Record model.
- **Client-Sponsored Visas**: Where the client or their entity sponsors the employee's visa.
- **Self-Sponsored Visas**: Supported with documentation and eligibility validation.

### Work permit requests

- Standalone work permit processing for non-EOR customers.
- Support for temporary work authorization where applicable.

### Global mobility support

- Relocation assistance and immigration guidance for employees moving across countries.
- Cross-border hiring compliance support in over 50 countries.

### Document management

- Collection, validation, and storage of immigration documents.
- Ongoing document tracking for expiration and compliance needs.

### Case management

- Tracking and monitoring of each immigration case through defined steps.
- Communication handling with clients and applicants.
- Deadline reminders and document submission workflows.

### Compliance assurance

- Ensuring all immigration actions meet local legal requirements.
- Verifying work authorization before employment begins.

### Business expansion support

- Facilitating hiring in new or complex international markets.
- Streamlining visa processes to enable faster onboarding.

## Before you begin

Prepare the following information before calling the Immigration API:

- A valid [token](https://developer.deel.com/docs/api-tokens-1) to authenticate your requests
- The country code from the [Get countries](https://developer.deel.com/reference/getcountries) endpoint. This code is used to specify the country

The Immigration API helps manage your workforce's immigration processes by providing endpoints for creating and managing immigration cases. The endpoint allows you to:

- [Manage immigration cases](#manage-immigration-cases)
- [Track case status updates using webhooks](#track-case-status-updates-using-webhooks)
- [Manage documents](#manage-documents)

## Manage immigration cases

### Create a new immigration case

Use the [Create immigration case](https://developer.deel.com/reference/createcase) endpoint to initiate a new immigration case for your workforce. There is a subtle difference of parameters between the different types of cases, so make sure to check the table below for the required parameters

The following types of immigration cases can be created:

- **Right to work**: A visa application where Deel's immigration team reviews an employee's legal eligibility to work in a specific country. This ensures legal compliance.
- **EOR (Employer of Record) Visa Application**: A visa application where Deel sponsors the visa. The applicant is employed by Deel, and Deel is responsible for documentation and compliance.
- **Sponsored Visa Application**: A visa application where the client’s entity sponsors the visa. Deel facilitates the Visa application process using the client's entity.

Additionally, clients can initiate **pre-hire assessments** to evaluate visa eligibility before creating a contract:

- **Pre-hire EOR visa application**: An assessment that checks an applicant’s visa eligibility before initiating a contract with Deel as the Employer of Record.
- **Pre-hire sponsorship visa application**: Similar to the above, but the client sponsors the visa. It allows evaluation of visa eligibility before committing to a contract.

These pre-hire assessments help clients determine visa feasibility before entering into formal employment agreements.

### Creating a case for different case types

All immigration case types are created using the same API endpoint:  
[**Create Immigration Case API**](https://developer.deel.com/reference/createcase).

When calling this API, the `case_type` you choose will determine which fields are required and how the system processes the request.

Before using the API:

- Confirm that the **contract type** and **contract status** are compatible with the selected `case_type`
- Review the individual case type sections below for:
  - Business rules
  - Prerequisites
  - Supported workflows
- Refer to the [**API Reference**](https://developer.deel.com/reference/createcase) for:
  - Field-level documentation
  - Sample request payloads

When calling this API, the case_type you choose will determine which fields are required and how the system processes the request.

## Case type: `EOR_VISA`

This case type is used for visa cases for Deel EOR (Employer of Record) contracts.

### Summary

Created when onboarding a new EOR employee or supporting existing ones. The case includes following processes:

- Eligibility check 
- Visa application 
- Document review and validation

### Prerequisites

- An **EOR contract** must exist. [Create Contract](https://developer.deel.com/docs/create-contract)
- Visa type should be provided from one of the supported visas of the hiring country. (Optional) [Get Visa Types](https://developer.deel.com/reference/immigrationvisatypes)

> 📘 Case creation constraints
> 
> - If the employee **has not completed onboarding** on the Deel platform, only **one immigration case** can be created at a time.
> - If the employee **has completed onboarding**, multiple immigration cases can be created as needed.

### Contract compatibility

| Supported Contract Types | Required Contract Status                                         | Additional Requirements                              |
| ------------------------ | ---------------------------------------------------------------- | ---------------------------------------------------- |
| EOR                      | Any (e.g., IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN) | Refer to **Case Creation Constraints** section above |

## Case type: `RIGHT_TO_WORK`

This case type is used for **compliance-driven** validation of an individual’s legal right to work in a specific country.

### Summary

This case type is created during employee onboarding or when an existing work authorization document is expiring. It is particularly applicable when the **employee's contract country differs from their nationality**, and they already possess a visa.  
The purpose of this case is to:

- Review provided visa or documentation
- Validate legal work eligibility based on destination country compliance standards

### Prerequisites

- A contract must exist (direct/contractor/EOR). [Create Contract](https://developer.deel.com/docs/create-contract)

### Contract compatibility

| Supported Contract Types | Required Contract Status | Additional Requirements                                              |
| ------------------------ | ------------------------ | -------------------------------------------------------------------- |
| EOR                      | IN_PROGRESS              | Employee must have completed onboarding, and has an active contract  |
| Direct / Contractor      | N/A                      | Applicable when contract country is not same as employee nationality |

***

## Case type: `SPONSORED_VISA`

This case type is used for visa cases **sponsored by the employer or client via their own entity** (not Deel).

### Summary

This case type supports scenarios where Deel is not the visa sponsor. Instead, the client's internal entity handles sponsorship. The case includes following processes:

- Eligibility check
- Visa application
- Document review and validation

### Prerequisites

- A contract must exist and be of type **contractor** or **direct**.
- A valid [entity](https://developer.deel.com/reference/getlegalentitylist) must exist.
- Visa type should be provided from one of the supported visas of the hiring country. (Optional) [Get Visa Types](https://developer.deel.com/reference/immigrationvisatypes)

### Contract compatibility

| Supported Contract Types | Required Contract Status                             | Additional Requirements |
| ------------------------ | ---------------------------------------------------- | ----------------------- |
| ONGOING_TIME_BASED       | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| PAY_AS_YOU_GO_TIME_BASED | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| PAYG_MILESTONES          | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| PAYG_TASKS               | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| GLOBAL_PAYROLL           | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| HRIS_DIRECT_EMPLOYEE     | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |
| MILESTONES               | IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN | None                    |

***

## Case type: `PRE_HIRE_EOR_VISA`

This case type is used to assess visa eligibility for potential employees before an EOR contract is created.

### Summary

Created in pre-hiring stages, typically to assess potential EOR candidates. The case includes the following processes:

- Pre-hire eligibility assessment
- Early review of visa feasibility
- Contract is created and gets attached to the case after creation
- Visa application
- Document review and validation

![](https://files.readme.io/b6963071699c819e65ee3b8efe3ff09b5bb129998242a9ba460d592acc96fe76-pre-hire-case-flow-diagram.png)


### Prerequisites

- A team must exist. [Get Team](https://developer.deel.com/reference/getteams)
- **Contract is not required initially**, but it **gets attached to the case after contract creation**.
- Visa type should be provided from one of the supported visas of the hiring country. (Optional) [Get Visa Types](https://developer.deel.com/reference/immigrationvisatypes)

### Contract compatibility

| Supported Contract Types | Required Contract Status                                         | Additional Requirements |
| ------------------------ | ---------------------------------------------------------------- | ----------------------- |
| EOR                      | Any (e.g., IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN) | None                    |

***

## Case type: `PRE_HIRE_SPONSORSHIP_VISA`

This case type is used to evaluate visa options for potential hires before a contract exists.

### Summary

This case is created during the early hiring stages to assess visa eligibility **before contract creation**, typically initiated from the “Check Visa Eligibility” flow or contract setup. Unlike `PRE_HIRE_EOR_VISA`, where Deel sponsors the visa, here **the client (via their own entity) is the sponsoring organization**.

Key Points:

- Pre-hire visa assessment allows evaluating candidate eligibility without an existing contract
- Client sponsors the visa through their own legal entity
- Contract creation is mandatory before proceeding to the visa application stage
- The contract is automatically **attached to the case after creation**

### Step-by-Step Process

1. Start visa eligibility check
2. Select preferred visa type
3. Choose sponsoring entity (client’s own legal entity)
4. Deel reviews the case and provides an eligibility decision
5. Client reviews application fees
6. Contract is created and **automatically attached to the case** before visa application proceeds

### Prerequisites

- A team must exist. [Get Team](https://developer.deel.com/reference/getteams)
- Sponsoring entity (client legal entity) must exist.
- Visa type should be provided from one of the supported hiring country. (Optional) [Get Visa Types](https://developer.deel.com/reference/immigrationvisatypes)

### Contract compatibility

| Supported Contract Types | Required Contract Status                                         | Additional Requirements |
| ------------------------ | ---------------------------------------------------------------- | ----------------------- |
| HRIS_DIRECT_EMPLOYEE     | Any (e.g., IN_PROGRESS, ONBOARDING, WAITING_FOR_CONTRACTOR_SIGN) | None                    |

### Retrieve an immigration case

You can use the [Get immigration case](https://developer.deel.com/reference/immigrationcasedetails) endpoint to return immigration case information.  
The endpoint supports several types of cases.

To retrieve an immigration case, make a `GET` request to the endpoint.

### Retrieving an immigration case

All immigration case types can be retrieved using this API endpoint:  
[**Get Immigration Case API**](https://developer.deel.com/reference/immigrationcasedetails)

## Track case status updates using webhooks

The **Immigration API** provides a dedicated webhook event to receive updates on the status of immigration cases.

### Event: `immigration.case.process.status.update`

This event notifies your system when an immigration case or a process within a case has been updated.

For more details on webhook setup and security, visit the [Webhooks Guide](https://developer.deel.com/docs/webhooks).

The `immigration.case.process.status.update` event returns a payload with the following information:

```json
{
  "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
  "status": "Open",
  "case_type": "Right To Work",
  "visa_type": "B-1",
  "country_code": "US",
  "process": {
    "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "name": "Work Authorization Verification",
    "status": "In Review"
  },
  "applicant": {
    "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "external_id": "123123"
  }
}
```

Where:

| Name                  | Type   | Description                                           | Example                                |
| --------------------- | ------ | ----------------------------------------------------- | -------------------------------------- |
| id                    | UUID   | Unique identifier for the id associated with the case | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| status                | string | The status of immigration case                        | `Open`                                 |
| case_type             | string | Type of the immigration case                          | `Right To Work`                        |
| visa_type             | string | The type of the visa for the case.                    | `B-1`                                  |
| country_code          | string | ISO 3166-1 alpha-2 country code                       | `UK`                                   |
| process.id            | UUID   | Unique identifier of the immigration process          | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| process.name          | string | Name of the current immigration process               | `Work Authorization Verification`      |
| process.status        | string | Status of the process                                 | `In Review`                            |
| applicant.id          | UUID   | Internal unique ID for the applicant                  | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| applicant.external_id | number | External ID used by your system to link the applicant | `123123`                               |

## Manage documents

This section explains how to manage documents using the endpoints provided by the Immigration API.

### Get documents by ID

Retrieve document information for a specific document ID, including its status, type, and download link if available.

#### API reference

[Get documents by ID](https://developer.deel.com/reference/immigrationdocument)

### Get visa/document types by country

Fetch the list of supported visa or document types required for immigration cases, based on the specified country.

#### API reference

[Get documents by ID](https://developer.deel.com/reference/immigrationvisatypes)

---
title: "Managing task-based contractors"
slug: "managing-task-based-contractors"
excerpt: ""
hidden: false
createdAt: "Fri Nov 29 2024 16:20:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 11:48:46 GMT+0000 (Coordinated Universal Time)"
---
Organizations with workforces consisting of independent contractors who perform task-based work can face significant operational challenges when it comes to hiring, tracking, paying, and offboarding contractors. This is common in organizations that hire translators, designers, or other professionals engaged in project-based work.

This article illustrates how organizations with such characteristics can build applications that leverage the Deel API to automate the contractor working relationship throughout their lifecycle, including hiring, task tracking, payments, offboarding, and reporting.

## In this guide

- [Part 1: Hiring contractors](#part-1-hiring-contractors)
- [Part 2: Tracking work](#part-2-tracking-work)
- [Part 3: Handling payments](#part-3-handling-payments)
- [Part 4: Accounting and reporting](#part-4-accounting-and-reporting)
- [Part 5: Offboarding contractors](#part-5-offboarding-contractors)

## Part 1: Hiring contractors

To begin, you need to hire contractors by creating and signing contracts.

![](https://files.readme.io/683d86b898277592b09173256e1de5e2726535cba2b1a7d0425062494a50c41f-task-based-contractor-flow-diagram-part1.png)


### Step 1: Creating the contract

When a contractor joins your platform, you can automatically initiate the contract creation process using the Deel API.  
This can be done using the [Create a new contract (POST)](https://developer.deel.com/reference/createcontract) endpoint to create a task-based pay as you go contract.

For more information, visit [Create a contract](https://developer.deel.com/docs/create-contract).

### Step 2: Signing the contract

After the contract is created, the next step is to sign the contract. The signature is usually done first by the manager, then the contractor.

#### Manager signature

You can build your system to sign the contract as the employer:

1. (Optional) Show a preview of the contract using [Preview a contract agreement (GET)](https://developer.deel.com/reference/getcontractpreview) endpoint.
2. Sign the contract using [Sign a contract (POST)](https://developer.deel.com/reference/signcontract) endpoint.
3. Send the contract to the contractor using [Send contract to worker (POST)](https://developer.deel.com/reference/invitetosigncontract) endpoint.

#### Contractor signature

Once the contractor receives the invite to sign the contract, they can do so through Deel's UI. They will be prompted to sign up and then sign the contract.

For more information, visit [Contractor account overview](https://help.letsdeel.com/hc/en-gb/articles/9940209181457-Contractor-Account-Overview).

![](https://files.readme.io/5f8ce89a5c16cd73d6cc01900ede7032e359ac2f51f2d1976a78767dfc182985-task-based-contractor-flow-signing.png)


#### Keeping the signature status in sync

Once the contractor signs the contract, you can build your system to keep the signature status in sync.  
This can be done using the `signature` object returned for each contract through the [List of contracts (GET)](https://developer.deel.com/reference/getcontractlist) or the [Retrieve a single contract (GET)](https://developer.deel.com/reference/getcontractbyid) endpoints.

```json Example signatures object
    "signatures": {
      "client_signature": "string",
      "client_signed_at": "2022-05-24T09:38:46.235Z",
      "worker_signature": "string",
      "worker_signed_at": "2022-05-24T09:38:46.235Z",
      "signed_at": "2022-05-24T09:38:46.235Z"
    },
```

## Part 2: Tracking work

Once the contract becomes effective, both parties can start tracking work. Tracking work is done through [tasks](https://developer.deel.com/docs/tasks-1).  
Tasks can either be submitted by the manager or by the contractor.

![](https://files.readme.io/ad0ec85f071d1283e8e8db9556d5db00b3e0b58b9888d65d6e39a1292b57c6c0-task-based-contractor-flow-diagram-part2.png)


### Step 3: Submitting tasks

You can build your system so that, once contractors complete their work, they can submit tasks using the [Create new task (POST)](https://developer.deel.com/reference/createcontractpgotak) endpoint.

Tasks that are submitted by the contractor must be [approved by the manager](#step-4-reviewing-tasks).  
Tasks that are submitted by the manager are automatically approved.

The status of a task is defined using the `status` parameter in the task object.

### Step 4: Reviewing tasks

If tasks were submitted by the contractor, they must be approved by the manager to be [paid out](#part-3-handling-payments).

Depending on your workflow:

- Managers can review and approve submitted tasks through your system. The approval can be done either [in bulk](https://developer.deel.com/reference/createtaskmanyreview) or for [single tasks](https://developer.deel.com/reference/createtaskreviewbyid) using the dedicated endpoints.
- Alternatively, tasks can be automatically marked as approved upon submission if your business logic allows it.

## Part 3: Handling payments

Once tasks are approved, contractors can be paid for their work.

![](https://files.readme.io/fefecae0e94d8f3a3046d3529818d77ea398c63696128f55f7fabb921387db0e-task-based-contractor-flow-diagram-part3.png)


### Step 5: Paying workers

Managers must initiate payments through Deel's UI using one of the [available payment methods](https://help.letsdeel.com/hc/en-gb/sections/20560723002513-Payment-Methods).

Deel also offers [bulk-payment options](https://help.letsdeel.com/hc/en-gb/articles/4407745483153-How-To-Use-The-Mass-Pay-Feature-On-Deel) to pay multiple contractors at once and supports [several payment methods](https://help.letsdeel.com/hc/en-gb/sections/20560723002513-Payment-Methods).

Contractors can be paid at the end of the [payroll cycle](https://help.letsdeel.com/hc/en-gb/articles/4419648055185-What-Are-the-Payroll-Cut-off-Dates-and-Times) or with a [one-time payment](https://developer.deel.com/docs/ic-off-cycle-payments).

## Part 4: Accounting and reporting

After processing payments, you can use Deel's APIs also for accounting and reporting purposes, so that your system is in sync regarding payments and invoices.

![](https://files.readme.io/e7de00b26d97b7c7a339afeaf02b78ef8e2dca3e13fa09180c137b93169f3128-task-based-contractor-flow-diagram-part4.png)


### Step 6: Retrieving invoiced tasks

For example, if you're looking to understand which tasks have been invoiced,  
you can use the [Detailed payments report (GET)](https://developer.deel.com/reference/getdetailedpaymentsreport) endpoint, where each task is listed as a line item and linked to an invoice.

#### Other invoicing endpoints

There are additional endpoints that you can use to track invoices and payments between your organization and Deel.

- [Retrieve invoices (GET)](https://developer.deel.com/reference/getinvoicelist) to get data about the invoices related to your workforce
- [Retrieve Deel invoices (GET)](https://developer.deel.com/reference/getdeelinvoicelist) to get data about the invoices related to Deel fees
- [Download invoice PDF (GET)](https://developer.deel.com/reference/getbillinginvoicedownloadlink) to download an invoice in PDF
- [Download payment receipts (GET)](https://developer.deel.com/reference/getpaymentlist) to retrieve the payment receipts
- [Retrieve a payment breakdown (GET)](https://developer.deel.com/reference/getpaymentsbreakdownbyid) to get the details of a specific payment

For more information, visit [Accounting API](https://developer.deel.com/docs/accounting-api).

## Part 5: Offboarding contractors

When a contractor's services are no longer required, you can trigger the contract termination directly from your system.

![](https://files.readme.io/57d6a410c3aaf1f49dabe1261adf7051876b30ba12215813e460974b67b3e00a-task-based-contractor-flow-diagram-part5.png)


### Step 7: Terminating the contract

To terminate a contract, you can use the [Terminate contract (POST)](https://developer.deel.com/reference/terminatecontract) endpoint.

The data structure allows to terminate a contract immediately or schedule it for a future date.

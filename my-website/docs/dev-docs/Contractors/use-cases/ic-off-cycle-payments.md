---
title: "Making off-cycle payments to independent contractors"
slug: "ic-off-cycle-payments"
excerpt: "Learn how to manage off-cycle payments for your indepdent contractors using the Deel API and the Deel UI"
hidden: false
createdAt: "Mon Jan 27 2025 14:02:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 11:48:44 GMT+0000 (Coordinated Universal Time)"
---
Off-cycle payments (or one-off payments) are payments that are made outside of the standard payroll cycle. They are typically used for salary advances, expense reimbursements, or other one-time payments, but also when the working relationship with the worker requires immediate payouts.

If you have such needs, you can combine the off-cycle payments API and the Deel UI to manage off-cycle payments for independent contractors.

## In this article

- [Before you begin](#before-you-begin)
- [Step 1. Add an off-cycle payment (API)](#step-1-add-an-off-cycle-payment-api)
- [Step 2. Approve an off-cycle payment (UI)](#step-2-approve-an-off-cycle-payment-ui)
- [Step 3. Pay the off-cycle payment invoice (UI)](#step-3-pay-the-off-cycle-payment-invoice-ui)
- [Step 4. Deel pays out the independent contractor](#step-4-deel-pays-out-the-independent-contractor)

## Before you begin

This article assumes that you're familiar with:

- The fees and costs of running off-cycle payments
- The relationship between off-cycle payments and the standard payroll cycles
- The timeline to complete off-cycle payments
- The availability of off-cycle payments in different countries

If you are not familiar with these aspects, we recommend visiting our [Help Center](https://help.letsdeel.com/hc/en-gb/articles/4407745509393-How-to-Pay-a-Contractor-Out-of-Cycle-With-a-One-off-Payment).

## Step 1. Add an off-cycle payment (API)

You can add an off-cycle payment using the API by making a `POST` request to the Add off-cycle payment endpoint.

The code below shows a sample request to add an off-cycle payment. For more information, visit the API reference for [Add off-cycle payment](https://developer.deel.com/reference/createoffcyclepayment).

```curl
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/contracts/{{contract_id}}/off-cycle-payments \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "amount": 500,
    "description": "Reimbursement for travel expenses",
    "date_submitted": "2025-01-25"
  }
}
'
```

In the path:

|  Name         | Required | Type   | Format | Description                                                                                                                                            | Example   |
| ------------- | -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| `contract_id` | Yes      | String | -      | The ID of the contract. You can retrieve the contract ID using the [List of contracts](https://developer.deel.com/reference/getcontractlist) endpoint. | `d3m0d3m` |

In the body:

|  Name                 | Required | Type   | Format | Description                                                                                                      | Example                             |
| --------------------- | -------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `data.amount`         | Yes      | Number | -      | The amount of the off-cycle payment. The currency of the off-cycle payment matches the currency of the contract. | `500`                               |
| `data.description`    | Yes      | String | -      | The description of the off-cycle payment                                                                         | `Reimbursement for travel expenses` |
| `data.date_submitted` | Yes      | String | -      | The date when the off-cycle payment request is submitted                                                         | `2025-01-25`                        |

A successful response will return a `201` status code with the ID of the created off-cycle payment.

## Step 2. Approve an off-cycle payment (UI)

Once the request has been created, the off-cycle payment must be approved. Any user designated as approvers can approve an off-cycle payment.

To approve a off-cycle payment:

1. On the UI, go to **People**, open a contractor's page, then click **Payments, expenses & work submissions**.

   ![](https://files.readme.io/2f87b46951e07dca64d8a4a47a10a0f11b54032578a273c9c7e3a117de4436da-one-off-payments-expenses-worksubs.png)
2. Locate the **One-off payment** section, then do one of the following:

- If you have a single one-off payment to approve, click **Approve** next to the payment.
- If you have multiple one-off payments to approve, you can click **Approve all**, or click **View Invoice** and then approve single payments.

![](https://files.readme.io/1509617c88a8db858f1d097e33ba30a4a6dd8418a86f7721757134aa60a28910-one-off-payment-approve.png)


The off-cycle payment is approved and you can now proceed to [pay the invoice](#step-3-pay-the-off-cycle-payment-invoice-ui).

## Step 3. Pay the off-cycle payment invoice (UI)

Off-cycle payments are invoiced to you separately from the rest of the payroll cycle. For an off-cycle payment to be paid to the contractor, you must pay the invoice first. Off-cycle payments invoices are due within 30 days from their issue date. Once the invoice payment is received, we'll [process the payment](#step-4-deel-pays-out-the-independent-contractor) to the contractor.

> 📘 Each off-cycle payment request generates a separate invoice. To pay them in bulk, you must first approve all the requests and then pay the invoices.

Invoices can be paid from multiple areas of the UI. You have the following options:

- [Option 1. Pay the invoice from the contractor's page](#option-1-pay-the-invoice-from-the-contractors-page)
- [Option 2. Pay the invoice from the payroll page](#option-2-pay-the-invoice-from-the-payroll-page)

### Option 1. Pay the invoice from the contractor's page

To pay the invoice from the contractor's page:

1. From the contractor's page, locate the **One-off payment** section.
2. Click **Pay invoice** or **Pay all invoices** (depending on whether you have a single or multiple approved one-off payments).

> 👍 If you have multiple approved one-off payments but want to pay a specific invoice, you can click **View invoice**.

![](https://files.readme.io/bc51fc5476d5fd7f92f4cc9631fc20febf65bc1dfb4bb536e541f4c9d9b64ac3-one-off-payment-pay-all-invoices.png)


### Option 2. Pay the invoice from the payroll page

Alternatively, you can pay the invoice using the mass pay feature and selecting the invoices related to the one-off payment.

For full instructions on how to use the mass pay feature, visit [How to use the mass pay feature on Deel](https://help.letsdeel.com/hc/en-gb/articles/4407745483153-How-To-Use-The-Mass-Pay-Feature-On-Deel).

## Step 4. Deel pays out the independent contractor

Once we receive the invoice payment, we'll immediately transfer the funds to the contractor, who will receive them according to the standard banking system processing times.

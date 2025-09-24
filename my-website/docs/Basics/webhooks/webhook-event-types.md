---
title: "Webhook event types"
slug: "webhook-event-types"
excerpt: ""
hidden: false
createdAt: "Tue Mar 04 2025 10:52:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Sep 15 2025 09:31:44 GMT+0000 (Coordinated Universal Time)"
---
This article includes the list of webhook events that you can subscribe to. For the full payload details, use the [List of webhook event types](https://developer.deel.com/reference/getallwebhookeventtypes) endpoint or use UI. For more information, see [Webhooks overview](https://developer.deel.com/docs/webhooks) and [Get started with webhooks](https://developer.deel.com/docs/webhooks-get-started).

## Contracts

| Event                             | Description                                                                       |
| :-------------------------------- | :-------------------------------------------------------------------------------- |
| contract.amended                  | Triggered when a contract is amended and the amendment is signed by both parties. |
| contract.created                  | Triggered when a new contract is created.                                         |
| contract.duplicated               | Triggered when a contract is duplicated.                                          |
| contract.status.updated           | Triggered when a contract status changes.                                         |
| contract.terminated               | Triggered when a contract is terminated.                                          |
| contract.sign.team-member-invited | Triggered when a team member is invited to sign a contract.                       |

## Deel HR

| Event                       | Description                                      |
| :-------------------------- | :----------------------------------------------- |
| employee.created.direct     | Triggered when a direct employee is created.     |
| employee.created.contractor | Triggered when a contractor employee is created. |
| employee.created.eor        | Triggered when an EOR employee is created.       |
| employee.updated.direct     | Triggered when an employee is updated.           |
| worker.v2.created           | Triggered when a worker is created.              |
| worker.v2.deleted           | Triggered when a worker is deleted.              |

## Deel HR SCIM

| Event          | Description                                  |
| :------------- | :------------------------------------------- |
| worker.created | Triggered when a user is created in Deel HR. |

## Deel Engage

| Event                                         | Description                                                                   |
| :-------------------------------------------- | :---------------------------------------------------------------------------- |
| engage.learning.journeys.assignments.created  | Triggered when a Learning Journey Assignment is created.                      |
| engage.learning.journeys.assignments.reminded | Triggered when a Learning Journey Assignment Reminder is triggered by Client. |

## Deel IT

| Event                     | Description                                        |
| :------------------------ | :------------------------------------------------- |
| it-order.created          | Triggered when an order is placed through Deel IT. |
| it-asset.location-updated | Triggered when the location of an asset changes.   |

## EOR

| Event                        | Description                                              |
| :--------------------------- | :------------------------------------------------------- |
| eor.quote.created            | Triggered when the quote for an EOR contract is created. |
| eor.amendment.status.updated | Triggered when EOR amendment status is updated.          |

## Global payroll

| Event                     | Description                                                       |
| :------------------------ | :---------------------------------------------------------------- |
|  gp.termination.confirmed | Triggered when a global payroll employee termination is confirmed |

## Immigration

| Event                                  | Description                                         |
| :------------------------------------- | :-------------------------------------------------- |
| immigration.case.process.status.update | Triggered when status of case or process is changed |

## Invoice Adjustments

| Event                                   | Description                                                    |
| :-------------------------------------- | :------------------------------------------------------------- |
| invoice-adjustment.created              | Triggered when a new invoice adjustment is created.            |
| invoice-adjustment.reviewed             | Triggered when an invoice adjustment is approved or denied.    |
| invoice-adjustment.pending-for-approval |  Triggered when an invoice adjustment is pending for approval. |

## OAuth2

| Event                | Description                                |
| :------------------- | :----------------------------------------- |
| oauth2.token.revoked | Triggered when an OAuth2 token is revoked. |

## Onboarding

| Event                        | Description                                        |
| :--------------------------- | :------------------------------------------------- |
| onboarding.checklist.updated | Triggered when the onboarding checklist is updated |
| onboarding.status.updated    | Triggered when the onboarding status is updated    |

## Payments

| Event                       | Description                                                                                                         |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| payment.statement.initiated | Triggered when a payment statement is created, to notify stakeholders that a new payment is available for download. |
| payment.statement.mark-paid | Triggered when a payment statement is marked as paid.                                                               |

## Payslips

| Event                  | Description                               |
| :--------------------- | :---------------------------------------- |
| eor.payslips.available | Triggered when EOR payslips are available |
| gp.payslips.available  | Triggered when payslips are available     |

## Profile

| Event               | Description                           |
| :------------------ | :------------------------------------ |
| profile.kyc.changed | Triggered when Profile KYC is changed |

## Timesheets

| Event              | Description                                       |
| :----------------- | :------------------------------------------------ |
| timesheet.created  | Triggered when a new timesheet is created.        |
| timesheet.reviewed | Triggered when a timesheet is approved or denied. |

## Time off

| Event             | Description                                                |
| :---------------- | :--------------------------------------------------------- |
| time-off.created  | Triggered when a new time off request is created.          |
| time-off.reviewed | Triggered when a time off request is approved or denied.   |
| time-off.updated  | Triggered when a time off request is updated.              |
| time-off.deleted  | Triggered when a time off request is deleted or cancelled. |

## Verifications

| Event                    | Description                                     |
| :----------------------- | :---------------------------------------------- |
| bgcheck.result.available | Triggered when a background check is completed. |

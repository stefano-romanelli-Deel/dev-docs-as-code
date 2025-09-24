---
title: "Manage contractor timesheets"
slug: "manage-contractor-timesheets"
excerpt: ""
hidden: false
createdAt: "Mon Feb 03 2025 14:52:38 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Feb 17 2025 15:44:42 GMT+0000 (Coordinated Universal Time)"
---
Organizations use separate time-tracking systems to monitor the hours worked by their contractors.

The Timesheets API, allows organizations working with contractors following the pay-as-you-go model to automate this process by syncing timesheet data directly from their time-tracking systems to Deel, ensuring contractors are accurately paid for their recorded hours.

> 📘 Only works with Pay-as-you-go contracts
> 
> Other models of contracts, such as task-based or milestone-based, are not supported because time sheets are not part of how work is tracked. If you're looking for information on how to track work employees in Global Payroll, see [Time tracking](https://developer.deel.com/docs/time-tracking).

This article explains the high-level process for submitting and approving timesheets, as well as how to use the Timesheets API to go through the entire process of recording time worked by contractors.

## In this guide

- [Step 1: Create timesheet entry](#step-1-create-timesheet-entry)
- [Step 2: (Optional) Update timesheet entry](#step-2-optional-update-timesheet-entry)
- [Step 3: Review timesheet entry](#step-3-review-timesheet-entry)

Refer to the following diagram for an overview of the timesheet submission and approval process.

![](https://files.readme.io/74518c02f8c71134467c0e89ba8c1e027d9c7b5e1a19eab52f8614eee797f92e-timesheet-submission-diagram.png)


## Step 1: Create timesheet entry

Both clients and contractors can create timesheet entries using the `Create timesheet entry` endpoint. This ensures that the hours worked are logged into Deel for subsequent payment processing.

To create a timesheet entry, use the [Create timesheet entry (POST)](https://developer.deel.com/reference/createtimesheet) endpoint.

Refer to the [API reference](https://developer.deel.com/reference/createtimesheet) for full request and response examples.

## Step 2: (Optional) Update timesheet entry

Once a timesheet entry has been created, it can be updated if corrections are required. For example, the contractor may need to make corrections, or the client may need to adjust the recorded hours.

> 📘 Updating is only possible before a timesheet entry is approved

To update a timesheet entry:

1. Retrieve the timesheet entry using the [Retrieve timesheet entry (GET)](https://developer.deel.com/reference/gettimesheetbyid) endpoint.
2. Modify the entry using the [Update timesheet entry (PATCH)](https://developer.deel.com/reference/updatetimesheetbyid) endpoint.

## Step 3: Review timesheet entry

The review processes differ based on who submitted the timesheet:

- **Client-submitted timesheets** are automatically approved.
- **Contractor-submitted timesheets** require client approval. This ensures that recorded hours are reviewed before payment.

To approve contractor-submitted timesheets:

1. Retrieve pending timesheets using:
   - [Retrieve list of timesheets (GET)](https://developer.deel.com/reference/gettimesheets)
   - [Retrieve list of timesheets by contract (GET)](https://developer.deel.com/reference/gettimesheetsbycontract)
2. Approve timesheets using:
   - [Review single timesheet (POST)](https://developer.deel.com/reference/createtimesheetreview)
   - [Review multiple timesheets (POST)](https://developer.deel.com/reference/createtimesheetreviews)

Once a timesheet is approved, it will be reflected on the invoice and paid out to the contractor based on the payment agreements between the parties.

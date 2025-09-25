---
title: "Time tracking"
slug: "time-tracking"
excerpt: "Learn how to use the time tracking API to keep the time sheets of your Global Payroll employees under control"
hidden: false
createdAt: "Mon Nov 04 2024 11:35:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Sep 23 2025 08:49:16 GMT+0000 (Coordinated Universal Time)"
---
With the time tracking API, you can manage the time worked by employees, and add, update, retrieve and delete their shifts.

> 📘 The time tracking API only works for [Global Payroll](https://help.letsdeel.com/hc/en-gb/articles/9080297174033-Global-Payroll-Overview)
> 
> Independent contractors use timesheets to track their time. For more information, see [Timesheets](https://developer.deel.com/docs/timesheets-1).

## Before you begin

Here's a few things to keep in mind before starting to manage shifts:

- Shifts are linked to contracts. To manage shifts, you need the contract ID that you can retrieve from the [GET list of contracts](https://developer.deel.com/reference/listofcontracts) endpoint.
- Shifts are processed and compensated at the end of each payroll cycle. For more information, see [Shifts and payroll cycles](#shifts-and-payroll-cycles).
- If you submit a shift for a past payroll cycle, it will be compensated at the end of the current cycle without validating if the date of the shift falls within the current cycle.
- Shifts are compensated according to a combination of the shift rate of a shift submitted and the hourly base salary of the worker.

## Shift types

Shifts can be submitted in two formats:

- [Categorized shifts](#categorized-shifts)
- [Uncategorized (raw) shifts](#uncategorized-raw-shifts)

### Categorized shifts

Categorized shifts are suited for when shifts are categorized outside Deel and the shift rates (pay codes/category) are known. Usage of this API also requires you to [set up shift rates](#create-a-shift-rate) using the shift rates.

Following is an example of a categorized shift:

```json
{
  "external_id": "shift_123",
  "date_of_work": "2024-04-01",
  "summary": {
    "shift_rate_external_id": "rate123",
    "time_unit": "HOUR",
    "time_amount": 15.50
  }
}
```

### Uncategorized (raw) shifts

Uncategorized shifts are used to capture the shift information in a more granular way. For instance, we capture the start, end, breaks information about a shift, as opposed to the categorized shifts where we capture summary information like the total hours worked, total break hours etc. There is no need to setup shift rate for uncategorized shifts.

```json
{
  "external_id": "shift_456",
  "date_of_work": "2024-04-01",
  "meta": {
    "start": {
      "date": "2024-04-01",
      "time": "09:00",
      "is_rest_day": false,
      "is_public_holiday": false
    },
    "end": {
      "date": "2024-04-01",
      "time": "17:00",
      "is_rest_day": false,
      "is_public_holiday": false
    },
    "breaks": [
      {
        "end": {
          "date": "2024-04-01",
          "time": "12:00"
        },
        "start": {
          "date": "2024-04-01",
          "time": "11:00"
        },
        "is_paid": true
      }
    ],
    "approval_date": "2024-04-03"
  }
}
```

### Shifts and payroll cycles

When you submit a shift, the shift is automatically associated to the relevant payroll cycle based on the submission time stamp and the cycle's cutoff date. The cutoff date is the last day for the manager to approve the submitted shifts to be processed within the current payroll cycle.

- If the shift is approved before the cutoff date, the submission is processed within the current cycle
- If the shift is approved after the cutoff date, the submission is processed in the next cycle

The payroll calendar is configured per entity by your Deel representative when you onboard. That's when you decide the cutoff dates. If you have questions about your cutoff dates, contact your Deel representative. For more information, see [Understanding the Deel Global Payroll Calendar](https://help.letsdeel.com/hc/en-gb/articles/34654118966801-Understanding-the-Deel-Global-Payroll-Calendar).

![](https://files.readme.io/083d18de16a7f5b99411e160e22c7d837faaa30de045cf3fba54b2576b85166f-shifts-cutoff-date.png)


> 🚧 Contact support for late shift submissions
> 
> If the payroll cutoff date has already passed and waiting for the next cycle for the shift to be processed is not an option for you, you can contact support to process the shift in a special off-cycle payroll run. Off-cycle payroll runs have an additional fee that depends on your contract agreement.
> 
> Make sure to provide the shift details via a CSV file through the support channel.

### Preventing late submissions with `payroll_cycle_ref.date`

To avoid accidental late submissions that result in a shift being processed in the next cycle, you can include the optional `payroll_cycle_ref.date` parameter when submitting a shift. This parameter ensures that the shift is only associated with the specified cycle if the submission is timely, avoiding shifts being unintentionally pushed to the next payroll cycle.

When you pass a `payroll_cycle_ref.date`, you're declaring your intended payroll cycle for the shift. The system compares the request's time stamp with the cycle's cutoff date and checks whether the current submission falls within the specified cycle.

- If the submission timestamp is before the cutoff of the current cycle, the request succeeds
- If the submission timestamp is after the cutoff, the request is rejected

This validation ensures that the shift is only associated with the specified cycle if the submission is timely.

Without the `payroll_cycle_ref.date` parameter, the system automatically determines the cycle based on the submission time — which may lead to late shifts being silently pushed to the next cycle. Use this parameter when you want explicit alignment with a particular payroll cycle.

Here's an example of how to use the `payroll_cycle_re.date` parameter:

> 👍 Format of the `payroll_cycle_ref`
> 
> The `payroll_cycle_ref.date` follows the [ISO 8601 date and time format](https://en.wikipedia.org/wiki/ISO_8601). You can use any date within the cycle's start and end dates, but we recommend using the cycle's end date for clarity.

```json
{
  "data": {
    "contract_id": "123456",
    "shifts": [
      {
        "external_id": "shift_123456",
        "description": "This is a sample shift description.",
        "date_of_work": "2023-10-01",
        "payroll_cycle_ref": {
          "date": "2025-06-04T00:00:00.000Z",
        },
        "summary": {
          "shift_rate_external_id": "rate1234",
          "time_unit": "HOUR",
          "time_amount": 15.50
        }
      }
    ]
```

## Manage shifts

This section covers how to add, update, and delete shifts for an employee.

### Add shifts

This section covers how to add shifts for an employee. There are different endpoints available for adding shifts based on the shift type:

- [Add categorized shifts](https://developer.deel.com/docs/time-tracking#add-categorized-shifts)
- [Add categorized shifts - Legacy (Not Recommended)](https://developer.deel.com/docs/time-tracking#legacy-add-categorized-shifts)
- [Add uncategorized (raw) shifts](https://developer.deel.com/docs/time-tracking#add-uncategorized-raw-shifts)

#### Add categorized shifts

You can add multiple categorized shifts for a single contract by providing an array of shifts. Before creating a categorized shift, you need to [create a shift rate](https://developer.deel.com/reference/createanewshiftrate) that you will link to the shift.

You can add a shift using any of the following time units: `HOUR` , `DAY` , `WEEK` , and `MONTH`.

To add shifts, make a POST request to the [Create a time tracking shift](https://developer.deel.com/reference/createshifts) endpoint.

```bash
curl --location --request POST 'https://api.letsdeel.com/rest/v2/time_tracking/shifts' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "contract_id": "123456",
        "shifts": [
            {
                "external_id": "shift_123456",
                "description": "This is a sample shift description.",
                "date_of_work": "2023-10-01",
                "payroll_cycle_ref": {
                    "date": "2023-10-31T00:00:00.000Z"
                },
                "summary": {
                    "shift_rate_external_id": "rate1234",
                    "time_unit": "HOUR",
                    "time_amount": 15.50
                }
            }
        ]
    }
}'
```

In the body:

| Name                           | Required | Type   | Format               | Description                                                                                                                                             | Example                               |
| ------------------------------ | -------- | ------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| contract_id                    | true     | string | -                    | Unique identifier of the contract for which shifts are being submitted                                                                                  | `123456`                              |
| description                    | true     | string | -                    | Description of shift. Use it to describe what kind of work is done during the shift.                                                                    | `This is a sample shift description.` |
| external_id                    | true     | string | -                    | User-defined ID of the shift                                                                                                                            | `shift_123456`                        |
| date_of_work                   | true     | string | date                 | Date on which shift is performed. It is used to identify the payroll cycle of the shift                                                                 | `2023-10-01`                          |
| payroll_cycle_ref.date         | false    | string | date-time (ISO 8601) | Reference date of the payroll cycle in which shift should be processed (We recommend to send the payroll cycle end date as the payroll cycle reference) | `2023-10-31T00:00:00.000Z`            |
| summary                        | true     | object | -                    | Object containing numerical data about the shift. This data is used to calculate the amount to be paid for the shift.                                   | -                                     |
| summary.shift_rate_external_id | true     | string | -                    | ID of the shift rate. Use it to link the shift to [a shift rate you created](#create-a-shift-rate).                                                     | `rate1234`                            |
| summary.time_unit              | true     | string | -                    | Time unit for the shift. Possible values: `HOUR`, `DAY`, `WEEK`, `MONTH`.                                                                               | `HOUR`                                |
| summary.time_amount            | false    | number | -                    | Length of the shift, expressed in the selected time unit                                                                                                | `15.50`                               |

A successful response (`200`) returns the details of the shift created.

```json
{
  "data": [
    {
      "external_id": "95c35493-41aa-44f8-9154-5a25cbbc1865",
      "organization_id": 0,
      "description": "string",
      "date_of_work": "2019-08-24T14:15:22Z",
      "contract_id": "string",
      "payroll_cycle_ref": {
        "date": "2023-10-31T00:00:00.000Z"
      },
      "summary": {
        "shift_rate_external_id": "rate1234",
        "time_unit": "HOUR",
        "time_amount": 15.50,
        "total_payable_hours": 15.50
      },
      "created_at": "2022-05-24T09:38:46.235Z",
      "updated_at": "2022-05-24T09:38:46.235Z"
    }
  ]
}
```

Where:

| Name                   | Required | Type   | Format               | Description                                                                                                           | Example                               |
| ---------------------- | -------- | ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| external_id            | true     | string | -                    | User-defined ID of the shift                                                                                          | `shift_123456`                        |
| organization_id        | true     | number | -                    | The ID of your organization                                                                                           | `123456`                              |
| description            | true     | string | -                    | Description of shift                                                                                                  | `This is a sample shift description.` |
| date_of_work           | true     | string | date-time            | Date of the shift                                                                                                     | `2019-08-24T14:15:22Z`                |
| payroll_cycle_ref.date | false    | string | date-time (ISO 8601) | Reference date of the payroll cycle in which shift will be processed                                                  | `2023-10-31T00:00:00.000Z`            |
| contract_id            | true     | string | -                    | Unique identifier of the contract that shifts were submitted for                                                      | `123456`                              |
| summary                | true     | object | -                    | Object containing numerical data about the shift. This data is used to calculate the amount to be paid for the shift. | -                                     |
| created_at             | true     | string | date-time            | Date on which the shift is created                                                                                    | `2022-05-24T09:38:46.235Z`            |
| updated_at             | true     | string | date-time            | Date on which the shift is updated                                                                                    | `2022-05-24T09:38:46.235Z`            |

Note: The `total_payable_hours` is set by default by the API when your `time_unit` is hour. 

#### Add categorized shifts (Legacy)

This method is still supported, but it is recommended to use [Add categorized shifts](https://developer.deel.com/docs/time-tracking#add-categorized-shifts) instead.

This shift type adds a shift without requiring `time_amount` and `time_unit` in the request body. By default, `time_amount` is set to `summary.total_payable_hours` and `time_unit` is set to `HOUR`. You can perform the same operations on these shifts as you would with [categorized shifts](https://developer.deel.com/docs/time-tracking#add-categorized-shifts) by using the same payload.

```bash
curl --location --request POST 'https://api.letsdeel.com/rest/v2/time_tracking/shifts' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "contract_id": "123456",
        "shifts": [
            {
                "external_id": "shift_123456",
                "description": "This is a sample shift description.",
                "date_of_work": "2023-10-01",
                "payroll_cycle_ref": {
                    "date": "2023-10-31T00:00:00.000Z"
                },
                "summary": {
                    "shift_rate_external_id": "rate1234",
                    "shift_duration_hours": 8,
                    "total_break_hours": 1,
                    "payable_break_hours": 0.5,
                    "total_payable_hours": 7.5
                }
            }
        ]
    }
}'
```

In the body:

| Name                           | Required | Type   | Format               | Description                                                                                                                                             | Example                               |
| ------------------------------ | -------- | ------ | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| contract_id                    | true     | string | -                    | Unique identifier of the contract for which shifts are being submitted                                                                                  | `123456`                              |
| description                    | true     | string | -                    | Description of shift. Use it to describe what kind of work is done during the shift.                                                                    | `This is a sample shift description.` |
| external_id                    | true     | string | -                    | User-defined ID of the shift                                                                                                                            | `shift_123456`                        |
| date_of_work                   | true     | string | date                 | Date on which shift is performed. It is used to identify the payroll cycle of the shift                                                                 | `2023-10-01`                          |
| payroll_cycle_ref.date         | false    | string | date-time (ISO 8601) | Reference date of the payroll cycle in which shift should be processed (We recommend to send the payroll cycle end date as the payroll cycle reference) | `2023-10-31T00:00:00.000Z`            |
| summary                        | true     | object | -                    | Object containing numerical data about the shift. This data is used to calculate the amount to be paid for the shift.                                   | -                                     |
| summary.shift_rate_external_id | true     | string | -                    | ID of the shift rate. Use it to link the shift to [a shift rate you created](#create-a-shift-rate).                                                     | `rate1234`                            |
| summary.shift_duration_hours   | false    | number | -                    | Total time of the shift in hours                                                                                                                        | `8`                                   |
| summary.total_break_hours      | false    | number | -                    | Total break time in hours                                                                                                                               | `1`                                   |
| summary.payable_break_hours    | false    | number | -                    | Total breaks hours that must be paid                                                                                                                    | `0.5`                                 |
| summary.total_payable_hours    | true     | number | -                    | Total hours that need be paid using the shift rate provided above                                                                                       | `7.5`                                 |

A successful response (`200`) returns the details of the shift created.

```json
{
  "data": [
    {
      "external_id": "95c35493-41aa-44f8-9154-5a25cbbc1865",
      "organization_id": 0,
      "description": "string",
      "date_of_work": "2019-08-24T14:15:22Z",
      "contract_id": "string",
      "payroll_cycle_ref": {
        "date": "2023-10-31T00:00:00.000Z"
      },
      "summary": {
        "shift_rate_external_id": "rate1234",
        "time_unit": "HOUR",
        "time_amount": 7.5,
        "shift_duration_hours": 8,
        "total_break_hours": 1,
        "payable_break_hours": 0.5,
        "total_payable_hours": 7.5
      },
      "created_at": "2022-05-24T09:38:46.235Z",
      "updated_at": "2022-05-24T09:38:46.235Z"
    }
  ]
}
```

Where:

| Name                   | Required | Type   | Format               | Description                                                                                                           | Example                               |
| ---------------------- | -------- | ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| external_id            | true     | string | -                    | User-defined ID of the shift                                                                                          | `shift_123456`                        |
| organization_id        | true     | number | -                    | The ID of your organization                                                                                           | `123456`                              |
| description            | true     | string | -                    | Description of shift                                                                                                  | `This is a sample shift description.` |
| date_of_work           | true     | string | date-time            | Date of the shift                                                                                                     | `2019-08-24T14:15:22Z`                |
| payroll_cycle_ref.date | false    | string | date-time (ISO 8601) | Reference date of the payroll cycle in which shift will be processed                                                  | `2023-10-31T00:00:00.000Z`            |
| contract_id            | true     | string | -                    | Unique identifier of the contract that shifts were submitted for                                                      | `123456`                              |
| summary                | true     | object | -                    | Object containing numerical data about the shift. This data is used to calculate the amount to be paid for the shift. | -                                     |
| created_at             | true     | string | date-time            | Date on which the shift is created                                                                                    | `2022-05-24T09:38:46.235Z`            |
| updated_at             | true     | string | date-time            | Date on which the shift is updated                                                                                    | `2022-05-24T09:38:46.235Z`            |

#### Add uncategorized (raw) shifts

You can add multiple uncategorized shifts for a single contract by providing an array of shifts.

To add shifts, make a POST request to the [Create uncategorized (raw) shift](https://developer.deel.com/reference/createrawshifts) endpoint.

```bash
curl --location --request POST 'https://api.letsdeel.com/rest/v2/time_tracking/shifts/raw' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "contract_id": "123456",
        "shifts": [
            {
                "external_id": "shift_123456",
                "description": "This is a sample shift description.",
                "date_of_work": "2024-04-01",
                "meta": {
                  "start": {
                    "date": "2024-04-01",
                    "time": "09:00",
                    "is_rest_day": false,
                    "is_public_holiday": false
                  },
                  "end": {
                    "date": "2024-04-01",
                    "time": "17:00",
                    "is_rest_day": false,
                    "is_public_holiday": false
                  },
                  "breaks": [
                    {
                      "end": {
                        "date": "2024-04-01",
                        "time": "12:00"
                      },
                      "start": {
                        "date": "2024-04-01",
                        "time": "11:00"
                      },
                      "is_paid": true
                    }
                  ],
                  "approval_date": "2024-04-03"
                }
            }
        ]
    }
}'
```

In the body:

| Name                         | Required | Type    | Format       | Description                                                                             | Example                               |
| ---------------------------- | -------- | ------- | ------------ | --------------------------------------------------------------------------------------- | ------------------------------------- |
| contract_id                  | true     | string  | -            | Unique identifier of the contract for which shifts are being submitted                  | `123456`                              |
| external_id                  | true     | string  | -            | User-defined ID of the shift                                                            | `shift_123456`                        |
| description                  | true     | string  | -            | Description of shift. Use it to describe what kind of work is done during the shift.    | `This is a sample shift description.` |
| date_of_work                 | true     | string  | date         | Date on which shift is performed. It is used to identify the payroll cycle of the shift | `2024-04-01`                          |
| meta                         | true     | object  | -            | Object containing detailed start/end times, breaks, and approval metadata               | -                                     |
| meta.start.date              | true     | string  | date         | Date when the shift starts                                                              | `2024-04-01`                          |
| meta.start.time              | true     | string  | time (HH:mm) | Start time of the shift                                                                 | `09:00`                               |
| meta.start.is_rest_day       | true     | boolean | -            | Indicates if the shift start is on a rest day                                           | `false`                               |
| meta.start.is_public_holiday | true     | boolean | -            | Indicates if the shift start is on a public holiday                                     | `false`                               |
| meta.end.date                | true     | string  | date         | Date when the shift ends                                                                | `2024-04-01`                          |
| meta.end.time                | true     | string  | time (HH:mm) | End time of the shift                                                                   | `17:00`                               |
| meta.end.is_rest_day         | true     | boolean | -            | Indicates if the shift end is on a rest day                                             | `false`                               |
| meta.end.is_public_holiday   | true     | boolean | -            | Indicates if the shift end is on a public holiday                                       | `false`                               |
| meta.breaks                  | false    | array   | -            | List of breaks taken during the shift                                                   | -                                     |
| meta.breaks\[].start.date    | true     | string  | date         | Break start date                                                                        | `2024-04-01`                          |
| meta.breaks\[].start.time    | true     | string  | time (HH:mm) | Break start time                                                                        | `11:00`                               |
| meta.breaks\[].end.date      | true     | string  | date         | Break end date                                                                          | `2024-04-01`                          |
| meta.breaks\[].end.time      | true     | string  | time (HH:mm) | Break end time                                                                          | `12:00`                               |
| meta.breaks\[].is_paid       | false    | boolean | -            | Indicates whether the break is paid                                                     | `true`                                |
| meta.approval_date           | false    | string  | date         | Date when the shift was approved by a manager                                           | `2024-04-03`                          |

A successful response (`200`) returns the details of the shift created.

```json
{
  "data": [
    {
      "external_id": "shift_example05",
      "description": "This is a sample shift description 5",
      "date_of_work": "2025-06-01",
      "created_at": "2025-06-30T19:31:54.402Z",
      "updated_at": "2025-06-30T19:31:54.402Z",
      "contract_id": "mjgd99e",
      "meta": {
        "start": {
          "date": "2024-02-12",
          "time": "08:00",
          "is_rest_day": false,
          "is_public_holiday": false
        },
        "end": {
          "date": "2024-02-12",
          "time": "16:00",
          "is_rest_day": false,
          "is_public_holiday": false
        },
        "approval_date": "2024-12-11"
      }
    }
  ]
}
```

Where:

| Name                         | Required | Type    | Format       | Description                                                      | Example                                |
| ---------------------------- | -------- | ------- | ------------ | ---------------------------------------------------------------- | -------------------------------------- |
| external_id                  | true     | string  | -            | User-defined ID of the shift                                     | `shift_example05`                      |
| description                  | true     | string  | -            | Description of shift                                             | `This is a sample shift description 5` |
| date_of_work                 | true     | string  | date         | Date of the shift                                                | `2025-06-01`                           |
| contract_id                  | true     | string  | -            | Unique identifier of the contract that shifts were submitted for | `mjgd99e`                              |
| created_at                   | true     | string  | date-time    | Date on which the shift is created                               | `2025-06-30T19:31:54.402Z`             |
| updated_at                   | true     | string  | date-time    | Date on which the shift is updated                               | `2025-06-30T19:31:54.402Z`             |
| meta                         | true     | object  | -            | Object containing detailed start/end times and approval date     | -                                      |
| meta.start.date              | true     | string  | date         | Date when the shift starts                                       | `2024-02-12`                           |
| meta.start.time              | true     | string  | time (HH:mm) | Start time of the shift                                          | `08:00`                                |
| meta.start.is_rest_day       | true     | boolean | -            | Indicates if the shift start is on a rest day                    | `false`                                |
| meta.start.is_public_holiday | true     | boolean | -            | Indicates if the shift start is on a public holiday              | `false`                                |
| meta.end.date                | true     | string  | date         | Date when the shift ends                                         | `2024-02-12`                           |
| meta.end.time                | true     | string  | time (HH:mm) | End time of the shift                                            | `16:00`                                |
| meta.end.is_rest_day         | true     | boolean | -            | Indicates if the shift end is on a rest day                      | `false`                                |
| meta.end.is_public_holiday   | true     | boolean | -            | Indicates if the shift end is on a public holiday                | `false`                                |
| meta.approval_date           | false    | string  | date         | Date when the shift was approved by a manager                    | `2024-12-11`                           |

### List shifts in your organization

You can list the shifts in your organization and sort them by the time of creation.

To list shifts, make a GET request to the [List time tracking shifts](https://developer.deel.com/reference/listofshifts) endpoint.

```curl
curl --location --request GET 'https://api.letsdeel.com/rest/v2/time_tracking/shifts?limit=10&offset=20&contract_id[]=abcd&contract_id[]=abcd2&from_date=2023-10-01&to_date=2023-10-02' \
--header 'Authorization: Bearer {{token}}'
```

In the query:

| Name           | Required | Type      | Format      | Description                                                    | Example                                 |
| -------------- | -------- | --------- | ----------- | -------------------------------------------------------------- | --------------------------------------- |
| limit          | false    | number    |             | Number of rows that must be returned in one API call           | 100                                     |
| offset         | false    | number    |             | Number of rows that must be skipped when returning the results | 10                                      |
| contract_id\[] | false    | string\[] | array param | Filter shifts by one or more contract IDs                      | contract_id\[]=abcd&contract_id\[]=efgh |
| from_date      | false    | string    | YYYY-MM-DD  | Filter shifts from this date (inclusive)                       | 2023-10-01                              |
| to_date        | false    | string    | YYYY-MM-DD  | Filter shifts until this date (inclusive)                      | 2023-10-02                              |

> 📘 Use the array syntax `contract_id[]=value` to filter for contract IDs. For multiple contract IDs, you can use `contract_id[]=value1&contract_id[]=value2`.

A successful response (`200`) returns the list of shifts available in your organization and matching any filters applied. For example:

```json
{
  "data": [
    {
      "external_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "organization_id": 0,
      "description": "string",
      "date_of_work": "2019-08-24T14:15:22Z",
      "contract_id": "string",
      "summary": {
        "shift_rate_external_id": "rate1234",
        "time_unit": "HOUR",
        "time_amount": 15.50,
        "total_payable_hours": 15.50
      },
      "created_at": "2022-05-24T09:38:46.235Z",
      "updated_at": "2022-05-24T09:38:46.235Z"
    }
  ],
  "page": {
    "total_rows": 0,
    "items_per_page": 1,
    "offset": 999999999
  }
}
```

Where:

| Name | Required | Type   | Format | Description                                                                | Example |
| ---- | -------- | ------ | ------ | -------------------------------------------------------------------------- | ------- |
| data | true     | array  | -      | The list of shifts available                                               | -       |
| page | true     | object | -      | Contains information to navigate to the next set of results, if applicable | -       |

### Retrieve a single shift

You can retrieve the information of a single shift starting from the `external_id` of the shift.

To retrieve a shift, make a GET request to the [Retrieve a single time tracking shift](https://developer.deel.com/reference/gettimetrackingshiftbyexternalid) endpoint.

```curl
curl --location --request GET 'https://api.letsdeel.com/rest/v2/time_tracking/shifts/{{external_id}}' \
--header 'Authorization: Bearer {{token}}'
```

A successful response (`200`) returns the information of the requested shift.

```json
{
  "external_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
  "organization_id": 0,
  "description": "string",
  "date_of_work": "2019-08-24T14:15:22Z",
  "contract_id": "string",
  "summary": {
    "shift_rate_external_id": "rate1234",
    "time_unit": "HOUR",
    "time_amount": 15.50,
    "total_payable_hours": 15.50
  },
  "created_at": "2022-05-24T09:38:46.235Z",
  "updated_at": "2022-05-24T09:38:46.235Z"
}
```

### Update shifts

If you need it, you can update the information of a shift before it's processed. After a shift is processed, your ability to amend it depends on the shift type:

- You can amend a categorized shift using [correction shifts](#correction-shifts)
- You cannot amend uncategorized (raw) shifts

This section explains how to update shifts that haven't been processed for payroll:

- [Update categorized shift for an employee](#update-categorized-shift-for-an-employee)
- [Update uncategorized (raw) shift for an employee](#update-uncategorized-raw-shift-for-an-employee)

### Update categorized shift for an employee

If you need it, you can update the information of a categorized shift.

> 📘 You can only update shifts that haven't been processed for payroll
> 
> Shifts are processed for payroll at the cutoff date.

To update a categorized shift, make a PATCH request to the [Update a time tracking shift](https://developer.deel.com/reference/updateashift) endpoint.

```curl
curl --location --request PATCH 'https://api.letsdeel.com/rest/v2/time_tracking/shifts/{{external_id}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "description": "This is a sample shift description.",
        "date_of_work": "2023-10-01",
        "payroll_cycle_ref": {
          "date": "2023-10-31T00:00:00.000Z"
        },
        "summary": {
          "time_amount": 15.50,
        }
    }
}'
```

In the path:

| Name        | Required | Type   | Format | Description                  | Example        |
| ----------- | -------- | ------ | ------ | ---------------------------- | -------------- |
| external_id | true     | string | -      | User-defined ID of the shift | `shift_123456` |

In the body:

| Name | Required | Type   | Format | Description                                                 | Example |
| ---- | -------- | ------ | ------ | ----------------------------------------------------------- | ------- |
| data | true     | object | -      | Contains the information of the shift that must be updated. | -       |

A successful response (`200`) returns the updated shift. For example:

```json
{
  "external_id": "95c35493-41aa-44f8-9154-5a25cbbc1865",
  "organization_id": 0,
  "description": "string",
  "date_of_work": "2019-08-24T14:15:22Z",
  "contract_id": "string",
  "payroll_cycle_ref": {
    "date": "2023-10-31T00:00:00.000Z"
  },
  "summary": {
    "shift_rate_external_id": "rate1234",
    "time_unit": "HOUR",
    "time_amount": 15.50,
    "total_payable_hours": 15.50
  },
  "created_at": "2022-05-24T09:38:46.235Z",
  "updated_at": "2022-05-24T09:38:46.235Z"
}
```

### Update uncategorized (raw) shift for an employee

If you need it, you can update the information of an uncategorized shift.

> 📘 You can only update shifts that haven't been processed for payroll
> 
> Shifts are processed for payroll at the cutoff date.

To update an uncategorized shift, make a PATCH request to the [Update a raw time tracking shift](https://developer.deel.com/reference/updaterawshift) endpoint.

```bash
curl --location --request PATCH 'https://api.letsdeel.com/rest/v2/time_tracking/shifts/raw/{{external_id}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "description": "This is a sample shift updated now again.",
        "date_of_work": "2023-10-01",
        "meta": {
            "start": {
                "date": "2024-02-12",
                "time": "08:00",
                "is_rest_day": false,
                "is_public_holiday": false
            },
            "end": {
                "date": "2024-02-12",
                "time": "16:00",
                "is_rest_day": false,
                "is_public_holiday": false
            },
            "approval_date": "2024-12-11"
        }
    }
}'
```

In the path:

| Name        | Required | Type   | Format | Description                  | Example        |
| ----------- | -------- | ------ | ------ | ---------------------------- | -------------- |
| external_id | true     | string | -      | User-defined ID of the shift | `shift_123456` |

In the body:

| Name | Required | Type   | Format | Description                                                 | Example |
| ---- | -------- | ------ | ------ | ----------------------------------------------------------- | ------- |
| data | true     | object | -      | Contains the information of the shift that must be updated. | -       |

A successful response (`200`) returns the updated shift. For example:

```json
{
  "external_id": "95c35493-41aa-44f8-9154-5a25cbbc1865",
  "description": "string",
  "date_of_work": "2019-08-24T14:15:22Z",
  "contract_id": "string",
  "payroll_cycle_ref": {
    "date": "2023-10-31T00:00:00.000Z"
  },
  "meta": {
    "start": {
      "date": "2024-02-12",
      "time": "08:00",
      "is_rest_day": false,
      "is_public_holiday": false
    },
    "end": {
      "date": "2024-02-12",
      "time": "16:00",
      "is_rest_day": false,
      "is_public_holiday": false
    },
    "approval_date": "2024-12-11"
  },
  "created_at": "2022-05-24T09:38:46.235Z",
  "updated_at": "2022-05-24T09:38:46.235Z"
}
```

### Delete shift for a contract

You can delete a shift for a contract by using the `external_id` of the shift.

To delete a shift, make a DELETE request to the [Delete a time tracking shift](https://developer.deel.com/reference/deletetimetrackingshift) endpoint.

> 📘 You can only delete shifts that haven't been processed for payroll
> 
> Shifts are processed for payroll at the cutoff date.

```curl
curl --location --request DELETE 'https://api.letsdeel.com/rest/v2/time_tracking/shifts/{{external_id}}' \
--header 'Authorization: Bearer {{token}}'
```

Where:

| Name        | Required | Type   | Format | Description                  | Example        |
| ----------- | -------- | ------ | ------ | ---------------------------- | -------------- |
| external_id | true     | string | -      | User-defined ID of the shift | `shift_123456` |

A successful response (`204`) returns an empty body.

## Correction shifts

When you need to adjust hours for shifts that have already been processed for payroll, you can use correction shifts. Corrections create a new shift entry that adjusts the payable hours of the original shift. The correction will be processed in the next payroll cycle, ensuring accurate compensation without modifying historical payroll data.

Before using correction shifts, keep in mind the following aspects:

- Correction shifts can only be submitted for [categorized shifts](#categorized-shifts), not for [uncategorized shifts](#uncategorized-raw-shifts).
- Corrections can only be submitted for shifts that have already been processed. Unprocessed shifts can be corrected with an [update](#update-shifts).
- Correction shifts cannot be submitted for another correction shift
- Correction shifts cannot be updated but can be deleted

To submit a correction, use the same [Create a time tracking shift](https://developer.deel.com/reference/createshifts) endpoint, by specifying `CORRECTION_DELTA` as the `shift_type` and including a `corrections` array with additional fields to specify the correction details.

For example, you may have previously created a shift with 10 total payable hours and this shift has been already processed for payroll. If you later discover that the actual hours worked were 7.5, which requires a reduction of 2.5 hours, you can submit a correction as follows:

```bash
curl --location --request POST 'https://api.letsdeel.com/rest/v2/time_tracking/shifts' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "contract_id": "3j5z2e6",
        "shifts": [
            {
                "external_id": "shift_example47",
                "description": "Correction shift",
                "shift_type": "CORRECTION_DELTA",
                "shift_reference_id": "shift_example45",
                "corrections": [
                    {
                        "type": "SUBTRACTION",
                        "time_amount": 2.5
                    }
                ]
            }
        ]
    }
}'
```

In the body:

| Name                       | Required | Type   | Format | Description                                                                      | Example            |
| -------------------------- | -------- | ------ | ------ | -------------------------------------------------------------------------------- | ------------------ |
| contract_id                | true     | string | -      | Unique identifier of the contract for which the correction is being submitted    | `3j5z2e6`          |
| external_id                | true     | string | -      | User-defined ID for the correction shift                                         | `shift_example47`  |
| description                | true     | string | -      | Description of the correction. Use it to describe the reason for the correction. | `Correction shift` |
| shift_type                 | true     | string | -      | Type of shift being submitted. Use `CORRECTION_DELTA` for corrections            | `CORRECTION_DELTA` |
| shift_reference_id         | true     | string | -      | External ID of the original shift that is being corrected                        | `shift_example45`  |
| corrections                | true     | array  | -      | Array containing correction details                                              | -                  |
| corrections\[].type        | true     | string | -      | Type of correction. Use `SUBTRACTION` to reduce hours or `ADDITION` to add hours | `SUBTRACTION`      |
| corrections\[].time_amount | true     | number | -      | Amount of time to add or subtract from the original shift                        | `2.5`              |

A successful response (`200`) returns the details of the correction shift created.

```json
{
  "data": [
    {
      "external_id": "shift_example47",
      "description": "Correction shift",
      "date_of_work": "2019-08-24T14:15:22Z",
      "contract_id": "3j5z2e6",
      "summary": {
        "time_amount": -2.5,
        "total_payable_hours": -2.5
      },
      "shift_type": "CORRECTION_DELTA",
      "shift_reference_id": "shift_example45",
      "created_at": "2022-05-24T09:38:46.235Z",
      "updated_at": "2022-05-24T09:38:46.235Z"
    }
  ]
}
```

Where:

| Name                | Required | Type   | Format    | Description                                                                                                                     | Example                    |
| ------------------- | -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| external_id         | true     | string | -         | User-defined ID of the correction shift                                                                                         | `shift_example47`          |
| description         | true     | string | -         | Description of the correction                                                                                                   | `Correction shift`         |
| date_of_work        | true     | string | date-time | Date of the original shift being corrected                                                                                      | `2019-08-24T14:15:22Z`     |
| contract_id         | true     | string | -         | Unique identifier of the contract                                                                                               | `3j5z2e6`                  |
| summary             | true     | object | -         | Object containing the delta values for the correction. Negative values indicate reductions, positive values indicate additions. | -                          |
| summary.time_amount | true     | number | -         | Adjustment amount, negative for reduction and positive for increase                                                             | `-2.5`                     |
| shift_type          | true     | string | -         | Type of shift, will be `CORRECTION_DELTA` for corrections                                                                       | `CORRECTION_DELTA`         |
| shift_reference_id  | true     | string | -         | External ID of the original shift being corrected                                                                               | `shift_example45`          |
| created_at          | true     | string | date-time | Date on which the correction is created                                                                                         | `2022-05-24T09:38:46.235Z` |
| updated_at          | true     | string | date-time | Date on which the correction is updated                                                                                         | `2022-05-24T09:38:46.235Z` |

## Manage shift rates

Shift rates are used in payroll calculations to define the amount of the salary to be paid for a specific shift. There shift rate types are:

| Name                  | Description                                                                                                                                                                       | Formula                                                                                         | Example                                                                                                                                                                                                                            |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MULTIPLIER_PERCENTAGE | Defines the rate of a shift as a percentage of the salary, using the employee's hourly salary (if it's a hourly contract) or equivalent hourly salary (for non-hourly contracts). | `Total amount for shift  = (MULTIPLIER_PERCENTAGE/100) * Per_hour_salary * Total_payable_hours` | 10$/hour is the base salary, user submitted shift with total of 5 payable hours and according to the shift rate attached to the shift MULTIPLIER_PERCENTAGE is set to 200% so Total amount paid for the shift = 2 _ 10 \_ 5 = 100$ |
| PER_HOUR_FLAT_RATE    | Define the rate of a shift as a flat rate per hour.                                                                                                                               | `Total amount for shift = PER_HOUR_FLAT_RATE * Total_payable_hours`                             | PER_HOUR_FLAT_RATE set to 100$ and total_payable_hours for the shift are 5 hours Total amount paid for the shift = 100 \* 5 = 500$                                                                                                 |

### Create a shift rate

You can create shift rates for your organization, which you can then map to individual shifts [when adding them](#add-shifts).

To create a shift rate, make a POST request to the [time_tracking/shift_rates](https://developer.deel.com/reference/createtimetrackingshiftrate) endpoint.

```curl
curl --location --request POST 'https://api.letsdeel.com/rest/v2/time_tracking/shift_rates' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
        "external_id": "regular_rate_1",
        "name": "Regular Shift rate 1",
        "type": "PER_HOUR_FLAT_RATE",
        "value": 150
    }
}'
```

Where:

| Name         | Required | Type   | Format | Description                                       | Example          |
| ------------ | -------- | ------ | ------ | ------------------------------------------------- | ---------------- |
|  external_id | true     | string | -      | User defined unique identifier for the shift rate | `regular_rate_1` |

Step 1: Fill the below details related to the shift rate

| Name        | Required | Type   | Format | Description                                                                                                   | Example                |
| :---------- | :------- | :----- | :----- | :------------------------------------------------------------------------------------------------------------ | :--------------------- |
| external_id | true     | string | -      | User defined unique identifier for the shift rate                                                             | `regular_rate_1`       |
| name        | true     | string | -      | A human readable string to identify the purpose of the shift rate                                             | `Regular Shift rate 1` |
| type        | false    | string | ENUM   | Defines the type of rate that must be used. Use any of the [available shift rate types](#manage-shift-rates). | `PER_HOUR_FLAT_RATE`   |
| value       | false    | number | -      | Value of the shift rate, to use in combination with the `type` parameter                                      | 150                    |

### Retrieve the shift rate

You can also retrieve the shift rates starting from the `external_id` of the shift rate.

To retrieve a shift rate, make a GET request to the [Retrieve a single time tracking shift rate](https://developer.deel.com/reference/gettimetrackingshiftratebyexternalid) endpoint.

```curl
curl --location --request GET 'https://api.letsdeel.com/rest/v2/time_tracking/shift_rates/{{external_id}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json'
```

Where:

| Name        | Required | Type   | Format | Description                                       | Example        |
| ----------- | -------- | ------ | ------ | ------------------------------------------------- | -------------- |
| external_id | true     | string | -      | User-defined unique identifier for the shift rate | `shift_123456` |

A successful response (`200`) returns the shift rate of the requested shift. For example:

```json
{
  "data": {
    "organization_id": "string",
    "external_id": "string",
    "name": "string",
    "rate_type": "MULTIPLIER_PERCENTAGE",
    "value": 0,
    "created_at": "2022-05-24T09:38:46.235Z",
    "updated_at": "2022-05-24T09:38:46.235Z"
  }
}
```

### Retrieve shift rates

You can also retrieve the list of shift rates for your organization.

To retrieve a list of shift rates, make a GET request to the [List time tracking shift rates](https://developer.deel.com/reference/gettimetrackingshiftrates) endpoint.

```curl
curl --location --request GET 'https://api.letsdeel.com/rest/v2/time_tracking/shift_rates?limit=10&offset=5' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json'
```

| Name   | Required | Type   | Format | Description                                                    | Example |
| ------ | -------- | ------ | ------ | -------------------------------------------------------------- | ------- |
| limit  | false    | number |        | Number of rows that must be returned in one API call           | 100     |
| offset | false    | number |        | Number of rows that must be skipped when returning the results | 10      |

A successful response (`200`) returns the list of shift rates available in your organization and matching any filters applied. For example:

```json
{
  "data": [
    {
      "organization_id": "string",
      "external_id": "string",
      "name": "string",
      "rate_type": "MULTIPLIER_PERCENTAGE",
      "value": 0,
      "created_at": "2022-05-24T09:38:46.235Z",
      "updated_at": "2022-05-24T09:38:46.235Z"
    }
  ],
  "page": {
    "total_rows": 0,
    "items_per_page": 1,
    "offset": 999999999
  }
}
```

Where:

| Name            | Required | Type   | Format    | Description                                                                                             | Example                                      |
| --------------- | -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| data            | true     | array  | -         | An array of shift rates                                                                                 | `[shift_rate_1, shift_rate_2, shift_rate_3]` |
| organization_id | true     | number | -         | The ID of your organization                                                                             | `123456`                                     |
| external_id     | true     | string | -         | User defined unique identifier for the shift rate                                                       | `regular_rate_1`                             |
| name            | true     | string | -         | A human readable string to identify the purpose of the shift rate                                       | `Regular Shift rate 1`                       |
| rate_type       | false    | string | ENUM      | Defines the type of rate that must be used. Use any of the [available shift rates](#manage-shift-rates) | `PER_HOUR_FLAT_RATE`                         |
| value           | false    | number | -         | Value of the shift rate, to use in combination with the `type` parameter                                | 150                                          |
| created_at      | true     | string | date-time | Date on which the shift rate is created                                                                 | `2022-05-24T09:38:46.235Z`                   |
| updated_at      | true     | string | date-time | Date on which the shift rate is updated                                                                 | `2022-05-24T09:38:46.235Z`                   |
| page            | true     | object | -         | An object containing pagination information. Use it to navigate through sets of                         | -                                            |

### Update a shift rate

You can also update a shift rate if it's not being used in any shift, by using the `external_id` of the shift rate.

To update a shift rate, make a PATCH request to the [Update a time tracking shift rate](https://developer.deel.com/reference/updatetimetrackingshiftrate) endpoint.

> 📘 Only shift rates that are not used in any shift can be updated.

```curl
curl --location --request PATCH 'https://api.letsdeel.com/rest/v2/time_tracking/shift_rates/{{external_id}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data '{
    "data": {
         "name": "On-call shift rate",
        "type": "PER_HOUR_FLAT_RATE",
        "value": 150
    }
}'
```

In the path:

| Name        | Required | Type   | Format | Description                                       | Example          |
| ----------- | -------- | ------ | ------ | ------------------------------------------------- | ---------------- |
| external_id | true     | string | -      | User defined unique identifier for the shift rate | `regular_rate_1` |

In the body:

| Name  | Required | Type   | Format | Description                                                                                             | Example                |
| ----- | -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------- | ---------------------- |
| name  | true     | string | -      | A human readable string to identify the purpose of the shift rate                                       | `Regular Shift rate 1` |
| type  | true     | string | ENUM   | Defines the type of rate that must be used. Use any of the [available shift rates](#manage-shift-rates) | `PER_HOUR_FLAT_RATE`   |
| value | true     | number | -      | Value of the shift rate, to use in combination with the `type` parameter                                | 150                    |

A successful response (`200`) returns the updated shift rate. For example:

```json
{
  "data": {
    "organization_id": "string",
    "external_id": "string",
    "name": "string",
    "rate_type": "MULTIPLIER_PERCENTAGE",
    "value": 0,
    "created_at": "2022-05-24T09:38:46.235Z",
    "updated_at": "2022-05-24T09:38:46.235Z"
  }
}
```

### Delete a shift rate

You can also delete a shift rate if it's not being used in any shift, by using the `external_id` of the shift rate.

To delete a shift rate, make a DELETE request to the [Delete a time tracking shift rate](https://developer.deel.com/reference/deletetimetrackingshiftrate) endpoint.

> 📘 Only shift rates that are not used in any shift can be deleted.

```curl
curl --location --request DELETE 'https://api.letsdeel.com/rest/v2/time_tracking/shift_rates/{{external_id}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json'
```

A successful response (`204`) returns an empty body.

---
title: "Manage time off"
slug: "time-off"
excerpt: "Learn how to manage time off policies, entitlements, and requests using the API"
hidden: false
createdAt: "Wed Oct 09 2024 12:55:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:33:16 GMT+0000 (Coordinated Universal Time)"
---
Time off on Deel is policy based. This means that time-off policies are implemented at an organization level and can be assigned to specific groups of workers. Groups or individual workers are eligible to a certain amount of time off based on the details of their contract. Such eligibility renews at specific intervals, usually yearly, and is referred to as _entitlements_. Entitlements can vary based on tenure, position, or local labor laws.

 _Policies_, on the other hand, are where the rules of each time-off entitlement are defined.  
For example, a policy determines the number of days per year, whether the time off is paid, and so on.

This article explains how to manage workers' time off using the API.

## View time off entitlements of a worker

 The [Get Profile Entitlements](https://developer.deel.com/reference/get_time-offs-profile-hris-profile-id-entitlements) endpoint allows to retrieve the amount of time off that each worker is entitled to for each policy.

To view time off entitlements for a worker, make a GET request to the [Get Profile Entitlements](https://developer.deel.com/reference/get_time-offs-profile-hris-profile-id-entitlements) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/time_offs/profile/{hris_profile_id}/entitlements?policy_type_name=Paid%20leave&tracking_period_date=2023-02-01' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the path:

| Name              | Required | Type     | Format | Description                                                | Example                                |
| ----------------- | -------- | -------- | ------ | ---------------------------------------------------------- | -------------------------------------- |
| `hris_profile_id` | `true`   | `string` | UUID   | The ID of the worker you want to view the entitlements for | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

In the query:

| Name                   | Required | Type     | Format | Description                                                                                                                     | Example        |
| ---------------------- | -------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| `policy_type_name`     | `false`  | `string` | -      | Enum to filter the results by one of the available types. Values are expressed in ASCII.                                        | `Paid%20leave` |
| `tracking_period_date` | `false`  | `string` | `date` | Filter the results by the entitlements available at a specific date. Also known as 'holiday year'. Use the format `YYYY-MM-DD`. |                |

A successful response (`200`) returns the available entitlements for a specific worker and, optionally, matching any filtering criteria added in the request.

```json
{
  "entitlements": [
    {
      "policy": {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Unpaid leave",
        "policy_type_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "tracking_unit": "YEAR",
        "tracking_unit_amount": 1,
        "tracking_cadence": "FIXED_DAY",
        "tracking_start_date": "2023-01-01T00:00:00Z",
        "policy_type": {
          "id": "f9647da8-5649-4ea0-9c07-df3681d0e7ab",
          "name": "Unpaid leave"
        }
      },
      "id": "2024-01-01-d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "tracking_period": "2024-01-01T00:00:00Z",
      "tracking_period_end_date": "2024-12-31T00:00:00Z",
      "approved": "0.00",
      "balance_adjusted": "0.00",
      "used": "0.00",
      "expired": "0.00",
      "requested": "0.00",
      "rollovers": [],
      "events": [],
      "policy_allowance": {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "type": "BASE_ALLOWANCE",
        "entitlement_unit": "BUSINESS_DAY",
        "entitlement_unit_amount": null,
        "entitlement_start_type": "IMMEDIATELY",
        "entitlement_start_unit": null,
        "entitlement_start_unit_amount": null,
        "entitlement_expiration_unit": null,
        "entitlement_expiration_unit_amount": null,
        "balance_tracking_type": "FLEXIBLE_NO_LIMIT",
        "accrual_type": "TIMEFRAME",
        "accrual_unit": null,
        "accrual_unit_amount": null,
        "accrual_prorate_types": null,
        "accrual_application_type": null,
        "rollover_type": null,
        "rollover_limit_unit_amount": null,
        "rollover_expiration_unit": null,
        "rollover_expiration_unit_amount": null,
        "zero_out_negative_balances_on_rollover": true,
        "enable_bank_holidays": true,
        "part_time_worker_treatment_type": "SAME_AS_FTE",
        "balance_tracking_flexible_custom_request_amount": null,
        "part_time_worker_treatment_specific_amount": null,
        "part_time_worker_additional_allowance_type": "SAME_AS_FTE",
        "is_accrual_prorate_policy": false,
        "has_partial_prorate": true,
        "termination_type": "NO_PAYOUT",
        "created_at": "2024-09-30T12:58:06.396Z",
        "updated_at": "2024-09-30T12:58:06.396Z"
      },
      "total_entitlements": "0.00",
      "upcoming_accruals": "0.00",
      "accrual_amount": "0.00",
      "accrual_unit": "BUSINESS_DAY",
      "future_events": [],
      "past_tracking_periods": [
        "2023-01-01T00:00:00Z"
      ]
    },
    {
      …
    }
  ],
  "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
}
```

Where:

| Name                       | Type     | Format      | Description                                                                              | Example                                |
| -------------------------- | -------- | ----------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `id`                       | `string` | UUID        | The unique identifier of the entitlement                                                 | `160bbb27-a56d-4be5-af21-4ccc5d9ef2bb` |
| `tracking_period`          | `string` | `date-time` | The start of the entitlement                                                             | `2024-01-01T00:00:00Z`                 |
| `tracking_period_end_date` | `string` | `date-time` | The end of the entitlement                                                               | `2024-12-31T00:00:00Z`                 |
| `approved`                 | `string` | `float`     | The approved entitlement                                                                 | `0.00`                                 |
| `balance_adjusted`         | `string` | `float`     | The balance adjusted entitlement                                                         | `0.00`                                 |
| `used`                     | `string` | `float`     | The used entitlement                                                                     | `0.00`                                 |
| `expired`                  | `string` | `float`     | The expired entitlement                                                                  | `0.00`                                 |
| `requested`                | `string` | `float`     | The requested entitlement                                                                | `0.00`                                 |
| `rollovers`                | `array`  | -           | The rollovers entitlement                                                                | -                                      |
| `events`                   | `array`  | -           | The events entitlement                                                                   | -                                      |
| `total_entitlements`       | `string` | `float`     | The total entitlements entitlement                                                       | `0.00`                                 |
| `upcoming_accruals`        | `string` | `float`     | The upcoming accruals entitlement                                                        | `0.00`                                 |
| `accrual_amount`           | `string` | `float`     | The accrual amount entitlement                                                           | `0.00`                                 |
| `accrual_unit`             | `string` | -           | The accrual unit entitlement                                                             | -                                      |
| `future_events`            | `array`  | -           | The future events entitlement                                                            | -                                      |
| `past_tracking_periods`    | `array`  | -           | The past tracking periods entitlement                                                    | -                                      |
| `policy`                   | `object` | -           | Contains the details of the time-off policy that the entitlement is related to           | -                                      |
| `policy_allowance`         | `object` | -           | Contains the details of the time-off policy allowance that the entitlement is related to | -                                      |

## View policies assigned to a worker

Policies define common criteria for time off that can be applied to a set of workers. For example, a time off policy can determine how many days are granted, how they're accrued, and who can approve requests.

To view what policies are assigned to a worker, make a GET request to the [List Policies](https://developer.deel.com/reference/getpoliciesforprofile) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/time_offs/profile/{hris_profile_id}/policies?policy_type_name=Unpaid%20leave&policy_type_id=d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the path:

| Name              | Required | Type     | Format | Description                                            | Example                                |
| ----------------- | -------- | -------- | ------ | ------------------------------------------------------ | -------------------------------------- |
| `hris_profile_id` | `true`   | `string` | UUID   | The ID of the worker you want to view the policies for | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

In the query:

| Name               | Required | Type     | Format | Description                                                                                                   | Example                                |
| ------------------ | -------- | -------- | ------ | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `policy_type_name` | `false`  | `string` | -      | Enum to filter the results by one of the available types, based on their name. Values are expressed in ASCII. | `Paid%20leave`                         |
| `policy_type_id`   | `false`  | `string` | UUID   | Enum to filter the results by one of the available types, based on their ID.                                  | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

A successful response returns the available policy a specific worker and, optionally, matching any filtering criteria added in the request.

```json
{
  "policies": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "name": "Unpaid leave",
      "description": "Unpaid leave",
      "policy_type_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "tracking_unit": "YEAR",
      "tracking_unit_amount": 1,
      "tracking_cadence": "FIXED_DAY",
      "tracking_start_date": "2023-01-01T00:00:00Z",
      "created_at": "2023-09-14T10:13:53.942Z",
      "updated_at": "2023-09-14T18:22:06.629Z",
      "leave_type": "SHORT_TERM_LEAVE",
      "policy_type": {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Unpaid leave"
      },
      "time_off_types": [
        {
          "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "name": "Unpaid leave"
        }
      ]
    }
  ]
}
```

Where:

|  Name                  |  Type       |  Format                                   |  Description                                                                                                                              |  Example                               |
| ---------------------- | ----------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
|  `policies`            |  `array`    | -                                         | The list of time-off policies associated to a user and matching the filtering criteria. Each object inside the array represents a policy. | -                                      |
| `id`                   | `string`    | `uuid`                                    | The unique ID of the time-off policy                                                                                                      | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `name`                 | `string`    | -                                         | The name of the time-off policy                                                                                                           | `Unpaid leave`                         |
| `description`          | `string`    | -                                         | The description of the time-off policy                                                                                                    | `Unpaid leave`                         |
| `policy_type_id`       | `string`    | The unique ID of the time-off policy type | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0`                                                                                                    |                                        |
| `tracking_unit_amount` | `float`     | -                                         | The amount of time used to track time off.                                                                                                | `1`                                    |
| `tracking_cadence`     | `string`    | -                                         | The cadence of time off. Possible values are: `FIXED_DAY`, `ANNIVERSARY`.                                                                 | `FIXED_DAY`                            |
| `tracking_start_date`  | `date-time` | -                                         | The start of the time off. The format is ISO 8601.                                                                                        | `2023-01-01T00:00:00Z`                 |
| `created_at`           | `date-time` | -                                         | The time at which the time-off policy was created. The format is ISO 8601.                                                                | `2023-09-14T10:13:53.942Z`             |
| `updated_at`           | `date-time` | -                                         | The time at which the time-off policy was last updated. The format is ISO 8601.                                                           | `2023-09-14T18:22:06.629Z`             |
| `leave_type`           | `string`    | -                                         | The type of leave. Possible values are: `SHORT_TERM_LEAVE`, `LONG_TERM_LEAVE`.                                                            | `SHORT_TERM_LEAVE`                     |
| `time_off_types`       | `array`     | -                                         | The list of time off types associated with the policy.                                                                                    | -                                      |
| `policy_type`          | `object`    | -                                         | Object representing the policy type that the policy belongs to.                                                                           | -                                      |
| `policy_type.id`       | `float`     | -                                         | The ID of the policy type.                                                                                                                | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `policy_type.name`     | `string`    | -                                         | The name of the policy type.                                                                                                              | `Unpaid leave`                         |

## Manage time-off requests

The time-off API also provides endpoints for managing worker time-off requests.

### View time-off requests for a worker

The [List time-off requests](https://developer.deel.com/reference/gettimeoffsquery) endpoint allows you to retrieve a list of time-off requests for a specific worker.

To view time-off requests for a worker, make a GET request to the [List time-off requests](https://developer.deel.com/reference/gettimeoffsquery) endpoint.

```curl
curl --request GET \
     --url https://api-sandbox.demo.deel.com/rest/v2/time_offs/profile/{hris_profile_id} \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the path:

| Name              | Required | Type     | Format | Description                                                     | Example                                |
| ----------------- | -------- | -------- | ------ | --------------------------------------------------------------- | -------------------------------------- |
| `hris_profile_id` | `true`   | `string` | UUID   | The ID of the worker you want to view the time-off requests for | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

Optionally, you can include the following filtering criteria as query parameters:

| Name                  | Required | Type      | Format    | Description                                                                                           | Example                                    |
| --------------------- | -------- | --------- | --------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| `organization_id`     | `false`  | `string`  | UUID      | The ID of the organization that the time-off request belongs to                                       | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0`     |
| `status`              | `false`  | `array`   | -         | The status of the time-off request. Possible values are: `REQUESTED`, `APPROVED`, `REJECTED`, `USED`. | `["REQUESTED", "APPROVED"]`                |
| `start_date`          | `false`  | `string`  | date-time | The start date of the time-off request. The format is ISO 8601.                                       | `2023-01-01T00:00:00Z`                     |
| `end_date`            | `false`  | `string`  | date-time | The end date of the time-off request. The format is ISO 8601.                                         | `2023-01-01T00:00:00Z`                     |
| `approval_start_date` | `false`  | `string`  | date-time | The start date of the approval of the time-off request. The format is ISO 8601.                       | `2023-01-01T00:00:00Z`                     |
| `approval_end_date`   | `false`  | `string`  | date-time | The end date of the approval of the time-off request. The format is ISO 8601.                         | `2023-01-01T00:00:00Z`                     |
| `updated_start_date`  | `false`  | `string`  | date-time | The start date of the last update of the time-off request. The format is ISO 8601.                    | `2023-01-01T00:00:00Z`                     |
| `updated_end_date`    | `false`  | `string`  | date-time | The end date of the last update of the time-off request. The format is ISO 8601.                      | `2023-01-01T00:00:00Z`                     |
| `page_size`           | `false`  | `integer` | -         | The number of results per page. The range is from 5 to 200.                                           | `200`                                      |
| `policy_types`        | `false`  | `array`   | -         | The list of policy types that the time-off request belongs to.                                        | `["d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"]` |
| `next`                | `false`  | `string`  | -         | The next page of results.                                                                             | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0`     |

A successful response (`200`) returns the list of time-off requests for the specific worker.

```json
{
  "page": 0,
  "page_size": 100,
  "has_next_page": false,
  "data": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "recipient_profile": {
        "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requester_profile": {
        "client_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requested_at": "2024-10-08",
      "other_type_description": null,
      "description": "Gonna visit my crocodile for its birthday",
      "status": "APPROVED",
      "start_date": "2024-10-09",
      "end_date": "2024-10-10",
      "deduction_amount": null,
      "is_paid": true,
      "half_start_date": false,
      "half_end_date": false,
      "amount": 2,
      "contract_oid": "d3m0d3m",
      "time_off_percentage": null,
      "is_end_date_estimated": false
    },
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "recipient_profile": {
        "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requester_profile": {
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requested_at": "2024-10-08",
      "other_type_description": null,
      "description": "Visiting the fam",
      "status": "REQUESTED",
      "start_date": "2024-10-01",
      "end_date": "2024-10-03",
      "deduction_amount": null,
      "is_paid": true,
      "half_start_date": false,
      "half_end_date": false,
      "amount": 3,
      "contract_oid": "d3m0d3m",
      "time_off_percentage": null,
      "is_end_date_estimated": false
    }
  ]
}
```

Where:

| Name                                  | Type      | Format    | Description                                                                                                   | Example                                |
| ------------------------------------- | --------- | --------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `id`                                  | `string`  | UUID      | The unique ID of the time-off request                                                                         | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `recipient_profile.hris_profile_id`   | `string`  | UUID      | The ID of the worker for whom the time-off request was requested                                              | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `recipient_profile.organization_id`   | `string`  | UUID      | The ID of the organization that the worker for whom the time-off was requested belongs to                     | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requester_profile.client_profile_id` | `string`  | UUID      | The ID of the worker who requested the time-off. Sometimes this can be a different worker from the recipient. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requester_profile.organization_id`   | `string`  | UUID      | The ID of the organization that the worker who requested the time-off belongs to                              | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requested_at`                        | `string`  | date-time | The time at which the time-off request was requested. The format is YYYY-MM-DD.                               | `2024-10-08`                           |
| `other_type_description`              | `string`  | -         | If the time off type is not a predefined type, describes the time-off type                                    | `Special bonus`                        |
| `description`                         | `string`  | -         | The description of the time-off request                                                                       | `Visiting the fam`                     |
| `status`                              | `string`  | -         | The status of the time-off request. Possible values are: `REQUESTED`, `APPROVED`, `REJECTED`, `USED`.         | `REQUESTED`                            |
| `start_date`                          | `string`  | date-time | The start date of the time-off request. The format is YYYY-MM-DD.                                             | `2024-10-01`                           |
| `end_date`                            | `string`  | date-time | The end date of the time-off request. The format is YYYY-MM-DD.                                               | `2024-10-03`                           |
| `deduction_amount`                    | `float`   | -         | If the time off results in a salary deduction for the worker, the amount that will be deducted                | `null`                                 |
| `is_paid`                             | `boolean` | -         | Whether the time-off is paid or not                                                                           | `true`                                 |
| `half_start_date`                     | `boolean` | -         | Whether the start date of the time-off is half a day or not                                                   | `false`                                |
| `half_end_date`                       | `boolean` | -         | Whether the end date of the time-off is half a day or not                                                     | `false`                                |
| `amount`                              | `integer` | -         | The number of days of the time-off request                                                                    | `3`                                    |
| `contract_oid`                        | `string`  | UUID      | The ID of the contract that the time-off request belongs to                                                   | `d3m0d3m`                              |
| `time_off_percentage`                 | `float`   | -         | If the time off is expressed in percentage, the percentage of the time-off request                            | `null`                                 |
| `is_end_date_estimated`               | `boolean` | -         | Whether the end date of the time-off request is estimated or not                                              | `false`                                |

### Create a time-off request for a worker

Creating time-off requests from the API can be useful if you want to programmatically create them or if you want to sync the time-off requests between your platform and Deel. You can add time-off requests for the time-off types available in the platform or create custom time-off types.

To create a time-off request for a worker, make a POST request to the [Create Time Off Request](https://developer.deel.com/reference/create_time-off-request) endpoint.

```curl
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/time_offs \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "is_paid": true,
    "recipient_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "reason": "Gonna visit Jupiter",
    "start_date": "2024-10-06T00:00:00Z",
    "end_date": "2024-10-07T00:00:00Z",
    "time_off_type_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "description": "Gonna visit Jupiter"
  }
}
'
```

In the body:

| Name                   | Required | Type      | Format    | Description                                                                                                                                                                                    | Example                                |
| ---------------------- | -------- | --------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `is_paid`              | `false`  | `boolean` | -         | Whether the time-off is paid or not. Defaults to `false` when not provided.                                                                                                                    | `true`                                 |
| `recipient_profile_id` | `true`   | `string`  | UUID      | The ID of the worker you want to create a time-off request for                                                                                                                                 | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `reason`               | `false`  | `string`  | -         | The reason for the time-off request                                                                                                                                                            | `Gonna visit Jupiter`                  |
| `start_date`           | `true`   | `string`  | date-time | The start date of the time-off request. The format is ISO 8601.                                                                                                                                | `2024-10-06T00:00:00Z`                 |
| `end_date`             | `true`   | `string`  | date-time | The end date of the time-off request. The format is ISO 8601.                                                                                                                                  | `2024-10-07T00:00:00Z`                 |
| `time_off_type_id`     | `true`   | `string`  | UUID      | The ID of the time-off type you want to create a time-off request for. You can retrieve this ID from the [list policies](https://developer.deel.com/reference/getpoliciesforprofile) endpoint. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `description`          | `false`  | `string`  | -         | The description of the time-off request                                                                                                                                                        | `Gonna visit Jupiter`                  |

A successful response (`201`) returns the details of the time-off request that was just created.

```json
{
  "timeOffs": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "recipient_profile": {
        "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requester_profile": {
        "client_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requested_at": "2024-10-09T00:00:00.000Z",
      "other_type_description": "Describe something here",
      "description": "Gonna visit Jupiter",
      "reason": "Gonna visit Jupiter",
      "status": "USED",
      "start_date": "2024-09-29T00:00:00Z",
      "end_date": "2024-09-30T00:00:00Z",
      "deduction_amount": null,
      "is_paid": true,
      "half_start_date": false,
      "half_end_date": false,
      "amount": 1,
      "contract_oid": "d3m0d3m",
      "approved_at": "2024-10-09T00:00:00.000Z",
      "created_at": "2024-10-09T09:27:34.858Z",
      "updated_at": "2024-10-09T09:27:34.858Z",
      "time_off_dailies": [
        {
          "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "time_off_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "amount": 0,
          "date": "2024-09-29T00:00:00Z",
          "type": "NON_WORKING_DAY",
          "description": null,
          "created_at": "2024-10-09T09:27:34.858Z",
          "updated_at": "2024-10-09T09:27:34.858Z"
        },
        {
          "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "time_off_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "amount": 1,
          "date": "2024-09-30T00:00:00Z",
          "type": "WORKING_DAY",
          "description": null,
          "created_at": "2024-10-09T09:27:34.858Z",
          "updated_at": "2024-10-09T09:27:34.858Z"
        }
      ],
      "time_off_percentage": null,
      "is_end_date_estimated": false
    }
  ]
}
```

Where:

| Name                                  | Type      | Format    | Description                                                                                                   | Example                                |
| ------------------------------------- | --------- | --------- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `id`                                  | `string`  | -         | The unique ID of the time-off request                                                                         | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `recipient_profile.hris_profile_id`   | `string`  | -         | The ID of the worker for whom the time-off request was requested                                              | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `recipient_profile.organization_id`   | `string`  | -         | The ID of the organization that the worker for whom the time-off was requested belongs to                     | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requester_profile.client_profile_id` | `string`  | -         | The ID of the worker who requested the time-off. Sometimes this can be a different worker from the recipient. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requester_profile.organization_id`   | `string`  | -         | The ID of the organization that the worker who requested the time-off belongs to                              | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `requested_at`                        | `string`  | date-time | The time at which the time-off request was requested. The format is ISO 8601.                                 | `2024-10-09T09:27:34.858Z`             |
| `other_type_description`              | `string`  | -         | If the time off type is not a predefined type, describes the time-off type                                    | `null`                                 |
| `description`                         | `string`  | -         | The description of the time-off request                                                                       | `Describe something here`              |
| `status`                              | `string`  | -         | The status of the time-off request. Possible values are: `REQUESTED`, `APPROVED`, `REJECTED`, `USED`.         | `USED`                                 |
| `start_date`                          | `string`  | date-time | The start date of the time-off request. The format is ISO 8601.                                               | `2024-10-10T00:00:00Z`                 |
| `end_date`                            | `string`  | date-time | The end date of the time-off request. The format is ISO 8601.                                                 | `2024-10-10T00:00:00Z`                 |
| `deduction_amount`                    | `float`   | -         | The amount of money to be deducted from the worker's salary.                                                  | `100.0`                                |
| `is_paid`                             | `boolean` | -         | Whether the time-off is paid or not.                                                                          | `true`                                 |
| `half_start_date`                     | `boolean` | -         | Whether the start date of the time-off is a half-day.                                                         | `false`                                |
| `half_end_date`                       | `boolean` | -         | Whether the end date of the time-off is a half-day.                                                           | `false`                                |
| `amount`                              | `string`  | -         | The number of days of the time-off request.                                                                   | `2`                                    |
| `time_off_dailies`                    | `array`   | -         | A list of objects containing details for each day of the time-off request.                                    |  \-                                    |
| `time_off_percentage`                 | `float`   | -         | The percentage of the time-off request that is paid.                                                          | `10.0`                                 |
| `is_end_date_estimated`               | `boolean` | -         | Whether the end date of the time-off request is estimated.                                                    | `false`                                |

Note down the following parameters, as they're required to update or delete the time-off requests later:

- `recipient_profile_id`
- `start_date`
- `end_date`
- `id`

### Update a time-off request for a worker

Updating time-off requests is useful to change its dates, other details, or its approval status.

To update a time-off request, make a `PATCH` request to the [Update time-off request](https://developer.deel.com/reference/updatetimeoff) endpoint and include in the body the information that you want to update.

```curl
curl --request PATCH \
     --url https://api-sandbox.demo.deel.com/rest/v2/time_offs/{time_off_id} \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "recipient_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "start_date": "2024-10-06T00:00:00Z",
    "end_date": "2024-10-07T00:00:00Z",
    "time_off_type_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
    "description": "Gonna visit Saturn"
  }
}
'
```

In the path:

| Name           | Required  | Type   | Format                                                                                           | Description                            | Example |
| -------------- | --------- | ------ | ------------------------------------------------------------------------------------------------ | -------------------------------------- | ------- |
|  `time_off_id` |  `string` | `uuid` | The unique ID of the time-off request. It's returned when you create a time-off request as `id`. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` | -       |

In the body:

| Name                   | Required | Type     | Format    | Description                                                     | Example                                |
| ---------------------- | -------- | -------- | --------- | --------------------------------------------------------------- | -------------------------------------- |
| `recipient_profile_id` | `true`   | `string` | `uuid`    | The unique ID of the worker                                     | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `start_date`           | `true`   | `string` | date-time | The start date of the time-off request. The format is ISO 8601. | `2024-10-10T00:00:00Z`                 |
| `end_date`             | `true`   | `string` | date-time | The end date of the time-off request. The format is ISO 8601.   | `2024-10-10T00:00:00Z`                 |
| `time_off_type_id`     | `true`   | `string` | `uuid`    | The unique ID of the time-off type                              | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |
| `description`          | `false`  | `string` | -         | The description of the time-off request                         | `Gonna visit Saturn`                   |

Other optional parameters aren't shown in the example. Check [#create-a-time-off-request-for-a-worker](#create-a-time-off-request-for-a-worker) for more information about the optional parameters.

A successful response (`200`) returns the details of the updated time-off request.

```json
{
  "timeOffs": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "recipient_profile": {
        "hris_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requester_profile": {
        "client_profile_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "organization_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
      },
      "requested_at": "2024-10-09T00:00:00.000Z",
      "other_type_description": "Describe something here",
      "description": "Gonna visit Saturn",
      "reason": "Gonna visit Jupiter",
      "status": "USED",
      "start_date": "2024-10-06T00:00:00Z",
      "end_date": "2024-10-07T00:00:00Z",
      "deduction_amount": null,
      "is_paid": true,
      "half_start_date": false,
      "half_end_date": false,
      "amount": 1,
      "contract_oid": "d3m0d3m",
      "approved_at": "2024-10-09T00:00:00.000Z",
      "created_at": "2024-10-09T09:27:34.858Z",
      "updated_at": "2024-10-09T09:27:34.858Z",
      "time_off_dailies": [
        {
          "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "time_off_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "amount": 0,
          "date": "2024-10-06T00:00:00Z",
          "type": "NON_WORKING_DAY",
          "description": null,
          "created_at": "2024-10-09T09:27:34.858Z",
          "updated_at": "2024-10-09T09:27:34.858Z"
        },
        {
          "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "time_off_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
          "amount": 1,
          "date": "2024-10-07T00:00:00Z",
          "type": "WORKING_DAY",
          "description": null,
          "created_at": "2024-10-09T09:27:34.858Z",
          "updated_at": "2024-10-09T09:27:34.858Z"
        }
      ],
      "time_off_percentage": null,
      "is_end_date_estimated": false
    }
  ]
}
```

### Delete a time-off request for a worker

Deleting a time-off request requires the ID of the time-off request you want to delete. You can find the ID in the response when you (#create-a-time-off-request-for-a-worker) or, alternatively, you can find it by [viewing the time-off requests of a worker](#view-time-off-requests-for-a-worker).

To delete a time-off request for a worker, make a `DELETE` request to the [Delete time-off request](https://developer.deel.com/reference/deletetimeoff) endpoint.

```curl
curl --request DELETE \
     --url https://api-sandbox.demo.deel.com/rest/v2/time_offs/{time_off_id} \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

In the path:

| Name          | Required | Type   | Format | Description                                                                                                                                    | Example                                |
| ------------- | -------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `time_off_id` | true     | string | -      | The ID of the time-off request. Retrieve it from the [List time-off requests](https://developer.deel.com/reference/gettimeoffsquery) endpoint. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

A successful response (`204`) confirms that the entry is deleted from the system.

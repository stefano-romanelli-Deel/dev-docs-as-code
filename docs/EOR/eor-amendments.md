---
title: "EOR contract amendments"
slug: "eor-amendments"
excerpt: ""
hidden: false
createdAt: "Thu Mar 27 2025 10:51:16 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Aug 19 2025 14:35:20 GMT+0000 (Coordinated Universal Time)"
---
The EOR contract amendment API lets you update contract terms through a structured approval process that follows predefined compliance rules.

An amendment is a change to one or more contract terms, referred to as data points, such as employment type, job title, scope, or salary. Instead of modifying the original contract document, the amendment is issued as a separate addendum to the employment agreement. The contract entity in the database, including its ID, remains the same. Only specific values, like salary, are updated with a new effective date.

You or Deel can initiate an amendment. The process includes multiple steps and requires approval from both you and the employee. Modification and approval rules vary based on the amended data point and country-specific regulations.

## Amendment flows

Amendments can be initiated by you or or by Deel. The steps an amendment goes through are different depending on who initiates it.

### Scenario when you requests an amendment

1. Create an amendment using the [Upsert amendment](https://developer.deel.com/reference/upsertamendment) endpoint.
2. Confirm the amendment.
3. Depending on the amendment content, the change may be applied immediately or require approval from Deel and the employee. The API response includes the current amendment status.
4. If the amendment is not applied immediately, Deel reviews it and sends it to the employee for signing.
5. The employee reviews the amendment and signs it using the [Sign amendment](https://developer.deel.com/reference/acceptamendmentemployee) endpoint.

### Scenario when Deel requests an amendment

1. Deel creates an amendment.
2. You review the amendment and either accepts, using the [Accept amendment](https://developer.deel.com/reference/acceptamendmentclient) endpoint, or cancels, using [Cancel amendment](https://developer.deel.com/reference/cancelamendment).
3. If accepted, the employee reviews and signs using the [Sign amendment](https://developer.deel.com/reference/acceptamendmentemployee) endpoint.

### When does deel create amendments?

Deel may create amendments in the following cases:

- At your request. When you ask for a change that requires Deel involvement.
- To ensure compliance. When a contract update is needed to meet legal or regulatory requirements.
- For restricted changes. Some updates are only available through admin amendments due to system limitations or internal policies.

### Amendment effective date

The effective date is the date when the amendment becomes active.  
This date determines when the changes in the amendment will take effect. It also determines when those changes appear in payroll, invoices, or other downstream processes.

#### Why it works this way

Different amendment fields trigger different business logic. Based on what you are changing, Deel dynamically calculates a valid effective date range.

To support this flexibility, Deel exposes the [Effective Date Limitations](https://developer.deel.com/reference/getEffectiveDateLimitations) API that you need to call to retrieve the valid effective date limits for a specific amendment. This ensures that:

- Your system always works with the correct date limits.
- Deel applies the correct validations automatically based on the amendment content, helping you avoid false validations or user errors.
- You can choose to show or disable the effective date field in your UI.
- You can apply validation rules or pre-fill values based on internal workflows.

> 📘 Amendments on contracts that are not yet active can't have an effective date.

#### When to fetch effective date limits

You must fetch the effective date limitations:

- Immediately after creating or updating an amendment.
- Before setting or submitting the effective date.
- Before confirming the amendment, if any changes were made after fetching the last effective date.

> 🚧 Effective date validation depends on content
> 
> The valid effective date range is based on the specific changes in the amendment. Always fetch the date limits only after all changes to the amendment are finalized.

#### What happens based on the effective date

| Efective date                       | What happens                                                                                                                                              |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Effective date in the future        | The amendment gets an `upcoming` status. It won’t affect contract values immediately.                                                                     |
| Effective date today or in the past | The amendment becomes `active` as soon as it’s processed and signed.                                                                                      |
| Effective date not provided         | The amendment becomes `active` immediately after signing are completed,  Deel uses the date when all parties confirm the amendment as the effective date. |

Amendments in `upcoming` status do not affect payroll, invoicing, or contract terms until they are activated by Deel’s internal job on the effective date.

#### High-level flow

The diagram below shows how the effective date influences the amendment lifecycle, from creation to activation:

![](https://files.readme.io/4f037549d00c76b8bb06f5cf34d45ff1d7aa2326da0d3fb44005358ab8f162af-amendment-effective-date-flow.png)


#### UI behavior: is_hidden and is_disabled

When you fetch effective date limitations, the response includes flags that guide you in rendering the field in your UI.

| Field         | Client-side behavior                                                                                                      |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `is_hidden`   | (Optional) Suggests that the field may be hidden from the user interface. You may decide whether to follow this behavior. |
| `is_disabled` | If true, the field should not be editable. You must use the default value provided.                                       |

> 📘 Hiding the field
> 
> If your use case involves applying an automatic default effective date, such as aligning it with the start of the payroll cycle, hiding the field might improve user experience.

#### Validation rules

The validation logic for effective dates ensures that all amendments respect configuration limits, providing flexibility while preventing invalid data entry.

| Scenario                                         | Requirement                                                                                    |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| `is_disabled = true` and `is_hidden = true`      | Field must not be included in the request.                                                     |
| `is_disabled = true` and default date is present | Field must exactly match the default effective date.                                           |
| `min`, `max`, or `default` is present            | A valid effective date must be provided and must fall within range.                            |
| No limits defined                                | Field is optional. System will automatically set it to when all parties confirm the amendment. |

##### Validation runs at two points

- On create or update. Runs when you send the effective date in the request payload.
- On confirmation. The effective date is always validated when the amendment is confirmed, regardless of its draft status.

> 📘 Draft amendments are validated only when you provide an effective date.

### Webhook events

Webhooks are triggered at key stages of the amendment process and provide automatic updates on status changes.

| Event                              | Description                                                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EOR_AMENDMENT_V2_IN_REVIEW`       | Triggered when you create an amendment. Sent after the amendment is confirmed.                                                                      |
| `EOR_AMENDMENT_V2_CLIENT_SIGN`     | Triggered when Deel creates an amendment. Sent after a Deel admin creates the amendment.                                                            |
| `EOR_AMENDMENT_V2_EMPLOYEE_SIGN`   | Triggered when you accept an amendment created by Deel. Sent after you review and accept the amendment.                                             |
| `EOR_AMENDMENT_V2_CLIENT_ACTIVE`   | Triggered when an amendment becomes active. Sent once all necessary approvals are complet.                                                          |
| `EOR_AMENDMENT_V2_CLIENT_REJECTED` | Triggered when an amendment is canceled. Sent when a Deel admin rejects the amendment.                                                              |
| `EOR_AMENDMENT_V2_CLIENT_VOID`     | Triggered when an amendment is voided. Sent when the void deadline has passed for an in-progress amendment, meaning it can no longer become active. |

### Amendment types

Each amendment has a type that determines how it is processed. The type is returned in the response when creating or updating an amendment. It is based on the amendment settings and the data points being amended.

An amendment can have one of the following types:

- `INSTANT`: Activated immediately after you confirm it. No Deel review or employee signature is required.
- `AUTOMATED`: Activated once the employee signs it. Deel review is not required.
- `LEGAL` or `OPS`: Requires Deel review because at least one data point is set to require internal review. The difference between `LEGAL` and `OPS` is internal only and relates to how Deel conducts the review. For example, the review may involve document preparation. After Deel completes the review, the amendment is sent to the employee for review and signature. The amendment is activated once the employee signs it.
- `DISABLED`: Contains at least one data point that is restricted from being changed by the amendment settings.
- `CUSTOM`: Manually created by a Deel admin.

> 📘 If at least one data point requires Deel review (`LEGAL` or `OPS`), the amendment type is set to match.  
> Data points that would otherwise be `INSTANT` or `AUTOMATED` follow the same review and activation flow as `LEGAL` or `OPS` amendments.

### Examples

#### Example 1: Germany (instant amendment)

In this Germany example, both `holidays` (holiday increase) and `timeOffType` changes are instant. They are activated once the amendment becomes active.  

The amendment `type` is `INSTANT`. In `items`, each data point also has `INSTANT` as its type:  

```json
{
  "type": "INSTANT",
  "items": [
    {
      "data_point": "holidays",
      "id": "59d9a2d5-9ea0-4f7f-8ac0-1db66e62d9fa",
      "item": "holidaysIncrease",
      "type": "INSTANT",
      "previous_value": "6",
      "new_value": "12"
    },
    {
      "data_point": "timeOffType",
      "id": "78743852-4dea-4b7c-bbac-44828a7d9b97",
      "item": "timeOffType",
      "type": "INSTANT",
      "previous_value": "STANDARD",
      "new_value": "SPECIFIC"
    }
  ]
}
```

#### Example 2: Greece (legal amendment)

For Greece, the same data points require Deel review because one of the items has the `LEGAL` type:

```json
{
  "type": "LEGAL",
  "items": [
    {
      "data_point": "holidays",
      "id": "f783003f-777f-425a-9a14-faf6457b7585",
      "item": "holidaysIncrease",
      "type": "INSTANT",
      "previous_value": "6",
      "new_value": "10"
    },
    {
      "data_point": "timeOffType",
      "id": "d9dffd0a-6443-4992-9aa7-d859bd9d4d4d",
      "item": "timeOffType",
      "type": "LEGAL",
      "previous_value": "STANDARD",
      "new_value": "SPECIFIC"
    }
  ]
}
```

### Amendment statuses

Amendment statuses are returned in an array within the API response. Check the most recent status to determine the amendment's current state.

| Status                                                            | Description                                                                |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `Draft`                                                           | The amendment is in draft state and can still be modified.                 |
| `Active`                                                          | The amendment is active.                                                   |
| `Cancelled`                                                       | The amendment is canceled.                                                 |
| `AwaitingSignature.SOW.PendingClientSignature`                    | Waiting for your acceptance. Used when Deel created the amendment.         |
| `AwaitingSignature.EA.PendingEmployeeSignature`                   | Waiting for employee signature. Used when you and Deel have accepted.      |
| `PreparingDocuments.AmendmentRequested.EA.PendingDocumentSubmit`  | Waiting for Deel review. Used when the amendment type is `LEGAL` or `OPS`. |
| `PreparingDocuments.AmendmentRequested.SOW.PendingDocumentSubmit` | Waiting for Deel review. Used when the amendment type is `LEGAL` or `OPS`. |

#### Example: Amendment status array explained

Below is an example of an amendment status array from the API response. In this example:

- The amendment is in the `PreparingDocuments` phase.  
- The request is logged as `PreparingDocuments.AmendmentRequested`.  
- The amendment is waiting for Deel review (`PreparingDocuments.AmendmentRequested.SOW.PendingDocumentSubmit`). Further actions are required before it can proceed.  

```json
[
  {
    "name": "PreparingDocuments",
    "friendly_name": "Preparing documents",
    "_amendment_flow_status": {
      "created_at": "2025-03-19T17:15:02.053Z"
    }
  },
  {
    "name": "PreparingDocuments.AmendmentRequested",
    "friendly_name": "Amendment requested",
    "_amendment_flow_status": {
      "created_at": "2025-03-19T17:15:02.053Z"
    }
  },
  {
    "name": "PreparingDocuments.AmendmentRequested.SOW.PendingDocumentSubmit",
    "friendly_name": "Awaiting review",
    "_amendment_flow_status": {
      "created_at": "2025-03-19T17:15:02.053Z"
    }
  }
]
```

## Retrieve contract information

To retrieve available amendment settings, you first need the contract ID. Use the [List of contracts](https://developer.deel.com/reference/listofcontracts) endpoint to retrieve your contracts. You can filter and sort the list to find the correct `contractId`. 

Use the returned `contractId` in the next step.

```shell
curl --location -g --request GET '{{host}}/rest/v2/contracts?limit=2&sort_by=worker_name&order_direction=desc' \
--header 'Authorization: Bearer {{token}}'
```

## Retrieve amendment settings

Once you have a contract ID, use it to retrieve valid amendment settings. These are based on the contract and country-specific rules.

Use the `contract_oid` path parameter to fetch available data points and rules. This returns all configurable data points and validation logic.

```shell
curl --location -g --request GET '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/amendment-settings' \
--header 'Authorization: Bearer {{token}}'
```

### Example response

```json
[
  {
    "data_point": "noticePeriodType",
    "rules": [
      {
        "nullable": false,
        "is_editable": true,
        "possible_options": [
          "STANDARD",
          "CUSTOM"
        ],
        "requires": {
          "employment_type": "Full-time"
        }
      },
      {
        "nullable": false,
        "is_editable": true,
        "possible_options": [
          "STANDARD",
          "CUSTOM"
        ],
        "requires": {
          "employment_type": "Part-time"
        }
      }
    ]
  }
]
```

## Understand how amendment settings work

The response for `amendment-settings` includes a list of configurable contract fields. Each field is described by a `data_point` object that defines how it can be changed.

Key elements:

- Each `data_point` represents an attribute in the contract that may be amended.
- The `requires` object defines conditions that must be met for the change to be allowed. All fields in `requires` must match either the current contract or the amendment request.
- Numeric fields include `min` and `max` constraints.
- `possible_options` lists the allowed values for the data point.
- `is_editable` indicates if the field can be updated. If a field is not editable, the reason is not returned in the API. It may be due to country rules, amendment restrictions, or other pending amendments, for example, currency.
- `additional_details` may include validation notes or business constraints.
- Date fields can include `min_date` and `max_date`, formatted as `YYYY-MM-DD`, for example, `2025-06-17`.

### Examples of amendment rules

These examples show how the API applies rules to control when you can update specific fields.

1. **Require a field in the contract or request:**

You can only apply this rule if the contract or amendment request includes `contract_term: "Definite"`.

```json
{
    "nullable": false,
    "is_editable": true,
    "min_date": "2025-06-02",
    "requires": {
        "contract_term": "Definite"
    }
}
```

2. **Employment type restriction:**

You can set `employment_type` to `Full-time` only if `contract_term` is `Indefinite`.

```json
{
    "nullable": false,
    "is_editable": true,
    "possible_options": ["Full-time"],
    "requires": { "contract_term": "Indefinite" }
}
```

3. **Numeric constraints:**

This rule allows minimum and maximum values when `employment_type` is `Full-time`.

```json
{
    "nullable": false,
    "is_editable": true,
    "min": 6,
    "max": 12,
    "requires": { "employment_type": "Full-time" }
}
```

4. **Use external validation**

This rule ensures that validation is handled externally.

```json
{
    "nullable": false,
    "is_editable": true,
    "external_validation": true
}
```

## Create or update a draft amendment

You can create or update an amendment by specifying the _contract\_oid_.

If you include an ID, the API updates the draft amendment with that ID. If you it, the API creates a new draft.

```shell
curl --location -g --request POST '{{host}}/rest/v2/eor/amendments/{{contract_oid}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": {
        "time_off_type": "SPECIFIC",
        "holidays": 109082,
        "employment_type": "Part-time",
        "id": "5bbd6aa1-4f00-494e-b031-73c066140b4e"
    }
}'
```

## Validation errors and disabled amendments

If your amendment request fails validation, the API returns a `400 Bad Request` response.

The response includes details about any validation errors and disabled data points.

### Example response

```json
{
  "validation_error": [
    {
      "error": "The minimum holidays for NG is 6 day(s)",
      "item": "holidays",
      "previous_value": "6",
      "new_value": "2"
    }
  ],
  "disabled_amendments": [
    {
      "type": "DISABLED",
      "previous_value": "STANDARD",
      "new_value": "SPECIFIC",
      "data_point": "timeOffType",
      "error": "timeOffType is disabled in country Nigeria"
    }
  ]
}
```

### Response properties

#### `validation_error` (array)

Lists validation errors found in the amendment request.

- `error` _(string)_: Describes the failed validation rule  
  Example: `"The minimum holidays for NG is 6 day(s)"`
- `item` _(string)_: Name of the data point with the error  
  Example: `"holidays"`
- `previous_value` _(string)_: Previous valid value value before the amendment  
  Example: `"6"`
- `new_value` _(string)_: Value submitted in the amendment that caused the validation error  
  Example: `"2"`

***

#### `disabled_amendments` (array)

Lists data points that can't be amended due to restrictions.

- `type` _(string)_: Type of amendment restriction. It is set to `"DISABLED"`  
  Example: `"DISABLED"`
- `previous_value` _(string)_: Previous valid value before the attempted change  
  Example: `"STANDARD"`
- `new_value` _(string)_: Value that is not allowed  
  Example: `"SPECIFIC"`
- `data_point` _(string)_: Field that is disabled for the amendment  
  Example: `"timeOffType"`
- `error` _(string)_: Reason the amendment is disabled  
  Example: `"timeOffType is disabled in country Nigeria"`

***

#### `status` _(integer)_

The HTTP status code for the response.  
Example: `400`

## Confirm an amendment

To confirm a draft amendment, use the _contract\_oid_ and _amendment\_flow\_id_. Only draft amendment can be confirmed.

After confirmation, the flow depends on the amendment type. If the type is instant, the amendment becomes active immediately. If it requires signatures, Deel or the employee must approve it first.

```shell
curl --location -g --request PUT '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}/actions/confirm' \
--header 'Authorization: Bearer {{token}}'
```

## Validate data points

To validate specific data points within an EOR contract that has `external_validation:true`, use the _oid_ parameter.

```shell
curl --location -g --request POST '{{host}}/rest/v2/eor/amendments/:contract_oid/validate \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "jobTitle": "Software Engineer",
    "scope": "Test scope",
}'
```

## Cancel an amendment

To cancel an amendment, use the _contract\_oid_ and _amendment\_flow\_id_. You can cancel an amendment any time before the employee signs it. After cancellation, you can delete it if needed.

```shell
curl --location -g --request DELETE '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}' \
--header 'Authorization: Bearer {{token}}'
```

## Download amendment PDF

Retrieve the Statement of Work (EA) document download link for a confirmed amendment. This is only available after the amendment is confirmed and while the contract is in progress.

The download link expires after 15 minutes.

```shell
curl --location -g --request GET '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}/pdf' \
--header 'Authorization: Bearer {{token}}'
```

## Accept or reject an amendment

Use this endpoint to accept or reject an amendment submitted by a Deel admin.

After acceptance, the amendment either becomes active immediately or moves to the signature step, depending on its type.

```shell
curl --location -g --request PUT '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}/actions/accept' \
--header 'Authorization: Bearer {{token}}'
```

## Sign an approved amendment

An employee can sign an amendment approved by both the client and admin. After signing, the amendment becomes active.

```shell
curl --location -g --request PUT '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}/actions/sign' \
--header 'Authorization: Bearer {{token}}'
```

## Retrieve list of amendments

Retrieve all amendments for a specific contract.

```shell
curl --location -g --request GET '{{host}}/rest/v2/eor/amendments/{{contract_oid}}' \
--header 'Authorization: Bearer {{token}}'
```

## Retrieve a specific amendment

Retrieve details of a specific amendment

```shell
curl --location -g --request GET '{{host}}/rest/v2/eor/amendments/{{contract_oid}}/{{amendment_flow_id}}' \
--header 'Authorization: Bearer {{token}}'
```

## Use external APIs for specific amendments

Some data points require additional API calls to retrieve or validate values before you include them in an amendment request.

### Amend seniorityId

To amend `seniorityId`, use the following API to retrieve the available seniority levels:

[Get Seniority List](https://developer.deel.com/reference/getsenioritylist)

The retrieved `seniorityId` should be included in the amendment request.

### Amend jobTitle or scope

To amend `jobTitle` or `scope`, validate the values first using the **Validate Data Points** API.

### Effective date limits for amendment

Follow these steps to use effective date limitations:

1. Create an amendment using the [Create Amendment endpoint](https://developer.deel.com/reference/upsertamendment) endpoint.
2. Call the [Get Effective Date Limitations](https://developer.deel.com/reference/getEffectiveDateLimitations) endpoint.
3. Use the returned rules to set the effective date in the UI.
4. (Optional) If required, submit the amendment with an effective date.

### Probation period settings

The `probationPeriod` data point supports multiple rule types and constraints, depending on the contract type and country-specific settings.

#### Rule-based configuration

Set the probation period based on a rule and cap value:

```json
{
  "rule": "ONE_QUARTER_OF_CONTRACT_DURATION",
  "cap": 100
}
```

#### Tenure-based configuration

Other configurations define probation periods based on the employee’s expected duration of employment:

```json
{
  "minEmploymentDuration": 6,
  "maxEmploymentDuration": 12,
  "employmentDurationType": "MONTH",
  "probationPeriod": 90
}
```

### General rules

- For `Indefinite` contracts, the probation period must be between 90 and 180 days, regardless of whether the employment type is Full-time or Part-time.
- For `Definite` contracts, the minimum probation period is 20 days. The maximum value is calculated dynamically.

### Dynamic calculation for Definite contracts

When the contract term is `Definite`,  the API calculates the maximum probation period using `contractDurationInDays` and the country-specific rule `eorCountryData.maxProbationTypeForDefinite`.

Available rule types:

`HALF_OF_CONTRACT_DURATION`

- Maximum probation period is half the contract duration.  
  Example: A 180-day contract allows up to 180 / 2 = 90 days.

`ONE_QUARTER_OF_CONTRACT_DURATION`

- Maximum probation period is one-quarter of the contract duration.  
  Example: A 180-day contract allows up to 180 / 4 = 45 days.

`ONE_THIRD_OF_CONTRACT_DURATION` (default)

- If no country rule is defined, the fallback is one-third of the contract duration.  
  Example: A 180-day contract allows up to 180 / 3 = 60 days.

### Cap on maximum probation period

The API may apply a cap to limit the maximum probation period, even when it uses a duration-based rule.

- If `additional_details` includes a cap value, the system uses the lower value between the calculated maximum and the cap.
- The cap applies only when the probation period is based on:
  - `HALF_OF_CONTRACT_DURATION`
  - `ONE_QUARTER_OF_CONTRACT_DURATION`
  - `ONE_THIRD_OF_CONTRACT_DURATION`

**Example**:

If the contract duration is 180 days and the rule is `HALF_OF_CONTRACT_DURATION`, the calculated maximum is 90 days. However, if a cap of 60 days exists in `additional_details`, the maximum probation period is limited to 60 days.

This ensures that the probation period for Definite contracts remains proportional to the contract length  
while complying with country-specific regulations and additional constraints.

> 📘 `probationPeriod` settings for `Definite` contracts only support the rule-based configurations listed above.

### Settings for notice period after probation rules

The `noticePeriodAfterProbation` data point follows specific rules based on `employment_type` and `notice_period_type`.

### General rules

These rules apply only when notice_period_type is set to `CUSTOM`.

- The `min` and `max` notice period values range from 0 to 12 weeks.
- Rules vary for `Full-time` and `Part-time` employees.
- The notice period _before_ probation must always be shorter than the notice period _after_ probation.

### Tenure-based notice period

Only `noticePeriodAfterProbation` supports tenure-based rules.  
These rules depend on the contract duration and define different notice period values for different tenure ranges.

### Example rule definition

```json
{
  "data_point": "noticePeriodAfterProbation",
  "rules": [
    {
      "nullable": true,
      "min": 0,
      "max": 12,
      "is_editable": true,
      "requires": {
        "notice_period_type": "CUSTOM",
        "employment_type": "Full-time"
      },
      "additional_details": {
        "tenure_based_rules": [
          {
            "maxEmploymentDuration": 24,
            "minEmploymentDuration": 12,
            "noticeValue": 30,
            "employmentDurationType": "MONTH"
          },
          {
            "maxEmploymentDuration": 34,
            "minEmploymentDuration": 25,
            "noticeValue": 50,
            "employmentDurationType": "MONTH"
          }
        ],
        "time_unit": "WEEK",
        "note": "Notice period before probation should be less than notice period after probation"
      }
    },
    {
      "nullable": false,
      "min": 0,
      "max": 12,
      "is_editable": true,
      "requires": {
        "notice_period_type": "CUSTOM",
        "employment_type": "Part-time"
      },
      "additional_details": {
        "time_unit": "WEEK",
        "note": "Notice period before probation should be less than notice period after probation"
      }
    }
  ]
}
```

## How to create and process amendment with examples

1. Retrieve Amendment Settings

```shell
curl --location --request GET '{{host}}/rest/v2/eor/amendments/374xe7e/amendment-settings' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{token}}' \
--data '{
    "data": {
        "timeOffType": "SPECIFIC",
        "holidays": 24
    }
}'
```

Response

```json
{
  "data": [
    {
      "data_point": "contractTerm",
      "rules": [
        {
          "nullable": false,
          "is_editable": false,
          "possible_options": [
            "Definite",
            "Indefinite"
          ]
        }
      ]
    },
    {
      "data_point": "employmentType",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "possible_options": [
            "Full-time"
          ]
        }
      ]
    },
    {
      "data_point": "endDate",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "min_date": "2025-06-23",
          "requires": {
            "contract_term": "Definite"
          }
        }
      ]
    },
    {
      "data_point": "holidays",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "min": 6,
          "requires": {
            "employment_type": "Full-time",
            "time_off_type": "SPECIFIC"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "min": 6,
          "requires": {
            "employment_type": "Part-time",
            "time_off_type": "SPECIFIC"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "min": 6,
          "max": 6,
          "requires": {
            "employment_type": "Full-time",
            "time_off_type": "STANDARD"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "min": 6,
          "max": 6,
          "requires": {
            "employment_type": "Part-time",
            "time_off_type": "STANDARD"
          }
        }
      ]
    },
    {
      "data_point": "jobTitle",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "external_validation": true
        }
      ]
    },
    {
      "data_point": "noticePeriodAfterProbation",
      "rules": [
        {
          "nullable": true,
          "min": 4,
          "max": 4,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Indefinite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation",
            "tenure_based_rules": [
              {
                "min_employment_duration": 1,
                "max_employment_duration": 4,
                "employment_duration_type": "MONTH",
                "notice_value": 6
              },
              {
                "min_employment_duration": 5,
                "max_employment_duration": 9,
                "employment_duration_type": "MONTH",
                "notice_value": 10
              }
            ]
          },
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Definite",
            "employment_type": "Full-time"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Indefinite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Definite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 4,
          "max": 4,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Indefinite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation",
            "tenure_based_rules": [
              {
                "min_employment_duration": 1,
                "max_employment_duration": 4,
                "employment_duration_type": "MONTH",
                "notice_value": 6
              },
              {
                "min_employment_duration": 5,
                "max_employment_duration": 9,
                "employment_duration_type": "MONTH",
                "notice_value": 10
              }
            ]
          },
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Definite",
            "employment_type": "Part-time"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Indefinite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Definite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        }
      ]
    },
    {
      "data_point": "noticePeriodDuringProbation",
      "rules": [
        {
          "nullable": true,
          "min": 1,
          "max": 1,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Indefinite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 2,
          "max": 2,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Definite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Indefinite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Definite",
            "employment_type": "Full-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 1,
          "max": 1,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Indefinite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 2,
          "max": 2,
          "is_editable": true,
          "requires": {
            "notice_period_type": "STANDARD",
            "contract_term": "Definite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Indefinite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        },
        {
          "nullable": true,
          "min": 0,
          "max": 12,
          "is_editable": true,
          "requires": {
            "notice_period_type": "CUSTOM",
            "contract_term": "Definite",
            "employment_type": "Part-time"
          },
          "additional_details": {
            "time_unit": "WEEK",
            "note": "Notice period before probation should be less than notice period after probation"
          }
        }
      ]
    },
    {
      "data_point": "noticePeriodType",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "possible_options": [
            "STANDARD",
            "CUSTOM"
          ],
          "requires": {
            "employment_type": "Full-time"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "possible_options": [
            "STANDARD",
            "CUSTOM"
          ],
          "requires": {
            "employment_type": "Part-time"
          }
        }
      ]
    },
    {
      "data_point": "probationPeriod",
      "rules": [
        {
          "nullable": true,
          "min": 90,
          "max": 180,
          "is_editable": true,
          "requires": {
            "employment_type": "Full-time",
            "contract_term": "Indefinite"
          }
        },
        {
          "nullable": true,
          "min": 90,
          "max": 180,
          "is_editable": true,
          "requires": {
            "employment_type": "Part-time",
            "contract_term": "Indefinite"
          }
        },
        {
          "nullable": true,
          "min": 90,
          "max": 0,
          "is_editable": true,
          "requires": {
            "contract_term": "Definite"
          },
          "additional_details": {
            "rule": "ONE_QUARTER_OF_CONTRACT_DURATION",
            "cap": 100
          }
        }
      ]
    },
    {
      "data_point": "scope",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "external_validation": true
        }
      ]
    },
    {
      "data_point": "seniority",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "external_validation": true
        }
      ]
    },
    {
      "data_point": "startDate",
      "rules": [
        {
          "nullable": false,
          "is_editable": false,
          "min_date": "2024-12-13"
        }
      ]
    },
    {
      "data_point": "timeOffType",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "possible_options": [
            "STANDARD",
            "SPECIFIC"
          ]
        }
      ]
    },
    {
      "data_point": "workHoursPerWeek",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "max": 40,
          "min": 40,
          "requires": {
            "employment_type": "Full-time"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "max": 39,
          "min": 1,
          "requires": {
            "employment_type": "Part-time"
          }
        }
      ]
    },
    {
      "data_point": "employmentState",
      "rules": [
        {
          "nullable": false,
          "is_editable": false,
          "possible_options": []
        }
      ]
    },
    {
      "data_point": "salary",
      "rules": [
        {
          "nullable": false,
          "is_editable": true,
          "min": 527.7849922722874,
          "max": 259475.48134227723,
          "requires": {
            "employment_type": "full-time"
          }
        },
        {
          "nullable": false,
          "is_editable": true,
          "max": 259475.48134227723,
          "requires": {
            "employment_type": "part-time"
          }
        }
      ]
    }
  ]
}
```

2. Create Amendment

```shell
curl --location '{{host}}/rest/v2/eor/amendments/374xe7e/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{token}}' \
--data '{
    "data": {
        "time_off_type": "SPECIFIC",
        "holidays": 12,
        "employment_type": "Part-time"
    }
}'
```

Response

```json

{
  "data": {
    "id": "116fdec2-d8b6-4c64-82d9-089cccf92731",
    "effective_date": null,
    "salary": "100000.0000",
    "employment_type": "Full-time",
    "seniority_id": 34,
    "job_title": "Account Executive",
    "time_off_type": "SPECIFIC",
    "probation_period_type_for_definite": null,
    "document_type": "SOW_EA",
    "holidays": 12,
    "probation_period": 90,
    "scope": "Duties and Responsibilities\n\n- Create detailed business plans designed to attain predetermined goals and quotas.\n- Manage the entire sales cycle from finding a client to securing a deal.\n- Unearth new sales opportunities through networking and turn them into long-term partnerships.\n- Present products to prospective clients.\n- Provide professional after-sales support to maximize customer loyalty.\n- Remain in regular contact with your clients to understand and meet their needs.\n- Respond to complaints and resolve issues to the customer's satisfaction and to maintain the company's reputation.\n- Negotiate agreements.\n- Maintains all sales databases necessary to report sales activity and customer information.\n- Attends all sales meetings and training sessions as required by management.",
    "employee_nationality": "NG",
    "employment_state": null,
    "start_date": "2024-12-13T00:00:00.000Z",
    "end_date": null,
    "work_hours_per_week": "40.00",
    "sick_leave_days": null,
    "type": "LEGAL",
    "created_at": "2025-03-25T11:32:35.320Z",
    "requested_by": 1430095,
    "is_hrx_action_needed": false,
    "legal_context": null,
    "rejection_context": null,
    "void_deadline": null,
    "void_deadline_type": null,
    "notice_period_type": "STANDARD",
    "notice_period_after_probation": "4",
    "notice_period_during_probation": "1",
    "notice_period_time_unit": "WEEK",
    "currency": "USD",
    "is_effective_date_updated": false,
    "description": null,
    "work_schedule_id": null,
    "work_schedule_rules_version": null,
    "source": "PUBLIC_API",
    "amendment_statuses": [
      {
        "name": "Draft",
        "friendly_name": "Draft",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:35.358Z"
        }
      }
    ],
    "items": [
      {
        "data_point": "holidays",
        "id": "4bc539c7-50a7-41eb-b6a3-a5d00ed0a8f2",
        "item": "holidaysIncrease",
        "type": "INSTANT",
        "previous_value": "6",
        "new_value": "12"
      },
      {
        "data_point": "timeOffType",
        "id": "0deaa6a0-54be-43f4-af72-368548166323",
        "item": "timeOffType",
        "type": "LEGAL",
        "previous_value": "STANDARD",
        "new_value": "SPECIFIC"
      }
    ]
  }
}
```

2.1 Update the amendment if needed, using id from the response

```shell
curl --location '{{host}}/rest/v2/eor/amendments/374xe7e/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{token}}' \
--data '{
    "data": {
        "time_off_type": "SPECIFIC",
        "holidays": 16,
        "employment_type": "Part-time"
        id: "116fdec2-d8b6-4c64-82d9-089cccf92731"
    }
}'
```

2.2 Use the amendment `id` to fetch the effective date limits. If you support it, display a calendar using the date limits and flags returned in the response

```shell
curl --location 'https://api-gateway.deel.training/rest/v2/eor/amendments/mdyyevp/34c6ef5a-b18b-461f-a0d3-83a306d271d9/validation-rules/effective-date-limitations' \
--header 'Authorization: Bearer {API_TOKEN}'
```

Response

```shell
{
  "data": {
    "is_hidden": false,
    "is_disabled": false,
    "min_effective_date": "2025-07-01",
    "max_effective_date": "2025-12-31",
    "default_effective_date": "2025-08-01",
    "message": "The effective date should align with the payroll cycle."
  }
}
```

2.3 Set the effective date by calling the [update amendment endpoint](https://developer.deel.com/reference/upsertamendm), using the `id` from the response.

```shell
curl --location '{{host}}/rest/v2/eor/amendments/374xe7e/' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{token}}' \
--data 
'{
    "data": {
      "time_off_type": "SPECIFIC",
      "holidays": 16,
      "effective_date": "2025-08-01",
      id: "116fdec2-d8b6-4c64-82d9-089cccf92731"
    }
}'
```

3. Confirm the amendment using id from the response

```shell
curl --location --request POST '{{host}}/rest/v2/eor/amendments/374xe7e/116fdec2-d8b6-4c64-82d9-089cccf92731/actions/confirm' \
--header 'accept: application/json' \
--header 'Authorization: Bearer {{token}}'
```

Response

```json
{
  "data": {
    "id": "116fdec2-d8b6-4c64-82d9-089cccf92731",
    "effective_date": null,
    "salary": "100000.0000",
    "employment_type": "Full-time",
    "seniority_id": 34,
    "job_title": "Account Executive",
    "time_off_type": "SPECIFIC",
    "probation_period_type_for_definite": null,
    "document_type": "SOW_EA",
    "holidays": 12,
    "probation_period": 90,
    "scope": "Duties and Responsibilities\n\n- Create detailed business plans designed to attain predetermined goals and quotas.\n- Manage the entire sales cycle from finding a client to securing a deal.\n- Unearth new sales opportunities through networking and turn them into long-term partnerships.\n- Present products to prospective clients.\n- Provide professional after-sales support to maximize customer loyalty.\n- Remain in regular contact with your clients to understand and meet their needs.\n- Respond to complaints and resolve issues to the customer's satisfaction and to maintain the company's reputation.\n- Negotiate agreements.\n- Maintains all sales databases necessary to report sales activity and customer information.\n- Attends all sales meetings and training sessions as required by management.",
    "employee_nationality": "NG",
    "employment_state": null,
    "start_date": "2024-12-13T00:00:00.000Z",
    "end_date": null,
    "work_hours_per_week": "40.00",
    "sick_leave_days": null,
    "type": "LEGAL",
    "created_at": "2025-03-25T11:32:35.320Z",
    "requested_by": 1430095,
    "is_hrx_action_needed": false,
    "legal_context": null,
    "rejection_context": null,
    "void_deadline": null,
    "void_deadline_type": null,
    "notice_period_type": "STANDARD",
    "notice_period_after_probation": "4",
    "notice_period_during_probation": "1",
    "notice_period_time_unit": "WEEK",
    "currency": "USD",
    "is_effective_date_updated": false,
    "description": null,
    "work_schedule_id": null,
    "work_schedule_rules_version": null,
    "source": "PUBLIC_API",
    "amendment_statuses": [
      {
        "name": "PreparingDocuments.AmendmentRequested.EA",
        "friendly_name": "Ea",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.EA.PendingDocumentSubmit",
        "friendly_name": "Awaiting review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.SOW",
        "friendly_name": "Sow",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.SOW.PendingDocumentSubmit",
        "friendly_name": "Awaiting review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.CustomReview",
        "friendly_name": "Custom review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.CustomReview.CustomSkipped",
        "friendly_name": "Custom skipped",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested",
        "friendly_name": "Amendment requested",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments",
        "friendly_name": "Preparing documents",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      }
    ],
    "items": [
      {
        "data_point": "holidays",
        "id": "4bc539c7-50a7-41eb-b6a3-a5d00ed0a8f2",
        "item": "holidaysIncrease",
        "type": "INSTANT",
        "previous_value": "6",
        "new_value": "12"
      },
      {
        "data_point": "timeOffType",
        "id": "0deaa6a0-54be-43f4-af72-368548166323",
        "item": "timeOffType",
        "type": "LEGAL",
        "previous_value": "STANDARD",
        "new_value": "SPECIFIC"
      }
    ]
  }
}
```

4. Wait for the amendment to be reviewed. You can monitor status using get endpoint.

```shell
curl --location '{{host}}/rest/v2/eor/amendments/374xe7e/116fdec2-d8b6-4c64-82d9-089cccf92731' \
--header 'accept: application/json' \
--header 'Authorization: Bearer {{token}}'
```

Response

```json
{
  "data": {
    "id": "116fdec2-d8b6-4c64-82d9-089cccf92731",
    "effective_date": null,
    "salary": "100000.0000",
    "employment_type": "Full-time",
    "seniority_id": 34,
    "job_title": "Account Executive",
    "time_off_type": "SPECIFIC",
    "probation_period_type_for_definite": null,
    "document_type": "SOW_EA",
    "holidays": 12,
    "probation_period": 90,
    "scope": "Duties and Responsibilities\n\n- Create detailed business plans designed to attain predetermined goals and quotas.\n- Manage the entire sales cycle from finding a client to securing a deal.\n- Unearth new sales opportunities through networking and turn them into long-term partnerships.\n- Present products to prospective clients.\n- Provide professional after-sales support to maximize customer loyalty.\n- Remain in regular contact with your clients to understand and meet their needs.\n- Respond to complaints and resolve issues to the customer's satisfaction and to maintain the company's reputation.\n- Negotiate agreements.\n- Maintains all sales databases necessary to report sales activity and customer information.\n- Attends all sales meetings and training sessions as required by management.",
    "employee_nationality": "NG",
    "employment_state": null,
    "start_date": "2024-12-13T00:00:00.000Z",
    "end_date": null,
    "work_hours_per_week": "40.00",
    "sick_leave_days": null,
    "type": "LEGAL",
    "created_at": "2025-03-25T11:32:35.320Z",
    "requested_by": 1430095,
    "is_hrx_action_needed": false,
    "legal_context": null,
    "rejection_context": null,
    "void_deadline": null,
    "void_deadline_type": null,
    "notice_period_type": "STANDARD",
    "notice_period_after_probation": "4",
    "notice_period_during_probation": "1",
    "notice_period_time_unit": "WEEK",
    "currency": "USD",
    "is_effective_date_updated": false,
    "description": null,
    "work_schedule_id": null,
    "work_schedule_rules_version": null,
    "source": "PUBLIC_API",
    "amendment_statuses": [
      {
        "name": "PreparingDocuments.AmendmentRequested.EA",
        "friendly_name": "Ea",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.EA.PendingDocumentSubmit",
        "friendly_name": "Awaiting review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.SOW",
        "friendly_name": "Sow",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.SOW.PendingDocumentSubmit",
        "friendly_name": "Awaiting review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.CustomReview",
        "friendly_name": "Custom review",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested.CustomReview.CustomSkipped",
        "friendly_name": "Custom skipped",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments.AmendmentRequested",
        "friendly_name": "Amendment requested",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      },
      {
        "name": "PreparingDocuments",
        "friendly_name": "Preparing documents",
        "_amendment_flow_status": {
          "created_at": "2025-03-25T11:32:52.963Z"
        }
      }
    ],
    "items": [
      {
        "data_point": "holidays",
        "id": "4bc539c7-50a7-41eb-b6a3-a5d00ed0a8f2",
        "item": "holidaysIncrease",
        "type": "INSTANT",
        "previous_value": "6",
        "new_value": "12"
      },
      {
        "data_point": "timeOffType",
        "id": "0deaa6a0-54be-43f4-af72-368548166323",
        "item": "timeOffType",
        "type": "LEGAL",
        "previous_value": "STANDARD",
        "new_value": "SPECIFIC"
      }
    ]
  }
}
```

Or you can use the webhook to get the status of the amendment

```json
{
  "data": {
    "meta": {
      "event_type": "eor.amendment.status.updated",
      "event_type_id": "de688244-7869-46db-8ac7-00083965cc9b",
      "organization_id": "9c09a153-1418-4127-8c44-e99483e7c321",
      "organization_name": "20TT65OV",
      "tracking_id": "d09a72b0002191b65de3a453d177f1a7"
    },
    "resource": {
      "amendment_flow_id": "116fdec2-d8b6-4c64-82d9-089cccf92731",
      "organization_id": "9c09a153-1418-4127-8c44-e99483e7c321",
      "status": "EOR_AMENDMENT_V2_CLIENT_ACTIVE"
    }
  },
  "timestamp": "2025-02-07T12:36:16.360Z"
}
```

To get link to download the EA document

```shell
curl --location '{{host}}/rest/v2/eor/amendments/374xe7e/51005644-d775-421c-9e59-c0aeacd8d4c1/pdf' \
--header 'accept: application/json' \
--header 'Authorization: Bearer {{token}}'
```

Response

```json
{
  "data": {
    "url": "{{host}}/eor-experience-dev/amendment_documents/fb4a3959-0a93-4dd9-9b46-7f1af60b2bbd.pdf?AWSAccessKeyId=TEST_ACCESS_KEY&Expires=1673158576&Signature=TEST_SIGNATURE"
  }
}
```

5. While the amendment in not active you can cancel it

```shell
curl --location --request DELETE '{{host}}/rest/v2/eor/amendments/374xe7e/3c810625-8108-43c2-8aca-14a552255148' \
--header 'accept: application/json' \
--header 'Authorization: Bearer {{token}}'
```

Response

```json
{
    "data": {
        "success": true
    }
}
```

6. Once its review by Deel employee need to sign it

```shell
curl --location --request POST '{{host}}/rest/v2/eor/amendments/374xe7e/116fdec2-d8b6-4c64-82d9-089cccf92731/actions/sign' \
--header 'accept: application/json' \
--header 'Authorization: Bearer {{token}}'
```

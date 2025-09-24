---
title: "Accounting API"
slug: "accounting-api"
excerpt: "Learn how to use the accounting API to keep track of your payments to Deel"
hidden: false
createdAt: "Wed Nov 20 2024 12:28:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Jun 30 2025 15:00:06 GMT+0000 (Coordinated Universal Time)"
---
The Accounting API helps with your bookkeeping by providing endpoints for retrieving invoice and payment data. Specifically, the endpoints allow to:

- [Retrieve invoices](#retrieve-invoices)
- [Retrieve payment receipts](#retrieve-payment-receipts)
- [Retrieve a payment breakdown](#retrieve-a-payment-breakdown)

## Retrieve invoices

Invoices are organized into two categories: Deel fees and worker salaries. There's a separate endpoint for each invoices:

- [Retrieve worker salary invoices](#retrieve-worker-salary-invoices)
- [Retrieve Deel fees invoices](#retrieve-deel-fees-invoices)

### Retrieve worker salary invoices

You can use the [Retrieve invoices](https://developer.deel.com/reference/getinvoicelist) endpoint to retrieve the invoices that are related to the salaries of your workforce.

To retrieve the worker salary invoices, make a GET request to the endpoint.

```curl
curl --request GET \
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/invoices?issued_from_date=2024-11-09&issued_to_date=2024-11-14&entities=company&limit=10&offset=0' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}'
```

In the query:

| Name             | Required | Type   | Format | Description                                                                                                                                                                                          | Example    |
| ---------------- | -------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| issued_from_date | false    | string | -      | The start of the date range that you can filter invoices by                                                                                                                                          | 2024-11-09 |
| issued_to_date   | false    | string | -      | The end of the date range that you can filter invoices by                                                                                                                                            | 2024-11-14 |
| entities         | false    | string | enum   | Filter invoices by legal entity type. The entity type can be either `company` or `individual`. More information at [List of legal entities](https://developer.deel.com/reference/getlegalentitylist) | company    |
| limit            | false    | number | -      | Number of results to be returned in the response                                                                                                                                                     | 100        |
| offset           | false    | number | -      | The number of results that the response starts from. All results before this number are skipped.                                                                                                     | 10         |

A successful response (`200`) returns the list of invoices available in your organization and matching any filters applied. For example:

```json
{
  "data": [
    {
      "id": "rhCTiRd9Mad41RwjsFWw-",
      "status": "paid",
      "currency": "GBP",
      "created_at": "2022-05-24T09:38:46.235Z",
      "total": "1000",
      "label": "INV-2023-4",
      "paid_at": "2022-05-24T09:38:46.235Z",
      "vat_total": "210",
      "vat_percentage": "21",
      "is_overdue": true,
      "issued_at": "2022-05-24T09:38:46.235Z",
      "vat_id": "string",
      "due_date": "2022-05-24T09:38:46.235Z",
      "contract_id": "string"
    }
  ],
  "page": {
    "total_rows": 0,
    "items_per_page": 0,
    "offset": 0
  }
}
```

Where:

| Name           | Required | Type    | Format    | Description                                                                             | Example                  |
| -------------- | -------- | ------- | --------- | --------------------------------------------------------------------------------------- | ------------------------ |
| id             | true     | string  | UUID      | The ID of the invoice.                                                                  | rhCTiRd9Mad41RwjsFWw-    |
| status         | true     | string  | enum      | The status of the invoice.                                                              | paid                     |
| currency       | true     | string  | enum      | The currency of the invoice.                                                            | GBP                      |
| created_at     | true     | string  | date-time | Date on which the invoice is created                                                    | 2022-05-24T09:38:46.235Z |
| total          | true     | number  | -         | The total amount of the invoice.                                                        | 1000                     |
| label          | true     | string  | -         | The label of the invoice.                                                               | INV-2023-4               |
| paid_at        | true     | string  | date-time | Date on which the invoice is paid                                                       | 2022-05-24T09:38:46.235Z |
| vat_total      | true     | number  | -         | The total VAT amount of the invoice.                                                    | 210                      |
| vat_percentage | true     | number  | -         | The VAT percentage of the invoice.                                                      | 21                       |
| is_overdue     | true     | boolean | -         | Defines if the invoice is overdue or not.                                               | true                     |
| issued_at      | true     | string  | date-time | Date on which the invoice is issued                                                     | 2022-05-24T09:38:46.235Z |
| vat_id         | true     | string  | -         | The VAT ID of the invoice.                                                              | string                   |
| due_date       | true     | string  | date-time | Date on which the invoice is due                                                        | 2022-05-24T09:38:46.235Z |
| contract_id    | true     | string  | -         | Unique identifier of the contract that invoices were submitted for                      | string                   |
| page           | true     | object  | -         | An object containing pagination information. Use it to navigate through sets of results | -                        |

### Retrieve Deel fees invoices

Deel fees are invoiced separately from [your worker's salaries](#retrieve-invoices). You can use the [Retrieve Deel invoices](https://developer.deel.com/reference/getdeelinvoicelist) endpoint to retrieve the invoices that are related to Deel fees.

To retrieve the Deel fees invoices, make a GET request to the endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/invoices/deel?limit=10&offset=0&contract_id=54d268g' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}'
```

In the query:

| Name        | Required | Type   | Format | Description                                                                                                                                                                            | Example |
| ----------- | -------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| limit       | false    | number | -      | Number of results to be returned in the response                                                                                                                                       | 100     |
| offset      | false    | number | -      | The number of results that the response starts from. All results before this number are skipped.                                                                                       | 10      |
| contract_id | true     | string | -      | Unique identifier of the contract that fee invoices were generated for. You can obtain it from the [List of contracts](https://developer.deel.com/reference/getcontractlist) endpoint. | d3g0d3g |

A successful response (`200`) returns the list of invoices for Deel fees that match the filters. For example:

```json
{
  "data": [
    {
      "id": "rhCTiRd9Mad41RwjsFWw-",
      "label": "INV-2023-4",
      "status": "paid",
      "currency": "GBP",
      "total": "1000",
      "created_at": "2024-05-24T09:38:46.235Z"
    }
  ],
  "page": {
    "total_rows": 0,
    "items_per_page": 0,
    "offset": 0
  }
}
```

Where:

| Name       | Required | Type   | Format    | Description                                                                              | Example                  |
| ---------- | -------- | ------ | --------- | ---------------------------------------------------------------------------------------- | ------------------------ |
| id         | true     | string | UUID      | The unique ID of the invoice                                                             | rhCTiRd9Mad41RwjsFWw-    |
| label      | true     | string | -         | The label of the invoice                                                                 | INV-2023-4               |
| status     | true     | string | enum      | The status of the invoice                                                                | paid                     |
| currency   | true     | string | -         | The currency code of the invoice                                                         | GBP                      |
| total      | true     | number | -         | The total amount of the invoice                                                          | 1000                     |
| created_at | true     | string | date-time | Date on which the invoice is created                                                     | 2022-05-24T09:38:46.235Z |
| page       | true     | object | -         | An object containing pagination information. Use it to navigate through sets of results. | -                        |

### Download invoice PDF

For each invoice, you can also download the invoices as a PDF files. Both the [worker salary invoices](#retrieve-worker-salary-invoices) and [Deel fee invoices](#retrieve-deel-fees-invoices) are available.

To download an invoice, make a GET request to the [Download invoice PDF](https://developer.deel.com/reference/getbillinginvoicedownloadlink) endpoint.

```curl
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/invoices/{id}/download \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}'
```

In the path:

| Name | Required | Type   | Format | Description                                       | Example               |
| ---- | -------- | ------ | ------ | ------------------------------------------------- | --------------------- |
| id   | true     | string | UUID   | The unique ID of the invoice. You can retrieve it | d3m0d3m0d3m0d3m0d3m0d |

A successful response (`200`) returns the link to download the PDF file. For example:

```json
{
  "data": {
    "url": "https://url.com/invoices/12345.pdf"
  }
}
```

### Retrieve payment receipts

For each payment made to Deel for the issued invoices, you can also retrieve the receipts.

To retrieve the receipts, make a GET request to the [Retrieve payment receipts](https://developer.deel.com/reference/getpaymentlist) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/payments?date_from=2024-10-11&date_to=2024-10-19&currencies=EUR&entities=individual' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}'
```

In the query, you can specify the following parameters to filter the results:

| Name       | Required | Type   | Format | Description                                                                                                                                                     | Example    |
| ---------- | -------- | ------ | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| date_from  | true     | string | date   | The start date of the payment receipts. The format is `YYYY-MM-DD`.                                                                                             | 2024-10-11 |
| date_to    | true     | string | date   | The end date of the payment receipts. The format is `YYYY-MM-DD`.                                                                                               | 2024-10-19 |
| currencies | true     | string | -      | The currency codes of the payment receipts. You can retrieve the available currencies from [Currency list](https://developer.deel.com/reference/getcurrencies). | EUR        |
| entities   | true     | string | -      | The entities of the payment receipts                                                                                                                            | individual |

A successful response (`200`) returns the list of payment receipts that match the filters. For example:

```json
{
  "data": {
    "rows": [
      {
        "id": 12345,
        "payment_method": {
          "type": "stripe_bacs_debit"
        },
        "status": "paid",
        "payment_currency": "GBP",
        "label": "string",
        "paid_at": "2022-05-24T09:38:46.235Z",
        "created_at": "2022-05-24T09:38:46.235Z",
        "total": "1000.00",
        "workers": [
          {
            "id": 123456,
            "name": "Jane Doe",
            "picUrl": "string",
            "contract_id": "string"
          }
        ]
      }
    ],
    "total": 1
  }
}
```

Where:

| Name                    | Required | Type   | Format    | Description                                                                                                                                                   | Example                  |
| ----------------------- | -------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| id                      | true     | number | -         | The ID of the payment receipt. You can use this ID to [retrieve the payment breakdown](#retrieve-a-payment-breakdown).                                        | 12345                    |
| payment_method          | true     | object | -         | The payment method of the payment receipt                                                                                                                     | -                        |
| payment_method.type     | true     | string | enum      | The type of the payment method                                                                                                                                | stripe_bacs_debit        |
| status                  | true     | string | enum      | The status of the payment receipt                                                                                                                             | paid                     |
| payment_currency        | true     | string | enum      | The currency code of the payment receipt. You can retrieve the available currencies from [Currency list](https://developer.deel.com/reference/getcurrencies). | GBP                      |
| label                   | true     | string | -         | The label of the payment receipt                                                                                                                              | string                   |
| paid_at                 | true     | string | date-time | Date on which the payment receipt is paid                                                                                                                     | 2022-05-24T09:38:46.235Z |
| created_at              | true     | string | date-time | Date on which the payment receipt is created                                                                                                                  | 2022-05-24T09:38:46.235Z |
| total                   | true     | number | -         | The total amount of the payment receipt                                                                                                                       | 1000.00                  |
| workers                 | true     | array  | -         | Contains objects that represent the workers that the payment receipt is related to                                                                            | -                        |
| workers.\[].id          | true     | number | -         | The ID of the worker                                                                                                                                          | 123456                   |
| workers.\[].name        | true     | string | -         | The name of the worker                                                                                                                                        | Jane Doe                 |
| workers.\[].picUrl      | true     | string | -         | The URL of the worker's profile picture                                                                                                                       | string                   |
| workers.\[].contract_id | true     | string | -         | The contract ID of the worker                                                                                                                                 | string                   |

### Retrieve a payment breakdown

You can retrieve the breakdown of the payments made to Deel by using the payment ID that is returned in the [payment receipt](#retrieve-payment-receipts). The breakdown includes all the details of a payment and is available for both [Deel fee](#retrieve-deel-fees-invoices) and [worker](#retrieve-worker-invoices) invoices.

To retrieve the breakdown, make a GET request to the [Retrieve a payment breakdown](https://developer.deel.com/reference/retrieveapaymentbreakdown) endpoint.

```curl
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/payments/{payment_id}/breakdown \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{token}}'
```

In the path:

| Name       | Required | Type   | Format | Description                                                                                                                                                                  | Example               |
| ---------- | -------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| payment_id | true     | string | -      | Unique identifier to retrieve the payment breakdown. You can retrieve it from the [Retrieve payment receipts](https://developer.deel.com/reference/getpaymentlist) endpoint. | YJdYFAA586JYf8A324T57 |

A successful response (`200`) returns the breakdown of the payment. An empty parameter means that the parameter is either not provided or not applicable.

> 📘 1 breakdown item = 1 object
> 
> Each breakdown item is an object in the `data` array.

For example:

```json
{
  "data": [
    {
      "date": "2022-10-01T00:59:28.482Z",
      "work": "3000.00",
      "bonus": "500.00",
      "total": "3500.00",
      "others": "0.00",
      "currency": "USD",
      "expenses": "0.00",
      "group_id": "4fd2daf5-7d59-4990-ba17-5dfc5f1034d0",
      "overtime": "0.00",
      "pro_rata": "0.00",
      "approvers": "John Smith, Jane Doe",
      "frequency": "monthly",
      "adjustment": "0.00",
      "deductions": "0.00",
      "commissions": "0.00",
      "approve_date": "2022-10-28T14:32:15.847Z",
      "payment_date": "2022-11-01T17:20:32.837Z",
      "contract_type": "ongoing_time_based",
      "processing_fee": "0.00",
      "contract_country": "US",
      "contractor_email": "name@email.com",
      "payment_currency": "USD",
      "contract_start_date": "2020-03-31T10:58:49.780Z",
      "general_ledger_account": "6000 - Office Expenses",
      "total_payment_currency": "1000.00",
      "contractor_employee_name": "Jane Doe",
      "contractor_unique_identifier": "550e8400-e29b-41d4-a716-446655440000"
    }
  ]
}
```

Where:

| Name                         | Required | Type   | Format    | Description                                                                    | Example                                                       |
| ---------------------------- | -------- | ------ | --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- |
| date                         | true     | string | date-time | Date on which the item is paid                                                 | 2022-05-24T09:38:46.235Z                                      |
| general_ledger_account       | true     | string | -         | Returns the name of the general ledger account if the payment is linked to one | -                                                             |
| team                         | true     | string | -         | The team of the item                                                           | Deel Inc.                                                     |
| contractor_unique_identifier | true     | string | -         | The unique identifier of the worker                                            | 12345                                                         |
| contractor_employee_name     | true     | string | -         | The name of the contractor                                                     | Michael Scott                                                 |
| contractor_email             | true     | string | -         | The email of the contractor                                                    | [michael@dundermifflin.com](mailto:michael@dundermifflin.com) |
| invoice_number               | true     | string | -         | The invoice number of the item                                                 | 5069872                                                       |
| currency                     | true     | string | enum      | The currency code of the item                                                  | USD                                                           |
| payment_currency             | true     | string | enum      | The currency code of the item                                                  | USD                                                           |
| receipt_number               | true     | string | -         | The receipt number of the item                                                 | 5551621                                                       |
| work                         | true     | number | -         | The amount of the base work for the item                                       | 0.00                                                          |
| bonus                        | true     | number | -         | The amount of the bonus for the item                                           | 0.00                                                          |
| expenses                     | true     | number | -         | The amount of the expenses for the item                                        | 0.00                                                          |
| commissions                  | true     | number | -         | The commissions amount of the item                                             | 0.00                                                          |
| deductions                   | true     | number | -         | The deductions amount of the item                                              | 0.00                                                          |
| overtime                     | true     | number | -         | The overtime amount of the item                                                | 0.00                                                          |
| pro_rata                     | true     | number | -         | The pro rata amount of the item                                                | 0.00                                                          |
| others                       | true     | number | -         | The others amount of the item                                                  | 0.00                                                          |
| processing_fee               | true     | number | -         | The processing fee amount of the item                                          | 0.00                                                          |
| adjustment                   | true     | number | -         | The adjustment amount of the item                                              | 0.00                                                          |
| total                        | true     | number | -         | The total amount of the item                                                   | 1000.00                                                       |
| total_payment_currency       | true     | number | -         | The total amount of the item in the payment currency                           | 1000.00                                                       |
| payment_date                 | true     | string | date-time | Date on which the item is paid                                                 | 2022-11-01T17:20:32.837Z                                      |
| frequency                    | true     | string | -         | The frequency of the item                                                      | -                                                             |
| contract_country             | true     | string | -         | The country of the contractor                                                  | US                                                            |
| contract_start_date          | true     | string | date-time | The start date of the contract                                                 | 2020-03-31T10:58:49.780Z                                      |
| approvers                    | true     | string | -         | The approvers of the item                                                      | string                                                        |
| approve_date                 | true     | string | date-time | Date on which the item is approved                                             | string                                                        |

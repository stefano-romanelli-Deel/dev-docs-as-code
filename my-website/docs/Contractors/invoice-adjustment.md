---
title: "Invoice Adjustment"
slug: "invoice-adjustment"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:57:18 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:29:16 GMT+0000 (Coordinated Universal Time)"
---
# Create an invoice adjustment

You might want to adjust the pay of your contractor. Within Deel, you can add a bonus, commission, deduction, expense, overtime, time-off, VAT %, or other adjustments to an invoice.

```shell
curl --location --request POST 'https://api.letsdeel.com/rest/v2/invoice-adjustments' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "contract_id": "a1b2b3",
    "amount": 1,
    "description": "my bonus",
    "date_submitted": "2022-06-31",
    "type": "bonus"
  }
}'
```

# Update an existing adjustment

You can furthermore update an existing invoice adjustment, for example, the bonus or the time-off. Please note that you will need the _timesheetId_ to update an existing adjustment.

**Step 1**: Retrieve the _timesheetId_

```shell
curl --location -g --request GET '{{host}}/rest/v2/contracts/{{contractId}}/timesheets?statuses[]=pending' \
--header 'Authorization: Bearer {token}'
```

**Step 2**: Update an existing adjustment

```shell
curl --location -g --request PATCH '{{host}}/rest/v2/invoice-adjustments/{{timesheetId}}' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "amount": 222,
    "description": "bonus - updated"
  }
}'
```

> 📘 Adjsuting VATs
> 
> It is not possible to update VAT adjustments, we recommend you delete the existing VAT and create a new invoice adjustment.

# Delete an invoice adjustment

```shell
curl --location -g --request DELETE '{{host}}/rest/v2/invoice-adjustments/{{timesheetIdVat}}?reason=my reason to delete' \
--header 'Authorization: Bearer {token}'
```

# Approve an invoice adjustment

The invoice adjustment can also be submitted by the worker and you are able to review that invoice adjustment and then either approve it...

```shell
curl --location -g --request POST '{{host}}/rest/v2/invoice-adjustments/{{timesheetId}}/reviews' \
--header 'Authorization: Bearer {token} ' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "status": "approved",
    "reason": "my reason"
  }
}'
```

# Decline an invoice adjustment

... or decline it.

```shell
curl --location -g --request POST '{{host}}/rest/v2/invoice-adjustments/{{timesheetId}}/reviews' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "status": "declined",
    "reason": "my reason"
  }
}'
```

# Search for an invoice line item

You can retrieve a list of invoice details. This list can be filtered to your needs by providing additional parameters e.g. contract_id, contract_type, etc.

```shell
curl --location -g --request GET '{{host}}/rest/v2/invoice-adjustments?types[]=bonus' \
--header 'Authorization: Bearer {token}'
```

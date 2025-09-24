---
title: "Update PTO (Paid Time Off)"
slug: "gp-pto"
excerpt: ""
hidden: true
createdAt: "Mon Oct 30 2023 10:44:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:37:15 GMT+0000 (Coordinated Universal Time)"
---
To update an employee's PTO, hit the `/v2/gp/workers/:worker-id/pto-policy` endpoint with the following parameters:

- `accrual_start_date`
- `yearly_allowance`

# Sample Request & Response

**Request URL**

```curl
PATCH https://api.letsdeel.com/rest/v2/gp/workers/:worker-id/pto-policy
```

**Request & Response**

```json Request
PATCH 'https://api.letsdeel.com/rest/v2/gp/workers/3d32cb84-5b40-4223-89e4-b325b7d68403/pto-policy' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--data-raw '{ 
    "data": {
        "accrual_start_date": "2023-10-01",
        "yearly_allowance": "32"
    }
}'
```
```json Response
{
    "data": {
        "updated": true
     }
}
```

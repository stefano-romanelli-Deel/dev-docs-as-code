---
title: "Update Employee Address"
slug: "gp-employee-address"
excerpt: ""
hidden: true
createdAt: "Mon Oct 30 2023 10:43:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:36:12 GMT+0000 (Coordinated Universal Time)"
---
To update an employee's address, hit the `/v2/gp/workers/:worker_id/address` endpoint with any or all of the following parameters:

- `state`
- `city`
- `street`
- `zip`

**NOTE**: You can't update an employee's country using this API

After successfully executing the API call, a `200` response will be returned featuring a data object that contains the employee's updated address. 

# Sample Request & Response

**Request URL**

```curl
PATCH https://api.letsdeel.com/rest/v2/gp/workers/:worker_id/address
```

**Request & Response**

```json Request
PATCH 'https://api.letsdeel.com/rest/v2/gp/workers/3d32cb84-5b40-4223-89e4-b325b7d68403/address' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--data-raw '{ 
    "data": {
        "state": "TX",
        "city": "Williams",
        "street": "5 Nowhere Street",
        "zip": "2554"
    }
}'
```
```json Response
{
    "data": {
        "country": "GB",
        "state": "TX",
        "city": "Williams",
        "street": "5 Nowhere Street",
        "zip": "2554",
        "updated_at": "2023-10-30T10:58:02.134Z"
    }
}
```

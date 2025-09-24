---
title: "Update Compensation"
slug: "update-compensation"
excerpt: ""
hidden: true
createdAt: "Mon Oct 30 2023 10:38:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:37:30 GMT+0000 (Coordinated Universal Time)"
---
To update an employee's compensation, hit the `/v2/gp/workers/:worker_id/compensation` endpoint with the following parameters:

- `scale`
- `salary`
- `effective_date`

After successfully executing the API call, a `200` response will be returned featuring an array of objects showing all compensation data for the employee - outdated, active and upcoming.

# Sample Request & Response

**Request URL**

```Text cURL
PATCH https://api.letsdeel.com/rest/v2/gp/workers/:worker_id/compensation
```

**Request & Response**

```Text Request
PATCH 'https://api.letsdeel.com/rest/v2/gp/workers/3d32cb84-5b40-4223-89e4-b325b7d68403/compensation' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--data-raw '{ 
    "data": {
        "scale": "YEAR",
        "salary": 137000,
        "effective_date": "2023-10-31"
}
}'
```
```Text Response
{
    "data": [
        {
            "status": "ACTIVE",
            "scale": "YEAR",
            "salary": "100000",
            "effective_date": "2023-09-26"
        },
        {
            "status": "OUTDATED",
            "scale": "MONTH",
            "salary": "12000",
            "effective_date": "2023-10-24"
        },
        {
            "status": "UPCOMING",
            "scale": "YEAR",
            "salary": "137000",
            "effective_date": "2023-10-31"
        }
    ]
}
```

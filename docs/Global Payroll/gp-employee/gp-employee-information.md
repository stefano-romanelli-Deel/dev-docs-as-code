---
title: "Update Employee Information"
slug: "gp-employee-information"
excerpt: ""
hidden: true
createdAt: "Mon Oct 30 2023 10:44:09 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:37:01 GMT+0000 (Coordinated Universal Time)"
---
To update an employee's information, hit the `/v2/gp/workers/:id/employee-information` endpoint with any or all of the following parameters:

- `first_name`
- `middle_name`
- `last_name`
- `date_of_birth`
- `gender`
- `marital_status`

After successfully executing the API call, a `201` response will be generated featuring a data object that contains the employee's updated information. 

# Sample Request & Response

**Request URL**

```curl
PATCH https://api.letsdeel.com/rest/v2/gp/workers/:worker_id/employee-information
```

**Request & Response**

```json Request
POST 'https://api.letsdeel.com/rest/v2/gp/workers/3d32cb84-5b40-4223-89e4-b325b7d68403/employee-information' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--header 'x-client-id: {client_id}' \
--data-raw '{ 
    "data": {
        "first_name": "Annie",
        "middle_name": "Hash",
        "last_name": "Gornals",
        "gender": "Female",
        "marital_status": "Single",
        "date_of_birth": "1988-10-13"
    }
}'
```
```json Response
{
    "data": {
        "first_name": "Annie",
        "middle_name": "Hash",
        "last_name": "Gornals",
        "gender": "Female",
        "marital_status": "Single",
        "date_of_birth": "1988-10-13"
     }
}
```

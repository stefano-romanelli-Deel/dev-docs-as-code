---
title: "Contracts"
slug: "gp-contracts"
excerpt: ""
hidden: false
createdAt: "Tue Jul 18 2023 11:28:04 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:34:16 GMT+0000 (Coordinated Universal Time)"
---
With Deel Global Payroll API, you can create a contract

## Create a Contract

You create a contract by sending an HTTP request to the URL below. Like most REST API requests, it should contain:

1. **Method**: POST
2. **Authorization**: Bearer token
3. **Data**: An object that is made up of other objects - employee, employment, client and compensation details

If all required fields in your request are available and accurate, the response will be  details of your created Global Payroll contract.

## Sample Request & Response

**Request URL**

```curl
POST https://api.letsdeel.com/rest/v2/contracts/gp
```

**Request & Response**

```json Request
POST 'https://api.letsdeel.com/rest/v2/contracts/gp' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--header 'x-client-id: {client_id}' \
--data-raw '{ 
    "data": {
        "employee": {
            "first_name": "Dwayne",
            "last_name": "Johnson",
            "email": "dwayne@johnson.com",
            "nationality": "PL",
            "address": {
                "street": "Deel Street",
                "city": "London",
                "state": "London",
                "zip": "5243",
                "country": "GB"
            }
        },
        "employment": {
            "type": "Full-time",
            "start_date": "2023-07-21",
            "holidays": {
                "allowance": 20,
                "start_date": "2023-11-12"
            }
        },
        "job_title": "Actor",
        "client": {
            "legal_entity": {
                "id": 703553
            },
            "team": {
                "id": 150725
            }
        },
        "compensation_details": {
            "salary": 100000,
            "currency": "GBP",
            "scale": "YEAR"
        }
    }
}'
```
```json Response
{
    "data": {
        "id": "jeg7285",
        "type": "global_payroll",
        "created_at": "2023-07-11T14:03:13.521Z",
        "status": "onboarding",
        "job_title": "Actor",
        "employment": {
            "start_date": "2023-07-21T00:00:00.000Z",
            "end_date": null,
            "country": "GB",
            "state": "London",
            "type": "Full-time",
            "work_visa_required": false,
            "holidays": {
                "allowance": 20,
                "start_date": "2023-11-12T00:00:00.000Z"
            }
        },
        "client": {
            "legal_entity": {
                "name": "GB entity"
            }
        },
        "compensation_details": {
            "salary": 100000,
            "currency": "GBP",
            "scale": "YEAR"
        },
        "employee": {
            "first_name": "Dwayne",
            "last_name": "Johnson",
            "email": "dwayne@johnson.com"
        }
    }
}
```

**Request Fields**

| Object               | Field           | Type   | Required | Description             |
| :------------------- | :-------------- | :----- | :------- | :---------------------- |
| employee             | first_name      | string | yes      | Employee's first name.  |
|                      | last_name       | string | yes      | Employee's last name.   |
|                      | email           | string | yes      | Employee's email.       |
|                      | nationality     | string | no       | Employee's nationality. |
|                      | job_title       | string | yes      | Employee's job title.   |
| address              | street          | string | yes      | Employee's street.      |
|                      | city            | string | yes      | Employee's city.        |
|                      | state           | string | no       | Employee's state.       |
|                      | zip             | string | yes      | Employee's zip code.    |
|                      | country         | string | yes      | Employee's country.     |
| employment           | type            | string | yes      | Employment type         |
|                      | start_date      | string | yes      | Employment start date.  |
| holidays             | allowance       | number | yes      | Holidays allowance      |
|                      | start_date      | string | yes      | Holidays start date.    |
| client               | legal_entity.id | number | yes      | Client legal entity ID. |
|                      | team.id         | number | yes      | Client team ID.         |
| compensation_details | salary          | number | yes      | Compensation salary.    |
|                      | currency        | string | no       | Compensation currency.  |
|                      | scale           | string | yes      | Compensation scale.     |

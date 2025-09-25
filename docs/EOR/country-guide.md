---
title: "Country Guide"
slug: "country-guide"
excerpt: ""
hidden: false
createdAt: "Tue Jul 18 2023 08:18:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:32:59 GMT+0000 (Coordinated Universal Time)"
---
Hiring full-time employees across the globe can be a complex process, requiring businesses to navigate and comply with various local laws and regulations. 

The country guide endpoint offered by Deel allows you to access up-to-date information about hiring employees in any Deel-supported country. This API provides comprehensive data on local labor laws, employment regulations, tax requirements, and other crucial details that employers need to consider when hiring in a specific country. By leveraging this endpoint, you can ensure compliance with local legal frameworks and avoid potential pitfalls associated with international hiring.

For instance, consider a scenario where a company based in the United States wants to hire an employee in Germany. Using Deel's country guide endpoint, the company can retrieve real-time information on German employment laws, such as minimum wage, working hour limits, and mandatory benefits. 

**Request**

```shell
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/eor/validations/GB \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {token}'
```

**Response**

_The data shown below is a sample. Please use the API to get the latest data._

```json
{
  "data": {
    "holiday": {
      "min": "20",
      "max": null,
    },
    "part_time_holiday": {
      "type": "PRORATED",
      "min": "20"
    },
    "sick_days": {
      "min": "0",
      "max": "28"
    },
    "salary": {
      "min": "18915.84",
      "max": "1000000.00"
    },
    "probation": {
      "min": null,
      "max": 180
    },
    "part_time_probation": {
      "min": null,
      "max": 180
    },
    "work_schedule": {
      "days": {
        "max": null,
        "min": "5.0000"
      },
      "hours": {
        "max": null,
        "min": "8.0000"
      }
    },
    "currency": "GBP",
    "start_date_buffer": 2,
    "definite_contract": {
      "type": "ALLOWED_WITHOUT_LIMITATION",
      "maximum_limitation": null
    },
    "adjustments_information_box": "For reimbursable costs connected to carrying out work, choose \"expenses\".\nFor fixed or recurring amounts provided as a benefit to employee, choose \"allowances\".",
    "health_insurance": {
      "status": "ENABLED",
      "providers": [
        {
          "name": "Unisure",
          "is_unisure": true,
          "home_page_url": "https://www.unisuregroup.com/",
          "currency": "USD",
          "attachments": [
            {
              "id": 20362,
              "label": "Unisure_OnePager_ 2023.pdf"
            }
          ],
          "plans": [
            {
              "name": "Bronze Plan",
              "price": null,
              "currency": "USD",
              "is_enabled": true,
              "id": 67
            },
            {
              "name": "Silver Plan",
              "price": null,
              "currency": "USD",
              "is_enabled": true,
              "id": 68
            },
            {
              "name": "Gold Plan",
              "price": null,
              "currency": "USD",
              "is_enabled": true,
              "id": 69
            },
            {
              "name": "Platinum Plan",
              "price": null,
              "currency": "USD",
              "is_enabled": true,
              "id": 70
            }
          ]
        },
        {
          "name": "Freedom - Ben",
          "is_unisure": false,
          "home_page_url": "https://www.freedomhealthinsurance.co.uk/",
          "currency": "GBP",
          "attachments": [
            {
              "id": 34409,
              "label": "Freedom Health UK.pdf"
            }
          ],
          "plans": [
            {
              "name": "Single Employee Coverage",
              "price": null,
              "currency": "GBP",
              "is_enabled": true,
              "id": 386
            },
            {
              "name": "Employee + Dependent Coverage",
              "price": null,
              "currency": "GBP",
              "is_enabled": true,
              "id": 387
            }
          ]
        }
      ]
    }
  }
}
```

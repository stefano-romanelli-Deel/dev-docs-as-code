---
title: "Payslips"
slug: "payslips"
excerpt: ""
hidden: true
createdAt: "Fri Oct 27 2023 11:12:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:34:39 GMT+0000 (Coordinated Universal Time)"
---
Gone are the days of painstakingly fetching employee payslips from Deel, a slow and error-prone process. Welcome to a new era with Deel Global Payroll API, where automatically retrieving employee payslips is a breeze! 

Our Payslips API is a game-changer, making it possible to easily access and download a list of payslips for each employee in PDF format. This presents a great opportunity to seamlessly integrate GP payslips into your HRIS (Human Resources Information System) to streamline the payroll process, reduce manual intervention, and improve overall efficiency. 

# Implemented Features

1. Get Payslips: An API endpoint that allows authorized users to retrieve payslips for a specific employee.
2. Download Payslip PDF: An API endpoint that allows authorized users to download the pdf file for a specific payslip.

# Get Payslips

You get a worker's payslip by sending an HTTP request to the URL below. Your request should contain:

1. **Method**: GET
2. **Authorization**: Bearer token
3. **Worker ID**: The ID for the worker whose payslip you're looking to retrieve

If all required fields in your request are available and accurate, the response will be details of the requested payslips.

## Sample Request & Response

**Request URL**

```curl
GET https://api.letsdeel.com/rest/v2/gp/workers/:worker_id/payslips
```

**Samples**

```Text Request
GET curl --location 'https://api.letsdeel.com/rest/v2/gp/workers/2d23cb84-5b40-2432-99e4-b325b7d68403/payslips' \
--header 'Authorization: Bearer {token}' \
```
```json Response
{
    "data": [
        {
            "id": "aKZMPQaRo46b",
            "from": "2023-10-25",
            "to": null,
            "status": "PUBLISHED"
        },
        {
            "id": "RAWe1rRx2r63",
            "from": "2023-09-01",
            "to": "2023-09-30",
            "status": "PUBLISHED"
        }
    ]
}
```

# Download Payslip PDF

You can download a payslip by sending an HTTP request to the URL below. Your request should contain:

1. **Method**: GET
2. **Authorization**: Bearer token
3. **Worker ID**: The ID for the worker whose payslip you're looking to download
4. **Payslip ID**: The ID for the payslip you're looking to download

If all required fields in your request are available and accurate, the response will be a url of the payslip to be downloaded (PDF).

## Sample Request & Response

**Request URL**

```Text cURL
GET https://api.letsdeel.com/rest/v2/gp/workers/:worker_id/payslips/:payslip_id/download
```

**Samples**

```Text Request
GET curl --location 'https://api.letsdeel.com/rest/v2/gp/workers/2d23cb84-5b40-2432-99e4-b325b7d68403/payslips/aKZMPQaRo46b/download' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "data": {
        "url": "https://s3.eu-west-1.amazonaws.com/api-dev-eks.letsdeel.com/employee_payslips/aMKZRQaPo46b_Payslip_Davidovski202023-09-26_Andrzej_2023-10-25.pdf?AWSAccessKeyId=ASIATHF2L5PZV6OC5XOY&Expires=1698657306&Signature=Kt3drSM0UwhQaYumf8zsRUPJHdY%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEKn%3G%3G%3G%3G%3G%3G%3G%3G%3G%3GwEaCWV1LXdlc3QtMSJGMEQCIDd3gbetnudR8OjMF82aN3qsnFf44aQwY5PlX7YPSPPhAiBKBF9nJgV0n1VpgZxjiyrvtnaet1pqlUFKtYOZ7561mCqFBQjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAMaDDIyMTU4MTY2NzMxNSIMQNjMe%2F9VZb7JACSUKtkELxUt0Y93HLANBAZ1ny9ypvFsy%2BKizwa%2BOy7LRoXaZ3ZWdpNyKPE9O8YTNzgA%2BZqKTgayI8SEb6oIof7jqWVYlYqkwZjeepqIaI0YufOqTqv11jHX%2BrhUj688XFZIYGz%2FmF6io7s0mKlRBg%2FLExv2Zn2X%2FSzC9pXvY8QXPVSUSkDIgipLfZ%2FlY2VDC0P4CBlOePjl%2F%2Be%2FvMrFnDVFS4yQLDVEgRRN6vOt4qF%2FyfOGo2xTreylu1vT0PJWJAiMhjefV0sO69XpSX9VD1t8w5W0dqd7i5Bdfdoxlq2DokwaLFRnJqif3DEd%2FQrrqVL6VQWwOnhmQwfLnr66mPOMshIZfL49Gfb9rz0WiARDLgEwyhbSDMJa03xQoSi7XGu1%2B1gQllOtdG8dXfKajQD4gjO1%2BAQi%2B4IETG3V5Ae8nsL2xMY3GfdwLpQtGkb85yKBzpVzfvmFPbEhibWNKbTVBKxGHraaNvOu0dK43xrPCmkdvfG2VRmqhNYJkjO6VDQWLoC6oc2CYbJDpXhxrPMykREnI13WHeS00CrEtys2bh%2FbXToz%2BuSwNnpiq7HWkHvGd6lB%2BTYY9P8pwWbnkEMepXBV8Qo2RESxmqHNOnQAkqg0KbwbpQI5SIFAyzM64D3KtaojYopTb3vL1rT9i2Fh%2F9yTpvEWoU42ZRZdV%2BpSEXqYM%2FgI%2BVkr0xMim0SLwi9ChWEfREU4dF4M9AVkAj7yHR0dMPDyZlzMz1RhD4cUE%2BsjN6wBcTov2LKFHNtUoVkqtcAMwlwlzoH2MKzjkjCab3799b%2BXnZVdkHEjnTDu5f2pBjqbAb89TCOkLgL5je7jPfsegdroxL5krWBICkG2dlIO%2FWmI59m9GqNj6S1ZJV6Fj1Bnvriv732sba1dRZN2ujbUiKZ3AM5JadaGv0m3KVwmZdMAHCO%2FayNmBKC3Bpwht1YoPmle1Nd3El25HiooHaC7Qra65zwiLz3uExbPC79v6%2FhTrghzUZGKg1LGUQP38uM%2B8xNLAjBoRRCwG8RS"
    }
}
```

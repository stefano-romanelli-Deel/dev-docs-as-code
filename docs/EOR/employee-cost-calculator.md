---
title: "Employee Cost Calculator"
slug: "employee-cost-calculator"
excerpt: ""
hidden: false
createdAt: "Tue Feb 20 2024 13:00:32 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:33:33 GMT+0000 (Coordinated Universal Time)"
---
The Employee Cost Calculator API integrates a powerful cost calculation feature into your software, helping you figure out the total cost of hiring someone, including their salary, benefits, and other employer expenses. Here's a simplified guide to get you started:

# Getting Started with the Cost Calculator API

## Step 1: Prepare Your Request Parameters

Before you start, ensure you have the following data ready:

| Parameter | Description                             | Type   | Example     |
| :-------- | :-------------------------------------- | :----- | :---------- |
| Country   | The country where the employee is based | string | Netherlands |
| Salary    | The employee's monthly salary           | int    | 5000        |
| Currency  | The currency for the salary             | string | EUR         |

## Step 2: Make Your API Request

Use the following template to create your API request - sending the values of the indicated parameters to our API.

**Sample Request:**

```
curl --location 'https://api.letsdeel.com/rest/v2/eor/employment_cost' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--data '{
    "data": {
        "country": "Netherlands",
        "salary": 5000,
        "currency": "EUR",
    }
}'
```

Remember to replace token in the example below with your actual API token.

## Step 3: Analyze the API Response

If your API request is successful, you'll receive a response containing detailed cost information. Here's how to interpret the key components:

**Sample Response:**

```
{
    "salary": "5000.00",
    "currency": "EUR",
    "country": "Netherlands",
    "country_code": "NL",
    "frequency": "Monthly",
    "deel_fee": "549.91",
    "severance_accural": "0.00",
    "total_costs": "7262.68",
    "employer_costs": "914.00",
    "costs": [...],
    "benefits_data": [
		 ],
    "additional_data": {
        "additional_notes": [
        ]
    }
}
```

Response Fields:

1. `salary`, `currency`, `country`: Confirm these values match your request.
2. `deel_fee`: The fee charged by the Deel (in input currency).
3. `severance_accural`: Any severance costs accrued.
4. `total_costs`: The total cost of employing the individual, including salary, deel fee, and additional costs.
5. `employer_costs`: Costs borne by the employer, separate from the salary.
6. `benefits_data`: Details of any benefits included in the total costs.
7. `additional_data`: Any additional notes or information relevant to the employment costs.

# Using Cost Calculator API with Benefits

Integrating benefits into your employment cost calculations can provide a more accurate picture of overall expenses. Follow these steps to include benefits like health insurance and pension in your calculations using the Employee Cost Calculator API.

## Step 1: Check for Available Benefits

To find out what benefits (like health insurance or pension) are available in your employee's country using the API, make a request to the following endpoint.

**Sample Request**

```
curl --location 'https://api.letsdeel.com/rest/v2/eor/validations/NL' \
--header 'Authorization: Bearer {token}'
```

**Expected Response**

```
{
    "data": {
        "currency": "EUR",
        "health_insurance": {
            "status": "DISABLED",
            "providers": []
        },
        "pension": {
            "status": "ENABLED",
            "providers": [
                {
                    "id": "01c60f26-fe0e-48f3-82d5-b899848eee7b",
                    "name": "Nationale Nederlanden",
                    "home_page_url": "https://www.nn.nl/"
                }
            ]
        },
        "mandatory_fields": [... ]
    }
}
```

Note: Focus on the providers parameter under each benefit type to find available options with their respective ids.

## Step 2: Calculate Costs With Benefits

Adjust your API request to include benefits, adding the provider_id for any benefit you want to consider.

**Sample Request with Benefits:**

```
curl --location 'https://api.letsdeel.com/rest/v2/eor/employment_cost' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--data '{
    "data": {
        "country": "Netherlands",
        "salary": 5000,
        "currency": "EUR",
        "benefits": [{
            "provider_id": "01c60f26-fe0e-48f3-82d5-b899848eee7b"
        }
        ]
    }
}'
```

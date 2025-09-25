---
title: "Getting Started"
slug: "getting-started-3"
excerpt: ""
hidden: false
createdAt: "Wed Jun 07 2023 08:36:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:38:16 GMT+0000 (Coordinated Universal Time)"
---
Getting started with the Onboarding API is easy:

1. Create an OAuth app.
2. Authorize users. 
3. Create candidates. 

# Create an OAuth App

Onboarding API requires an OAuth app. To get started as a partner, create an OAuth App in Deel. You can follow [this guide](https://developer.deel.com/docs/oauth2-apps) to create OAuth app in Deel. Once you create an OAuth app, follow the [OAuth - Getting Started](https://developer.deel.com/docs/getting-started-1) guide to implement OAuth in your app.

# Authorize users

Once you implement OAuth in your application, enable your users to connect Deel to your organization. 

> 📘 Please make sure to ask for **candidates:write** scope permission. It is required to create candidates. It is also the only scope you will need for this API write access.

![](https://files.readme.io/2c03843-pika-1686127301828-1x.png)

After retrieving the access token, you can make API calls to create candidates in Deel. 

# Create a Candidate

**Request URL**

```curl
POST https://api.letsdeel.com/rest/v2/candidates
```

**Request Body**

```json
POST 'https://api.letsdeel.com/rest/v2/candidates' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--header 'x-client-id: {client_id}' \
--data-raw '{ 
    "data": {
      "id": "dhzj64mgen",
      "first_name": "Taylor",
      "last_name": "Swift",
      "status": "offer-accepted",
      "link": "https://your-ats.com/path/to/candidate/dhzj64mgen",
      "email": "taylor@swift.com",
      "nationality": "US",
      "country": "US",
      "state": "PA",
      "job_title": "Singer",
      "start_date": "2023-06-30",
    }
}'
```

**Response Body**

```
{
    "data": {
        "created": true
    }
}
```

**Fields**

| Field | Description | Required | Enums |
| :--- | :--- | :--- | :--- |
| id | Candidate's unique identifier in your system | Yes |  |
| first_name | Candidate's first name. | Yes |  |
| last_name | Candidate's last name. | Yes |  |
| status | Offer status. | Yes | offer-accepted, offer-sent, offer-declined,  
offer-deleted |
| link | Link to the candidate's profile in your system. | Yes |  |
| start_date | Expected start date. | Yes |  |
| email | Candidate's expected email. |  |  |
| nationality | Candidate's nationality. |  |  |
| country | Country where this job is located. |  |  |
| state | State where this job is located. |  |  |
| job_title | Job title. |  |  |

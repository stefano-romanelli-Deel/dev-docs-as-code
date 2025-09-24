---
title: "Candidates"
slug: "candidates"
excerpt: ""
hidden: false
createdAt: "Wed Jun 07 2023 08:34:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:37:56 GMT+0000 (Coordinated Universal Time)"
---
With SCIM API you can create candidates in Deel.

## Create a Candidate

**Request URL**

```curl
POST https://api.letsdeel.com/rest/v2/candidates
```

**Request & Response**

```json Request
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
```json Response
{
    "message": "Ok"
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

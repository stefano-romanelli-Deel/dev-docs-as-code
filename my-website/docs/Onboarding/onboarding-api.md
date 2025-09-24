---
title: "Introduction"
slug: "onboarding-api"
excerpt: ""
hidden: false
createdAt: "Tue May 23 2023 08:51:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:38:28 GMT+0000 (Coordinated Universal Time)"
---
Onboarding API enables Deel partners to onboard candidates in Deel. You can make an API call with minimal input to create a candidate in Deel.

```curl
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
      "email": "taylor@swift.com"
    }
}'
```

Candidates created with the API will show up in Deel at the top of the People list. Clients can click the "Review & Onboard" button to onboard candidates.

![](https://files.readme.io/723ec9c-pika-1685023814761-1x.png)

A client can click Onboard next to a candidate to onboard that candidate.

![](https://files.readme.io/f1ba5f9-pika-1685023833000-1x.png)

When the client clicks the "Onboard" button, they are taken to the Add People page where they can add this person to Deel.

![](https://files.readme.io/c98a8b6-pika-1685023850289-1x.png)

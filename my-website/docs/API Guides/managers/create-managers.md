---
title: "Create Managers"
slug: "create-managers"
excerpt: ""
hidden: false
createdAt: "Tue Jul 18 2023 11:24:06 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 13:50:52 GMT+0000 (Coordinated Universal Time)"
---
To add new managers to your Deel account, hit the `/v2/managers` endpoint with the following parameters:

- `first_name`
- `last_name`
- `email`

After successfully executing the API call, a `201` response will be generated, confirming the successful creation of the new manager profile. 

# Sample Request & Response

**Request URL**

```curl
POST https://api.letsdeel.com/rest/v2/managers
```

**Request & Response**

```json Request
POST 'https://api.letsdeel.com/rest/v2/managers' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {token}' \
--header 'x-client-id: {client_id}' \
--data-raw '{ 
    "data": {
            "first_name": "Nic",
            "last_name": "Jokic",
            "email": "nic@jokic.com",
    }
}'
```
```json Response
{
    "data": {
        "id": "728445",
        "first_name": "Nic",
        "last_name": "Jokic",
        "email": "nic@jokic.com"
     }
}
```

***

# UI Representation

To see the added manager on your Deel dashboard, go to **Organization Settings** and select the **Managers** tab to see a list of added managers. Upon refreshing the user interface, you'll notice the inclusion of the newly created manager profile.

![](https://files.readme.io/ccc85f5-create-manager.png)

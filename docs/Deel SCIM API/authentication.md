---
title: "Authentication"
slug: "authentication"
excerpt: ""
hidden: false
createdAt: "Tue Mar 28 2023 12:51:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
Deel SCIM API uses Organization tokens to authenticate requests. A bearer token is required to authenticate all API requests.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

```
curl -X GET 'api.letsdeel.com/scim/v2/Users' \
-H 'Authorization: Bearer YOUR-TOKEN-HERE'
```

**Generating Access Tokens**

1. Navigate to **Apps & Integrations > Developer Center**.
2. On the organization tokens tab, click on the “Generate New Token” button.
3. In the popup, name your token and select your scopes (at least `users:read`)
4. Make sure to copy and save your token once is generated. You won't be able to see it again!

![](https://files.readme.io/3fe9d1e-Screenshot_2023-03-28_at_17.50.38.png "Screenshot 2023-03-28 at 17.50.38.png")

**OAuth 2.0 for API partners**

Deel SCIM API only supports Organization apps. Please make sure to select the organization app type when creating an OAuth app for SCIM API integration. Get started with Deel OAuth 2.0 [here](https://developer.deel.com/docs/getting-started-1).

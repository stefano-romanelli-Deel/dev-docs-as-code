---
title: "Token Rotation"
slug: "token-rotation"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 12:42:59 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:22:55 GMT+0000 (Coordinated Universal Time)"
---
API credentials should be changed regularly. Employees leave, API credentials can be accidentally committed to version control, and wide-reaching security flaws can be discovered. While these situations pose security risks, in most cases you can address them without causing any downtime for your app by rotating your API credentials.

## Request a new access token

Refresh each access token stored by your application by requesting new tokens. Use basic authorization with your `client_id` as login and `client_secret` as a password:

```
curl --location --request POST 'https://app.deel.com/oauth2/tokens' \
--header 'Authorization: Basic {gHukem719Tg1EhqEzGeq9iAfPIuatCKHAoFLG}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token={refresh_token}' \
--data-urlencode 'redirect_uri={redirect_uri}'
```

### Request Body

Please use the following parameters in the request body:

| Parameter     | Description                                                                                                                                        |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| grant_type    | Identification of the grant type. Please use `grant_type=refresh_token`.                                                                           |
| refresh_token | The refresh code your app received in [step 4](https://developer.deel.com/docs/getting-started-1#step-4-get-an-access-token).                      |
| redirect_uri  | The URL to which the user is redirected after authorizing the app. The complete URL specified here must match the redirect URI provided in step 1. |

### Authentication

Please use the Basic authentication method to authenticate this request, similar to in step 4.

### Response

The server responds with an access token:

```
{
    "access_token": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "expires_in": 2592000,
    "refresh_token": "IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
    "token_type": "Bearer",
    "scope": "contracts:read contracts:write"
}
```

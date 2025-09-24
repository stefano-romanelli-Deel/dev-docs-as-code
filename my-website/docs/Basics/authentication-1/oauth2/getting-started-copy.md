---
title: "Getting Started"
slug: "getting-started-copy"
excerpt: ""
hidden: true
createdAt: "Tue Aug 29 2023 02:16:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 13:54:20 GMT+0000 (Coordinated Universal Time)"
---
OAuth authentication may seem more complex than Basic authentication, but the enhanced security it provides justifies the extra steps. Deel, prioritizing user convenience, has streamlined its OAuth implementation to minimize redirects, simplifying the process even further. 

To successfully integrate OAuth, concentrate on these two primary steps:

1. Get app credentials
2. Get access tokens with OAuth

# 1. Get App Credentials

The first step is to secure your application's **key** `client Id` and **secret** `client secret` which serve as identifying credentials throughout the authorization journey. Follow the steps here to [create an app](https://developer.deel.com/docs/oauth2-apps). 

> 🚧 Copy and store your app secret (client secret) as it won't show again.

***

# 2. Get access tokens with OAuth

To secure access tokens using OAuth, follow these three sub-steps: request specific permissions (scopes) from the user, await their consent, and then exchange a temporary code for an access token.

## Ask for scopes

Before accessing user data, your app must obtain explicit permission. During app development, determine a concise list of [scopes](https://developer.deel.com/docs/scopes-1) that your app requires to function fully and whenever a user attempts to link Deel with your app, present these permissions for their approval.

To ask for scopes, redirect the user to `https://auth.letsdeel.com/oauth2/authorize`

> 📘 Sandbox
> 
> When using the sandbox, use [https://auth-demo.letsdeel.com](https://auth-demo.letsdeel.com) as the host URL for OAuth.

The full redirect URL looks something like this:

```
https://auth.letsdeel.com/oauth2/authorize?client_id=1c2ccb6b-avds-47c1-a6n1-dfd29kh8dye4&redirect_uri=https%3A%2F%2Fexample.com%2Fredirect&scope=contracts%3Aread%20contracts%3Awrite%20organizations%3Aread&response_type=code&state=fp1eh3jkly
```

| Query parameter | Description                                                                                                                                                                                                                                                                                                                        |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client_id       | Client id for the app.                                                                                                                                                                                                                                                                                                             |
| redirect_uri    | The URL to which the user is redirected after authorizing the app. The complete URL specified here must match the redirect URI provided in step 1.                                                                                                                                                                                 |
| scope           | Encoded space-separated list of scopes. For example, to create contracts and read contracts use `scope=contracts%3Aread%20contracts%3Awrite`.                                                                                                                                                                                      |
| response_type   | Expected response type. Always use `response_type=code`.                                                                                                                                                                                                                                                                           |
| state           | A randomly selected value provided by your app is unique for each authorization request. During the OAuth2 callback, your app must check that this value matches the one you provided during authorization. This mechanism is important for the [security of your app](https://datatracker.ietf.org/doc/html/rfc6819#section-3.6). |

When the user arrives at your redirect URL, Deel shows the following prompt to receive authorization from the user:

![](https://files.readme.io/d158b1b-perm2.png)


![](https://files.readme.io/ccc402e-perm-end.png)


***

## Wait for user to give permission

Once the user clicks on the **Allow** button (_as indicated in the image above_), your app gets the green light to access the specified scopes. Subsequently, they will be redirected back to your app's server with the authorization_code included in the redirection URL.

```
https://example.com/redirect?code={authorization_code}&state={state}
```

> 🚧 Before proceeding, ensure your app verifies the state parameter. It should match the value given to Deel.

***

## Exchange a temporary code for a full access token.

Once the security check is verified successfully, you're set to swap the authorization code for an access token, which boasts a more extended validity period. Here's how you can make that request to Deel:

### Authorization

Structure your Authorization header as follows:

`Authorization: Basic <credentials>`

To authenticate this request, use the Basic authentication method.

Constructing the Encoded Credentials:

1. **Combine Credentials**: Join the app's client_id and client_secret using a colon (:).  
   For example, if they are `wwsfnelo80` and `0afs7xv0d9` respectively, your combined string should be `wwsfnelo80:0afs7xv0d9`.
2. **Encode in Base64**: Encode the combined string using [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64) encoding. From our example, this produces `d3dzZm5lbG84MDowYWZzN3h2MGQ5`.

Thus, the final request would have the header:

```
Authorization: Basic d3dzZm5lbG84MDowYWZzN3h2MGQ5
```

| Type     | Parameter     | Description                                                                                                                                        |
| :------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| Request  | grant_type    | Identification of the grant type. Please use `grant_type=authorization_code`.                                                                      |
|          | code          | The authorization code your app received in step 3.                                                                                                |
|          | redirect_uri  | The URL to which the user is redirected after authorizing the app. The complete URL specified here must match the redirect URI provided in step 1. |
| Response | access_token  | The access token that can be used to authenticate requests to Deel API.                                                                            |
|          | expires_in    | The number of seconds this token is valid for after being generated.                                                                               |
|          | refresh_token | A refresh token can be used to rotate the access token when expired.                                                                               |
|          | token_type    | Deel access tokens are Bearer tokens.                                                                                                              |
|          | scope         | List of scopes this token grants access to.                                                                                                        |

## Sample Request & Response

```Text Request
POST 'https://auth.letsdeel.com/oauth2/tokens' \
--header 'Authorization: Basic d3dzZm5lbG84MDowYWZzN3h2MGQ5' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code={authorization_code}' \
--data-urlencode 'redirect_uri={redirectUri}'
```
```Text Response
{
    "access_token": "MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3",
    "expires_in": 2592000,
    "refresh_token": "IwOGYzYTlmM2YxOTQ5MGE3YmNmMDFkNTVk",
    "token_type": "Bearer",
    "scope": "contracts:read contracts:write"
}
```

***

## Make authenticated requests

After your app has obtained an API access token, it can make authenticated requests to the Deel API. These requests are accompanied by these headers: `Authorization: Bearer {access_token}` and `x-client-id: {client_id}` where `{access_token}` is replaced with the access token retrieved in step 4 and `{client_id}` is replaced with the `client_id` retrieved in step 1.

The following example shows how to retrieve a list of contracts using the Deel API.

```Text Request
curl -X GET 'https://api.letsdeel.com/rest/v2/contracts' \
--header 'Authorization: Bearer MTQ0NjJkZmQ5OTM2NDE1ZTZjNGZmZjI3'
--header 'x-client-id: {client_id}'
```

***

## Token validity

The OAuth2 access token is valid for `2592000` seconds (30 days) after generation. Refresh tokens are valid for `7776000` seconds (90 days) after being generated.

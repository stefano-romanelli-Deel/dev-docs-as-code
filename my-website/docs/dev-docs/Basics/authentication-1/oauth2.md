---
title: "OAuth2"
slug: "oauth2"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:26:09 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
# Introduction to OAuth2

OAuth 2.0 is the industry-standard protocol for authorizing or giving permissions to apps. This differs from authentication, which is the process of verifying the identity of the user or the app.

# The OAuth2 flow

Deel uses OAuth 2.0’s [authorization code grant flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) to issue access tokens on behalf of users. The OAuth2 flow is used so that clients can authorize apps to access data in their accounts. For example, an app might be authorized to access contracts and invoices data in an organization.

The following diagram illustrates the OAuth flow based on the actions of the user, your app, and Deel:

![](https://files.readme.io/383529f-auth-flow.png "auth-flow.png")

1. The user makes a request to connect to Deel.
2. The app redirects to Deel to load the OAuth2 grant screen and requests the user to authorize the required scopes.
3. The user authorizes the app by consenting to the requested scopes.
4. The app receives an authorization code. This is a temporary credential representing the authorization.
5. The app requests an access token by authenticating with Deel and presenting the authorization code and their client/app credentials.
6. Deel authenticates the app, validates the authorization code, and then issues and returns an access token and a refresh token. The app can now request data from Deel.
7. The app uses the access token to make requests to the Deel API together with their client/app ID.
8. Deel validates the access token and allows access to the requested RESTful resource e.g. getting a list of contracts according to the OAuth2 permission scopes.

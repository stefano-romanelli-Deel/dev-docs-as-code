---
title: "Create a Magic Link"
slug: "creating-magic-links"
excerpt: ""
hidden: false
createdAt: "Wed Aug 13 2025 10:52:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Aug 21 2025 13:56:46 GMT+0000 (Coordinated Universal Time)"
---
Magic Links enable your workers to access Deel directly from your platform, without entering their email or password.

By generating a secure, one-click login session, you can embed Deel directly into your product. This ensures workers can move between your platform and Deel without interruption.

Key benefits of using Magic Links include:

- **Frictionless authentication**: Workers access Deel without entering credentials, improving the user journey across integrated platforms.
- **Custom integration**: Maintain full control over how and where the login experience appears in your app or workflow.
- **Secure, session-based access**: Each link is tied to a verified worker session with limited lifetime, ensuring safe authentication.
- **Improved engagement**: Simplifying access reduces barriers for workers to complete their tasks.

Magic Links are available via the Deel API and require a valid worker session token to generate. This guide covers how they work and how to use them.

Use the following steps to generate a magic link that allows a worker to access Deel through your platform.

1. [Generate an organization access token](https://developer.deel.com/docs/creating-magic-links#step-1---generate-an-organization-access-token)
2. [Create a worker token](https://developer.deel.com/docs/creating-magic-links#step-2---create-a-worker-token)
3. [Generate Magic Link](https://developer.deel.com/docs/creating-magic-links#step-3---generate-magic-link)
4. [Using the Magic Link](https://developer.deel.com/docs/creating-magic-links#step-4---using-the-magic-link)

##  Step 1 - Generate an organization access token

Follow the [API Tokens](https://developer.deel.com/docs/api-tokens-1) guide to generate a new organization token. The overall process remains the same, with the following exceptions:

- Step 4: When selecting scopes, make sure to include `admin:worker`.
- Step 5: Under **Sensitive data**, turn both toggles off to avoid requesting unnecessary access.

> 📘 To access this scope, the `orgsAllowedAdminScopesEnabled` feature flag must be enabled for the organization. This flag is managed in the Integrations service.

## Step 2 - Create a worker token

To create a worker token, follow the steps outlined in the [Managing worker tokens](https://developer.deel.com/docs/managing-worker-tokens) guide. The relevant section provides details on generating a session token for a worker.

> 📘 The `profile_id` must be the worker’s public HRIS profile ID. Make sure the profile belongs to your organization and is associated with a valid user. This ID is required to generate the worker session token, which is used to create the Magic Link.

## Step 3 - Generate Magic Link

Once you have a valid worker session token, use the [POST /rest/v2/magic-link](https://developer.deel.com/reference/createmagiclink) endpoint to generate a login session. There are two available modes depending on how you want to guide the worker's experience.

- [Option A: Engage learning mode](https://developer.deel.com/docs/creating-magic-links#option-a-engage-learning-mode)
- [Option B: General white-label mode](https://developer.deel.com/docs/creating-magic-links#option-b-general-white-label-mode)

### Option A: Engage learning mode

Use this mode when the worker should stay in a locked learning journey, without navigating away from the assigned resources.

```curl
curl -X POST 'https://api-gateway.deel.training/rest/v2/magic-link' \
-H 'x-auth-token: WORKER_SESSION_TOKEN' \
-H 'Content-Type: application/json' \
-d '{
  "data": {
    "redirect_path": "/learning/resources/enrolled",
    "on_success_redirect_url": "https://google.com/"
  }
}'
```

What happens:

- The worker is redirected to the specified learning path.
- Journey-only mode is activated, preventing the worker from navigating elsewhere within Deel.

### Option B: General white-label mode

Use this mode for a standard login experience. The worker lands on the specified page and can continue using Deel.

```curl
curl -X POST 'https://api-gateway.deel.training/rest/v2/magic-link' \
-H 'x-auth-token: WORKER_SESSION_TOKEN' \
-H 'Content-Type: application/json' \
-d '{
  "data": {
    "redirect_path": "/workforce-planning/onboarding"
  }
}'
```

What happens:

- The worker is redirected to the given path inside Deel.
- They can navigate freely throughout the platform.

### Response example

Both modes return a secure Magic Link and its expiration time.

```json
{
  "data": {
    "magic_link": "https://dev.deel.wtf/login/session token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9",
    "expires_at": "2025-07-11T16:32:49.600Z"
  }
}
```

## Step 4 - Using the Magic Link

Once you receive the magic\_link from the API response, open the URL in your browser to start the worker session.

**Example URL**:

```text
https://dev.deel.wtf/login/session?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
```

When the link is opened:

- The frontend detects that this is a Magic Link token, not a standard login.
- If another user is currently signed in, they’ll be automatically logged out.
- Deel verifies that the toke n is valid, not expired, and has not already been used.
- Magic Link configuration is saved to `localStorage.magicLinkConfig`.
- If `on_success_redirect_url` was included, journey-only mode is activated.
- The worker is redirected to the `redirect_path` you specified in the request.

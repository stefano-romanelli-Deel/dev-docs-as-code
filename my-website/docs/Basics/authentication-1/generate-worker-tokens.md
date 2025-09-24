---
title: "Generate worker tokens"
slug: "generate-worker-tokens"
excerpt: "Learn how to generate worker tokens to perform actions on behalf of workers"
hidden: true
createdAt: "Fri May 16 2025 16:31:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Sep 23 2025 13:54:43 GMT+0000 (Coordinated Universal Time)"
---
If you're an organization using [White Label](https://help.letsdeel.com/hc/en-gb/articles/28670391654929) and want to handle the full worker lifecycle—hiring, onboarding, payroll, and so on—through your own application, you can use worker tokens. Worker tokens lets you perform actions on behalf of your EOR workers without them ever needing to log into Deel.

> 👍 Worker tokens are supported for EOR workers

Worker tokens allow an organization to authenticate as a worker and perform actions on their behalf. This lets you build applications where you can securely handle worker operations such as signing contracts, uploading documents, or retrieving payslips.

> 📘 Get the worker's legal consent first
> 
> Performing actions on behalf of a worker may have legal implications. We recommend that you get the worker's legal consent first.

![](https://files.readme.io/75f6ca758c3dd04191b4f26652644c8b7c77ec85104f17582e88b0f4ae312d76-worker-token-diagram.png)


## Before you begin

Before generating worker tokens, ensure the following prerequisites are met:

- [White Label](https://help.letsdeel.com/hc/en-gb/articles/28670391654929-Overview-White-Label) enabled for your organization.
- The ability to generate worker tokens for your organization. Ask your Deel representative to enable this feature for you.

## Step 1. Obtain an org token

To generate worker tokens, you will need to obtain an org-wide token that includes the scope `admin:worker`, along with the scopes required to create a contract or retrieve contract information:

- Contracts:
  - If you have already created a contract, `contracts:read`
  - If you have not created a contract yet, `forms:read`, `contracts:read`, `contracts:write`, and `organizations:read`
- Generate worker tokens: `admin:worker`

To obtain an org token, you can follow the steps [API tokens](https://developer.deel.com/docs/api-tokens-1).

## Step 2. Retrieve the contract ID

The contract ID is needed to create a worker profile. There are 2 ways to obtain the contract ID, depending on whether you have already created a contract or not:

- If you have already created a contract, you can use the [List contracts](https://developer.deel.com/reference/listofcontracts) endpoint to retrieve the contract ID.
- If you have not created a contract yet, you can create one following the steps in the [Create an EOR contract](https://developer.deel.com/docs/eor-create-contract) documentation. When the contract is successfully created, the `contract_id` is returned in the response. 

## Step 3. Create a worker profile

The worker profile is usually created when the worker goes through onboarding. This step allows you to create the worker profile in advance and obtain a profile ID, which you can then use to perform other operations such as obtaining a worker token.

Use the endpoint [Create EOR worker](https://developer.deel.com/reference/createeorworker) to create a new EOR worker profile.

> 👍 Retrieve profile ID for existing contracts
> 
> If you have already created a contract, you can use one of the following endpoints to retrieve the worker's profile ID:
> 
> - [List of people](https://developer.deel.com/reference/listofpeople), as `id`
> - [List of contracts](https://developer.deel.com/reference/listofcontracts), as `worker.id`

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor/worker \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "contract_id": "mp4y66j"
  }
}
'
```

A successful response (`200`) returns the `hris_profile_id` of the newly-created worker profile. You can use that to [generate the worker token](#step-4-generate-a-worker-token).

```json
{
  "data": {
    "user_id": "00000000-0000-0000-0000-000000000000",
    "profile_id": "00000000-0000-0000-0000-000000000000",
    "hris_profile_id": "00000000-0000-0000-0000-000000000000"
  }
}
```

## Step 4. Generate a worker token

Once you have the `hris_profile_id`, use the [Create worker access token](https://developer.deel.com/reference/createworkeraccesstoken) endpoint to generate a worker token.

> 📘 Worker token security
> 
> For security reasons, worker tokens only last for 24 hours and only 1 worker token can exist at a time for a given worker. When you stop meeting any of these requirements, you'll need to generate a new token.

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/workers/session \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'Authorization: Bearer {TOKEN}' \
     --data '{
  "data": {
    "hris_profile_id": "prf_xyz789uvw321"
  }
}'
```

Where:

- `hris_profile_id` is the `hris_profile_id` of the worker you want to generate a token for.
- `{TOKEN}` is your admin token with the `admin:worker` scope.

A successful response (`201`) returns the worker token and its expiration timestamp.

```json
{  
  "data": {  
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",  
    "expires_at": "2023-10-01T12:00:00Z"  
  }  
}
```

## Next steps

With the obtained token, you can start performing actions on behalf of the worker. This means that you can build custom interfaces that allow users to signing contracts, upload documents, track work, or receive payslips.

To confirm that the worker token is working correctly, you can also call [`GET /people/me`](https://developer.deel.com/reference/getpeopleme) with the token in the Authorization header.

```bash
curl -X GET "https://api.letsdeel.com/rest/v2/people/me" \
  -H "Authorization: Bearer {WORKER_TOKEN}"
```

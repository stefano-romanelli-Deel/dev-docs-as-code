---
title: "Invite a contractor"
slug: "invite-contractor"
excerpt: "Learn how to invite a contractor to sign the contract and complete the contract creation process"
hidden: false
createdAt: "Wed Aug 07 2024 10:43:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 25 2025 14:37:47 GMT+0000 (Coordinated Universal Time)"
---
After [you have signed the contract](https://developer.deel.com/docs/sign-contract), the independent contractor must also sign it. This guide explains how to invite the contractor to sign the contract using the API.

## Before you begin

To invite the contractor to sign the contract, make sure to have:

- The contract ID returned when [creating the contract](https://developer.deel.com/docs/create-contract)
- The contractor's email address

## Step 1. Sending the contract

To send the contract, make a `POST` request to the [Send contract to worker](https://developer.deel.com/reference/invitetosigncontract) endpoint.

```curl
curl --request POST \
    --url 'https://api.letsdeel.com/rest/v2/CONTRACT_ID/invitations' \
    --header 'accept: application/json' \
    --header 'authorization: Bearer TOKEN' \
    --header 'content-type: application/json' \
    --data '
{
  "data": {
    "email": "demo@email.com",
    "locale": "en",
    "message": "Welcome to Acme Corp! Please sign the contract. We look forward to start working with you."
  }
}
'
```

In the path:

| Name          | Required | Type   | Format | Description                                           | Example    |
| ------------- | -------- | ------ | ------ | ----------------------------------------------------- | ---------- |
| `CONTRACT_ID` | true     | string | UUID   | The ID of the contract that the contractor must sign. | `d3m0d3m0` |

In the body:

| Name      | Required | Type   | Format | Description                                                                            | Example                                                                                      |
| --------- | -------- | ------ | ------ | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `email`   | true     | string | email  | The email address of the contractor.                                                   | `demo@email.com`                                                                             |
| `locale`  | false    | string | ISO    | The language code for the invitation email. Uses a two-letter ISO 639-1 language code. | `en`                                                                                         |
| `message` | false    | string | -      | The message that will appear in the invitation sent to the contractor.                 | `Welcome to Acme Corp! Please sign the contract. We look forward to start working with you.` |

> 🚧 A note on emails
> 
> - If you're planning on creating a contract for testing purposes, don't use the same email used for the client account. Emails in the system must be unique and each one is linked to a separate account.
> - Emails are not sent out when using the sandbox, so you won't receive the invitation email. To test the contract signing process, follow the instructions in [Step 2. Test the contract signing as an Independent Contractor (from UI)](https://developer.deel.com/docs/invite-contractor#step-2-test-the-contract-signing-as-a-contractor-from-ui).

A successful response (`201`) returns a confirmation message that the invitation was sent and the contractor will receive the contract agreement to sign.

```json
{
  "data": {
    "created": true
  }
}
```

## Step 2. Test the contract signing as a Independent Contractor (from UI)

If you're on a [Sandbox](https://developer.deel.com/docs/sandbox), you can simulate the contract signing process as an contractor from the UI. When impersonating an contractor, keep in mind:

- Use a unique email address for the contractor account. If the email address already exists in the system, login issues may occur.
- Invitation emails are not sent in sandbox. Instead, locate the invite link directly from the UI.

To test the contract signing:

1. After [signing the contract](https://developer.deel.com/docs/sign-contract), log into your [Deel sandbox account](https://demo.deel.com/login).
2. Go to **People**, locate the contractor, and click on their name to open their profile.
3. On their profile page, under the **Contracts** card, click **View contract** for the one you would like to sign as an contractor.
4. On the contract page, click **Copy Invitation Link**.

![](https://files.readme.io/5ffb701d08f3db211b9463ae7db32e2a57b1efd7a0c61991f7b079b5f5070195-Screenshot_2024-09-03_at_11.46.23.png)


5. Open an incognito browser session and paste the invitation link.
6. Complete the onboarding process as an contractor. For detailed instructions on how to complete the creation of the contractor account, visit [Contractor Account Overview](https://help.letsdeel.com/hc/en-gb/articles/9940209181457-Contractor-Account-Overview).
7. Sign the contract. You can find it on the **Contracts** card on the home page. To sign the contract, open it and then click **Review & Sign**.

![](https://files.readme.io/dcfaf8547c2b4a187aaf26abb1c5c432dae02e676127a78be05f54ad68c7e126-Screenshot_2024-09-03_at_15.18.52.png)


> 📘 Additional forms or documents may be required
> 
> Based on the country of residence of the contractor or the country where the company has business in, as a contractor you may be required to fill additional forms or provide additional documents.

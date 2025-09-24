---
title: "Sign a contract"
slug: "sign-contract"
excerpt: "Learn how to sign a contract when hiring a contractor."
hidden: false
createdAt: "Mon Aug 05 2024 10:03:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 25 2025 14:35:27 GMT+0000 (Coordinated Universal Time)"
---
After [creating a contract](https://developer.deel.com/docs/create-contract), both you (the employer) and the independent contractor are required to sign the contract agreement. There are two ways to sign a contract:

- [Using Deel's default contract template](https://developer.deel.com/docs/sign-contract#sign-using-the-default-contract-template)
- [Using a custom contract template](https://developer.deel.com/docs/sign-contract#sign-using-a-custom-contract-template)

## Before you begin

To sign a contract, make sure to have:

- The contract ID returned when [creating the contract](https://developer.deel.com/docs/create-contract#7-make-the-api-request)
- (Optional) A [contract template ID](https://developer.deel.com/docs/sign-contract#sign-using-a-custom-contract-template) if signing with a custom template

## Sign using the default contract template

When signing a contract, the default contract template is used automatically when a custom contract template is not specified.

This section explains how to sign a contract using the default contract template.

### Step 1. (Optional) Preview contract agreement

Preview the contract agreement as HTML using the [Preview a contract agreement](https://developer.deel.com/reference/getcontractpreview) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/contracts/CONTRACT_ID/preview' \
     --header 'authorization: Bearer TOKEN' \
     --header 'accept: text/html' \
```

In the path:

| Name          | Required | Type   | Format | Description                              | Example  |
| ------------- | -------- | ------ | ------ | ---------------------------------------- | -------- |
| `CONTRACT_ID` | true     | string | UUID   | The ID of the agreement being previewed. | d3m0d3m0 |

A successful response (`200`) will return the contract agreement in HTML format.

```html
<!DOCTYPE html>
<html>
CONTRACT_CONTENT
</html>
```

In the body, `CONTRACT_CONTENT` is the contract agreement in HTML format.

### Step 2. Sign the contract

Once the contract has been [previewed](https://developer.deel.com/docs/sign-contract#step-1-retrieve-the-contract-template-id), both parties can sign it. By default, you are required to sign the contract first, and then invite the contractor to sign it afterwards.

To sign the contract, make a POST request to the [Sign contract](https://developer.deel.com/reference/signcontract) endpoint.

```curl
curl --request POST \
     --url 'https://api.letsdeel.com/rest/v2/contracts/CONTRACT_ID/signatures' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "client_signature": "Michael Scott"
      }
}
'
```

In the path:

| Name          | Required | Type   | Format | Description                          | Example  |
| ------------- | -------- | ------ | ------ | ------------------------------------ | -------- |
| `CONTRACT_ID` | true     | string | UUID   | The ID of the agreement being signed | d3m0d3m0 |

In the body:

| Name               | Required | Type   | Format    | Description                                 | Example       |
| ------------------ | -------- | ------ | --------- | ------------------------------------------- | ------------- |
| `client_signature` | true     | string | Full name | The name of the person signing the contract | Michael Scott |

A successful response (`200`) will return a confirmation message that the contract has been created.

```json
{
  "data": {
    "created": true
  }
}
```

## Sign using a custom contract template

You can also sign a contract using a custom template that was created in the UI.  
To do this, [retrieve the template ID](https://developer.deel.com/docs/sign-contract#step-1-retrieve-the-contract-template-id) and use it when previewing or signing the contract.

> 📘 Only showing additional parameters
> 
> This section expands on the default process for [signing a contract](#sign-using-the-default-contract-template), only additional calls and parameters are explained. Use these calls and parameters to complement the ones explained for the default process.

### Step 1. Retrieve the contract template ID

To retrieve the contract template ID, make a GET request to the [Get contract templates](https://developer.deel.com/reference/getcontracttemplates) endpoint.

```curl
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/contract-templates \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

A successful response (`200`) returns the list of the available contract templates. The `title` field can help identifying the template. Save the `id` of the contract template, you need it in the next steps to preview and sign the contract.

```json
{
  "data": [
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "title": "My demo contract template"
    },
    {
      "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
      "title": "My other demo contract template"
    }
  ]
}
```

### Step 2. Preview the contract agreement using a custom contract template

When [previewing the contract agreement](https://developer.deel.com/docs/sign-contract#step-1-retrieve-the-contract-template-id), a custom contract template can be used instead of the default one.

To preview the contract using a custom contract template, include its ID in the request body when making a GET request to the [Preview contract agreement](https://developer.deel.com/reference/getcontractpreview) endpoint.

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/contracts/CONTRACT_ID/preview?templateId=TEMPLATE_ID' \
     --header 'accept: text/html' \
     --header 'authorization: Bearer TOKEN'
```

In the query:

| Name          | Required | Type   | Format | Description                                            | Example                              |
| ------------- | -------- | ------ | ------ | ------------------------------------------------------ | ------------------------------------ |
| `TEMPLATE_ID` | false    | string | UUID   | The ID of the contract template to use for the preview | d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0 |

### Step 3. Sign the contract using a custom contract template

When signing the contract with a custom contract template, include the template ID in the request body of the [Sign contract](https://developer.deel.com/reference/signcontract) endpoint.

```curl
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/contracts/CONTRACT_ID/signatures \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "client_signature": "Michael Scott",
    "contract_template_id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
  }
}
'
```

In the body:

| Name                        | Required | Type   | Format | Description                                                                                                                                                                     | Example                                |
| --------------------------- | -------- | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `data.contract_template_id` | false    | string | UUID   | The ID of the contract template being used to sign the contract. When the `contract_template_id` is not specified, contracts are created with Deel's default contract template. | `d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0` |

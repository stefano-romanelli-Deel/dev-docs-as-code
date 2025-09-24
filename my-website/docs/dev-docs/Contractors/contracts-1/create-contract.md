---
title: "Create a contract"
slug: "create-contract"
excerpt: "Learn how to create a contract and start hiring independent contractors"
hidden: false
createdAt: "Fri Aug 02 2024 09:55:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 25 2025 13:53:31 GMT+0000 (Coordinated Universal Time)"
---
# Create a contract

Creating a contract is the first step to hiring an independent contractor through Deel. Contracts are created using the [Create contract](https://developer.deel.com/reference/createanewcontract) endpoint, with a shared payload structure and type-specific variations.

This guide explains the endpoints involved in the process and the high-level data structure, and will prepare you to create the various contract types available.

- [Fixed rate](https://developer.deel.com/docs/create-contract-fixed-rate)
- [Fixed rate pay as you go](https://developer.deel.com/docs/create-contract-payg-fixed)
- [Task based pay as you go](https://developer.deel.com/docs/create-contract-payg-task)
- [Milestone based](https://developer.deel.com/docs/create-contract-milestone)

## Before you begin

Before preparing the payload, make sure to retrieve:

- A valid [API token](https://developer.deel.com/docs/api-tokens-1) to authenticate your requests
- The legal entity ID from the [Get list of legal entities](https://developer.deel.com/reference/getlegalentitylist) endpoint
- The group ID from the [Get team list](https://developer.deel.com/reference/getteams) endpoint

> 👍 Other endpoints will be used to retrieve additional information needed to create a contract
> 
> We recommend becoming familiar with them:
> 
> - [GET job title list](https://developer.deel.com/reference/getjobtitlelist)
> - [GET seniority levels](https://developer.deel.com/reference/retrievesenioritylevels)

## Request payload structure

Use the [Create contract](https://developer.deel.com/reference/createanewcontract) endpoint to set up any contract. The difference between them is in the parameters that you pass in the request payload.

The request payload includes the contract details in the `data` object. The following sections explain each object in the payload, followed by a full sample request.

```curl Request payload
curl --request POST \
     --url 'https://api.letsdeel.com/rest/v2/contracts' \
     --header 'authorization: Bearer TOKEN' \
     --header 'content-type: application/json' \
     --data-raw '
{
  "data": {
    …
  }
}'
```

> 👍 Creating a contract with a custom PDF
> 
> You can also create a contract with a custom PDF. To do so, you must use `form-data` for the request body and attach the file. For example:
> 
> ```curl Request payload
> curl --request POST \
>      --url 'https://api.letsdeel.com/rest/v2/contracts' \
>      --header 'authorization: Bearer TOKEN' \
>      --header 'content-type: multipart/form-data' \
>      --form 'param1="value1"' \
>      --form 'param2="value2"' \
>      --form 'parent_param[child_param]="value3"' \
>      --form 'custom_contract_file=@"{path_to_pdf_file}"'
> ```
> 
> Where `{path_to_pdf_file}` is the path to the PDF file on your local machine.

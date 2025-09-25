---
title: "Signing an EOR contract"
slug: "eor-sign-contract"
excerpt: "Learn how to complete the contract signature process and onboard an EOR worker"
hidden: false
createdAt: "Wed Jul 09 2025 13:37:06 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 09 2025 14:36:08 GMT+0000 (Coordinated Universal Time)"
---
Signing a contract gives it legal validity. When hiring an EOR worker, there are 2 types of contracts that are created:

- One between you and Deel, that establishes the costs of employment, your role in the relationship with the worker being hired, and Deel's responsibilities as the employer of record.
- One between Deel, as the employer of record, and the worker, that formalizes the employment terms and initiates the legal working relationship with the employee.

This guide follows on the first contract, the one between you and Deel, and explains how to sign it in order to move the hiring process forward.

1. You sign the contract as the employer organization
2. We, Deel, sign the contract as the employer of record
3. The worker signs the contract

![](https://files.readme.io/1c3d0fe164bd0ae9983f3dc0172c910d3c7bffd0b41b99cf37162699b6c54dd9-eor-sign-contract-diagram.png)


## Step 1. Deel signs the contract

After you [create the contract](https://developers.deel.com/docs/eor-create-contract), we review the contract, issue the quote, and sign the contract.

- If the quote can be issued automatically, we also sign the contract automatically
- If the quote cannot be issued automatically, we issue the quote and sign the contract manually, which can take up to 24 hours

> 📘 Automatic signature depends on country-specific and job-scope validations
> 
> We automatically sign the contract only in some countries and only if the [job scope has been previously validated](https://developers.deel.com/docs/eor-create-contract#step-2-define-the-job-scope).

Until a contract is reviewed and signed by us, its status is `under_review`. When we sign it, the status changes to `waiting_for_client_sign`. The various methods to check the status of a contract are explained in [Step 3. Review the quote from Deel](https://developers.deel.com/docs/eor-create-contract#step-3-review-the-quote-from-deel).

## Step 2: You sign the contract

If, after [creating the contract](https://developers.deel.com/docs/eor-create-contract) and reviewing the [quote received](https://developers.deel.com/docs/eor-create-contract#step-3-review-the-quote-from-deel), you agree with the terms and costs, you can proceed to signing the contract. This action will initiate the creation of the employee agreement and the onboarding of the worker to the platform.

When signing a contract, you must to pass the `contract_id` returned when [creating the contract](https://developer.deel.com/docs/eor-create-contract#step-3-create-the-contract).

If you want to use a different contract template, you can pass the `template_id` of the template you want to use. You can retrieve it from the the [Retrieve contract templates](https://developer.deel.com/reference/retrievecontracttemplates) endpoint.

> 📘 New templates can only be created from the UI
> 
> For more information, visit [Creating a custom employee agreement template](https://help.letsdeel.com/hc/en-gb/articles/17327200583057-Creating-a-Custom-Employee-Agreement-Template).

To sign the contract, make a `POST` request to the [Sign a contract](https://developer.deel.com/reference/signcontract) endpoint.

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/contracts/37nex2x/signatures \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "client_signature": "Michael Scott",
    "contract_template_id": "12345"
  }
}
'
```

A successful response (`201`) returns a confirmation that the contract has been signed.

```json
{
  "data": {
    "created": true
  }
}
```

After you sign the contract, its status changes to `waiting_for_employee_contract`.

## Worker onboarding

At this point, we start preparing the employee agreement and send a welcome email to the worker. In the welcome email, they'll be asked to sign up to the platform and complete the onboarding process, which is required before they can sign the employee agreement.

Visit [Worker onboarding](https://developer.deel.com/docs/eor-worker-onboarding) for a step-by-step guide on the onboarding process.

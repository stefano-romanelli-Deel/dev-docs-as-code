---
title: "Onboarding as an EOR worker"
slug: "eor-worker-onboarding"
excerpt: "Learn how to complete the EOR hiring process by onboarding the EOR worker"
hidden: false
createdAt: "Wed Jul 09 2025 13:37:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 09 2025 13:38:26 GMT+0000 (Coordinated Universal Time)"
---
This guide walks you through the final phase of hiring an EOR employee, which consists in the worker onboarding and signing the employee agreement.

![](https://files.readme.io/65585dacad17585ca5fe9e843fa303e4a391d8bd0150c588c379fb4f004bdb71-eor-worker-onboarding-diagram.png)


## Step 1. Worker creates a Deel account

After you [sign an EOR contract](https://developers.deel.com/docs/eor-sign-contract), we start preparing the employee agreement and send a welcome email to the worker. In the welcome email, they'll be asked to sign up to the platform and complete the onboarding process, which is required before they can sign the employee agreement.

## Step 2: Onboarding

Onboarding consists in collecting additional country-specific information, compliance documents, and verifying the worker's identity. While the steps listed in this section don't have to be completed in the exact order, onboarding is only considered completed only after they have all been completed successfully.

> 🚧 Worker token required
> 
> For legal reasons, the submission of compliance documents must be done by the worker, so all the endpoints listed in this section require a worker token. Building a solution that involves worker actions assumes that they're built upon worker token authentication.
> 
> The ability to generate a worker token by the employer on behalf of the worker is currently in private beta. If you can't get a worker to generate their own token, reach out to your Deel representative and we'll enable the ability to generate tokens on the worker's behalf for you.

### Submit additional information

#### Retrieve the additional information required

Make a `GET` request to the [Get worker additional fields for EOR](https://developer.deel.com/reference/getworkeradditionalfieldsforeor) endpoint, passing the country code as a path parameter, to understand the country-specific fields required for onboarding, such as Tax ID or marital status.

```bash
curl --request GET \
     --url https://api-sandbox.demo.deel.com/rest/v2/forms/eor/worker-additional-fields/ES \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}'
```

A successful response (`200`) returns the list of fields. The following is an example and has been trimmed for brevity. For a full list of fields, visit the [API reference forGet worker additional fields for EOR](https://developer.deel.com/reference/getworkeradditionalfieldsforeor).

```json
{
  "data": [
    {
      "key": "tax_residence",
      "type": "string",
      "is_required": true,
      "ui_guide": {
        "label": "Tax Residence",
        "field_type": "select"
      },
      "values_allowed": ["Spain", "France", "Germany", "..."]
    },
    {
      "key": "phone",
      "type": "string",
      "is_required": true,
      "ui_guide": { "label": "Phone", "field_type": "phone" }
    },
    {
      "key": "dob",
      "type": "string",
      "is_required": true,
      "ui_guide": { "label": "Date of Birth", "field_type": "date" },
      "validation": [
        { "type": "REGEX", "value": "^.*$", "error_message": "Invalid date" }
      ]
    },
    {
      "key": "gender",
      "type": "string",
      "is_required": true,
      "ui_guide": { "label": "Gender", "field_type": "select" },
      "values_allowed": ["Male", "Female"]
    },
    {
      "key": "tax_resident_bl",
      "type": "string",
      "is_required": true,
      "ui_guide": {
        "label": "Beckham Law Resident?",
        "field_type": "select"
      },
      "values_allowed": ["Yes", "No"]
    },
    {
      "key": "passport_number",
      "type": "string",
      "is_required": true,
      "dependencies": [{ "key": "id_type", "value": "Passport" }]
    },
    {
      "key": "dependent1_birth_year",
      "type": "number",
      "dependencies": [
        { "key": "how_many_dependents_do_you_have", "value": { "op": "gt", "value": "0" } }
      ]
    }
  ]
}
```

#### Submit the additional information

You can now use the information retrieved in the [previous step](#retrieve-the-additional-information-required) and make a `POST` request to the [Add additional information](https://developer.deel.com/reference/addadditionalinformation) endpoint, passing the contract ID as a path parameter, to submit the additional information required.

```bash
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor/workers/contracts/{CONTRACT_ID}/additional-information \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "is_payslip_access_allowed": true,
    "is_compliance_access_allowed": true,
    "city": "Málaga",
    "phone": "+3412345678",
    "state": "Andalusía",
    "street": "Calle Soleada",
    "zip_code": "12345",
    "tax_residence": "ES"
  }
}
'
```

A successful response (`200`) returns a confirmation that the additional information has been submitted.

```json
{
  "data": {
    "updated": true
  }
}
```

### Handle compliance documents

To fulfill compliance obligations, workers must also submit compliance documents. This section explains how to gather all the required documents and submit them.

#### Retrieve the list of required documents

Use the [List of employee compliance documents](https://developer.deel.com/reference/listofemployeecompliancedocuments) to retrieve required documents. The list returned is based on the worker's country, which is automatically determined from the token. Note down the ID of the documents, because it will be needed to [upload the documents](#upload-compliance-documents).

> 📘 This request requires a worker token.

```bash
curl --request GET \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor/workers/compliance-documents \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}'
```

A successful response (`200`) returns the list of compliance documents that the worker must submit.

> 📘 Some documents require using a template
> 
> When that's the case, the response contains a `has_template: true` parameter. Note down the ID of the documents that require using a template, and use it to [retrieve the template](#retrieve-templates). You will later fill out the template to submit the document.

```json
{
  "data": {
    "documents": [
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "I-9",
        "description": "The I-9 form, formally titled \"Employment Eligibility Verification,\" is a U.S. government form used to verify an individual's eligibility to work in the U.S.\n",
        "is_optional": false,
        "country": "US",
        "has_template": true,
        "fillable": true,
        "filenames": [
          "I-9.jpg"
        ],
        "uploaded_at": "2025-06-19T02:33:22.342Z",
        "status": null
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "W-4",
        "description": "The W-4 form is used to inform the employer how much tax should be withheld from each paycheck. The form is issued by the IRS and used to calculate payroll taxes which are then remitted to the IRS and the state (if applicable) on behalf of employees.",
        "is_optional": false,
        "country": "US",
        "has_template": true,
        "fillable": true,
        "filenames": [
          "W-4.jpg"
        ],
        "uploaded_at": "2025-06-19T02:33:22.342Z",
        "status": null
      },
      {
        "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0",
        "name": "Void check or direct deposit form",
        "description": "A Void Check or Direct Deposit Form is a document used to set up automatic deposit of paychecks into an employee's bank account.",
        "is_optional": false,
        "country": "US",
        "has_template": false,
        "fillable": false,
        "filenames": [
          "Void check or direct deposit form.jpg"
        ],
        "uploaded_at": "2025-06-19T02:33:22.342Z",
        "status": null
      },
      {
        "id": "f4ee60d8-eb19-43a8-a6c7-a7985b31feb1",
        "name": "Passport / ID",
        "description": "Your Passport or U.S. ID. is a government-issued document used to verify an individual's identity or U.S. citizenship",
        "is_optional": false,
        "country": "US",
        "has_template": false,
        "fillable": false,
        "filenames": [
          "Passport / ID.jpg"
        ],
        "uploaded_at": "2025-06-19T02:33:22.342Z",
        "status": null
      }
    ]
  }
}
```

#### Retrieve templates

You can retrieve templates for documents that require to use it. Use the [Download employee compliance document template](https://developer.deel.com/reference/downloademployeecompliancedocumenttemplate) endpoint, passing the document ID in the path, to retrieve the template.

> 📘 This request requires a worker token

```bash
curl --request GET \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor/workers/compliance-documents/{DOCUMENT_ID}/templates/download \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}'
```

A successful response (`200`) returns the template download URL. Make sure to download the file before the link expires.

```json
{
  "data": {
    "url": "https://app.deel.com/contract_requirement_templates/{VERY_LONG_SLUG}",
    "expires_at": "2025-07-03T15:00:46.141Z"
  }
}
```

#### Upload compliance documents

After collecting and filling compliance the documents, upload them using the [Upload employee compliance document](https://developer.deel.com/reference/uploademployeecompliancedocument) endpoint. You'll need the `document_id` returned in the response when [retrieving the required documents](#retrieve-the-list-of-required-documents).

This endpoint uses `multipart/form-data` for the content type.

> 📘 This request requires a worker token

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor/workers/compliance-documents/d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0 \
     --header 'accept: application/json' \
     --header 'content-type: multipart/form-data' \
     --form file='@document.pdf'
```

A successful response (`200`) returns a confirmation that the document has been uploaded.

```json
{
  "data": {
    "success": true
  }
}
```

### Step 3. Verify the worker's identity

Depending on the country and case, different verification methods are available:

- Automated identity verification (Veriff)
- Manual screening

While the automated identity verification is immediate, the manual screening can take up to 24 hours to complete. Consider this when planning the onboarding process.

For more information, visit our [Help Center](https://help.letsdeel.com/hc/en-gb/articles/17505958579985-How-to-Verify-an-Employee-Account).

#### Create a Veriff session

Veriff is a third-party identity verification service that is used to verify the worker's identity. Using Veriff is the recommended way to verify the worker's identity.

To create a Veriff session, use the [Create Veriff session](https://developer.deel.com/reference/createveriffsession) endpoint. The same endpoint can also be used to recreate a Veriff session request in case it fails or expires, or update the personal information linked to Veriff.

> 📘 This request requires a worker token

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/veriff/session \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "user_input": {
      "last_name": "Scott",
      "first_name": "Michael",
      "middle_name": "null"
    },
    "operation_type": "IDENTITY_VERIFICATION_KYC"
  }
}
'
```

A successful response (`201`) contains the link to initiate the Veriff session. The worker can follow the link to complete the verification process.

```json
{
  "data": {
    "url": "https://magic.veriff.me/v/{TOKEN}"
  }
}
```

#### Request a manual screening

If the [Veriff screening](#create-a-veriff-session) is not an option for you, you can request a manual screening. To request a manual screening, use the [Create manual verification screening](https://developer.deel.com/reference/createmanualverificationscreening) endpoint and upload the required documents.

This endpoint uses `multipart/form-data` for the content type.

> 📘 This request requires a worker token

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/screenings/manual-verification \
     --header 'accept: application/json' \
     --header 'content-type: multipart/form-data' \
     --form document_type=PASSPORT \
     --form operation_type=IDENTITY_RESUBMISSION_KYC \
     --form translation_required=false \
     --form back='@id-back-side.png' \
     --form front='@id-front-side.png' \
     --form additional='@additional-file.pdf' \
     --form selfie_with_id='@selfie-with-id.png' \
     --form document_country=US \
     --form proof_of_residence='@proof-of-residence.pdf'
```

A successful response (`201`) returns a confirmation that the documents required for the manual screening have been uploaded.

```json
{
  "data": {
    "success": "true"
  }
}
```

### Step 4. Add bank details

To complete the onboarding process, you must add bank details.

Adding bank details ensures that all the required information for a compliant working relationship is in place as well as ensuring that payroll is properly processed.

Bank details vary by country and currency. You'll be asked to provide the country and currency when retrieving the bank guide, which will return the list of required bank details for that country and currency as well as their expected format.

#### Retrieve the bank guide

Use the [Retrieve bank account guide](https://developer.deel.com/reference/retrievebankaccountguide) endpoint to understand the required bank details and their expected format. Pay special attention to the values of the `key` parameter, because you will be using them to pass the bank details in the next step. For example, if the currency code key is `currency_code`, you'll use `currency_code` to pass this information in the next step.

> 📘 This request requires a worker token

```bash
curl --request GET \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor/workers/banks-guide/country/ES/currency/EUR \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}'
```

A successful response (`200`) returns the list of required bank details, along with the accepted values and validation rules. You can use this information to upload the bank details in the [next step](#add-the-bank-details-to-the-contract) using the `key` parameter's value.

```json
{
  "fields": [
    {
      "key": "custom_name",
      "type": "text",
      "required": false,
      "label": "Account Custom Name",
      "validation": [
        { "type": "MIN_LENGTH", "value": 0 },
        { "type": "MAX_LENGTH", "value": 30 }
      ]
    },
    {
      "key": "payment_type",
      "type": "select",
      "required": true,
      "label": "Payment type",
      "values_allowed": [
        { "label": "Bank transfer", "value": "bank_transfer" }
      ]
    },
    {
      "key": "currency_code",
      "type": "select",
      "required": true,
      "label": "Currency",
      "values_allowed": [ { "label": "AED - Dirham", "value": "AED" }, ... ]
    },
    {
      "key": "full_name",
      "type": "text",
      "required": true,
      "label": "Full Name",
      "helper_text": "Latin chars only",
      "validation": [
        { "type": "MIN_LENGTH", "value": 1 },
        { "type": "MAX_LENGTH", "value": 140 },
        { "type": "REGEX", "value": "^[a-zA-Z...]*$" }
      ]
    },
    {
      "key": "address_line1",
      "type": "text",
      "required": true,
      "label": "Address Line 1",
      "validation": [
        { "type": "MIN_LENGTH", "value": 1 },
        { "type": "MAX_LENGTH", "value": 70 }
      ]
    },
    {
      "key": "city",
      "type": "text",
      "required": true,
      "label": "City",
      "validation": [
        { "type": "MIN_LENGTH", "value": 1 },
        { "type": "MAX_LENGTH", "value": 35 }
      ]
    },
    {
      "key": "country_code",
      "type": "select",
      "required": true,
      "label": "Country",
      "values_allowed": [ { "label": "Andorra", "value": "AD" }, ... ]
    },
    {
      "key": "swift_bic",
      "type": "text",
      "required": true,
      "label": "SWIFT BIC",
      "validation": [
        { "type": "MIN_LENGTH", "value": 8 },
        { "type": "MAX_LENGTH", "value": 11 },
        { "type": "REGEX", "value": "^[A-Z]{6}..." }
      ]
    },
    {
      "key": "iban",
      "type": "text",
      "required": true,
      "label": "IBAN",
      "helper_text": "International Bank Number",
      "validation": [
        { "type": "REGEX", "value": "^[^\\s`!@#..." }
      ]
    }
  ]
}
```

#### Add the bank details to the contract

Use the [Add bank account](https://developer.deel.com/reference/addbankaccount) endpoint and leverage the information retrieved in the [previous step](#retrieve-the-bank-guide) to add the bank details to the contract. 

> 📘 This request requires a worker token

```bash
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/eor/workers/banks \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": [
    {
      "key": "payment_type",
      "value": "bank_transfer"
    },
    {
      "key": "currency_code",
      "value": "EUR"
    }
  ]
}
'
```

A successful response (`201`) returns the ID of the bank details recorded for the worker, which can be used for future consultation or updates.

```json
{
  "data": {
    "id": "d3m0d3m0-d3m0-d3m0-d3m0-d3m0d3m0d3m0"
  }
}
```

## Step 5: The worker signs the contract

Once the worker has completed the onboarding process and submitted all the required information and documents, we prepare the employee agreement and send it to the worker so that they can sign it.

### View the employee agreement

As a first step, workers can download the employee agreement in PDF using the [Download employee agreement PDF](https://developer.deel.com/reference/downloademployeeagreementpdf) endpoint, passing the contract ID in the path.

> 📘 This request requires a worker token

```bash
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/eor/workers/contracts/37nex2x/employee-agreement/download \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}'
```

A successful response (`200`) returns the employee agreement download URL. Make sure to download the file before the link expires.

```
{  
  "data": {  
    "url": "[https://api.letsdeel.com/employee-agreement/12345.pdf"](https://api.letsdeel.com/employee-agreement/12345.pdf"),  
    "expires_at": "2020-03-31T10:58:49.780Z"  
  }  
}
``

### Sign the employee agreement

Workers can sign the employee agreement using the [Sign a contract](https://developer.deel.com/reference/signacontract) endpoint, passing the contract ID in the path and their signature in the body.

> 📘 This request requires a worker token

```bash
curl --request POST \
     --url https://api.letsdeel.com/rest/v2/eor/workers/contracts/mryv8dx/signatures \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'authorization: Bearer {WORKER_TOKEN}' \
     --data '
{
  "data": {
    "signature": "Michael Scott"
  }
}
'
```

A successful response (`201`) returns a confirmation that the worker has signed the contract.

```json
{
  "data": {
    "created": true
  }
}
```

## Next steps

After the worker signs the contract, Deel signs it too. After Deel signs the contract, it becomes effective and the worker can start working.

> 📘 For the contract to become effective, the payment to Deel that covers the costs of the contract must be already made. The lack of a payment for the contract results in the contract not becoming effective, even if all parties have signed it.

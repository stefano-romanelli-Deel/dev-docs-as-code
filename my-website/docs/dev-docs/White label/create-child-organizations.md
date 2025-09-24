---
title: "Create child organizations"
slug: "create-child-organizations"
excerpt: "Learn how White Label resellers can create and manage child organizations under their parent account programmatically"
hidden: false
createdAt: "Mon Sep 08 2025 15:10:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Sep 10 2025 10:52:47 GMT+0000 (Coordinated Universal Time)"
---
If you are a White Label reseller, you can create child organizations under your parent account programmatically. This lets you onboard and manage client organizations at scale without relying on manual setup.

## Before you begin

Make sure you have the following prerequisites:

- A valid [API token](https://developer.deel.com/docs/api-tokens-1) for the parent organization.
- [Partner Portal](https://help.letsdeel.com/hc/en-gb/articles/36145460305169-Getting-started-with-the-Partner-Portal) activated for the parent organization.

> 👍 The Partner Portal can be activated by a Deel representative once your partnership begins. Contact us if you would like to become a partner.

## Step 1: Send the request

Use the [Create child organization](https://developer.deel.com/reference/createchildorganization) endpoint to create a new child organization.

> 📘 The email of the child organization admin must be unique
> 
> If the same email is already used for another organization, you must use a different one.

```bash
curl --request POST \
     --url https://api-sandbox.demo.deel.com/rest/v2/organizations/children \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {TOKEN}' \
     --header 'content-type: application/json' \
     --data '
{
  "data": {
    "child_organization": {
      "name": "Example Organization Ltd",
      "department": "Finance",
      "is_api_enabled": true,
      "workforce_size": 100,
      "headquarters_country": "US"
    },
    "parent_organization": {
      "admin_email": "demo@email.com"
    }
  }
}
'
```

Where:

| Field                                     | Required | Type    | Format                                                                      | Description                                                                                                                | Example                                   |
| ----------------------------------------- | -------- | ------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `child_organization.name`                 | Yes      | string  | -                                                                           | The name of the child organization.                                                                                        | "Example Organization Ltd"                |
| `child_organization.department`           | No       | string  | -                                                                           | The name of the department where the manager will be assigned.                                                             | "Finance"                                 |
| `child_organization.is_api_enabled`       | No       | boolean | -                                                                           | Flag that enables the public API for the child organization. Enable this if the child organization needs to use Deel APIs. | true                                      |
| `child_organization.workforce_size`       | No       | integer |                                                                             | The number of workers in the child organization. Accepted values must be between 1 and 100000.                             | 100                                       |
| `child_organization.headquarters_country` | No       | string  | [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) code | The headquarters country code of the child organization.                                                                   | "US"                                      |
| `parent_organization.admin_email`         | Yes      | string  | email                                                                       | The email address of the parent organization admin.                                                                        | "[demo@email.com](mailto:demo@email.com)" |

A successful response (`201`) returns the child organization details and a scoped service account ID.

```json
{
  "data": [
    {
      "id": "00000000-0000-0000-0000-000000000000",
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmdJZCI6IjliM2M2ZjRkLTI3ZTEtNDZjMi1iYzJlLTNlNWEyOWFmOGQxOSJ9.s3cr3tSignatur3",
      "created_at": "2024-10-10T10:00:00Z",
      "updated_at": "2024-10-10T10:00:00Z"
    }
  ]
}
```

Where:

| Field        | Description                                                    |
| ------------ | -------------------------------------------------------------- |
| `id`         | A unique service account ID of the created child organization. |
| `token`      | The Auth token for the child organization.                     |
| `created_at` | The timestamp when the child organization was created.         |
| `updated_at` | The timestamp when the child organization was last updated.    |

After you create a child organization, the returned auth token enables the new organization to make subsequent API calls, such as onboarding workers, setting up legal entities, or configuring payroll and payouts.

---
title: "Using the SCIM API for user provisioning"
slug: "using-the-deel-scim-api-for-user-provisioning"
excerpt: "You can use Deel SCIM API to provision users from Deel to other systems: learn how."
hidden: false
createdAt: "Mon Oct 21 2024 10:08:53 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Mar 07 2025 16:21:40 GMT+0000 (Coordinated Universal Time)"
---
System for Cross-domain Identity Management (SCIM) is a standard for managing user identity information. Using SCIM guarantees that their information is consistent across all systems.

Deel can act as the system of record for your organization. You can use the SCIM API to pull information about users created in Deel and create user accounts in other systems such as identity providers (IdPs) or third-party applications.

This guide explains how to create a user provisioning integration using Deel's SCIM API and shares some best practices to follow.

## Table of contents

In this article:

- [What you need](#what-you-need)
- [Authenticating your calls](#authenticating-your-calls)
- [SCIM users scopes](#scim-users-scopes)
- [SCIM user object](#scim-user-object)
- [Retrieving the user list](#retrieving-the-user-list)
- [Syncing with your system](#syncing-with-your-system)
- [Frequently-asked questions (FAQs)](#frequently-asked-questions-faqs)

## What you need

To use Deel's SCIM API, you'll need:

- An active Deel account
- Users to provision to your system [already exist in Deel](https://help.letsdeel.com/hc/en-gb/sections/20347193192593-Contract-Creation-and-Management)
- A Deel user with the [Organization Admin or IT Developer Admin role](https://help.letsdeel.com/hc/en-gb/articles/13923716480401-What-Are-the-Different-Roles-for-Organization-Admins-in-Deel)

Also, before starting to build the integration, we recommend becoming familiar with the [SCIM API endpoints](https://developer.deel.com/reference/searchviaget).

> 📘 The SCIM API doesn't return manager-type users
> 
> This guide leverages the SCIM API, which currently only supports [worker-type users](https://developer.deel.com/docs/managers), [manager-type users](https://developer.deel.com/docs/managers) are not supported.

## Authenticating your calls

There are 2 ways to authenticate your SCIM integration:

- [Using OAuth2](https://developer.deel.com/docs/oauth2-apps)
- [Using access tokens](https://developer.deel.com/docs/api-tokens-1)

> 📘 Choose organization-level permissions
> 
> Whether you use OAuth2 or access tokens, SCIM integrations require organization-level permissions. Make sure to choose the correct permissions when generating a token or creating a new OAuth2 app.

## SCIM users scopes

A SCIM user provisioning integration requires the `users:read` scope, make sure to select it when creating the token. OAuth2 apps include all the [available scopes](https://developer.deel.com/docs/scopes-1), so there's no need to specify the scope in this case.

![](https://files.readme.io/ae905ef18a1a5f7e7ae2811610ce432f3c21ef06b77621ba0a6323ab70c29c70-tokens-people-users-read.png)


## SCIM user object

SCIM users are built around their `work_email`. If their `work_email` is not set, they won't be showing up in the list of users returned by the SCIM API. For more information, see [List users](https://developer.deel.com/reference/searchviaget).

Here's an example of a SCIM user object:

```json
{
  "active": true,
  "id": "ecce878f-dd78-4e09-a663-51599ce47f3e",
  "emails": [
    {
      "value": "michael@dundermifflin.com",
      "type": "home",
      "primary": true
    },
    {
      "value": "michael@dundermifflin.com",
      "type": "work",
      "primary": false
    },
    {
      "value": "michael@dundermifflin.com",
      "type": "other",
      "primary": false
    }
  ],
  "name": {
    "familyName": "Scott",
    "givenName": "Michael"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "department": "",
    "costCenter": "US entity",
    "organization": "Dunder Mifflin",
    "manager": {
      "value": "",
      "displayName": " ",
      "email": ""
    }
  },
  "urn:ietf:params:scim:schemas:extension:2.0:User": {
    "preferredFirstName": "Michael",
    "preferredLastName": "Scott",
    "preferredName": "Michael Scott",
    "workerId": "310",
    "organizationalStructures": [],
    "startDate": "2024-09-09",
    "endDate": "",
    "birthday": "",
    "hiringStatus": "onboarding_overdue",
    "state": "BC",
    "country": "CA",
    "employments": [
      {
        "contractId": "nw7n2ev",
        "title": "Product manager",
        "startDate": "2024-09-09",
        "contractType": "direct_employee",
        "state": "PA",
        "country": "USA",
        "active": false,
        "team": {
          "name": "USA - group"
        }
      }
    ],
    "customFields": [],
    "isManager": false,
    "departmentHierarchy": null,
    "departmentExternalId": null,
    "departmentExternalIdHierarchy": null
  },
  "userName": "michael@dundermifflin.com",
  "title": "Product manager",
  "userType": "direct_employee",
  "addresses": [
    {
      "streetAddress": "Parkour Road 1",
      "locality": "Scranton",
      "region": "PA",
      "postalCode": "12345",
      "country": "USA",
      "type": "other"
    }
  ],
  "meta": {
    "created": "2024-10-15T09:23:55.881Z",
    "lastModified": "2024-10-15T10:36:57.100Z",
    "resourceType": "User",
    "location": "https://api.letsdeel.com/scim/v2/Users/ecce878f-dd78-4e09-a663-51599ce47f3e"
  }
}
```

## Retrieving the user list

To retrieve the users that you want to provision through the integration, you must use the [List users](https://developer.deel.com/reference/searchviaget) endpoint.

By default, the endpoint returns 50 users for each request, but you can change the limit up to `99` by using the `count` query parameter. When creating the integration, make sure that all the users are retrieved before syncing them with your system.

For example, if you want to retrieve the first 99 users, you can use the following query:

```curl
curl --request GET \
GET curl --location 'https://api.letsdeel.com/scim/v2/Users?startIndex=1&count=99' \
--header 'Authorization: Bearer {token}' \
```

> 📘 The SCIM API is base 1
> 
> Counting for the filters starts at `1` instead of `0`.

## Syncing with your system

After [retrieving the user list](#retrieving-the-user-list), build your application so that it syncs users with your system periodically.

The sync frequency depends on how often your workers are onboarded or offboarded:

- If it happens happens once a day, set the sync to happen every 24 hours
- If it happens multiple multiple times a day, you could sync the worker, we recommend syncing no more than every 3 hours to avoid hitting [rate limits](https://developer.deel.com/docs/rate-limits-1)

## Frequently-asked questions (FAQs)

**Does the Deel SCIM API support user groups?**

Our SCIM API doesn't currently support user groups.

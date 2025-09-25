---
title: "Use Deel for profile sourcing to Okta"
slug: "use-deel-for-profile-sourcing-to-okta"
excerpt: "Learn how to make Deel your profile source for Okta"
hidden: false
createdAt: "Thu Oct 03 2024 06:37:14 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Aug 07 2025 11:26:50 GMT+0000 (Coordinated Universal Time)"
---
Deel can act as the source of truth for user identities in Okta, or other SSO providers. Doing so will allow you to create users on Deel, then automatically provision them in Okta using SCIM. This article explains how to configure Deel as the profile source.

In this article:

- [Before you begin](#before-you-begin)
- [Step 1. Create a SWA integration in Okta](#step-1-create-a-swa-integration-in-okta)
- [Step 2. Add SCIM provisioning](#step-2-add-scim-provisioning)
- [Step 3. Configure SCIM provisioning](#step-3-configure-scim-provisioning)
- [Step 4. Map attributes](#step-4-map-attributes)
- [Next up](#next-up)
- [Further reference](#further-reference)

## Before you begin

To complete this setup, you'll need:

- A valid [Deel API access token](https://developer.deel.com/docs/api-tokens-1)
- The correct Okta tier and permissions that allow you to perform the steps described

> 📘 The SCIM API doesn't return manager-type users
> 
> This guide leverages the SCIM API, which currently only supports [worker-type users](https://developer.deel.com/docs/managers), [manager-type users](https://developer.deel.com/docs/managers) are not supported.

## Step 1. Create a SWA integration in Okta

Begin by creating an SSO integration that supports SCIM. For the integration to work with Deel, it must be a SWA integration.

To create an SWA integration:

1. In the Admin Console, go to **Applications** > **Applications**.
2. Click **Create App Integration**.
3. Select **SWA - Secure Web Authentication** as the Sign-on method, then click **Next**.

![](https://files.readme.io/baf364c5c5daafb4479464a273f3ee9e5470f9d1254f290a55e8d6b9d49d7fbf-Screenshot_2024-10-02_at_15.58.59.png)


4. On the **Create SWA Integration** page, fill in the details, then click **Finish**. Make sure you configure the settings as described in the following table.

| Field                          | Value                                    |
| ------------------------------ | ---------------------------------------- |
| **Who sets the credentials?**  | Administrator sets username and password |
| **Application username**       | Email                                    |

## Step 2. Add SCIM provisioning

1. After you create your integration, click the **General** tab.
2. In the **App Settings** section, click **Edit**.
3. In the **Provisioning** field, select **SCIM**, and then click **Save**.

## Step 3. Configure SCIM provisioning

1. After adding the SCIM provisioning, click the **Provisioning** tab.
2. In **Settings** > **Integration**, click **Edit**.
3. In the **SCIM Connection** section, configure the settings, then click **Save**. Make sure you configure the settings as described in the following table.

| Field                                 | Value                                                                                                    |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **SCIM connector base URL**           | [https://api.letsdeel.com/scim/v2/](https://api.letsdeel.com/scim/v2/)                                                                      |
| **Unique identifier field for users** | id                                                                                                       |
| **Supported provisioning actions**    | Import New Users and Profile Updates, Push New Users, Push Profile Updates                               |
| **Authentication Mode**               | HTTP Header                                                                                              |
| **Authorization**                     |  Enter the access token retrieved from the Deel UI as indicated in [Before you begin](#before-you-begin) |

4. In **Settings** > **To Okta**, click **Edit** next to the **General** section.
5. Modify the settings as described in the following table, then click **Save**.

| Field                    | Value              |
| ------------------------ | ------------------ |
| **Okta username format** | Custom             |
| Custom expression        | `appuser.userName` |

6. Click **Edit** next to the **User Creation & Matching** section.
7. Modify the settings as described in the following table, then click **Save**.

| Field                                               | Value                                         |
| --------------------------------------------------- | --------------------------------------------- |
| **Imported user is an exact match to Okta user if** |  The following attribute matches: `login`     |
| **Confirm new users**                               |  Select the option **Auto-confirm new users** |

## Step 4. Map attributes

> 📘 Mapping based on the default Okta fields
> 
> If you have custom fields, discuss the mapping with your Deel representative to get the best results. Most fields are available through the People and SCIM APIs, and others can be mapped through the Custom Fields API. For more information, visit the [Developer Portal](https://developer.deel.com/reference).

1. In **Settings** > **To Okta**, locate the **Okta Attribute Mappings** section.
2. Edit the attribute mappings according to the following table.

| **Okta Attribute**                     | **Value**                      |
| -------------------------------------- | ------------------------------ |
| Username `login`                       | Configured in Sign On settings |
| First name `firstName`                 | `givenName`                    |
| Last name `lastName`                   | `familyName`                   |
| Middle name `middleName`               | `middleName`                   |
| Honorific prefix `honorificPrefix`     | `honorificPrefix`              |
| Honorific suffix `honorificSuffix`     | `honorificSuffix`              |
| Primary email `email`                  | `email`                        |
| Title `title`                          | `title`                        |
| Display name `displayName`             | `displayName`                  |
| Nickname `nickName`                    | `nickName`                     |
| Profile Url `profileUrl`               | `profileUrl`                   |
| Primary phone `primaryPhone`           | `primaryPhone`                 |
| Street address `streetAddress`         | `streetAddress`                |
| City `city`                            | `locality`                     |
| State `state`                          | `region`                       |
| Zip code `zipCode`                     | `postalCode`                   |
| Country code `countryCode`             | `country`                      |
| Postal Address `postalAddress`         | `formatted`                    |
| Preferred language `preferredLanguage` | `preferredLanguage`            |
| Locale `locale`                        | `locale`                       |
| Time zone `timezone`                   | `timezone`                     |
| User type `userType`                   | `userType`                     |
| Employee number `employeeNumber`       | `employeeNumber`               |
| Cost center `costCenter`               | `costCenter`                   |
| Organization `organization`            | `organization`                 |
| Division `division`                    | `division`                     |
| Department `department`                | `department`                   |
| ManagerId `managerId`                  | `managerValue`                 |
| Manager `manager`                      | `managerDisplayName`           |

## Step 5. First import

After mapping the attributes, users are ready to be imported for the first time.

To perform the import:

1. Click the **Import** tab.
2. Click **Import Now**.
3. Review the mapping information for each user, select the users you want to import, then click **Confirm Assignments**.

![](https://files.readme.io/76fad4b21a464cf5cec1b00bd1723f8b894a952381dd3285207d4fb427d520f0-Screenshot_2024-10-02_at_17.54.29.png)


4. On the **Confirm Imported User Assignments** dialog, click **Confirm**.

Once users are assigned, you can see the assignments from the **Assignments** tab.

## Further reference

This document is largely based on Okta's documentation. Here's the material we consulted to create this article:

- [Get started with app integrations](https://help.okta.com/en-us/content/topics/apps/apps-overview-get-started.htm) (Okta)
- [Add SCIM provisioning to app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_scim.htm) (Okta)
- [Create SWA app integrations](https://help.okta.com/en-us/content/topics/apps/apps_app_integration_wizard_swa.htm) (Okta)
- [What is profile sourcing?](https://support.okta.com/help/s/article/what-is-profile-sourcing) (Okta)
- [Attribute mappings](https://help.okta.com/en-us/content/topics/users-groups-profiles/usgp-about-attribute-mappings.htm) (Okta)
- [Okta Expression Language overview](https://developer.okta.com/docs/reference/okta-expression-language/) (Okta)
- [SCIM technical questions](https://developer.okta.com/docs/concepts/scim/faqs/) (Okta)
- [SCIM API introduction](https://developer.deel.com/docs/deel-scim-api-introduction) (Deel)
- [Plans and Pricing](https://www.okta.com/pricing)  (Okta)

## Next up

- Mapping employees to groups (coming soon)
- Offboarding employees (coming soon)

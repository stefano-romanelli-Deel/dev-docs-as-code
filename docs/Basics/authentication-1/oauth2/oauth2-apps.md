---
title: "Apps"
slug: "oauth2-apps"
excerpt: "Learn how to create apps and publish them to the App Store"
hidden: false
createdAt: "Mon Aug 22 2022 12:02:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Mar 07 2025 16:11:46 GMT+0000 (Coordinated Universal Time)"
---
A common use case for OAuth2 is to create apps for your organization or for the [App Store](#request-to-publish-an-app-to-the-app-store) to enhance some functionalities or to connect with third-party services.

> 📘 Only client users can use OAuth2 apps
> 
> To use an OAuth2 app, users must have a client role in Deel. Other roles, such as employees or independent contractors, cannot use OAuth2 apps.

## Create an app

To create an app:

1. Go to **More** > **Developer**.

   ![](https://files.readme.io/ca01b3f7528bb53b3d99f3ee79bdd46a46be28657d3b1e39400d131de9f8847b-Screenshot_2025-02-14_at_10.25.35.png)
2. On the **Developer Center** page, go to the **Apps** tab, and click **Create new app**.

   ![](https://files.readme.io/2c57862eb0249da20b8079e4fedf8776b17978c5d65e16bdd2ea1d9f476f0eb3-dev-center-apps-create.png)
3. Select the app type, fill the form with the app details, then click **Create**.

   ![](https://files.readme.io/5301c4f-pika-1685440759705-1x.png)

> 📘 The secret is only shown once when the app creation is confirmed. Store your secret somewhere safe or download the JSON file to make sure you don't lose access to it.

The app is created and ready to use.

> 👍 Apps are only available internally until approved
> 
> Once you create an app, it will be reviewed by our team. Until the app is approved, only users within your organization can use it. Once the app it's approved, also users outside of your organization will be able to use it.

### Organization apps and personal apps

Organization apps generate organization-level access tokens. These tokens are not tied to a user and can access all data in the organization. Personal apps generate personal access tokens limited to a user’s access.

For example, if you have an organization app when the Deel client gives you consent to read their contracts data, you can access all contracts in that organization even if the admin does not have access to a specific contract. With personal apps, you will only be able to access contracts the admin has access to.

| Integration use case                 | Recommended app type |
| :----------------------------------- | :------------------- |
| Contract data read integrations      | Organization         |
| Contract creation integrations       | Personal             |
| Timesheets integrations              | Organization         |
| Invoice adjustment integrations      | Organization         |
| Deel SCIM API integrations           | Organization         |
| Accounting integrations              | Organization         |
| SSO integrations (sign-in with Deel) | Personal             |

> 📘 All OAuth apps created before May 30th, 2023 are personal apps.

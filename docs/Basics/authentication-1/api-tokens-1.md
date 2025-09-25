---
title: "API Tokens"
slug: "api-tokens-1"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:23:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Mar 19 2025 11:25:12 GMT+0000 (Coordinated Universal Time)"
---
Deel API uses API tokens to authenticate requests. A bearer token is required to authenticate all API requests.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.

```
curl -X GET 'api.letsdeel.com/rest/v2/contracts' \
-H 'Authorization: Bearer YOUR-TOKEN-HERE'
```

## Generating access tokens

1. Go to **More** > **Developer**.

   ![](https://files.readme.io/8133e87602ef880b8551ee4660d09fe79adf6cacf160845f364af693c8109ec9-Screenshot_2025-02-14_at_10.25.35.png)
2. Go to the **Access Tokens** tab and click **Generate new token**.

   ![](https://files.readme.io/32d19257c6f2129ffe3935152548238f2ecf1c25c7afe3fdab07a1cb0213d92a-token-create-generate.png)
3. On the first step of the **Generate access token** wizard, enter a label, select the token type, then click **Next**.

   - Choose an organization token if you want to grant access to every resource in the organization
   - Choose a personal token if you want to grant access to the resources of the user who creates the token

     ![](https://files.readme.io/8819c5f6fac9f8afb8504a520c8691b37d138bbd1425108ac73ad9d63937e58b-token-create-details.png)
4. On the next step of the wizard, select the scopes for the token, then click **Next**.

   ![](https://files.readme.io/a77ff6ea4a286db773f159b75966b0f0cc38ccabf115040f8ebcfb1d58def7ef-token-create-scopes.png)
5. At the next step of the wizard, customize the access level of the token to sensitive data, then click **Next**.

   ![](https://files.readme.io/0d03db1cc12a856b200284a19ac25cb54154416eb665da08e5038cc7e04f6e82-token-create-sensitive-data.png)
6. On the last step of the wizard, review your settings, then click **Generate**.

   ![](https://files.readme.io/301e05a341e4457f052794f2214039a565d0765889d27b962ce04dc8fd537e46-token-create-review.png)

The token is generated, copy it somewhere safe because it won't be possible to display it again.

![](https://files.readme.io/1f4f369950177212ed01798696da5a0948561cc242ce11d1452b86b7323669fa-token-create-success.png)

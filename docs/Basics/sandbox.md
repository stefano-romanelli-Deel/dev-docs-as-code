---
title: "Using the sandbox"
slug: "sandbox"
excerpt: "Learn how to create a sandbox environment and use it to test your API calls"
hidden: false
createdAt: "Mon Aug 22 2022 08:38:38 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 26 2025 14:50:46 GMT+0000 (Coordinated Universal Time)"
---
You can create a sandbox environment to to mimic the characteristics of a production environment and test your API calls.

## Before you begin

Before creating a sandbox, keep these things in mind:

- Emails are not sent in the sandbox environment
- It's not possible to invite additional users to a sandbox account. We recommend sharing the sandbox access details with your team if you need more than one person to use it.

## Create a sandbox

To create a sandbox:

1. Go to **More** > **Developer** **App Store > Developer Center**.

   ![](https://files.readme.io/8aedb46dbe81ca699e1054fee8ea53be4619db6333f5b2b11837da527333ebee-nav-more-developer.png)
2. Go to the **API Sandbox** tab, then click **Create Sandbox**.

   ![](https://files.readme.io/2d9e7277a5b12e7c778b7906a229306a11adf4d2385dc344ae55504d6399b340-sandbox-create.png)
3. Enter an email and password for your sandbox account, then click **Confirm**.

   ![](https://files.readme.io/f2c83878bb7f870dfc3257c0451b5660687d3c2bd3815ab14b47028b8ce0cd36-sandbox-credentials.png)

> 📘 Make sure to note the email and password down, you'll need them to log in to the sandbox.

The sandbox is created. You can now access it by using the shortcut **Go to sandbox** from the **API Sandbox** tab, or visit `demo.letsdeel.com` and log in using the email and password you chose.

![](https://files.readme.io/f5d42bc030aa4a885820a547ba115ecf71e9b0c0e797b5627e83a73c118aa4ca-sandbox-go-to-sandbox.png)

## Sandbox API

The sandbox API works just like the production API. You can [generate an API token](/docs/Basics/authentication-1/api-tokens-1.md) and use it to make API calls. The sandbox API URL is `api-sandbox.demo.deel.com`.

Following is an example of an API request to the sandbox API URL.

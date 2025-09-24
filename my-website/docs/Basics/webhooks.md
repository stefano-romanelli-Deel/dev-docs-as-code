---
title: "Webhooks"
slug: "webhooks"
excerpt: ""
hidden: false
createdAt: "Fri Feb 28 2025 14:50:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Apr 29 2025 13:05:16 GMT+0000 (Coordinated Universal Time)"
---
Deel Webhooks deliver real-time notifications for key platform events, allowing you to build efficient and responsive integrations without relying on constant [polling](#webhooks-vs-polling).

## Key features

- Real-time updates: Receive notifications as events occur
- Secure delivery: Every payload is signed using SHA256
- Flexible subscriptions: Manage webhook subscriptions via API or Developer Center

## Use cases

Here are a few examples of how you might use webhooks:

- Syncing data: Automatically update your system when new contracts are created
- Real-time notifications: Trigger alerts or workflows in your internal tools when one of the events occurs
- Workflow automation: Start external processes based on specific events

## Webhooks vs polling

Polling is the act of calling an API recurrently to see if data is available. With webhooks, instead, you subscribe to specific events and the system will notify you when the event occurs.

![](https://files.readme.io/ef01798f0539431921576845a59b13883c4f09de57f5c342bcc7503f3dd8cf4e-webhooks-vs-polling-diagram.png)


### When to use polling

Use polling if:

- Updates are frequent
- You don't need updates in real-time

If your use case meets both conditions, polling is the ideal solution because you make an efficient use of your API calls, whereas [webhooks](#when-to-use-webhooks) would be very resource-intensive in this case.

### When to use webhooks

Use webhooks if:

- Updates are infrequent
- You need updates in real-time

If your use case meets both conditions, webhooks are the ideal solution because webhook notifications are triggered only when the event occurs, whereas polling would be very resource-intensive in this case.

|             | Polling                                                                                                            | Webhooks                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| When to use | - Updates are frequent<br/>- Updates are not needed in real-time                                                    | - Updates are infrequent<br/>- Updates are needed in real-time                                          |
| Why to use  | Returns data in real-time but can be resource-intensive, could make you run into rate limits or performance issues | Is efficient because is only triggered when the event occurs, but not appropriate for frequent updates |

## Get started with webhooks

Head over to [Get started with webhooks](/docs/webhooks-get-started) page to learn the basics for using webhooks.

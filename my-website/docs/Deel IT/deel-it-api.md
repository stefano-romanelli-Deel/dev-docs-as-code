---
title: "Deel IT API"
slug: "deel-it-api"
excerpt: "The Deel IT API lets you access and manage your organization’s equipment and asset data programmatically."
hidden: false
createdAt: "Mon Sep 01 2025 15:37:37 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Sep 01 2025 15:37:47 GMT+0000 (Coordinated Universal Time)"
---
The Deel IT API gives programmatic access to your organization's equipment and asset data within the Deel platform. It supports the equipment lifecycle, from procurement and shipping to retrieval.  

Using these endpoints provides the following benefits:  

- Data consistency: Synchronize asset and order information with internal systems so records remain aligned.  
- Custom reporting: Query API data to generate reports, dashboards, or automated IT workflows.  
- Automation with webhooks: Use Deel IT webhooks to receive notifications when assets change status, such as when they are approved, shipped, or created.  

This guide covers the core concepts and common use cases to help you get started.

> 📘 Migrating from Hofy
> 
> If your organization previously used the Hofy API, the Deel IT API is its official successor.  
> The legacy Hofy API is still supported, but you should plan to migrate. Migration involves updating your API calls to the Deel IT endpoints and reconfiguring your webhook handlers.

## Before you begin

Make sure you have the following prerequisites:

- An active Deel IT account for your organization. If it is not active, contact your Deel representative.  
- A [valid token](https://developer.deel.com/docs/api-tokens-1) to authenticate your requests.  

## Core concepts

To use the API effectively, it is important to understand the main resources:  

### Assets

Any physical piece of equipment, such as a laptop or monitor, that is managed in Deel IT. Each asset has a unique status, a location, and can be assigned to workers.

### Orders

A request for one or more pieces of equipment for a worker. The API lets you track order statuses, from approval through delivery.

### IT policies

A set of rules that define the equipment a worker is eligible for. These rules are fully configurable by each organization and are often based on roles or departments (for example, Engineering or Design). You can retrieve a list of these policies to understand your organization’s equipment standards.

## Common use cases and automations

The API is currently read-only (`GET`), but you can still automate processes by querying the API, subscribing to webhooks, or integrating with an orchestration platform.

Here are some common use cases:

- [Using Deel IT with Deel HR](#using-deel-it-with-deel-hr)
- [Synchronize with your internal asset management system](#synchronize-with-your-internal-asset-management-system)
- [Create custom reports and dashboards](#create-custom-reports-and-dashboards)

### Using Deel IT with Deel HR

You can use the Deel IT API together with Deel HR APIs and webhooks. For example:  

1. Trigger an HR event. An event occurs in Deel HR, such as creating a new employee, importing one from a third-party provider, or processing a contract termination. Deel sends an [HR webhook](https://developer.deel.com/docs/webhook-event-types), for example, `employee.created`, to your system.  
2. Retrieve HR data. Use the `hris_profile_id` from the webhook payload to call the [Deel People API](https://developer.deel.com/reference/getpeoplepersonalinformationbyid). This returns additional employee details, such as department, location, and job title.
3. Retrieve IT data With the `hris_profile_id` and employee context, call the Deel IT API to perform the required IT actions, such as verifying equipment assignment, checking IT policies, or creating tickets for further action.  

This setup lets you connect HR and IT events into a single workflow.  

### Synchronize with your internal asset management system

You can integrate Deel IT with your IT service management (ITSM) platform. This allows you to keep your ITSM up to date with the latest asset and order data.

**How to implement:**  

1. Fetch all current assets from Deel using the [List assets](https://developer.deel.com/reference/listitassets) endpoint.

> 👍 Use the `status=ACTIVE` parameter to only retrieve equipment that is currently in use or in inventory.

```bash

curl --request GET \
   --url 'https://api.letsdeel.com/rest/v2/it/assets?limit=50&status=ACTIVE' \
   --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
   --header 'accept: application/json'
```

In the query:

| Name   | Required | Type   | Format | Description                        | Example |
| ------ | -------- | ------ | ------ | ---------------------------------- | ------- |
| limit  | false    | number | int    | Maximum number of items to return. | 50      |
| status | false    | string | enum   | Filters assets by status.          | ACTIVE  |

2. Use [Deel IT webhooks](https://developer.deel.com/docs/webhook-event-types) to receive updates. You can subscribe to events such as `it-order.created` or `it-asset.location-updated`. When an event occurs, Deel sends a notification to your system, which can trigger a workflow to create tickets, update asset records, or log activities in your ITSM. This keeps synchronization accurate and reduces unnecessary API calls.  

### Create custom reports and dashboards

Use the API to create customized dashboards. Pull data from the [Retrieve asset](https://developer.deel.com/reference/getitasset) and [Retrieve order](https://developer.deel.com/reference/getitorder) endpoints into your internal business intelligence tools for deeper analysis.  

You can also combine Deel IT data with other systems to generate cross-functional reports. Examples include:  

- Correlating equipment spend from orders with departmental budgets from your finance platform.  
- Tracking asset assignments against hiring plans from your HR system.  

## Tips and best practices

### Pagination

The [List assets](https://developer.deel.com/reference/listitassets) endpoint results are paginated. Responses include:  

- `has_more` (boolean): Indicates if additional results are available.  
- `next_cursor` (string): A pointer to the position where the next request should continue.  

To retrieve the full list, continue calling the endpoint with the `cursor` query parameter until `has_more` is `false`.  

### Filters

The [List assets](https://developer.deel.com/reference/listitassets) endpoint supports query parameters that let you refine results. You can combine filters to create precise queries.  

For example, to list all laptops currently assigned to users:  

```bash
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/it/assets?limit=20&location=WITH_USER&category=LAPTOP' \
     --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

### List vs. detail endpoints

The [List assets](https://developer.deel.com/reference/listitassets) endpoint, returns a summary object for each item. A summary object contains key fields, such as the asset ID, but not all details.

To retrieve the complete dataset for a single item, use the [Retrieve asset](https://developer.deel.com/reference/getitasset) endpoint passing a unique ID. For example:  

```bash
curl --request GET \
     --url https://api.letsdeel.com/rest/v2/it/assets/{item_id} \
     --header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```

### Working with enums

Several fields in the API response use enums such as `ItemStatus`, `ItemLocation`, and `OrderStatus`. These fields can only take predefined values. Handle these values explicitly to keep your integration reliable and avoid errors if unexpected input is returned.

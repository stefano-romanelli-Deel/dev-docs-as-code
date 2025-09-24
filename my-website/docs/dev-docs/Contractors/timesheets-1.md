---
title: "Timesheets"
slug: "timesheets-1"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 13:52:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:30:55 GMT+0000 (Coordinated Universal Time)"
---
You can create, update, review and delete timesheets which are used to track the time a particular employee has worked during a certain period.

# Create a timesheet

To create a timesheet, you will need to extract the _contractIdTimeBased_ first.

**Step 1**: Retrieve the _contractIdTimeBased_

```shell
curl --location -g --request GET '{{host}}/rest/v2/contracts?limit=2&sort_by=worker_name&order_direction=desc' \
--header 'Authorization: Bearer {{token}}'
```

**Step 2**: Create the timesheet

```shell
curl --location -g --request POST '{{host}}/rest/v2/timesheets' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "contract_id": "{{contractIdTimeBased}}",
    "quantity": 1,
    "description": "worked",
    "date_submitted": "2022-05-16"
  }
}'
```

# Update a timesheet entry

You can update timesheets to make changes to an existing timesheet entry.  
For this, you will need to retrieve the _timesheetId_ for a specific contract.

**Step 1**: Retrieve the _timesheetId_ 

```shell
curl --location -g --request GET '{{host}}/rest/v2/contracts/{{contractId}}/timesheets?statuses[]=pending' \
--header 'Authorization: Bearer {{token}}'
```

**Step 2**: Update the timesheet entry

```shell
curl --location -g --request PATCH '{{host}}/rest/v2/timesheets/{{timesheetId}}' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "quantity": 1,
    "description": "worked - updated"
  }
}'
```

# Delete a timesheet entry

You are also able to delete timesheet entries from a timesheet:

```shell
curl --location -g --request DELETE '{{host}}/rest/v2/timesheets/{{timesheetId}}?reason=my reason to delete' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "contract_id": "{{contractId}}",
    "quantity": 1,
    "description": "worked",
    "date_submitted": "2022-05-06"
  }
}'
```

# Review timesheet entries

You can also review timesheets in order to approve or decline submitted work by specifying the _timesheetId_ 

```shell
curl --location -g --request POST '{{host}}/rest/v2/timesheets/{{timesheetId}}/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "status": "approved",
    "reason": "my reason"
  }
}'
```

**Reviewing multiple timesheets**

We also give you the possibility to approve or decline multiple timesheets at once

```shell
curl --location -g --request POST '{{host}}/rest/v2/timesheets/many/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "ids": [ {{timesheetId}} ],
    "status": "approved",
    "reason": "my reason"
  }
}'
```

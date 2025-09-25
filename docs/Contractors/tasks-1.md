---
title: "Tasks"
slug: "tasks-1"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:49:48 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:30:24 GMT+0000 (Coordinated Universal Time)"
---
The Pay-As-You-Go (PAYG) contract is an ongoing contract used to pay contractors based on the working days/hours or tasks they have submitted. The client signs the contract and pays the invoice at the end of a week or a month. The amount invoiced is generated based on the total time a contractor or client submits. This type of contract can be used for work of any scope.

When working with PAYG contractors, either you or the contractor can submit work as tasks.  
Work has to be submitted before the invoice cycle ends. After this date, the work submissions will be added to the following cycle.

# Create a new task

To create a new task for the contractor you will need to specify the task variables.

Create a new task for your PAYG contractor.

```shell Create a new task
curl --location -g --request POST '{{host}}/rest/v2/contracts/{{contractId}}/tasks' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "type": "payg_tasks",
    "title": "PAYG Contract",
    "country_code": "US",
    "state_code": "CO",
    "notice_period": 5,
    "job_title": {
      "name": "Software Engineer"
    },
    "seniority": {
      "id": 1
    },
    "client": {
      "legal_entity": {
        "id": 12345
      },
      "team": {
        "id": 45678
      }
    },
    "start_date": "2022-10-10",
    "termination_date": "2023-11-11",
    "scope_of_work": "Create software applications.",
    "compensation_details": {
      "currency_code": "USD",
      "scale": "weekly",
      "frequency": "monthly",
      "cycle_end": 25,
      "cycle_end_type": "DAY_OF_MONTH",
      "payment_due_type": "REGULAR",
      "payment_due_days": 5
    },
    "meta": {
      "documents_required": true
    }
  }
}'
```

# Review tasks

You can review tasks to approve or decline the submitted work. For that you will need to retrieve the _taskId_ first.

**Step 1**: Retrieve the _taskId_

```shell Retrieve the taskId
curl --location -g --request GET '{{host}}/rest/v2/contracts/{{contractIdTaskBased}}/tasks' \
--header 'Authorization: Bearer {{token}}' \
--data-raw ''
```

**Step 2**: Approve the task

```shell Approve the task
curl --location -g --request POST '{{host}}/rest/v2/contracts/{{contractIdTaskBased}}/tasks/{{taskId}}/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "status": "approved"
  }
}'
```

You are also able to review and then approve or decline multiple tasks by specifying the _taskId_

```shell Review multiple tasks
curl --location -g --request POST '{{host}}/rest/v2/contracts/{{contractIdTaskBased}}/tasks/many/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "status": "approved",
    "ids": [
      {{taskId}},
      {{taskId2}}
    ]
  }
}'
```

# Delete a task

You can delete tasks from a contract if they are not relevant anymore. 

```shell Delete a task
curl --location -g --request DELETE '{{host}}/rest/v2/contracts/{{contractIdTaskBased}}/tasks/{{taskId}}' \
--header 'Authorization: Bearer {{token}}' \
--data-raw ''
```

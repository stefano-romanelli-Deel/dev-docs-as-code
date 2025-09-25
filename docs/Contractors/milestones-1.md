---
title: "Milestones"
slug: "milestones-1"
excerpt: ""
hidden: false
createdAt: "Wed Aug 24 2022 12:32:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:29:52 GMT+0000 (Coordinated Universal Time)"
---
The milestone contract is a "one-time" contract where the client breaks down a project into milestones and assigns a rate to each of them. The money is released based on the approved work (milestone). This type of contract can be used for short-term projects of any scope.

## Create a milestone

You can create new milestones for a contract with the _contractId_ 

**Step 1**: Retrieve the _contractId_ 

```shell Retrieve contracts
curl --location -g --request GET '{{host}}/rest/v2/contracts?limit=2&sort_by=worker_name&order_direction=desc' \
--header 'Authorization: Bearer {{token}}'
```

**Step 2**: Create a milestone

```shell Create a milestone
curl --location -g --request POST '{{host}}/rest/v2/contracts/{{contractId}}/milestones' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "amount": "900.00",
    "title": "please sign",
    "description": "please sign"
  }
}'
```

## Review milestones

You can approve or decline milestones by specifying the _contractId_ and the _milestoneId_ 

**Step 1**: Retrieve the _contractId_

```shell Retrieve contracts
curl --location -g --request GET '{{host}}/rest/v2/contracts?limit=2&sort_by=worker_name&order_direction=desc' \
--header 'Authorization: Bearer {{token}}'
```

**Step 2**: Retrieve the _milestoneId_

```shell Retrieve milestoneId
curl --request GET '{{host}}/rest/v2/contracts/{{contractId}}/milestones' \
--header 'Authorization: Bearer {{token}}'
```

**Step 3**: Approve a milestone ...

```shell Approve a milestone
curl --request POST '{{host}}/rest/v2/contracts/{{contractId}}/milestones/{{milestoneId}}/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json'
     --data '
{
     "data": {
          "status": "approved",
          "reason": "Approved by me"
     }
}
'
```

... or decline it

```shell Decline a milestone
curl --request POST '{{host}}/rest/v2/contracts/{{contractId}}/milestones/{{milestoneId}}/reviews' \
--header 'Authorization: Bearer {{token}}' \
--header 'Content-Type: application/json'
     --data '
{
     "data": {
          "status": "declined",
          "reason": "Declined by me"
     }
}
'
```

## Review multiple milestones

You are also able to approve or decline multiple milestones at once by specifying the concerned _milestoneIds_ of the concerned contract

```shell Approve multiple milestones
curl --request POST '{{host}}/rest/v2/contracts/{{contractId}}/milestones/many/reviews' \
 --header 'Authorization: Bearer {{token}}' \
     --header 'Content-Type: application/json' \
     --data '
{
     "data": {
          "ids": [
               123,
               456,
               789
          ],
          "status": "approved",
          "reason": "Approved by me"
     }
}
'
```

## Delete milestones

You may also want to delete a milestone from a contract. This is possible by again specifying the _contractId_ and the _milestoneId_

```shell Delete a milestone
curl --request DELETE '{{host}}/rest/v2/contracts/{{contractId}}/milestones/{{milestoneId}}' \
--header 'Authorization: Bearer {{token}}'
```

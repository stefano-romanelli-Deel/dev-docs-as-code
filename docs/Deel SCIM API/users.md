---
title: "Users"
slug: "users"
excerpt: ""
hidden: false
createdAt: "Fri Mar 24 2023 12:42:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Mar 07 2025 16:17:47 GMT+0000 (Coordinated Universal Time)"
---
With SCIM API you can manage users in Deel. You can get the full list of users, filter by attribute or retrieve a specific user. 

# User Methods

## List Users

Retrieve a paginated user of users. 

`GET: https://api.letsdeel.com/scim/v2/Users`

Retrieves the list of users in Deel. Use startIndex and count query parameters to receive paginated results. Supports sorting and the filter parameter.

**Sample Response** 

```json
{
  "Resources": [
    {
      "active": false,
      "emails": [
        {
          "type": "work",
          "value": "work.email@example.com",
          "primary": true
        }
      ],
      "title": "Software Engineer",
      "userType": "Employee",
      "id": "97b727b8-bdb5-11ed-afa1-0242ac120002",
      "name": {
        "familyName": "Jane",
        "givenName": "Doe"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User"
      ],
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        "department": "Engineering",
        "costCenter": "UK Entity",
        "organization": "Deel",
        "manager": {
          "value": "b29a5ff0-bdb5-11ed-afa1-0242ac120002"
        }
      },
      "urn:ietf:params:scim:schemas:extension:2.0:User": {
        "startDate": "2023-03-24T12:52:30.370Z",
        "endDate": "2023-03-24T12:52:30.370Z"
      },
      "userName": "work.email@example.com",
      "meta": {
        "created": "2023-02-04T18:03:18.796Z",
        "lastModified": "2023-02-04T18:03:18.796Z",
        "resourceType": "User",
        "version": "W/a330bc54f0671c9",
        "location": "https://api.letsdeel.com/scim/v2/Users/97b727b8-bdb5-11ed-afa1-0242ac120002"
      }
    }
  ],
  "itemsPerPage": 0,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "startIndex": 0,
  "totalResults": 0
}
```

## Retrieve a single user

Retrieve a single user by Id

`GET: https://api.letsdeel.com/scim/v2/Users/:id`

Retrieves a single users in Deel.

**Sample Response** 

```json
{
  "active": false,
  "emails": [
    {
      "type": "work",
      "value": "work.email@example.com",
      "primary": true
    }
  ],
  "title": "Software Engineer",
  "userType": "Employee",
  "id": "97b727b8-bdb5-11ed-afa1-0242ac120002",
  "name": {
    "familyName": "Jane",
    "givenName": "Doe"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User"
  ],
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "department": "Engineering",
    "costCenter": "UK Entity",
    "organization": "Deel",
    "manager": {
      "value": "b29a5ff0-bdb5-11ed-afa1-0242ac120002"
    }
  },
  "urn:ietf:params:scim:schemas:extension:2.0:User": {
    "startDate": "2023-03-24T12:45:58.857Z",
    "endDate": "2023-03-24T12:45:58.857Z"
  },
  "userName": "work.email@example.com",
  "meta": {
    "created": "2023-02-04T18:03:18.796Z",
    "lastModified": "2023-02-04T18:03:18.796Z",
    "resourceType": "User",
    "version": "W/a330bc54f0671c9",
    "location": "https://api.letsdeel.com/scim/v2/Users/97b727b8-bdb5-11ed-afa1-0242ac120002"
  }
}
```

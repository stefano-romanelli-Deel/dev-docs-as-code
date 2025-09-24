---
title: "Filter Users"
slug: "filter-users"
excerpt: ""
hidden: false
createdAt: "Fri Aug 18 2023 14:58:23 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
When using the SCIM API Users endpoint, retrieving data can become cumbersome, particularly if your organization on Deel has a substantial number of users. However, prioritizing user convenience, we have introduced the filter users endpoint to address this concern. 

This endpoint enables you to effortlessly conduct precise searches within your people lists, thereby streamlining the process and saving valuable time and effort. 

Currently, there are three filtering options available: `email`, `given name`, and `family name`.

NB: **Only the eq (equals) operator is supported for all these filters.**

***

## Email

The email filter empowers you to conduct highly specific searches using email addresses. 

If you were searching for a user with the email "[rogerio@mycompany.com](mailto:user@companyx.co)"; you can effortlessly achieve this by crafting a query like `/Users?filter=email eq "rogerio"`. This allows you to swiftly locate all users that have `rogerio` in their email address.

```Text Request
GET curl --location 'https://api.letsdeel.com/scim/v2/Users?filter=email%20eq%20%22rogerio%22' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "totalResults": 1,
    "itemsPerPage": 50,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "active": false,
            "id": "34a06b03-613f-4770-b0ce-d8d1609d481d",
            "emails": [
                {
                    "value": "wagner.marcelino+regerio.skylab@deel.wtf",
                    "type": "home",
                    "primary": true
                },
                {
                    "value": "rogerio.skylab@deel.com",
                    "type": "work",
                    "primary": false
                },
                {
                    "value": "wagner.marcelino+regerio.skylab@deel.wtf",
                    "type": "other",
                    "primary": false
                }
            ],
            "name": {
                "familyName": "Skylab",
                "givenName": "Rogerio"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "department": "",
                "costCenter": "168029",
                "organization": "131702",
                "manager": {
                    "value": ""
                }
            },
            "urn:ietf:params:scim:schemas:extension:2.0:User": {
                "startDate": "2023-08-19",
                "endDate": "",
                "state": "CE",
                "country": "BR",
                "employments": [
                    {
                        "contractId": "3ed858v",
                        "title": "Accounting Assistant",
                        "startDate": "2023-08-19",
                        "contractType": "hris_direct_employee",
                        "state": "CE",
                        "country": "BR",
                        "active": false
                    }
                ]
            },
            "userName": "rogerio.skylab@deel.com",
            "title": "Accounting Assistant",
            "userType": "hris_direct_employee",
            "addresses": [
                {
                    "streetAddress": "Street alpha",
                    "locality": "Sao Paulo",
                    "region": "CE",
                    "postalCode": "01745889",
                    "country": "BR"
                }
            ],
            "meta": {
                "created": "2023-08-18T19:34:21.619Z",
                "lastModified": "2023-08-19T00:11:02.451Z",
                "resourceType": "User",
                "location": "https://api.letsdeel.com/scim/v2/Users/34a06b03-613f-4770-b0ce-d8d1609d18d4"
            }
        }
    ]
}
```

***

## Given Name

The given name filter enhances your search capabilities by enabling queries based on a user's first name. 

When searching for users with the given name "Star," you can conveniently perform this search using `/Users?filter=name.givenName eq "Star"`. This enhances your efficiency in locating all users with first names as `Star`, making your interaction with the API more intuitive and productive.

```Text Request
GET curl --location 'https://api.letsdeel.com/scim/v2/Users?filter=name.givenName%20eq%20%22Star%22' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "totalResults": 1,
    "itemsPerPage": 50,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "active": false,
            "id": "3e518797-76d6-4b2e-9dc0-9e801e8fff3c",
            "emails": [
                {
                    "value": "wagner.marcelino+star.lord@deel.wtf",
                    "type": "home",
                    "primary": true
                },
                {
                    "value": "star.lord@deel.com",
                    "type": "work",
                    "primary": false
                },
                {
                    "value": "wagner.marcelino+star.lord@deel.wtf",
                    "type": "other",
                    "primary": false
                }
            ],
            "name": {
                "familyName": "Lord",
                "givenName": "Star"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "department": "",
                "costCenter": "168029",
                "organization": "137102",
                "manager": {
                    "value": ""
                }
            },
            "urn:ietf:params:scim:schemas:extension:2.0:User": {
                "startDate": "2023-08-18",
                "endDate": "",
                "state": "AM",
                "country": "BR",
                "employments": [
                    {
                        "contractId": "3rvk99y",
                        "title": "Accounting",
                        "startDate": "2023-08-18",
                        "contractType": "hris_direct_employee",
                        "state": "AM",
                        "country": "BR",
                        "active": false
                    }
                ]
            },
            "userName": "star.lord@deel.com",
            "title": "Accounting",
            "userType": "hris_direct_employee",
            "addresses": [
                {
                    "streetAddress": "Street alpha",
                    "locality": "Sao Paulo",
                    "region": "AM",
                    "postalCode": "04512336",
                    "country": "BR"
                }
            ],
            "meta": {
                "created": "2023-08-17T14:31:37.661Z",
                "lastModified": "2023-08-18T00:10:33.954Z",
                "resourceType": "User",
                "location": "https://api.letsdeel.com/scim/v2/Users/3e518797-76d6-4b2e-9dc0-9e801e8fff3c"
            }
        }
    ]
}
```

***

## Family Name

The family name filter provides a targeted approach to searches centered around a user's last name. 

To get all users with the family name "Lord," you can search with `/Users?filter=name.familyName eq "Lord"`. This enriches your search precision, helping you identify all users with `Lord` family names, and ultimately contributing to a more organized and efficient workflow.

```Text Request
GET curl --location 'https://api.letsdeel.com/scim/v2/Users?filter=name.familyName%20eq%20%22Lord%22' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "totalResults": 1,
    "itemsPerPage": 50,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "active": false,
            "id": "3e518797-76d6-4b2e-9dc0-9e801e8fff3c",
            "emails": [
                {
                    "value": "wagner.marcelino+star.lord@deel.wtf",
                    "type": "home",
                    "primary": true
                },
                {
                    "value": "star.lord@deel.com",
                    "type": "work",
                    "primary": false
                },
                {
                    "value": "wagner.marcelino+star.lord@deel.wtf",
                    "type": "other",
                    "primary": false
                }
            ],
            "name": {
                "familyName": "Lord",
                "givenName": "Star"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "department": "",
                "costCenter": "168029",
                "organization": "173102",
                "manager": {
                    "value": ""
                }
            },
            "urn:ietf:params:scim:schemas:extension:2.0:User": {
                "startDate": "2023-08-18",
                "endDate": "",
                "state": "AM",
                "country": "BR",
                "employments": [
                    {
                        "contractId": "3rvk99y",
                        "title": "Accounting",
                        "startDate": "2023-08-18",
                        "contractType": "hris_direct_employee",
                        "state": "AM",
                        "country": "BR",
                        "active": false
                    }
                ]
            },
            "userName": "star.lord@deel.com",
            "title": "Accounting",
            "userType": "hris_direct_employee",
            "addresses": [
                {
                    "streetAddress": "Street alpha",
                    "locality": "Sao Paulo",
                    "region": "AM",
                    "postalCode": "04512336",
                    "country": "BR"
                }
            ],
            "meta": {
                "created": "2023-08-17T14:31:37.661Z",
                "lastModified": "2023-08-18T00:10:33.954Z",
                "resourceType": "User",
                "location": "https://api.letsdeel.com/scim/v2/Users/3e518797-76d6-4b2e-9dc0-9e801e8fff3c"
            }
        }
    ]
}
```

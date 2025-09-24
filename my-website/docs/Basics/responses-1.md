---
title: "Responses"
slug: "responses-1"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:33:54 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
When a request is successful, a response body will typically be sent back in the form of a JSON object.

Inside this JSON object, data will be set as the key. The value of these keys will generally be a JSON object for a request on a single object and an array of objects for a request on a collection of objects.

## Response for a single object

```
{
    "data": {
        "id": 1234
         . . .
     }
}
```

## Response to an object collection

```
{
    "data": [
    {
        "id": 1234
        . . .
    },
    {
        "id": 1235
        . . .
    }]
}
```

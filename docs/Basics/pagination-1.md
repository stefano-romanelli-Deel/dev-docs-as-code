---
title: "Pagination and sorting"
slug: "pagination-1"
excerpt: "Learn how to retrieve smaller sets of results, navigate pages, and sort large sets of resources using the API"
hidden: false
createdAt: "Mon Aug 22 2022 08:37:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 01 2024 13:01:54 GMT+0000 (Coordinated Universal Time)"
---
Deel APIs offer parameters that allow browsing the pages of results, sorting, or limiting the number of results returned by endpoints with large sets of resources.

> 📘 Confirm parameter availability for each endpoint
> 
> These parameters are not available for all endpoints. The [API reference](https://developer.deel.com/reference) of each endpoint is the source of truth for where limits, cursor-based pagination, and sorting are available.

## Limits

To preserve an optimal performance of the APIs, large sets of resources return a maximum of 99 results per page. If the number of results returned exceeds that number, [cursor-based pagination](#pagination) is used to divide the results.

When the `limit` parameter is available in an endpoint, you can set the number of resources you want to retrieve by including it as a query parameter in the request.

For example, to limit the number of results to 10:

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/contracts?limit=10' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

## Pagination

The APIs use cursor-based pagination to organize large sets of resources into pages and allow their browsing.

When results are returned in multiple pages, you will see a `page` object in the response.

```json
{
    "data": [
        …
    ],
    "page": {
        "cursor": "d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3",
        "total_rows": 1354
    }
}
```

Where:

| Name         | Type   | Format | Description                                                                                           | Example                                                                                                                                                                                      |
| ------------ | ------ | ------ | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`     | string | ID     | Indicates where the next page of results starts. Use it to navigate to the next page in your request. | `d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3` |
| `total_rows` | number | -      | Shows the total number of results available                                                           | 1354                                                                                                                                                                                         |

Note the value of the `cursor` parameter and append it as an `after_cursor` query parameter to your subsequent request to retrieve the next page of results.

For example:

```curl
curl --request GET \
     --url 'https://api.letsdeel.com/rest/v2/contracts?after_cursor=d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3m0d3' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer TOKEN'
```

This will return the next page of results for the given endpoint.

## Sorting

Additional sorting options are available for some endpoints, where appropriate, depending on the data model. In this section you can find some examples of the available sorting options:

| Name              | Type   | Format | Description                                                                                                                                                                                                                                              | Example       |
| ----------------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `order_direction` | string | enum   | Defines whether results should be sorted in ascending or descending order. The parameter that results are sorted by depends on the specific endpoint.                                                                                                    | `asc`, `desc` |
| `sort_by`         | string |  enum  | Allows to sort results by a specific field of the data model.                                                                                                                                                                                            | `start_date`  |
| `offset`          | number | -      | Provides the ability to start the results of the query from a specific index. The number is based on the database table row. For example, the first row is `0`, the fifth row is `4`. If you enter `4`, the fifth row will be the first result returned. | `0`           |

## Filtering

Additional filtering options may be available for some endpoints, where appropriate, depending on the data model. For more information, check the [API reference](https://developer.deel.com/reference) for the endpoint you're interested in.

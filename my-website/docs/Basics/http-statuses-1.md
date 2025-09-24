---
title: "HTTP Statuses"
slug: "http-statuses-1"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 08:33:25 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
# HTTP Statuses

Along with the HTTP methods that the API responds to, it will also return standard HTTP statuses, including error codes.

Codes in the `2xx` range indicate success. Codes in the `4xx` range indicate an error that failed given the information provided. Codes in the `5xx` range indicate an error with Deel’s servers.

```
HTTP/1.1 404 Not Found
{
    "errors": [{
        "message": "path not found"
    }]
}
```

## HTTP status code summary

| Code                    | Meaning                                                                                                                                                                                                                |
| :---------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200 - OK                | The request succeeded.                                                                                                                                                                                                 |
| 400 - Bad Request       | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).             |
| 401 - Unauthorized      | Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.                                   |
| 403 - Forbidden         | The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike `401 Unauthorized`, the client's identity is known to the server. |
| 404 - Not Found         | The server can not find the requested resource. In the browser, this means the URL is not recognized.                                                                                                                  |
| 429 - Too Many Requests | The user has sent too many requests in a given amount of time ("rate limiting").                                                                                                                                       |
| 500 - Server Error      | The server has encountered a situation it does not know how to handle.                                                                                                                                                 |

---
title: "Idempotency"
slug: "idempotency"
excerpt: ""
hidden: false
createdAt: "Wed Mar 19 2025 15:23:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Mar 27 2025 09:36:49 GMT+0000 (Coordinated Universal Time)"
---
Idempotency is the ability to ensure that the same operation can be made multiple times with the same effect as a single execution. This is particularly critical for state-changing operations such as resource creation or modification. Our API supports idempotency to help prevent duplicate operations, reduce the risk of data corruption, and improve the overall system reliability.

## Making idempotent requests

To take advantage of idempotency, a request to create or modify a resource must include a unique `Idempotency-Key` header. If your requests don't require idempotency, you can simply omit the header.

> 📘 Idempotency is supported only for `POST` and `PATCH` requests.
> 
> Methods like `GET`, `DELETE`, or `PUT` are inherently idempotent, so they do not require an idempotency key.

You can use any unique string for your idempotency key, but we recommend following these best practices to avoid collisions:

- Use a randomly generated UUID (version 4), almost every programming language has a [built-in UUID generator](https://www.uuidgenerator.net/dev-corner)
- We support a string as long as 64 characters, use as many characters as needed to guarantee uniqueness
- Let a key be unique for at least 24 hours, that's how long we cache responses for

Here's an example of an API request with an idempotency key:

```bash
curl https://api.letsdeel.com/rest/v2/{RESOURCE}   \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer {TOKEN}' \
  -H "idempotency-key: {YOUR_UNIQUE_KEY}" \
  --data-raw '{ "data": { … } }'
```

When a request with an idempotency key is received, the system checks if a response has already been generated for that key. If a previous successful (2xx) response exists, it is returned immediately. Note that only successful responses (2xx) are cached; responses for 4xx validation errors or 5xx server errors are not cached, allowing you to retry the request with the same idempotency key. For more information, see [Error handling](#error-handling)

Our system caches idempotent requests for 24 hours and, when it detects a cached response linked to the idempotency key, it returns it and adds an `x-original-request-id` header to the response, which contains the id of the original request. If the idempotency key is reused after the cached response expires, the system treats the request as a new one. This ensures that only the first valid execution of the request is recorded, while later retries consistently reflect the original outcome.

## Error handling

If you send a request with a new idempotency key and retry before the first request succeeds, you will receive a `429 - Request conflict detected. Try again in sometime` error along with a `Retry-After` header. Wait the number of seconds specified in the `Retry-After` header before retrying the request.

For other cases, retry only after the original request completes. If the original request was intentionally canceled, wait 2 minutes before retrying.

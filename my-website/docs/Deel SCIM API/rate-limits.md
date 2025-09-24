---
title: "Rate Limits"
slug: "rate-limits"
excerpt: ""
hidden: false
createdAt: "Mon Mar 27 2023 08:07:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 28 2024 19:21:47 GMT+0000 (Coordinated Universal Time)"
---
Requests through the Deel SCIM API are rate limited per token. Current rate limits:

- 5 request per second

Once you exceed either limit, you will be rate-limited until the next cycle starts. Space out any requests that you would otherwise issue in bursts for the best results.

If the rate limit is reached, subsequent requests will receive a 429 error code until the request reset has been reached. You can see the format of the response in the examples.

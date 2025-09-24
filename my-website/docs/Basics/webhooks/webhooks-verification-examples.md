---
title: "Webhooks verification examples"
slug: "webhooks-verification-examples"
excerpt: "A collection of code snippets to help you verify webhook signatures"
hidden: false
createdAt: "Fri May 09 2025 13:27:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 09 2025 13:40:05 GMT+0000 (Coordinated Universal Time)"
---
This article provides examples of how to verify webhook signatures in various languages and frameworks.

## NodeJS

Let’s take a look at what authenticating Webhooks using signature verification looks like with NodeJS

### Requirements

- Node.js >= 16
- Webhook configured to work with a [local server](https://developer.deel.com/docs/webhooks-get-started#testing-webhooks)

### Launch a local server with verification

1. Create 2 files `main.js` and `package.json`.
2. Copy content from the code snippet below.
3. Put your `Signing key` into the `secret` const.
4. Run `npm i`.
5. Run `npm start`.

```javascript main.js
const express = require('express');
const bodyParser = require('body-parser');
const crypto = require('node:crypto');

// App
const app = express();
const port = 1337;
const sigHeaderName = 'x-deel-signature';
const sigHashAlg = 'sha256';
const sigPrefix = 'POST';
const secret = 'your_webhook_signing_key';

//Get the raw body

//Validate payload
function validatePayload(req, res, next) {
    if (req.get(sigHeaderName)) {
        //Extract Signature header
        const sig = Buffer.from(req.get(sigHeaderName) || '', 'utf8')

        //Calculate HMAC
        const hmac = crypto.createHmac(sigHashAlg, secret)
        const digest = Buffer.from(hmac.update(sigPrefix + req.rawBody).digest('hex'), 'utf8');

        //Compare HMACs
        if (sig.length !== digest.length || !crypto.timingSafeEqual(digest, sig)) {
            const message = `Request body digest (${digest}) did not match ${sigHeaderName} (${sig})`;
            console.error(message);
            return res.status(401).send({
                message
            });
        } else {
            return res.status(200).send({
                message: `Webhook signature verification successful`
            });
        }
    }

    return next();
}

function post(req) {
    console.log(JSON.stringify(req.body, null, 2));
}

app.use(bodyParser.json(
    {
        verify: (req, res, buf, encoding) => {
            if (buf && buf.length) {
                req.rawBody = buf.toString(encoding || 'utf8');
            }
        },
    }
));

app.use(validatePayload);
app.post('/', post);
app.set('port', port);

app.listen(port, () => console.log(`Server running on localhost: ${port}`));
```

```json package.json
{
  "name": "validate-webhook",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node main.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "body-parser": "~1.20.1",
    "express": "~4.18.2"
  }
}
```

Once the server is running, you can use the below cURL after replacing placeholder values to verify the signature.

```curl
curl --location 'http://localhost:$PORT' \
--header 'x-deel-signature: <header value you received>' \
--header 'Content-Type: application/json' \
--data-raw '<data you received without any modification>'
```

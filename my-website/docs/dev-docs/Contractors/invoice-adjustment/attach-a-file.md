---
title: "Attach A File"
slug: "attach-a-file"
excerpt: ""
hidden: false
createdAt: "Wed Aug 24 2022 12:33:17 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:31:51 GMT+0000 (Coordinated Universal Time)"
---
You can attach files to certain endpoints, for example when adjusting an invoice

```shell
curl --location -g --request POST '{{host}}/rest/v2/invoice-adjustments' \
--header 'Authorization: Bearer {{token}}' \
--form 'contract_id="m4zwgdr"' \
--form 'amount="100"' \
--form 'type="expense"' \
--form 'description="Work monitor and keyboard."' \
--form 'date_submitted="2022-07-25"' \
--form 'file=@"/file/to/path"'
```

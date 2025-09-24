---
title: "Amend Contract"
slug: "amend-contract"
excerpt: ""
hidden: false
createdAt: "Mon Aug 22 2022 11:41:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 15:31:35 GMT+0000 (Coordinated Universal Time)"
---
Sometimes things change when it comes to employee contracts. So whether it is promoting someone to a new role and salary band, increasing their holiday days, or more, you can do this entirely via the Deel API.

| Clients can make amendments to                                       | Clients can not make amendments to                                           |
| :------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| ✅ Job title                                                          | ✘ Country of tax residence                                                   |
| ✅ Payment details (rate, invoice cycle, payment due date)            | ✘ Start date (original start date must remain but an amendment may be added) |
| ✅ Contract currency                                                  | ✘ Contract type                                                              |
| ✅ Work schedule                                                      | ✘ Client entity information                                                  |
| ✅ Scope of work                                                      |                                                                              |
| ✅ End of contract (end date and notice period)                       |                                                                              |
| ✅ Special clauses                                                    |                                                                              |
| ✅ Employee personal details (full legal name, passport number, etc.) |                                                                              |

# Amend a contract

**Step 1:** Amend contract

You can amend payment, job, or personal information.

Please see below an example of changing the seniority level of an existing contract:

```shell
curl --request POST \
     --url 'https://api.letsdeel.com/rest/v2/contracts/37nex2x/amendments' \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {token}' \
     --header 'content-type: application/json' \
     --data '
{
     "data": {
         "effective_date": "2023-01-01",
         "seniority_id": 2
     }
}
'
```

Below you can find another example of changing the payment information of an existing contract:

```shell
curl --location -g --request POST 'https://api.letsdeel.com/rest/v2/contracts/{{contractId}}/amendments' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "amount": 123,
    "scale": "daily",
    "effective_date": "2023-01-01",
    "frequency": "monthly",
    "cycle_end": 21,
    "cycle_end_type": "DAY_OF_MONTH",
    "payment_due_type": "REGULAR",
    "payment_due_days": 0,
    "pay_before_weekends": true
  }
}'
```

**Step 2**: Sign contract amendment

After you have amended the contract, you can sign the contract using the sign contract endpoint.

**Step 3**: Send the amended contract to the worker

When you have signed the amended contract, you will need to send a counterpart document to sign to your employee.

```shell Send contract to worker
curl --location -g --request POST 'https://api.letsdeel.com/rest/v2/contracts/{{contractId}}/invitations' \
--header 'Authorization: Bearer {token}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data": {
    "email": "{contractor_email}",
    "message": "Please review and sign the amended contract."
  }
}'
```

Finally, Deel will countersign both documents and the amendment will be active on the designated date.

> 📘 Please note that some changes may require an increase in deposit such as increasing the employee's salary or increasing the number of holiday days they will receive. In these situations, a member of the Deel team will reach out to explain the required next steps.

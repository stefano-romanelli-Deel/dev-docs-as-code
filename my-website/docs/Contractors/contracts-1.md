---
title: "Contracts"
slug: "contracts-1"
excerpt: ""
hidden: false
createdAt: "Wed Dec 28 2022 09:28:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 25 2025 13:49:53 GMT+0000 (Coordinated Universal Time)"
---
Hiring an independent contractor through the API starts with creating a contract. The contract defines the terms of work and any compliance documents required for the contractor.  
Once the contract is created, you can invite the contractor to sign it and start working with them.

This section explains how to use the API to hire contractors, from creating a contract to finilizaing signatures.

Hiring a contractor through the API involves several actions. You can:

1. Create different types of contracts, each tied to a specific payment model.
2. [Sign contracts](https://developer.deel.com/docs/sign-contract) on behalf of your organization
3. Invite contractors to review and [sign their contracts](https://developer.deel.com/docs/invite-contractor)
4. Attach custom PDFs, such as contract templates or compliance documents

## Contract types

The API supports several contract types. Each has its own fields and validation rules. Start with [Create a contract](https://developer.deel.com/docs/create-contract) for the common contract-creation steps and payload structure, then move to the type-specific guide:

- [Fixed rate](https://developer.deel.com/docs/create-contract-fixed-rate).
- [Pay as you go (fixed rate)](https://developer.deel.com/docs/create-contract-payg-fixed).
- [Pay as you go (task-based)](https://developer.deel.com/docs/create-contract-payg-task).
- [Milestone based](https://developer.deel.com/docs/create-contract-milestone).

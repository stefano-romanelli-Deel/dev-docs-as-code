---
title: "Managers"
slug: "managers"
excerpt: ""
hidden: false
createdAt: "Tue Jul 18 2023 11:21:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
Efficiently managing your organization hinges on building a reliable team of managers. On your organization's Deel account, you can add managers as a crucial step towards streamlining operations and enhancing accountability within your team. 

The Managers API gives Deel API clients the ability to programmatically create managers to be added to their accounts or display a list of managers on their accounts. 

This guide outlines the process of leveraging Deel's API to create manager profiles within your organization's account. 

## Implemented feature

With our Managers APIs, you can effortlessly:

1. Create Manager: Add a new manager to your organization by supplying the requisite details, thereby enhancing operational efficiency.

***

# API requirements

HTTP Method: POST 

Authorization: Bearer token

Data: An object with the manager's details

| Field      | Type   | Required | Description           |
| :--------- | :----- | :------- | :-------------------- |
| first_name | string | yes      | Manager's first name. |
| last_name  | string | yes      | Manager's last name.  |
| email      | string | yes      | Manager's email.      |

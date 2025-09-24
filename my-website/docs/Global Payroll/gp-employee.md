---
title: "Employee"
slug: "gp-employee"
excerpt: ""
hidden: true
createdAt: "Fri Oct 27 2023 12:14:34 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
Deel's Global Payroll API presents a streamlined and efficient way of managing employee details. With our latest update, managing employee data has never been more effortless and precise. Whether you're adjusting an employee's information, address, PTO or compensation details, our API makes these tasks a breeze.

# Implemented Features

The Worker resource of our Global Payroll API currently enables partners to perform various operations related to worker (employee) management. Hence with our API you can effortlessly:

1. Update Compensation: Streamline payroll processes, ensure timely and accurate compensation updates to maintain employee satisfaction.
2. Update Employee Address: Whether an employee has moved or there’s a need to correct an existing address, keep your employees’ address details current with this endpoint.
3. Update Employee Information: Enhance data accuracy, and improve HR efficiency, ensuring employee records reflect the most current information.
4. Update PTO: Save time, reduce errors, and easily manage or update your employees’ PTO records to ensure they are always up-to-date.

***

# API Requirements

You can update an employee's compensation by sending an HTTP request to the URL below. Like most REST API requests, it should contain:

1. **Method**: PATCH
2. **Authorization**: Bearer token
3. **Data**: An object that is made up of the required or optional parameters for each endpoint. 

| API                  | Parameter          | Type   | Required | Description               | Enums                                                                             |
| :------------------- | :----------------- | :----- | :------- | :------------------------ | :-------------------------------------------------------------------------------- |
| compensation         | scale              | string | yes      | Compensation scale        |                                                                                   |
|                      | salary             | int    | yes      | Employee's salary         |                                                                                   |
|                      | effective_date     | string | yes      | Compensation start date   |                                                                                   |
| employee address     | state              | string | no       | Employee's state          |                                                                                   |
|                      | city               | string | no       | Employee's city           |                                                                                   |
|                      | street             | string | no       | Employee's street         |                                                                                   |
|                      | zip                | string | no       | Employee's zip code       |                                                                                   |
| employee information | first_name         | string | no       | Employee's first name     |                                                                                   |
|                      | middle_name        | string | no       | Employee's middle name    |                                                                                   |
|                      | last_name          | string | no       | Employee's last name      |                                                                                   |
|                      | date_of_birth      | string | no       | Employee's date of birth  |                                                                                   |
|                      | gender             | string | no       | Employee's gender         |                                                                                   |
|                      | marital_status     | string | no       | Employee's marital status | single, married, divorced, separated, widowed, registered partnership, common law |
| PTO                  | accrual_start_date | string | yes      | PTO accrual start date    |                                                                                   |
|                      | yearly_allowance   | string | yes      | PTO yearly allowance      |                                                                                   |

---
title: "People"
slug: "people"
excerpt: ""
hidden: false
createdAt: "Fri Jul 21 2023 10:47:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 13:36:50 GMT+0000 (Coordinated Universal Time)"
---
Understanding the structure and people flow within your organization can be transformative for productivity, communication and streamlining operations. 

People API enables Deel API clients to programmatically fetch, analyze and leverage a comprehensive list of individuals associated with their organization to enhance team management and strategic decision-making.

This guide provides an in-depth overview of using the People API endpoint within your organization's account on Deel.

***

# API Requirements

HTTP Method: `GET`

Authorization: `Bearer token`

> ℹ️ Ensure that 'people:read' scope is enabled on your API access token.

Request parameters: There are currently six query filters accepted by the Get People API.

| Field           | Description                                                                                                     | Enums                                                                                                                                                                                                                                 |
| :-------------- | :-------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| limit           | Specifies maximum number of results to return                                                                   | 1-100                                                                                                                                                                                                                                 |
| offset          | Determines the point in the list where you want to start displaying content                                     |                                                                                                                                                                                                                                       |
| sort_by         | Defines the property by which the results should be sorted                                                      | id, first_name, last_name, full_name, email, personal_email, country, birth_date, pic_url, hiring_type, start_date, team, job_title, hiring_status, completion_date, monthly_payment, direct_manager, direct_reports_count, worker_id |
| sort_order      | Determines the order in which the results are sorted. 'asc' for ascending order and 'desc' for descending order | asc, desc                                                                                                                                                                                                                             |
| hiring_statuses | Filters the results based on their hiring status                                                                | inactive, onboarding                                                                                                                                                                                                                  |
| search          | Used to filter results based on a search term                                                                   | name, email                                                                                                                                                                                                                           |

***

# Get people

To retrieve a comprehensive list of people within your organization, providing you with valuable insights for making informed decision-making. Pass any of the accepted query filters with their corresponding enum, to the `rest/v2/people` endpoint.

**Request URL**

```js cURL
GET https://api.letsdeel.com/rest/v2/people
```

### Sample request & response

```js Request
curl --location 'https://api.letsdeel.com/rest/v2/people?hiring_statuses=inactive&sort_by=full_name&limit=2' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "data": [
        {
            "id": "dfd65727-e0f2-4e2e-94e3-91a19962d446",
            "created_at": "2023-07-10T12:13:13.440Z",
            "first_name": "Tom",
            "last_name": "Hanks",
            "full_name": "Tom Hanks",
            "emails": [
                {
                    "type": "primary",
                    "value": "tom@hanks.com"
                },
                {
                    "type": "work",
                    "value": null
                },
                {
                    "type": "personal",
                    "value": "tom@hanks.com"
                }
            ],
            "birth_date": null,
            "start_date": "2023-07-25",
            "nationality": null,
            "client_legal_entity": {
                "id": 242423,
                "name": "Aleena Moon"
            },
            "state": null,
            "seniority": null,
            "completion_date": "2023-07-19T13:06:30.918Z",
            "direct_manager": null,
            "direct_reports": null,
            "direct_reports_count": 0,
            "employments": [
                {
                    "id": "mx952ev",
                    "name": "PAYG API Task Based Contract",
                    "team": {
                        "id": 384149,
                        "name": "Oleena"
                    },
                    "email": "tom@hanks.com",
                    "state": null,
                    "country": null,
                    "payment": null,
                    "is_ended": true,
                    "timezone": null,
                    "job_title": "Business Analyst",
                    "seniority": null,
                    "start_date": "2023-07-25",
                    "work_email": null,
                    "hiring_type": "contractor",
                    "hiring_status": "inactive",
                    "completion_date": "2023-07-19T13:06:30.918Z",
                    "contract_status": "cancelled",
                    "voluntarily_left": null,
                    "contract_coverage": null,
                    "new_hiring_status": "inactive",
                    "client_legal_entity": {
                        "id": 232324,
                        "name": "Aleena Moon"
                    },
                    "has_eor_termination": null,
                    "contract_is_archived": false,
                    "contract_has_contractor": false,
                    "is_user_contract_deleted": false,
                    "hris_direct_employee_invitation": null
                }
            ],
            "hiring_status": "inactive",
            "new_hiring_status": "inactive",
            "hiring_type": "contractor",
            "job_title": "Business Analyst",
            "country": null,
            "timezone": null,
            "department": null,
            "work_location": null
        },
        {
            "id": "a4f91c16-2104-4841-ba4e-77fdcb5bc6ee",
            "created_at": "2023-07-21T07:44:58.437Z",
            "first_name": "Whitney",
            "last_name": "Houston",
            "full_name": "Whitney Houston",
            "emails": [
                {
                    "type": "primary",
                    "value": "whitney@houston.com"
                },
                {
                    "type": "work",
                    "value": null
                },
                {
                    "type": "personal",
                    "value": "whitney@houston.com"
                }
            ],
            "birth_date": null,
            "start_date": "2023-08-05",
            "nationality": null,
            "client_legal_entity": {
                "id": 232324,
                "name": "Aleena Moon"
            },
            "state": "BE",
            "seniority": "Lead (Individual Contributor Level 4)",
            "completion_date": "2023-07-21T07:45:11.807Z",
            "direct_manager": null,
            "direct_reports": null,
            "direct_reports_count": 0,
            "employments": [
                {
                    "id": "3edvyng",
                    "name": "Fixed-Rate API- 2023-07-21",
                    "team": {
                        "id": 384149,
                        "name": "Oleena"
                    },
                    "email": "whitney@houston.com",
                    "state": "BE",
                    "country": "GE",
                    "payment": null,
                    "is_ended": true,
                    "timezone": null,
                    "job_title": "QA Engineer",
                    "seniority": "Lead (Individual Contributor Level 4)",
                    "start_date": "2023-08-05",
                    "work_email": null,
                    "hiring_type": "contractor",
                    "hiring_status": "inactive",
                    "completion_date": "2023-07-21T07:45:11.807Z",
                    "contract_status": "cancelled",
                    "voluntarily_left": null,
                    "contract_coverage": null,
                    "new_hiring_status": "inactive",
                    "client_legal_entity": {
                        "id": 232324,
                        "name": "Aleena Moon"
                    },
                    "has_eor_termination": null,
                    "contract_is_archived": false,
                    "contract_has_contractor": false,
                    "is_user_contract_deleted": false,
                    "hris_direct_employee_invitation": null
                }
            ],
            "hiring_status": "inactive",
            "new_hiring_status": "inactive",
            "hiring_type": "contractor",
            "job_title": "QA Engineer",
            "country": "GE",
            "timezone": null,
            "department": null,
            "work_location": null
        }
    ]
}
```

<h1>Get a single person by id</h1>

To fetch detailed information for a specific person in your organization using their unique id, thus facilitating individual management and targeted communication. Replace `:id` in the endpoint `/v2/people/:id` with the id of the person whose data you're looking to get.

**Request URL**

```js cURL
GET https://api.letsdeel.com/rest/v2/people/:id
```

### Sample request & response

```js Request
curl --location 'https://api.letsdeel.com/rest/v2/people/a4f91c16-2104-4841-ba4e-77fdcb5bc6ee' \
--header 'Authorization: Bearer {token}' \
```
```Text Response
{
    "data": {
            "id": "a4f91c16-2104-4841-ba4e-77fdcb5bc6ee",
            "created_at": "2023-07-21T07:44:58.437Z",
            "first_name": "Whitney",
            "last_name": "Houston",
            "full_name": "Whitney Houston",
            "emails": [
                {
                    "type": "primary",
                    "value": "whitney@houston.com"
                },
                {
                    "type": "work",
                    "value": null
                },
                {
                    "type": "personal",
                    "value": "whitney@houston.com"
                }
            ],
            "birth_date": null,
            "start_date": "2023-08-05",
            "nationality": null,
            "client_legal_entity": {
                "id": 232324,
                "name": "Aleena Moon"
            },
            "state": "BE",
            "seniority": "Lead (Individual Contributor Level 4)",
            "completion_date": "2023-07-21T07:45:11.807Z",
            "direct_manager": null,
            "direct_reports": null,
            "direct_reports_count": 0,
            "employments": [
                {
                    "id": "3edvyng",
                    "name": "Fixed-Rate API- 2023-07-21",
                    "team": {
                        "id": 384149,
                        "name": "Oleena"
                    },
                    "email": "whitney@houston.com",
                    "state": "BE",
                    "country": "GE",
                    "payment": null,
                    "is_ended": true,
                    "timezone": null,
                    "job_title": "QA Engineer",
                    "seniority": "Lead (Individual Contributor Level 4)",
                    "start_date": "2023-08-05",
                    "work_email": null,
                    "hiring_type": "contractor",
                    "hiring_status": "inactive",
                    "completion_date": "2023-07-21T07:45:11.807Z",
                    "contract_status": "cancelled",
                    "voluntarily_left": null,
                    "contract_coverage": null,
                    "new_hiring_status": "inactive",
                    "client_legal_entity": {
                        "id": 232324,
                        "name": "Aleena Moon"
                    },
                    "has_eor_termination": null,
                    "contract_is_archived": false,
                    "contract_has_contractor": false,
                    "is_user_contract_deleted": false,
                    "hris_direct_employee_invitation": null
                }
            ],
            "hiring_status": "inactive",
            "new_hiring_status": "inactive",
            "hiring_type": "contractor",
            "job_title": "QA Engineer",
            "country": "GE",
            "timezone": null,
            "department": null,
            "work_location": null
        }
}
```

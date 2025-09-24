---
title: "Publish apps on App Store"
slug: "app-listing"
excerpt: "Learn how to submit your app to be published on the App Store"
hidden: false
createdAt: "Fri Sep 15 2023 16:38:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Dec 18 2024 10:22:26 GMT+0000 (Coordinated Universal Time)"
---
After you create an app, you can request to publish it to the App Store and make it available to users outside of your organization. To publish an app, you must submit a publishing request, then our team will review and approve it.

This article will guide you through the submission process and ensure your app meets the publishing standards.

## Before you begin

Before starting the submission, ensure that your app is:

- An [OAuth2 app](https://developer.deel.com/docs/oauth2), only those are [eligible for the App Store](https://developer.deel.com/docs/oauth2-apps)
- Complete and fully functional, we'll review your app during the submission process

## Start the Submission Process

When you're ready to start the submission process, 

1. Navigate to the **Apps** tab within the Developer Center.
2. Locate your app, click the ellipses (3 dots), and choose **Publish On App Store** from the dropdown menu.

![](https://files.readme.io/f5aae339f605f65d17dcdc6d8b20335961a0cf02117879ea7cee6da276f21450-developer-center-app-publish-calledout.png)


## Complete the listing wizard

The listing form is divided into several sections. In each section, you'll be asked to provide information about your app. Some of the information you provide will be visible in the app listing on the App Store, while other is only used by us to review your app.

You can refer to the following screenshot for a 1-to-1 mapping between what users see in the app store and the information requested in the app submission form.

![](https://files.readme.io/a468b28dd479d23a682a774141033b4085ddf27da427003f9a7b6046ec657284-app-elements-callouts.png)


### Step 1: App Store Card Details

The details you add at this step will be shown mainly in the app list, but also in the app page.

Fill the form with the following details, then click **Continue**.

![](https://files.readme.io/865a3b286b0bd9953b5e35c470e336bbad64c612d34b430d8953ad5c330ea51f-publish-app-step-1.png)


| Field              | Description                                                                                                                                                                                                                      |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App name           | The public name of the app, shown to all Deel users. You can edit this from the **Apps** section. For more information, visit [Create an app](https://developer.deel.com/docs/oauth2-apps#create-an-app). Maximum 30 characters. |
| Logo               | Shown in the app list and on the app page. For more information, visit [Logo requirements](#logo-requirements).                                                                                                                  |
| 1-line description | Describes your company and is shown in the app list and the app page. Maximum 50 characters.                                                                                                                                     |
| Categories         | Users can filter apps in the app store based on the categories you select. If you select more than one, they'll be used in order of appearance.                                                                                  |

### Step 2: App store page details

### App Store Page Details

The details you add at this step will be shown in the app's details page.

Fill the form with the following details, then click **Continue**.

![](https://files.readme.io/902c4f2f6d649db4bb96da10be0358033de3e9f28d6098a4e7a663437ca45773-publish-app-step-2.png)


| Field                        | Description                                                                                                                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Product description          | What you write here is shown in the **About** section. Use it to describe your product at a high level.                                                                                                                                                              |
| App description and features | What you write here is shown in the **Integration features** section. Use it to give a high level description of what the app does and provide a list of its main features. We recommend using bullet points to make sure the list is easy to understand.            |
| Landing page for referrals   | A link in the details page that allows users to navigate to your landing page. We recommend using a referral link to track traffic coming from the app store. For example, `https://www.acmecorp.com/?utm_source=deel&utm_medium=website&utm_campaign=integrations`. |

### Step 3: Help information

The details you add at this step will also be shown in the app's details page, with a stronger focus on helping users set the app up and getting support.

Fill the form with the following details, then click **Continue**.

![](https://files.readme.io/344511a55edc73648b1008e2f22077b93c09f68009f2a95e7148ae9027c98ca0-publish-app-step-3.png)


| Field             | Description                                                                                                                                                                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Help article link | URL to a help-center article on your website that will be shown in the **Help article** section. The article must include step-by-step instructions on how to set up the app. For more information, see an [example from eqtble](https://support.eqtble.com/integrations/hris/deel). |
| How to setup      | A summary of the steps needed to set up the app that will be show in the **How to set up** section. A short version of what users will find in the help article.                                                                                                                     |
| Support email     | An email address where users can reach out for support that will be show in the **How to get help?** section.                                                                                                                                                                        |

### Step 4: Material for Deel

We will store the details you provide at this step internally and use them to address potential user inquiries or recommendations.

Fill the form with the following details, then click **Submit**.

![](https://files.readme.io/7d4585532059933fcd6e61a5ea4a622c2d402cf469596e6441b4f6e489745f78-publish-app-step-4.png)


| Field                | Description                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Demo video link      | A video link showcasing the app. For detailed requirements, see [Video requirements](#video-requirements).                       |
| Escalation email     | An email address that only we will use to contact your organization if needed.                                                   |
| Test account details | We use these to test and review the app. For detailed requirements, see [Test account requirements](#test-account-requirements). |
| FAQ                  | The                                                                                                                              |
| Pricing              | We will use this to test and review the app. Your product pricing and features. You may link to your pricing page.               |

When you submit the form, the status of your app will change to **UNDER REVIEW**. Our team will evaluate your submission and if approved, your app will go live for everyone to explore.

![](https://files.readme.io/454d7a879dde3ac9b916a664ff5b5d859c8b7314757afe1e83a9471812f64d9b-publish-app-success.png)


## App submission reference

This section provides reference information for the submission process.

### Video requirements

The video that you submit must meet the following requirements:

- Be uploaded to a platform like YouTube, Loom, or Google Drive
- Be available through a public link
- Be less than 5 minutes long

We recommend to structure the video in the following way:

1. A quick introduction to your product.
2. How to set the integration with Deel.
3. Show how your app works, including what happens after it's connected to Deel, and how data is used in your app.

You can refer to [an example video](https://www.youtube.com/watch?v=G3b7XjYwfE0) for inspiration.

### Test account requirements

As the review from our team is mandatory, you must provide the following details:

- URL for the test account
- Test user account username and password
- Any technical documentation, if available

We use these details to test and review the integration. We assess whether the app functions as described at a high level and it meets our standards.

### Logo requirements

The logo that you submit must meet the following requirements:

- Square logo with a 1:1 aspect ratio
- Recommended dimensions: 200px x 200px
- PNG format with a transparent background
  - A colored background is fine if it's part of the logo color scheme

> 👍 Use a favicon or the first letter of your app’s wordmark if needed.

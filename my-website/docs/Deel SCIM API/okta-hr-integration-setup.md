---
title: "Okta HR Integration Setup"
slug: "okta-hr-integration-setup"
excerpt: ""
hidden: true
createdAt: "Wed Apr 05 2023 10:04:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 11 2023 18:35:07 GMT+0000 (Coordinated Universal Time)"
---
### Configuration in Deel

The first part of the integration includes setup to be completed within Deel.

1. Navigate to Apps & Integrations store. 

2. Find and click on Okta SCIM integration.

3. Click on the ‘Connect’ button.

4. Complete the instructions for Okta configuration.

### Configuration in Okta

The second part of the integration includes setup to be completed in Okta. 

1. Log into Okta as an Administrator.
2. Search for the Deel HR application and add it.
3. Click Add integration.
4. Select the Provisioning tab.
5. In the left menu, select Integration.
6. Click the Configure API integration button.
7. Select Enable API Integration.
8. Paste the Base URL from the previous step in the Base URL field.
9. Paste the Organization token in the API Token.
10. Click Save.
11. In the left menu, select To Okta.
12. Scroll down to the Profile & Lifecycle Sourcing section.
13. Click Edit.
14. Check the box next to Allow Deel HR to source Okta users.
15. Click Save.

# Release Notes

### 12 May 2025
- **Issue Detail:** We had an issue in Lab 1 Ex 1 while testing the Echo Api in APIM management service, where the GET retrieve operation for the Echo Api was giving a 404 Error not found response.
- **Resolution Steps:** Upon checking this with Microsoft support, we found that the endpoint associated with the Echo API has been migrated to a new on,e and as the migration process from MS is still in progress, the new endpoint is not reflecting. So I created a new Echo Api with the updated endpoint, and we got the expected response with it.
-  **Content update:**  Hence have added steps in the lab guide to create a new Echo API in Lab 1 with the updated endpoint.

### 31 December 2024

- Updated the content for **Exercise 9,Task 3: API Proxy to Serverless**. The Functions option in the Function App is no longer available. Included the steps to create the function and deploy it to the Function App using VS Code.

- Enhanced lab guide instructions and updated screenshots for better user experience.

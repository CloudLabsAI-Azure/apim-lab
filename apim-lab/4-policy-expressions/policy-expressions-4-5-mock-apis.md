## Exercise 4 Task 5: Mock policy

In this task, you will create a mock response for an API operation in the Star Wars API.

Mocking in Azure API Management is a useful mechanism for API consumers to interact with APIs without waiting for the backend to be ready. 

1. From your APIM instance, open the **Star Wars (1)** API and select **+ Add Operation (2)**. 

1. Create a new GET operation:
    - Display name: **Get Film** **(3)**
    - Name: **get-film** **(4)**
    - URL: **/film** **(5)**
 
      ![](media/E4T5S2-0209.png)
  
1. In the **Responses (1)** configuration tab, press **+ Add response (2)**, Select `200 OK` **(3)**.

    ![APIM Policy Mock Response](media/33a.png)

1. Click on **+ Add representation (1)** under Representations, from the content-type  drop-down select `application/json`**(2)** and add this below sample data under **Sample (3)** and click on **Save (4)**:

    ```json
    {
      "count": 1,
      "films": [{ "title": "A New Hope", "release-date": "05/25/1977" }]
    }
    ```
  
      ![APIM Policy Mock Frontend](media/p13t5p4.png)

1. Under **Inbound processing** section , click on **Policy code editor** for the **Get Film** Operation.

    ![](media/p13t5p5.png)
  
1. In the inbound policy editor, add **Mock Response** **(1)** under **Other policies** after the `<base />` tag and click on **Save (2)**.

    ```xml    
    <inbound>
        <base />
        <mock-response status-code="200" content-type="application/json" />
    </inbound>
    ```

      ![APIM Policy Mock Inbound](media/p13t5p6.png)

1. Invoke the API from the **Test (1)** tab, click on **Send (2)** to receive a `200` success **(3)** with the mocked film data .

    ![APIM Policy Mock Response](media/E4T5S7-0209.png)

   > **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
   > - If you receive a success message, you can proceed to the next task.
   > - If not, carefully read the error message and retry the step, following the instructions in the lab guide. 
   > - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help you out.

      <validation step="3083e0a3-97d5-46ce-bdf3-7c9e6cd526e7" />
---

## Summary 

In this task, you created a mock response for the "Get Film" operation in the Star Wars API using Azure API Management. The mock response returns a 200 OK status with sample JSON data containing film information, allowing API consumers to interact with the API without needing a backend service.

### Now, click on Next from the lower right corner to move on to the next page for further tasks of Exercise 4.

  ![](../gs/media/nextpagetab.png)

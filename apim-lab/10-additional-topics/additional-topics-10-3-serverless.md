## Continuation for Exercise 9,Task 3: API Proxy to Serverless

Azure Serverless (Functions and Logic Apps) can be configured to benefit from the advantages of Azure API Management.

### Task 3.1: Azure Functions

1. Create a simple function that is Triggered by an **HTTP Request**.

2. Search for **Function App**  in the portal, click on **Create** and select **Consumption**.
   
   ![](media/Pg28-funcapp.png)

   ![](media/api20.png)

4. Enter the following details:

   - Subscription: Select the default subscription (1)
   - Resource group: **apim-rg (2)**
   - Function name : **func-<inject key="Deployment ID" enableCopy="false" />** **(3)**
   - Runtime stack : Select **.Net (4)**
   - Version : **8(LTS), isolated worker model (5)**
   - Region: **Select the region you used for previous exercises (6)**
   - Operating System : **Windows (7)**
   - Click on **Review + Create (8)**.

      ![](media/api21.png)

5. On the **Review + Create** tab, click on **Create**.

6. Once the Resource is created click on **Go to Resource**.
   
7. Open Visual Studio Code from desktop.

9. Click on **Azure shaped icon (1)** and click on **Azure Functions (2)** and select **Create Function..(3)**.

      ![](media/a.png)

10. Please follow these steps after clicking on Create Function:
    
    - Navigate to `C:/LabFiles/functions` and click on the **functions** folder **(1)**
    - Select a language : **C# (2)**
    - Select a .NET runtime : **.NET 8.0 Isolated LTS (3)**
    - Select a template for your project's first function : **HTTP trigger (4)**
    - Provide a function name: **GetRandomColor (5)**
    - Provide a namespace: **Select the default (6)**
    - AccessRights: **Function (7)**
    - Select how you would like to open your project: **Open in current window (8)**

11. Click on **Yes, i trust the authors** when prompted.

       ![](media/api14.png)

12. Add the below mentioned code in the existing code as shown in the image below. Click on `Ctrl+S`.

      ```c#
      //string[] strColors = { "blue", "lightblue", "darkblue" };
      string[] strColors = { "green", "lightgreen", "darkgreen" };
   
      Random r = new Random();
      int rInt = r.Next(strColors.Length);
   
      return  (ActionResult)new OkObjectResult(strColors[rInt]);
      ```

       ![](media/T3.1S11.png)
   
13. Click on **Deploy to Azure** and follow the below steps:

       ![](media/api50.png)
    
    **Note:** If you recieve an error mentioning you are not sign in to Azure, click on Sign in and use the environment credentials to login, and then click on Deploy to Azure. 
     
    - Select a function app: **func-<inject key="Deployment ID" enableCopy="false" />** 
    - Click on **Deploy** when prompted.

         ![](media/api13.png)

         ![](media/funcdep01.png)

15. Lets add the function to Azure API Management. Navigate back to the **API Management service**, in the **API blade (1)** select **+ Add API (2)** and the **Function App tile (3)**.

       ![](media/api12.png)

   - Click on the **Browse** button to get a list of Functions in the subscription

        ![](media/06.png)

   - Select the Function App and then the Function

      ![](media/07.png)

      ![](media/08.png)

   - Amend the Names / Descriptions, URL suffix, and select the Products

      ![](media/09.png)

   - As previously added CORS policy

   - Validate the function works - either from the Azure management portal or the developer portal

      ![](media/10.png)

      ![](media/11.png)

> **Congratulations** on completing the task! Now, it's time to validate it.
<validation step="b25ed567-5d6a-4ddf-a9e0-dee66fcf78d7" />

### Task 3.2: Azure Logic Apps

- Create a simple logic app that is Triggered by an HTTP Request

1. Search for **Logic App** in the portal, click on **Add** and select **Consumption**.

   ![](media/Pg28-logicapp.png)

   ![](media/api30.png)
  
1. Enter the following details:

   - Subscription: Select the default subscription (1)
   - Resource group: **apim-rg (2)**
   - Logic App Name: **logicapp-<inject key="Deployment ID" enableCopy="false" />** **(3)**
   - Region : Select the regions you have used for previous exercises **(4)**
   - Click on **Review + create (5)**.

      ![](media/api11.png)

1. On the **Review + Create** tab, click on **Create**.

1. Once the Resource is created click on **Go to Resource**, from the left menu under Development Tools select **Logic app designer** and click on **Add a trigger (2)**.

   ![](media/api10.png)

1. In the logic app designer **search (1)** and **select (2)** **when a HTTP request is received**.

   ![](media/api40.png)

   - In the Request body JSON Schema **insert the following JSON (1)**, and select **+ New step (2)**.

      ```
      {
      "type" : "object",
      "properties" : {
            "msg": {
               "type" : "string"
            }
      }

      }
      ```

      ![](media/apim9.png)

1. Search for **Azure Functions**, and select the **Azure function** that you have created previously.

   ![](media/api17.png)

1. Add a new step to send e-mail, search for **Office 365 Outlook**, and select **send an email (v2)**. 

   - **To**: Specify your Email address, i.e. **<inject key="AzureAdUserEmail"></inject>** to receive the e-mail.
   - **Subject**: **Color**
   - **Body**: type **msg**, **:** and click on add dynamic content, select **msg**, type **Color**, **:** and click on add dynamic content, search **body** and select **body** which present in **Azure function**.

        ![](media/api18.png)

        ![](media/api19.png)

1. Select **+ New step**, search and select **Response**, now **save** the logic App.

   ![](media/T3.2S8.png)

   - Use the following sample message to generate the schema of the Request body payload.  By specifying the schema, the individual fields (in this case `msg`) can be extracted and referred to in the subsequent logic

      ```json
      {
      "msg": "text"
      }
      ```

1. Lets add the function to API Management. In the API blade select **+ Add API (1)** and the **Logic App (2)** tile

   ![](media/addapi.png)

   - Select the **Browse** button to get a list of **Logic Apps** in the subscription

      ![](media/browse.png)

   - Select the **Logic App**, and choose **Select**.

      ![](media/logicapp.png)

   - On the **Create from Logic App**, select **Full**. Amend the Names / Descriptions, Add URL suffix as **logicapp**, select the Products(Starter, Unlimited), and select **Create**.

      ![](media/create.png)

    - As previously add CORS policy

   - Validate the Logic App works - either from the Azure management portal or the developer portal.

      ![](media/18.png)

      ![](media/19.png)

   - Check the Logic App audit

      ![](media/20.png)

   - Check the email was sent

      ![](media/21.png)

--- 
> **Congratulations** on completing the task! Now, it's time to validate it.
<validation step="c60e228d-7a4a-49bb-a8da-dfa8c1415230" />

## Summary
In this task, you have integrated Azure Functions and Logic Apps with Azure API Management, exposing them as APIs with management capabilities. you have configured, tested, and audited these serverless resources within API Management for seamless integration with other services.

### Now, click on Next from the lower right corner to move on to the next page for further tasks.

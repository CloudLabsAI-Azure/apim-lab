## Task 3: API Proxy to Serverless

Azure Serverless (Functions and Logic Apps) can be configured to benefit from the advantages of Azure API Management.

### Task 3.1: Azure Functions

1. Create a simple function that is Triggered by an **HTTP Request**.

2. Search for **Azure Function** App in the portal, and select **Create**.
   
   ![](media/Pg28-funcapp.png)

3. Enter the following details:
   
   - Resource group: **apim-rg**
   - Function name : **func-<inject key="Deployment ID" enableCopy="false" />**
   - Do you want to deploy code or container image? : Select **Code**
   - Runtime stack : Select **.Net**
   - Version : 6(LTS)
   - Region: Select the region you used for previous exercises.
   - Operating System : Windows
   - Hosting option and plans : **Consumption (Serverless)**
   - Then click on **Review + Create**.

      ![](media/a.png)

4. On the **Review + Create** tab, click on **Create**.

5. Once the Resource is created click on **Go to Resource**, and select Create in Azure portal.

   ![](media/b.png)

6. Select **HTTP Trigger** **(1)** and enter the New Function as **GetRandomColor** **(2)**, and click on the **Create** **(3)**.

   ![](media/c.png)

7. Navigate to **Code + Test**, Replace the code with the following, and click on **Save**.


     ```c#
     //string[] strColors = { "blue", "lightblue", "darkblue" };
     string[] strColors = { "green", "lightgreen", "darkgreen" };

     Random r = new Random();
     int rInt = r.Next(strColors.Length);

     return  (ActionResult)new OkObjectResult(strColors[rInt]);
     ```

   ![](media/c1.png)


8. Lets add the function to Azure API Management. Navigate back to the **API Management service**, in the API blade select [+ Add API] and the [Function App] tile

   ![](media/ex9-t-38-s-8.png)

   - Click on the **Browse** button to get a list of Functions in the subscription

      ![](media/ex9-t-38-s-8-1.png)

   - Select the Function App and then the Function

      ![](media/ex9-t-38-s-8-2.png)

      ![](media/ex9-t-38-s-8-3.png)

   - Select the **Full** tab from the tab and Amend the Names / Descriptions, URL suffix, and select the Products. Click on **Create**.

      ![](media/ex9-t-38-s-8-4.png)

   - As previously added CORS policy

   - Validate the function works - either from the Azure management portal or the developer portal

      ![](media/ex9-t-38-s-8-5.png)

      ![](media/11.png)

### Task 3.2: Azure Logic Apps

- Create a simple logic app that is Triggered by an HTTP Request

1. Search for **Logic Apps** in the portal, and click on **Add**.

   ![](media/Pg28-logicapp.png)
  
1. Enter the following details:

   - Select Resource Group: **apim-rg**
   - Logic App Name: **logicapp-<inject key="Deployment ID" enableCopy="false" />**
   - Region : Select the regions you have used for previous exercises. 
   - Plan type : **Consumption**
   - Click on **Review + create**.

      ![](media/ex9-t-32-s2.png)

1. On the **Review + Create** tab, click on **Create**.

1. Once the Resource is created click on **Go to Resource**, from the left menu under Development Tools select **Logic app designer**.

1. In the logic app designer selects **when a HTTP request is received**.

   ![](media/e.png)

   - In the Request body JSON Schema insert the following JSON.

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

      ![](media/f.png)

1. Add a new step, search for **Azure Functions**, and Select the **Azure function** that you have created previously.

   ![](media/g.png)

1. Add a new step to send e-mail, search for **Office 365 Outlook**, Click on **Sign in**and select **send an email (v2)**. 

   - Specify your Email address to receive the e-mail.
   - In the body type **msg** and click on add dynamic content, select **msg**, type **Color** and Search **body** in dynamic content and select **Azure function.**

      ![](media/h.png)

5. Add a new step for **Response**, and **save** the logic App.

   ![](media/13.png)

   - Use the following sample message to generate the schema of the Request body payload.  By specifying the schema, the individual fields (in this case `msg`) can be extracted and referred to in the subsequent logic

   ```json
   {
     "msg": "text"
   }
   ```

6. Lets add the function to API Management. In the API blade select **+ Add API** and the **Logic App** tile

   ![](media/14.png)

   - Select the **Browse** button to get a list of **Logic Apps** in the subscription

      ![](media/15.png)

   - Select the **Logic App**.

      ![](media/16.png)

   - Amend the Names / Descriptions, Add URL suffix as **logicapp**,  and select the Products(Starter, Unlimited).

      ![](media/17.png)

    - As previously add CORS policy

   - Validate the Logic App works - either from the Azure management portal or the developer portal.

      ![](media/18.png)

      ![](media/19.png)

   - Check the Logic App audit

      ![](media/20.png)

   - Check the email was sent

      ![](media/21.png)

--- 
### Summary
In this task, you have integrated Azure Functions and Logic Apps with Azure API Management, exposing them as APIs with management capabilities. you have configured, tested, and audited these serverless resources within API Management for seamless integration with other services.
- Now, click on Next from the lower right corner to move on to the next page.

## Task 3: API Proxy to Serverless

Azure Serverless (Functions and Logic Apps) can be configured to benefit from the advantages of Azure API Management.

### Task 3.1: Azure Functions

- Create a simple function that is Triggered by an HTTP Request

Example:

![](media/04.png)

```c#
    //string[] strColors = { "blue", "lightblue", "darkblue" };
    string[] strColors = { "green", "lightgreen", "darkgreen" };

    Random r = new Random();
    int rInt = r.Next(strColors.Length);

    return  (ActionResult)new OkObjectResult(strColors[rInt]);
```

Lets add the function to Azure API Management. In the API blade select [+Add API] and the [Function App] tile

![](media/05.png)

- Select the [Browse] button to get a list of Functions in the subscription

![](media/06.png)

- Select the Function App and then the Function

![](media/07.png)

![](media/08.png)

- Amend the Names / Descriptions, URL suffix and select the Products

![](media/09.png)

- As previously add CORS policy

- Validate the function works - either from the Azure management portal or the developer portal

![](media/10.png)

![](media/11.png)

### Task 3.2: Azure Logic Apps

- Create a simple logic app that is Triggered by an HTTP Request

Example:

![](media/12.png)

![](media/13.png)

Use the following sample message to generate the schema of the Request body payload.  By specifying the schema, the individual fields (in this case `msg`) can be extracted and referred to in the subsequent logic

```json
{
  "msg": "text"
}
```

Lets add the function to API Managament. In the API blade select [+Add API] and the [Logic App] tile

![](media/14.png)

- Select the [Browse] button to get a list of Logic Apps in the subscription

![](media/15.png)

- Select the Logic App

![](media/16.png)

- Amend the Names / Descriptions, URL suffix  and select the Products

![](media/17.png)

 As previously add CORS policy

- Validate the Logic App works - either from the Azure management portal or the developer poral

![](media/18.png)

![](media/19.png)

- Check the Logic App audit

![](media/20.png)

- Check the email was sent

![](media/21.png)



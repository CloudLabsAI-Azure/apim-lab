## Continuation for Exercise 4,Task 3: Transformation policies

### Task 3.1: Transformation - replace string

The **find-and-replace** policy finds a substring in a request or response and replaces it with a different string.

1. Open **APIs (1)** and click the **Colors API (2)**, then select the **Get random color (3)** operation.

      ![APIM Policy Find & Replace](media/15.png)
  
1. In the **Outbound processing (1)** section, select **Policy code editor** with symbol **</>**.

      ![APIM Policy Find & Replace](media/c.png)
  
1. Place the cursor after the `<base />` element in the `<outbound>` section.

      ![APIM Policy Find & Replace](media/mapi2.png)

1. Click on **Show snippets** present in the top right corner, then select the **Find and replace string in body** transformation policy.  

      ![APIM Policy Find & Replace](media/mapi39.png)

1. Fill in the **`from` and `to` (1)** values accordingly and **Save (2)** the policy.

     ```xml  
    <outbound>
       <base />
       <find-and-replace from="blue" to="green" />
       <cache-store duration="15" />
   </outbound>
     ```

      ![APIM Policy Find & Replace](media/bluegreen.png)

1. Invoke the API using the Unlimited subscription key.

      ![APIM Policy Find & Replace](media/green.png)

   > **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
   > - If you receive a success message, you can proceed to the next task.
   > - If not, carefully read the error message and retry the step, following the instructions in the lab guide. 
   > - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help you out.
   
      <validation step="03f0ec31-cabc-4f84-a209-5bcc3555da80" />

---

### Task 3.2: Transformation - conditional

Policies can be applied very granularly. In this example, you are modifying the **Star Wars** API to return a limited set of information if the caller is using the **Starter** subscription. Other products, such as the **Unlimited** subscription, will receive the full response.  

The [context variable](https://docs.microsoft.com/en-us/azure/api-management/api-management-policy-expressions#ContextVariables) that is implicitly available in every policy expression provides access to the `Response` and `Product` below. 

> **Note**: After saving any changes in the policy if you see this below pop-up, click on **Discard**.

  ![APIM Policy Transform Starter Product](media/note.png)

1. Click **Star Wars (1)** API, then select the **Get People By Id (2)** operation.

      ![APIM Policy Transform Starter Product](media/19.png)
  
1. Similarly to the **Colors** API, we will add the outbound policy to conditionally change the response body. Replace the existing entries in the operation with the entire `<policies>` code below and click **Save**. 

    >Note that the inbound `Accept-Encoding` header is set to `deflate` to ensure that the response body is not encoded as that causes the JSON parsing to fail.  

    ```xml
    <policies>
        <inbound>
            <base />
            <set-header name="Accept-Encoding" exists-action="override">
                <value>deflate</value>
            </set-header>
        </inbound>
        <backend>
            <base />
        </backend>
        <outbound>
            <base />
            <choose>
                <when condition="@(context.Response.StatusCode == 200 && context.Product?.Name != "Unlimited")">
                    <set-body>@{
                            var response = context.Response.Body.As<JObject>();

                            foreach (var key in new [] {"hair_color", "skin_color", "eye_color", "gender"}) {
                                response.Property(key).Remove();
                            }

                            return response.ToString();
                        }
                    </set-body>
                </when>
            </choose>
        </outbound>
        <on-error>
            <base />
        </on-error>
    </policies>
    ```

1. Test the API on the **Test** **(1)** tab with **id** 1 **(1)** and apply the appropriate **Starter** or **Unlimited** **(3)** product scope. Examine the different responses.

      ![APIM Policy Transform Unlimited Product](media/set-people-id.png)

1. With **Starter** or **None** product scope:

      ![APIM Policy Transform Unlimited Product](media/20.png)

1. With **Unlimited** product scope. Notice the four properties in red that are not included in the **Starter** scope response.

      ![APIM Policy Transform Unlimited Product](media/21.png)

---

### Task 3.3: Transformation - XML to JSON 

A frequent requirement is to transform content, especially to maintain compatibility with legacy APIs. For this lab we are going back to the **Basic Calculator** API that returned an XML response. 

1. On **Design tab (1)**, select **Add two integers operation (2)**, then in **Outbound processing (3)** section click on **Policy code editor `</>` (4)** to transform the response body to JSON.

      ![](media/d.png)

    ```xml
    <outbound>
        <base />
        <xml-to-json kind="direct" apply="always" consider-accept-header="false" />
    </outbound>
    ```

      ![APIM Policy Find & Replace](media/mapi1.png)
   
1. Click on **Save**.

1. Test the API and examine the response. Note that it's now JSON.

      ![APIM Policy Transform XML to JSON](media/22.png)

### Task 3.4: Transformation - Delete response headers 

A frequent requirement is to remove headers, especially ones that return security-related or superfluous information.

1. Add an outbound policy to the same **Basic Calculator** API operation to remove specific response headers and click on **Save**.

    ```xml
    <outbound>
        <base />
        <xml-to-json kind="direct" apply="always" consider-accept-header="false" />
        <set-header name="x-aspnet-version" exists-action="delete" />
        <set-header name="x-powered-by" exists-action="delete" />
    </outbound>
    ```
      ![APIM Policy Find & Replace](media/mapi4.png)

1. Test the same **Add two integers** operation and examine the response, which now no longer contains the two headers. See above screenshot for how it looked prior.

      ![APIM Policy Delete Response Header](media/23.png)

### Task 3.5: Transformation - Amend what's passed to the backend 

Query string parameters and headers can be easily modified prior to sending the request on to the backend. 

1. Back in the same **Calculator** API operation, select the **Add two integer operation** and add **inbound Processing** policies to modify the query string and headers and click on **Save**.

    ```xml
    <inbound>
        <base />
        <set-query-parameter name="x-product-name" exists-action="override">
            <value>@(context.Product?.Name ?? "none")</value>
        </set-query-parameter>
        <set-header name="x-request-context-data" exists-action="override">
            <value>@(context.Deployment.Region)</value>
        </set-header>
    </inbound>
    ```
      ![APIM Policy Find & Replace](media/mapi5.png)

1. Test the call by using either the **Starter** or **Unlimited** product, click on Trace button and then inspect the result on the **Trace** tab. If Tracing is not enabled, press **Enable Tracing**, and on the Pop-up select **Enable Tracing for one hour**.

      ![](media/trace.png)

1. In the **Trace tab**, select **Backend**.

      ![APIM Policy Amend Backend Call](media/24.png)

      ![APIM Policy Find & Replace](media/mapi6.png)

      ![APIM Policy Find & Replace](media/mapi7.png)


---
## Summary
In these transformation tasks, you implemented various policies in Azure API Management:

1. You applied find-and-replace policies to modify response strings in the Colors API.

1. Conditional policies were used in the Star Wars API to customize responses based on subscription tiers.

1. You transformed XML to JSON in the Calculator API and removed specific response headers.

1. Query string parameters and headers were dynamically modified using inbound policies in the Calculator API.

### Now, click on Next from the lower right corner to move on to the next page for further tasks.


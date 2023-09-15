## Task 2: Caching policy

Azure API Management can be configured for response caching which can significantly reduce API latency, bandwidth consumption, and web service load for data that does not change frequently.

Using the Azure Management portal, navigate to the **Colors** API and set a caching policy for the `Get random color` call:
  - Press **Add policy**.

    ![APIM Adding Enable Caching](media/10.png)
    ![APIM Adding Enable Caching](media/11.png)

  - Select **Cache responses**.

    ![APIM Enable Caching](media/12.png)

  - Set a caching duration of `15` seconds.
    > Simple caching configuration is not yet implemented in the Azure Management portal. We shall see later how it can be done using policy expressions.

    ![APIM Cache Duration](media/13.png)

- Configure the Colors website from Exercise 3(Task 4.2) to use the Unlimited subscription URL.
- Select **Start**.
- Notice that for each 15 second period the same color is set.

> **Note:** If you are unable to see colors, please refresh the page once. 

  ![Colors Website Caching](media/14.png)

- Looking at the **Get Random color** GET API policies in the **Code View**, you'll see the caching policy defined:

  ```xml
  <policies>
      <inbound>
          <base />
          <cache-lookup vary-by-developer="false" vary-by-developer-groups="false" allow-private-response-caching="false" must-revalidate="false" downstream-caching-type="none" />
      </inbound>
      <backend>
          <base />
      </backend>
      <outbound>
          <base />
          <cache-store duration="15" />
      </outbound>
      <on-error>
          <base />
      </on-error>
  </policies>
  ```

### Summary
In this task, you configured response caching for the "Get random color" call in the Colors API using Azure API Management.
- Now, click on Next from the lower right corner to move on to the next page.

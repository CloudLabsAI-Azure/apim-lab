## Continuation for Exercise 4,Task 7: Abort processing policy

### Aborting the processing

The ability to terminate a response gracefully is of importance in a number of cases such as error handling or business logic. Using the `return-response` policies short-circuits the request and yields a response that often does not originate from the backend. Consider what general situations may make sense without shifting too much business logic into APIM.

1. Open **Calculator** API and Select **Design** Tab
1. Open the **Add two integers** operation.  
1. Open the **Code View**.
1. Add the **inbound** policy to test for a condition (just `true` for our example) and return an error.

    ![](media/Pg-16.png)
  
    ```xml
    <inbound>
        <base />
        <choose>
            <when condition="@(true)">
                <return-response response-variable-name="existing response variable">
                    <set-status code="500" reason="Internal Server Error" />
                    <set-header name="failure" exists-action="override">
                        <value>failure</value>
                    </set-header>
                    <set-body>Internal Server Error</set-body>
                </return-response>
            </when>
        </choose>
        <set-query-parameter name="x-product-name" exists-action="override">
            <value>@(context.Product?.Name ?? "none")</value>
        </set-query-parameter>
        <set-header name="x-request-context-data" exists-action="override">
            <value>@(context.Deployment.Region)</value>
        </set-header>
        <set-header name="x-request-received-time" exists-action="override">
            <value>{{TimeNow}}</value>
        </set-header>
    </inbound>
    ```

1. Invoke the API. 
1. Observe the 500 error.

    ![APIM Policy Abort Response](media/39.png)

  ### Clean Up

  Now that you have seen how to gracefully terminate a request with a response, it is time to clean up the code to prevent a downstream impact in subsequent labs. **Please remove the `<choose>` logic above to let all requests flow again, then save the changes.**\

  ![](./media/remove.png)

### Now, click on Next from the lower right corner to move on to the next page.

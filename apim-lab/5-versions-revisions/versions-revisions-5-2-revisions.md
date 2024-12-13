## Continuation for Exercise 5,Task 2: Revisions

### Task 2.1: Add a new revision

1. Select the **Star Wars** API **v2**.

      ![](media/07.png)

1. Select the **Revisions** tab.

      ![APIM Revisions Menu](media/08.png)
  
1. Add a new revision with the description `Adding a caching policy.`
  
      ![APIM Revision Create](media/09.png)

    > The new revision is online but not yet current. The previous revision continues to remain the active default. Having added the new revision has not resulted in any change for your API consumers.

      ![APIM Created Revision](media/10.png)

### Task 2.2: Add caching

1. Switch to the **Design** tab, then select the `Get People` operation.
    > **Revision 2** automatically became the active revision you are now making changes in. You can also switch between revisions, but **be aware that changes to the *Current* revision are live immediately**.

      ![APIM Revision Add Caching](media/11.png)

1. Navigate to the **Inbound processing** tab.
   
1. Add a 10-second caching policy for the **GET People** operation via the Code editor.

    ```xml
    <inbound>
        <base />
        <cache-lookup vary-by-developer="false" vary-by-developer-groups="false" allow-private-response-caching="false" must-revalidate="false" downstream-caching-type="none" />
    </inbound>
    <backend>
        <base />
    </backend>
    <outbound>
        <base />
        <cache-store duration="10" />
    </outbound>
    ```

      ![APIM Created Revision](media/mapi50.png)

      ![APIM Created Revision](media/mapi51.png)

1. Once the code is updated, the new policy will be created.
   
      ![APIM Revision Add Caching](media/12.png)

### Task 2.3: Test the new revision

1. Navigate to the **Test** tab from the top.

1. From the Azure portal, select the `Get People` operation and click on **Trace**.
  
     > **Note**: The revision number at the top of the page as well as in the request URL. The request URL should look similar to: `https://<your-apim-name>.azure-api.net/sw/v2;rev=2/people/`.

      ![APIM Revision Caching Test](media/13.png)

1. Test the API twice. The test trace should then show that the cache lookup occurred. 

      ![APIM Revision Caching Test](media/14.png)

### Task 2.4: Make current revision

1. Select the **Revisions** tab.
1. Click on the ellipsis for `rev2` and select the **current revision** option.

      ![APIM Revision Make Current](media/15.png)

1. Check the **Post to the Public Change log for the API** and provide the description as `Adding a caching policy to improve API response time`. Click on **Save**.

      ![APIM Revision Make Current](media/16.png)

1. The new revision is now the current/live one. When you test now, note that the URL no longer contains a specific revision. The old revision is still online and can now be accessed with the `rev` qualifier. 

    > Unlike versioning, revisioning requires no URL updates for the API consumer.

      ![APIM Revision Make Current](media/17.png)


   > **Congratulations** on completing the task! Now, it's time to validate it. Here are the steps:
   > - If you receive a success message, you can proceed to the next task.
   > - If not, carefully read the error message and retry the step, following the instructions in the lab guide. 
   > - If you need any assistance, please contact us at cloudlabs-support@spektrasystems.com. We are available 24/7 to help you out.
   
      <validation step="2f717235-f41e-4c63-9172-1171f22f99d2" />
--- 

### Summary
In this Task, a new revision is added to the Star Wars API in Azure API Management. This revision remains inactive until made current. Then, caching policies are applied to the GET operation of this new revision. Testing the API shows cache-lookup behavior. Finally, the new revision is made the current one, eliminating the need for URL updates for API consumers, illustrating the advantages of revisioning over versioning in APIM.

### Now, click on Next from the lower right corner to move on to the next page.

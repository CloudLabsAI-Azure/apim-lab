## Exercise 1: Verify Pre-Built API Management Instance

## Estimated Duration: 20 minutes

APIs enable digital experiences, simplify application integration, underpin new digital products, and make data and services reusable and universally accessible. With the proliferation and increasing dependency on APIs, organizations need to manage them as first-class assets throughout their lifecycle.
Azure API Management helps customers meet these challenges:

- Abstract backend architecture diversity and complexity from API consumers
- Securely expose services hosted on and outside of Azure as APIs
- Protect, accelerate, and observe APIs
- Enable API discovery and consumption by internal and external users

## Lab objectives

You will be able to complete the following tasks:

**Task 1**: Verifying the Azure API Management instance

## Task 1: Verifying the Azure API Management instance

Azure API Management instance has already been pre-deployed as part of the deployment for this lab.

1) Navigate to the **resource groups** in the Azure Portal and select the **apim-rg** resource group.

   ![01](media/P2-T1-S1.1.png)

2) On the resource groups **apim-rg**, select API Management service resource type with name **apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />** . 
   
   ![02](media/02.png)
   
   Please verify that the Azure API Management instance functions correctly by following these steps:

1) Navigate to the Azure API Management instance in the Azure Portal.  
2) Select the **APIs (1)** blade, then select the ***Echo API (2)***.

     ![APIM Echo API Test Send](media/P2-T1-S2.1.png)

4) Press the **Test (1)** tab, then select the **GET Retrieve resource (2)** operation and note the **Request URL (3)** in a text editor for later use.  
5) Press **Send (4)** to issue a simple request.  

     ![APIM Echo API Test Send](media/03.png)

6) Scroll down and observe the `200` Success HTTP response.  

     ![APIM Echo API Test Success](media/04.png)

At this time you have successfully verified that Azure API Management is set up!

## Verification Failure (and Path to Success)

You may have noticed the *Request URL* and may be tempted to put it in your browser, issue a CURL statement, etc. If you do, you may see a `401` error and wonder what's happening.

   ![APIM Echo API Test 401](media/05.png)

1. The reason for this unauthorized access status code is that the *Echo API* requires a subscription key to be set. Whereas tests originating in Azure API Management account for this automatically, external callers cannot (and, naturally, should not).

1. Navigate back to APIM in the portal, switch to the **Settings (1)** tab, uncheck **Subscription required (2)**, and press **Save (3)** at the bottom of the page.

1. Subscriptions are important and useful, but in this case, we just want to verify the Azure API Management instance is working as intended.

   ![APIM Echo API Disable Required Subscription](media/06.png)

1. Now there should be no error when you access the link in your browser. In fact, in order to verify the 200, it's easiest to open your Developer Tools (F12), navigate to the **Network** tab, and look at **All** requests to see the 200.

   ![APIM Echo API Browser Success](media/07.png)

1. Alternatively, open the command prompt and you can issue a verbose (`-v`) CURL command against the **Echo API** and observe the `200` Success:

   - **curl -v https://apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />.azure-api.net/echo/resource?param1=sample**

      ![APIM Echo API Curl Success](../../assets/images/apim-echo-api-test-6.png)

## Summary

In this exercise, you verified the setup and functionality of the Azure API Management instance by testing the Echo API and handling any issues related to subscription keys. This ensures that your API management environment is correctly configured and ready for further use. You are now prepared to proceed to the next exercise to deepen your understanding and management of APIs.

## Now, click on the Next from lower right corner to move on next page

# Exercise 1: Create an API Management instance
## Overview
APIs enable digital experiences, simplify application integration, underpin new digital products, and make data and services reusable and universally accessible. With the proliferation and increasing dependency on APIs, organizations need to manage them as first-class assets throughout their lifecycle.
Azure API Management helps customers meet these challenges:

- Abstract backend architecture diversity and complexity from API consumers
- Securely expose services hosted on and outside of Azure as APIs
- Protect, accelerate, and observe APIs
- Enable API discovery and consumption by internal and external users

## Task 1: Verifying the Azure API Management instance
Azure API Management instance has already been pre-deployed as part of the deployment for this lab.

1) Navigate to the resource groups in the Azure Portal and select the **apim-rg** resource group.

   ![01](media/01.png)

3) Select **apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />**
   
   ![02](media/02.png)
   
Please verify that the Azure API Management instance functions correctly by following these steps:

1) Navigate to the Azure API Management instance in the Azure Portal.  
2) Select the **APIs** blade, then select the *Echo API*.

  ![APIM Echo API Test Send](media/02a.png)

4) Press the **Test** tab, then select the **GET Retrieve resource** operation.  
5) Press **Send** to issue a simple request.  

  ![APIM Echo API Test Send](media/03.png)

5) Observe the `200` Success response.  

  ![APIM Echo API Test Success](media/04.png)

At this time you have successfully verified that Azure API Management is set up!

### Verification Failure (and Path to Success)

You may have noticed the *Request URL* and may be tempted to put it in your browser, issue a CURL statement, etc. If you do, you may see a `401` error and wonder what's happening.

![APIM Echo API Test 401](media/05.png)

The reason for this the unauthorized access status code is that the *Echo API* requires a subscription key to be set. Whereas tests originating in Azure API Management account for this automatically, external callers cannot (and, naturally, should not).

Back in APIM, switch to the **Settings** tab and uncheck **Subscription required** and press **Save** at the bottom of the page.

> Subscriptions are important and useful, but in this case, we just want to quickly verify the Azure API Management instance is working as intended.

![APIM Echo API Disable Required Subscription](media/06.png)

Accessing the link in your browser should now show you no error message. In fact, in order to verify the 200, it's easiest to open your Developer Tools (F12), navigate to the **Network** tab, and look at **All** requests to see the 200.

![APIM Echo API Browser Success](media/07.png)

Alternatively, you can issue a verbose (`-v`) CURL command against the **Echo API** and observe the `200` Success:

**curl -v https://apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />.azure-api.net/echo/resource?param1=sample**

![APIM Echo API Curl Success](../../assets/images/apim-echo-api-test-6.png)

### Summary
In this exercise, you have verified the Azure API management instance. Now, click on Next from the lower right corner to move on to the next page.

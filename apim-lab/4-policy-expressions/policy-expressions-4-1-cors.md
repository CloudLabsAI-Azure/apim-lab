# Exercise 4: Configure and implement policy expression to contol API behaviour and enforce rules.

### Estimated Duration: 50 minutes

## Lab Overview

In this lab, you will explore and apply different API Management policies such as CORS, caching, transformations, named values, mock responses, and request control.

## Lab objectives

In this lab, you will perform:

- Task 1: Cross-origin resource sharing (CORS) policy
- Task 2: Caching policy
- Task 3: Transformation policies  
    - Task 3.1: Transformation - replace string
    - Task 3.2: Transformation - conditional
    - Task 3.3: Transformation - XML to JSON
    - Task 3.4: Transformation - Delete response headers
    - Task 3.5: Transformation - Amend what's passed to the backend 
- Task 4: Named Values
- Task 5: Mock policy
- Task 6: Send One Way policy
- Task 7: Abort processing policy

## Task 1: Cross-origin resource sharing (CORS) policy

The [cors policy](<https://docs.microsoft.com/en-us/azure/api-management/api-management-cross-domain-policies#CORS>) adds cross-origin resource sharing (CORS) support to an operation or an API to allow cross-domain calls from browser-based clients.

1. We have already configured the **CORS** policy for our APIs in labs 2 & 3. Below is the resulting XML:

    ![APIM Policy CORS All APIs](media/08.png)  

1. Click on **CORS** under the **Inbound processing** tab to view the XML present within the **CORS** policy.

    ![APIM Policy CORS All APIs](media/all-api1.png)
   
    ![APIM Policy CORS All APIs](media/all-api-policy.png)  

### You have successfully completed the exercise. Click on **Next >>** to proceed with the next exercise.


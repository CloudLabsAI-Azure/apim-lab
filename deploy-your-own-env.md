### Get started with deploying your Environment.

This document will help you deploy the **Azure Cosmos DB for Multitenant Applications Workshop** lab envrionment in your Azure environment.To Deploy this lab in your env, Please follow the below steps;


1. You will need following to get started:

   - **Microsoft License**: Make sure your account has any M365 license.
   - **Azure subscription**: Create a free account [here](https://azure.microsoft.com/free/).
   - **Azure Permission**: Make sure you have owner Access to the Subscription.
   - **GitHub Account**: You would need a GitHub account to complete the lab [Click here to signup free GitHub Account](https://github.com/signup).

## Prepare your Azure Lab Environment.

1. Click on the below Deploy to Azure Button.

   [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https://experienceazure.blob.core.windows.net/templates/azure-api-management/depoly-01.json)

   - Select the available subscription and resource group. Provide the unique alpha numeric value for `Deployment` parameter. You can review the ARM template by clicking on Edit Template. Review and create your lab envrionment.
     
2. Deploy one more Resource group with name **myColorsAppRg** to be used in the lab later.
   
Once All the resources got deployed, you can login to the JumpVM to perform the lab. 

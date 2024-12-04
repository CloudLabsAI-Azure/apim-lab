## Exercise 8:  Fusion Dev

## Estimated Duration : 30 minutes

In this exercise, you'll create a Star Wars Fan Club mobile application using Power Apps and Azure API Management. You'll connect your member data from an Excel worksheet, integrate Star Wars character information through a custom connector, and customize the app to display favorite character details for each member.

## Lab objectives

You will be able to complete the following tasks:

**Task 1**: Power Apps and APIM

Task 1.1: Update CORS policy

Task 1.2: Create a custom connector

**Task 2**: View your custom connector in Power Platform

**Task 3**: Generate the Star Wars Fan Club Application

Task 3.1: Connect to the backing data source

**Task 4**: Add Favorite Character information

Task 4.1: Add the Star Wars API Data Source

Task 4.2: Customize the generated app

Task 4.3: Add controls to the View Detail screen

Task 4.4: Connect the Detail Screen to the Star Wars API

Task 4.5: Show the Star Wars character information on the Detail Screen


## Task 1: Power Apps and APIM

The *premier* Star Wars Fan club is growing and the club officers would like to upgrade from their existing member tracking worksheet to a mobile application that would be available to their members all over the world. The members would also like to see information about their favorite Star Wars movies and characters in the application that would update as new shows and movies are released.

In this exercise, you will be using [Star Wars API](https://swapi.dev/) with the Azure API Management instance that you created [in part three](../3-adding-apis/adding-apis-3-1-from-scratch.md) of this lab. The Excel worksheet of member profiles will serve as the primary backing data source and will be used to generate a base application. You will export the Star Wars API from Azure API Management as a Power Platform Custom Connector so that the Canvas App can access real-time Star Wars character information. For each of the Fan Club members, you can then search the Star Wars API character data and show information about their favorite character in the Canvas App.

> *Note: This exercise requires access to Power Apps Premium connectors. Sign up for a [free Developer Plan](https://powerapps.microsoft.com/en-us/developerplan/).* Use the credentials given in the lab environment to sign up for a Developer Plan.

### Task 1.1: Update CORS policy

1. In your Azure API Management resource, navigate to the **Portal Overview** under **Developer Portal** from the left pane to verify if CORS has been enabled globally. Here's what the Portal overview will look like if CORS has been enabled:

   ![](media/1.png)
 
1. Now go to **All APIs (1)**, and click on **edit icon (2)** from the Inbound Processing tab.

   ![](media/aaa1.png)

1. Click on **+ Add Allowed origin** and add https://flow.microsoft.com and https://make.powerapps.com as allowed origins, and click on **Save**.

   ![](media/aaa2.png)


### Task 1.2: Create a custom connector

>*Note*: Before proceeding further make sure you are signed in the Power platform with the given credentials in the resources tab.

1. From the left-menu, click on **Power platform** option from your Azure API Management instance, and select **Create a connector.**

   >**Note**: If the **Create a connector** is not visible, then follow these steps:
      - Click on Activate account and fill the required informations.
      - Use the email that is provided in the Environment section of the lab. and click on **Next**.
      - Enter any random 10-digit number in Phone number
      - Then Click on **Get Started**.
      - Go to the API management service page and click on **Create a connector**.
         >**Note**: If **You need a Power Apps license to use this app** error is showing up, try with the following link :- [https://make.powerapps.com](https://make.powerapps.com/)
         ![](media/demo.png)
         >**Note**: It might take some time to appear. Refresh the page and check again.
         ![](media/aa1.png)

2. Enter the following details:

   - API : Select the **Star Wars (1)** API 
   - Power Platform Environment: From the dropdown select **ODL_User <inject key="DeploymentID" enableCopy="false"/>'s Environment (2)**.
   - API display name: **Star Wars API (3)**
   - Click on **Create (4)**.

     ![](media/Pg25-1.png)

If you are unable to create a Power Connector from Azure API Management, you can also export an `OpenAPI v2 (JSON)` file that can be imported as a Custom Connector within the Power Platform. You can find a sample [here](https://github.com/Azure/apim-lab/blob/main/apim-lab/9-fusion-dev/Star%20Wars%20API.swagger.json).

### Task 2: View your custom connector in Power Platform

1. Go to [https://make.powerapps.com](https://make.powerapps.com/) and sign in.

1. Select **More (1)** from the left pane, and click on **Discover all (2)** to see your generated custom connector to your Azure API Management API.
   
   ![](media/more.png)

1. Scroll down and select **Custom Connectors**.

   ![](media/aaa3.png)

1. You can view the recently created **Star Wars API** custom connecter. From here, select the pencil icon to edit the custom connector.

   ![](media/3.png)
 
1. On the top left corner, select **1. General** from the drop-down select **Definition** screen, we need to define a search query string for people so that the Power App can search for character records by name.

   ![](media/def.png)

1. In the **Request** section, select **+ Import from sample (1)**. Enter a sample request **URL (2)** with the search query string, and select **Import (3)**:

   - **https://apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />.azure-api.net/sw/people?search=Luke**
       
      ![](media/aa3.png)

      ![](media/4.png)

1. In the **Response** section of the `getpeople` action, select the `200` response and then select **+ Import from sample**. Copy and paste a sample JSON response into the `Body` section of the response. Close the import panel and select **Update connector**. 

   - Navigate back to the **API Management service** in Azure Portal.
   
   - On the **API Management service** page, from the left menu, under **APIs**, select **APIs**. Select **Star Wars** drop-down and select **v2 (1)**. Select `Get People (2)`, and from the top menu select **Test (3)**, now select **Send (4)** and **copy (5)** the Response into a notepad. 

      ![](media/api.png)
  
   - Paste the response into the `Body` section of the response, and select **Import**.

      ![](media/aa5.png)

      ![](media/5.png)

1. Repeat the step-7 to import for the `getpeoplebyid` action.

   >**Note:** Delete if you have other **Actions** Apart from `getpeople` and `getpeoplebyid`.

1. In the **Policies** section select **+ New policy**.

1. Fill out the new policy with the following information:

     - **Name: set-origin-header (1)**
  
     - **Template: Set HTTP header (2)**
  
     - **Header name: Origin (3)**
  
     - **Header value: https://make.powerapps.com (4)**
  
     - **Action if the header exists: override (5)**
  
     - **Run policy on: request (6)**

       ![](media/setorigin.png)
      
       ![](media/action.png)

       ![](media/origin001.png)

1. Select **Update connector**.

1. Select **3. Definations**, from the top left corner, select **Test** screen, and create a new connection instance in the **Connections** section by clicking on the **+ New connection**. If prompted to provide the subscription key, navigate to Azure Portal and you can find the subscription key in the API Management Service, from the left menu under APIs click on **Subscriptions (1)**, choose **Unlimited**, click on **... > Show/hide keys (2)**. Copy the **Primary key (3)**.  

   ![](media/Pg25-subscriptionid.png)

1. Navigate back to the Power apps page, and paste the subscription key, select **Create**.

   ![](./media/addcon01.png)

1. Navigate back to the **Custom Connectors** page. Return to the **Test** page and test each of the API actions, in **getpeople** in the search section type **Luke** and select **Test operations**.

   ![](media/8.png)

   ![](./media/res01.png)

## **Task 3: Generate the Star Wars Fan Club Application**

### Task 3.1: Connect to the backing data source

1. Login to [Onedrive](https://onedrive.live.com/login/).

   > **Note:** Use the following credentials for Onedrive for business.
    
    * Email/Username: <inject key="AzureAdUserEmail"></inject>

    * Password: <inject key="AzureAdUserPassword"></inject>

1. On **Securely store and share files** page, select **Your OneDrive is ready**.

1. Select **+ Add new (1)**, click on **Files Upload (2)**, in the Jump VM, navigate to **C:\LabFiles\fanclubmembers.xlsx** path, and upload **fanclubmembers.xlsx**  to your OneDrive for Business account.

   ![](media/Pg25-onedrive.png)
 
3. Navigate back to Power Apps Editor, in the left pane, select **Home**.

4. Select **Create (1)** , select **Excel (2)** and then Create **+ New connection** with **OneDrive for Business**.

   ![](media/excel.png)
   
5. Under **Connections** , select **OneDrive for Business**, select **Create**, and select **<inject key="AzureAdUserEmail"></inject>**. On **Confirmation required** page, select **Allow access**. 

6. Under **Choose an Excel file** , select the **fanClubMembers.xlsx** file.

7. Under **Choose a table** , select the **MemberList** table.

8. Select **Connect** on the bottom right.

9. Power Apps will generate the app by inspecting your data and matching it with Power Apps screens.

   >**Note:** On **Welcome to Power Apps Studio** page, select **Skip**.

## **Task 4: Add Favorite Character information**

Your generated app will now be in edit mode in the Power Apps Studio.

### Task 4.1: Add the Star Wars API Data Source

1. Select **Data (1)** from the left pane and then select **+ Add data (2)** from the drop-down menu.

2. Search for **Star Wars (3)** in the search field and choose the connection to the **Star Wars API (4)**.

     ![](media/9.1.png)

### Task 4.2: Customize the generated app

Your generated app will now be in edit mode in the Power Apps Studio.

You can customize your app theme using the **Theme** drop-down menu and selecting an option. You can change or format the fields that are shown in the Gallery by selecting **Tree view** in the left pane, clicking on BrowseGallery1, and making edits in the right formatting pane.

![](media/10.png)

### Task 4.3: Add controls to the View Detail screen

1. In the Tree view, select **DetailScreen1**.

1. Select the **+** icon on the left side of the screen to bring up the **Insert** panel.

1. Select **Text Label** and add labels for the **Favorite Character:** section header and for each one of the character description fields.

1. For each label control, change the **Text** property in the right-side **Properties** panel to describe each field.

1. Drag the controls on the screen so they are below the header and are aligned with the center of the screen.

   ![](media/11.png)

### Task 4.4: Connect the Detail Screen to the Star Wars API

1. In the left pane, select the **Tree view** and then the **BrowseGallery1** on **Browsescreen1**.

2. Using the drop-down menu, select the **OnSelect** action that will be executed when a user selects a Fan Club member from the gallery.

3. In the **OnSelect** function, we will navigate to **DetailScreen1** and call the Star Wars API to get the character details for the member&#39;s favorite character.

    ```
    Navigate(DetailScreen1, ScreenTransition.None);

    ClearCollect(characterCollection, StarWars.getpeople({search: ThisItem.MemberFavoriteCharacter}).results);
    ```
    
    ![](media/onselect.png)

### Task 4.5: Show the Star Wars character information on the Detail Screen

1. For each of the description labels on **DetailScreen1** , change the **Text** property in the right-side **Properties** panel to include the data from the API. For example, for the **Name:** label: `&quot;Name:&quot; &amp; &quot; &quot; &amp; First(characterCollection).name`

    - Select `Name` Label and Enter `"Name: " & First(characterCollection).name`

       ![](media/fx.png)

    - Likewise, you can enter the following for each label:
    - Mass: `"Mass: " & Text(First(characterCollection).mass, "[$-en-US]0") & " kg"`
    - Height: `"Height: " & Text(First(characterCollection).height, "[$-en-US]0") & " cm"`
    - Birth year: `"Birth Year: " & First(characterCollection).birth_year`
    - Gender: `"Gender: " & First(characterCollection).gender`
   
2. Select **Play** in the upper-right corner to practice using the app.
 
   ![](media/powerapps-output1.png)

   ![](media/powerapps-output2.png)


> **Congratulations** on completing the task! Now, it's time to validate it.
<validation step="42b46870-763d-4674-95dd-eec0430e096d" />


--- 

### Summary
In this exercise, you have integrated the Star Wars API with Azure API Management, exported it as a Power Platform Custom Connector, and created a Canvas App to allow Fan Club members to search and view information about their favorite Star Wars characters.

### Now, click on Next from the lower right corner to move on to the next page.

# Exercise 8:  Fusion Dev
## Overview

In this exercise, you'll create a Star Wars Fan Club mobile application using Power Apps and Azure API Management. You'll connect your member data from an Excel worksheet, integrate Star Wars character information through a custom connector, and customize the app to display favorite character details for each member.

## Task 1: Power Apps and APIM

The *premier* Star Wars Fan club is growing and the club officers would like to upgrade from their existing member tracking worksheet to a mobile application that would be available to their members all over the world. The members would also like to see information about their favorite Star Wars movies and characters in the application that would update as new shows and movies are released.

In this exercise, you will be using [Star Wars API](https://swapi.dev/) with Azure API Management instance that you created [in part three](../3-adding-apis/adding-apis-3-1-from-scratch.md) of this lab. The Excel worksheet of member profiles will serve as the primary backing data source and will be used to generate a base application. You will export the Star Wars API from Azure API Management as a Power Platform Custom Connector so that the Canvas App can access real-time Star Wars character information. For each of the Fan Club members, you can then search the Star Wars API character data and show information about their favorite character in the Canvas App.

> *Note: This exercise requires access to Power Apps Premium connectors. Sign up for a [free Developer Plan](https://powerapps.microsoft.com/en-us/developerplan/).* Use the credentials given in the lab environment to sign up for a Developer plan.

### Task 1.1: Update CORS policy

Check Azure API Management -> Developer Portal -> Portal overview to see if CORS has been enabled globally. If it has been enabled, go to All APIs and add https://flow.microsoft.com and https://make.powerapps.com as allowed origins. Here's what the Portal overview will look like if CORS has been enabled:

 ![](media/1.png)
 
Add Allowed origins.

 ![](media/aaa1.png)

 ![](media/aaa2.png)


### Task 1.2: Create a custom connector

Click on **Power platform** option from your Azure API Management instance, and select **Create a connector.**

 ![](media/aa1.png)

Select the Star wars API  and click on create.

- Display Name : **Star Wars API**

 ![](media/aa2.png)

If you are unable to create a Power Connector from Azure API Management, you can also export an `OpenAPI v2 (JSON)` file that can be imported as a Custom Connector within Power Platform. You can find a sample [here](https://github.com/Azure/apim-lab/blob/main/apim-lab/9-fusion-dev/Star%20Wars%20API.swagger.json).

### Task 2: View your custom connector in Power Platform

1. Go to [https://make.powerapps.com](https://make.powerapps.com/) and sign in.
2. Select **Data** from the left pane, and then select **More**  and click on discover **Discover all** to see your generated custom connector to your Azure API Management API.
   
   ![](media/aaa4.png)

   ![](media/aaa3.png)

   ![](media/3.png)

4. From here, select the pencil icon to edit the custom connector.
5. On the **Definition** screen, we need to define a search query string for people so that the Power App can search for character records by name.

   ![](media/def.png)

6. Select the `GetPeople` action, and in the **Request** section, select **+ Import from sample**. Enter a sample request URL with the search query string:

   - **https://apim-dev-hol-ms-<inject key="Deployment ID" enableCopy="false" />.azure-api.net/sw/people?search=Luke**
       
   ![](media/aa3.png)

   ![](media/4.png)

7. In the **Response** section of the `getpeople` action, select the `200` response and then select **+ Import from sample**. Copy and paste a sample JSON response into the `Body` section of the response. Close the import panel and select **Update connector**. 

- Navigate back to the Azure API Management instance and Invoke `getpeople`, copy the Response, and paste it `Body` section of the response.

  ![](media/aa4.png)

  ![](media/aa5.png)

  ![](media/5.png)

8. Repeat this import for the `getpeoplebyid` action.

>**Note:** Delete if you have other **Actions** Apart from `getpeople` and `getpeoplebyid`.

9. In the **Policies** section select + New policy.
10. Fill out the new policy with the following information:

     **Name: set-origin-header**
  
     **Template: Set HTTP header**
  
     **Header name: Origin**
  
     **Header value: https://make.powerapps.com**
  
     **Action if the header exists: override**
  
     **Run policy on: request**

![](media/7.png)

11. Next, **Update connector**.

12. On the **Test** screen, create a new connection instance in the **Connections** section. If prompted to provide the subscription key, you can find the subscription key in the developer portal, click on profile, and copy the Primary key of the **unlimited** subscription.  You will then be redirected to the **Connections** area in Power Platform where your connection was created. Navigate back to the **Custom Connectors** page and edit the Star Wars API again. Return to the **Test** page and test each of the API actions.

![](media/8.png)

## **Task 3: Generate the Star Wars Fan Club Application**

### Task 3.1: Connect to the backing data source

1. In the Jump VM, Navigate to **C:\LabFiles\fanclubmembers.xlsx** and upload **fanclubmembers.xlsx** to your OneDrive for Business account.

> **Note:** Use the following credentials for Onedrive for business.
   * Email/Username: <inject key="AzureAdUserEmail"></inject>

   * Password: <inject key="AzureAdUserPassword"></inject>

2. Back in the Power Apps Editor, in the left pane, select **Home**.
4. Under **Create** , select **Excel** and then Create **New connection** with **OneDrive for Business**.

![](media/excel.png)
   
5. Under **Connections** , select **OneDrive for Business** and browse to the file location. 
7. Under **Choose an Excel file** , select the **FanClubMembers.xlsx** file.
8. Under **Choose a table** , select the **Members** table.
9. Select **Connect** on the bottom right.
10. Power Apps will generate the app by inspecting your data and matching it with Power Apps screens.

## **Task 4: Add Favorite Character information**

Your generated app will now be in edit mode in the Power Apps Studio.

### Task 4.1: Add the Star Wars API Data Source

1. Select **Data** from the left pane and then select **+ Add data** from the drop-down menu.
2. Search for Star Wars in the search field and choose the connection to the Star Wars API.

![](media/9.png)

### Task 4.2: Customize the generated app

Your generated app will now be in edit mode in the Power Apps Studio.

You can customize your app theme using the **Theme** drop-down menu and selecting an option. You can change or format the fields that are shown in the Gallery by selecting **Tree view** in the left pane, clicking on the BrowseGallery1, and making edits in the right formatting pane.

![](media/10.png)

### Task 4.3: Add controls to the View Detail screen

1. In the Tree view, select **DetailScreen1**.
1. Select the **+** icon on the left side of the screen to bring up the **Insert** panel.
2. Select **Text Label** and add labels for the Favorite Character section header and for each one of the character description fields.
3. For each label control, change the **Text** property in the right-side **Properties** panel to describe each field.
4. Drag the controls on the screen so they are below the header and are aligned with the center of the screen.

![](media/11.png)

### Task 4.4: Connect the Detail Screen to the Star Wars API

1. In the left pane, select the **Tree view** and then the **BrowseGallery1** on **Browsescreen1**.
2. Using the drop-down menu, select the **OnSelect** action that will be executed when a user selects a Fan Club member from the gallery.
3. In the **OnSelect** function, we will navigate to **DetailScreen1** and call the Star Wars API to get the character details for the member&#39;s favorite character.

```
Navigate(DetailScreen1, ScreenTransition.None);

ClearCollect(characterCollection, StarWarsAPI.getpeople({search: ThisItem.MemberFavoriteCharacter}).results);
```


![](media/onselect.png)

### Task 4.5: Show the Star Wars character information on the Detail Screen

1. For each of the description labels on **DetailScreen1** , change the **Text** property in the right-side **Properties** panel to include the data from the API. For example, for the **Name:** label: 
 
 `&quot;Name:&quot; &amp; &quot; &quot; &amp; First(characterCollection).name`

 - Select `Name` Label and Enter `"Name: " & First(characterCollection).name`

   ![](media/fx.png)

 - Likewise, you can enter the following for each label:
 - Mass: `"Mass: " & Text(First(characterCollection).mass, "[$-en-US]0") & " kg"`
 - Height: `"Height: " & Text(First(characterCollection).height, "[$-en-US]0") & " cm"`
 - Birth year: `"Birth Year: " & First(characterCollection).birth_year`
 - Gender: `"Gender: " & First(characterCollection).gender`
   
2. Select **Play** in the upper-right corner to practice using the app.
 
![](media/13.png)

![](media/14.png)

--- 

### Summary
In this exercise, you have integrated the Star Wars API with Azure API Management, exported it as a Power Platform Custom Connector, and created a Canvas App to allow Fan Club members to search and view information about their favorite Star Wars characters.

- Now, click on Next from the lower right corner to move on to the next page.

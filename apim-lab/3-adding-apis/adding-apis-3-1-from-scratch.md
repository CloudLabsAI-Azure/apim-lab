## Exercise 3: Adding APIs

- On the left menu, open the *APIs* blade. You will see all APIs, the possibility to add new ones, but also to customize existing ones.

  ![APIM APIs](media/01.png)

### Task 1: Add API from Scratch

Instead of developing an API, for this lab you will use the existing [*Star Wars* API](https://swapi.dev):

1) Click on **Add API**.  
2) Click on **HTTP - Manually define an HTTP API**.  
3) Select the **Full** option in the **Create an HTTP API** dialog.  
4) Enter **Display name** `Star Wars`, **Name** `star-wars`, and, optionally, **Description**.  
5) Assign `https://swapi.dev/api` to the **Web service URL**.  
6) Keep the **URL scheme** at `HTTPS` as we strive to enforce HTTPS only.  
7) Set the **API URL suffix** to `sw`. This allows us to compartmentalize the Azure API Management URLs for distinct APIs.  
8) Assign **Starter** and **Unlimited** products.  
9) Press **Create**.  

  > While it is conventionally a good idea to version APIs from the onset, we are omitting this step here for brevity of the labs.

  ![APIM Add Blank API](media/02.png)

- Once created, inside the *Star Wars* API press **+ Add operation** to declare two new operations:

  1) **Get People**  
    - Display name: **Get People**  
    - Name will be populate with: **get-people**  
    - URL: **GET /people/**  
  ![01](media/03.png)

  2) **Get People By Id**  
    - Display name: **Get People By Id**  
    - Name will be populate with: **get-people-by-id**  
    - URL: **GET /people/{id}/**
 
  

  ![APIM Star Wars API Add Operation](media/04.png)

### Task 2: Access Star Wars API from Developer Portal

- Switch now to the Developer Portal and sign in as a developer with a subscription. 
- Select **Explore APIs**. You should see both **Echo API** and **Star Wars**.

  ![APIM Developer Portal Echo & Star Wars APIs](media/05.png)

- Click on **Star Wars**. Try the **Get People** operation. Observe a successful `200` response.

  ![APIM Developer Portal Star Wars Try It](media/06.png)

- Now try the **Get People By Id** operation with `id = 2`

  ![APIM Developer Portal Star Wars Try It](media/07.png)

- Examine the successful `200` response with `C-3PO`'s details in the response body payload.
  
  ![APIM Developer Portal Star Wars Try It](media/08.png)
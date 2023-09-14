## Task 5: Product Management

A product contains one or more APIs as well as a usage quota and the terms of use. Once a product is published, developers can subscribe to the product and begin to use the product's APIs.

### Task 5.1: Product definition

- In the Azure Portal, open the resource menu item `Products`.

  ![APIM Products](media3/01.png)

- Let's add a new product tier called `Gold Tier`. 

  ![APIM Add Product](media3/02.png)

  ![APIM Add Product](media3/03.png)

- Next, we'll change the access control by clicking on **Gold Tier** and selecting **Access control** in the left pane.

  ![APIM Add Product Access](media3/04.png)

  Press **Add group**, check **Developers** and **Guests**, then press **Select**. The two added roles are shown now.

  ![APIM Add Product Access](media3/05.png)

  Back in the private browsing session, browse to **Products** and observe the new **Gold Tier**. 

  ![APIM Developer Portal Added Product](media3/06.png)

 ### Summary
  In this task, you created a new product tier called "Gold Tier" in Azure API Management. You also modified the access control settings for this product by adding the "Developers" and "Guests" groups, allowing them access to this product. This allows developers to subscribe to the "Gold Tier" product and access its associated APIs, establishing control and access policies for different user groups.
- Now, click on Next from the lower right corner to move on to the next page.

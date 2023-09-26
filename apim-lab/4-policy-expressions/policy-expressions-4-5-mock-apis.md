## Task 5: Mock policy

### Mock responses

Mocking in Azure API Management is a useful mechanism for API consumers to interact with APIs without waiting for the backend to be ready. 

- Open the **Star Wars** API and select **+ Add Operation**

![](media/30.png)

- Create a new GET operation:
  - Display name: **Get Film**
  - Name: **get-film**
  - URL: **/film**
- In the *Responses* configuration tab, press **+ Add response**, return `200 OK` with a representation with content type `application/json` and this sample data:

  ```json
  {
    "count": 1,
    "films": [{ "title": "A New Hope", "release-date": "05/25/1977" }]
  }
  ```
  
  ![APIM Policy Mock Frontend](media/31.png)

- Press **Save**.
- Open the Inbound processing **Code View**
- Add **Mock Response** under **Other policies** after the `<base />` tag.

  ```xml    
  <inbound>
      <base />
      <mock-response status-code="200" content-type="application/json" />
  </inbound>
  ```

  ![APIM Policy Mock Inbound](media/32.png)

- Invoke the API to receive a `200` success with the mocked film data.

  ![APIM Policy Mock Response](media/33.png)
---

### Summary 
In Azure API Management, a "Get Film" operation is created for the Star Wars API. This operation returns a mock response with a 200 OK status code and sample JSON data containing film information. An inbound policy is added to simulate the mock response, and when the API is invoked, it returns a 200 success status with the mocked film data.
- Now, click on Next from the lower right corner to move on to the next page.

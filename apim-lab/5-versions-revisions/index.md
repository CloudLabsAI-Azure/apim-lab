## Exercise 5:  Version and Revisions

## Estimated Duration: 50 minutes

## Overview

In this exercise, you will learn how to manage versions and revisions of your APIs in Azure API Management (APIM).

Versions and revisions provide you with elegant means to safely manage the lifecycle of your APIs. 

Versions of APIs are differentiated by a version identifier (e.g. `v1`, `v2`, etc.) through a versioning scheme such as a version path in the URL, a header, or a query string. Multiple versions can and may often be active at the same time to provide continued service while breaking changes may be introduced in newer versions.

Revisions allow you to safely make _non-breaking_ changes to your API. Developers who consume the API can be given details about the changes. Revisions can safely be tested before being activated for your consumers. Revisions also allow you to rollback changes. 

For more information, visit the [Versions & Revisions](https://azure.microsoft.com/en-us/blog/versions-revisions) documentation.

## Objectives

In this Exercise, you will perform:

- Task 1: Create a new version of an API
   - Task 1.1: Add a new version
   - Task 1.2: Test the new version
- Task 2: Create a new revision of an API
    - Task 2.1: Add a new revision
    - Task 2.2: Add caching
    - Task 2.3: Test the new revision
    - Task 2.4: Make current revision

### Now, click on Next from the lower right corner to move on to the next page for further tasks of Exercise 5.

  ![](../gs/media/api-07.png)

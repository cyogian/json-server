# Full Throttle Lab Assessment API

A Mock API made with [JSON Server by Typicode](https://github.com/typicode/json-server) for Full Throttle Lab Assessment Project.  
A JSON based Backend for Member Activity Viewer Application

Data Generated from [Mockaroo Realistic Data Generator](https://mockaroo.com/)
## Data Template Screenshot  

![](https://github.com/cyogian/json-server/raw/main/MockarooMockTemplateScreenshot.PNG)

## How did I create a suitable database?

#### The database file db.json was prepared in multiple steps:

- Generated Fake Data using Mockaroo, the template is displayed above.

- As the end_time should be greater then the `start_time` & mockaroo had no such method to generate `relative datetime`, I made custom python script to generate `random end_time`(greater than `start_time` but closer to 1-4 hours) for each member's each `activity_periods` entry. Thus converting `db_unstructured.json` to `db_structured.json` file using `generate_end_time.py`.

- Later realized that this structure itself is not suitable as per `JSON Specifications` to have multiple endpoints for fetching data. So in order to make it suitable for `json-server`, I created another python script to restructure the JSON File by separating the `activity_period` as a separate entity in another collection called `db.activity_periods` having entries with relationship to `db.members` collection using a foreign key called `memberId`. Thus converting `db_structured.json` to `db.json` using `restructuring_json.py` that will be used by `json-server` to autocreate a JSON API Server.

- Deployed the server on repl at [this link](https://json-server.cyogian.repl.co).

- The Frontent Site that uses this mock API is deployed on netlify at [this link](https://ftl.cyogian.dev) and a private github repository.

- **Started Mocking...**

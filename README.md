# Generic Flask Api and D3 Template
A couple simple examples of Flask to use as project starters on their own or stitched together.  The main idea was to create a few working examples of common app starters with enough starter code to get going while also keeping everything as simple as possible.

## Examples
+ [app.py](app.py) - shows basic a basic api with HTML templates, example of calling the api,and an exmple that can get and post data from the browser to Flask
    - D3.js V5
    - Bootstrap v5
    - style overrides in [static/css/style.css](static/css/style.css)
    - example api usage in [static/js/app.js](static/js/app.js)
    - example post usage in [static/js/post.js](static/js/post.js) and [templates/home.html](templates/home.html)
+ [app_basic.py](app%5Fbasic.py) - no db, just a basic api
+ [app_basic_postgres_api.py](app_basic_postgres_api.py) - shows basic connection to Postgres and returns query as json
+ [app_postgres_api_js_d3_html.py](app_postgres_api_js_d3_html.py)- Adds to previous with HTML templates, example of calling the api in app.js
    - D3.js V5
    - Bootstrap v5
    - style overrides in [static/css/style.css](static/css/style.css)
    - example api usage in [static/js/app.js](static/js/app.js)
+ [app_basic_mongo_api.py](app_basic_mongo_api.py) - basic mongo api
+ [app_mongo_d3.py](app_mongo_api_js_d3_html.py)  - Adds to previous with HTML templates, example of calling the api in app.js
    - D3.js V5
    - Bootstrap v5
    - style overrides in [static/css/style.css](static/css/style.css)
    - example api usage in [static/js/app.js](static/js/app.js)
## Templates
+ [Home page](templates/home.html)
+ [Default Page](templates/index.html)
+ [Post Example](templates/post.html)
    - only works when running [The basic post example](app.py)

+ Python requirements are located in [requirements.txt](requirements.txt)


##### Open License - I don't care what you do with this. if someone actually uses it or finds it helpful, let me know (or not)

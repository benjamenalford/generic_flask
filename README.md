# Generic Flask Api and D3 Template
A couple simple examples of Flask to use as project starters on their own or stitched together.

The main idea was to create a few working examples of common app starters with enough starter code to get going while also keeping everything as simple as possible. Let's not be clever,let's be clear. When an idea strikes here's just enough to connect the dots between UI and server.

### Libraries Used
Another design consideration with this project was to include as little dependcies as possiple while still providing enough to create begin creating a POC or utility with enough to make something that looks and functions well.

Little enough is included so that adding anything else one might need won't be an issue. Everything here is easily replaced and meant to be.

There's no configuration to mess with other than your own URLS ( which have been defaulted to OOTB and local instances of any servers) , any config is done where it's needed, when it's needed. Let's not spend 1 hour configuring a larger framework or get stuck on some benign minute of new lib X; let's get to work.

Libraries were chosen for their OOTB usuability, quality of official documentation, user community, extendability, adability, and general usage in the 'industry', coprorate world, and real world. With just the included examples, official site examples and documentation, code complete , your can just start writing code.

- JS - Older versions are used and this is intentional, life is not always cutting edge. Upgrade away and you shouldn't have any issues.
    - D3.js v5 - Swiss army knife of data manipulation and visualizations
    - Bootstrap v5 - the js is here to support the css, but you can get fancy with it if you need to.
- Python
    - Flask - It is what it is, a decent little web server in python
    - numpy - because
    - sqlalchemy - adapts to most databases, go commando or ORM depending on the mood.
    - pymongo - gets the job done
- UI
    - Bootstrap - It's default looks better than browser default,
- Databases
    - Postgres - It's used everywhere
    - MongoDb - the 'it could be anything' of no-sql databases, free cloud hosting as well.

### Examples
+ [app_basic.py](app%5Fbasic.py) - no db, just a basic api
+ [app.py](app.py) - shows basic a basic api with HTML templates, example of calling the api,and an exmple that can get and post data from the browser to Flask
    - example post usage in [static/js/post.js](static/js/post.js) and [templates/post.html](templates/post.html)
+ [app_basic_postgres_api.py](app_basic_postgres_api.py) - shows basic connection to Postgres and returns query as json
+ [app_postgres_api_js_d3_html.py](app_postgres_api_js_d3_html.py)- Adds to previous with HTML templates, example of calling the api in app.js
+ [app_basic_mongo_api.py](app_basic_mongo_api.py) - basic mongo api
+ [app_mongo_d3.py](app_mongo_api_js_d3_html.py)  - Adds to previous with HTML templates, example of calling the api in app.js
### HTML Templates
+ [Home page](templates/home.html) - page rendered using flask to create the elements on the page before it's sent to the browser. (no api used)
+ [Default Page](templates/index.html) - basic example in the consoles
+ [Post Example](templates/post.html) - entering data in the browser and sending it back to Flask for processing and returning the result and displaying on the page and in the consoles
    - only works when running [The basic post example](app.py)
### General
+ style overrides in [static/css/style.css](static/css/style.css)
+ example api usage in [static/js/app.js](static/js/app.js)
+ Python requirements are located in [requirements.txt](requirements.txt)

##### Open License - I don't care what you do with this. if someone actually uses it or finds it helpful, let me know (or not)

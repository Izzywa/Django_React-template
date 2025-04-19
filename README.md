# steps
1. create venv
2. install Django

```
pip3 install django djangorestframework
```

3. start project

```
django-admin startproject <project name>
```

4. cd into the project file
5. start app

```
django-admin startapp <app name>
```

6. add app in `INSTALLED_APP` in the `settings.py` folder
7. add `rest_framework` in the `INSTALLED_APP` too
8. add `urls.py` file to the apps
9. add path to the apps in the project `urls.py` file
10. makemigrations and migrate to initialise the database

## API views:
- import the restframework methods
```
from rest_framework.response import Response
from rest_framework.decorators import api_view
```

- return in `Response` to get API view

## React:
- cd into the project directory and run `npm` to see if npm and node installed
- cd into the frontend app directory
- add folders in the frontend directory
    - frontend > templates > frontend
    - frontend > static
        - frontend
        - css
    - frontend > src

- initialise a node project
    - will create all needed for a node project 
```
npm init -y
```

- install packages
    - `--save-dev`

```
webpack
webpack-cli
@babel/core
babel-loader
@babel/preset-env
@babel/preset-react
@babel/plugin-transform-class-properties
react
react-dom
```
- webpack: transpile all into one js file
- babel: turn code into compatible one with all browsers
- react

### install any other packages as needed

### add files in frontend app
- babel.config.json
    - snippets = `babel`
    - sets up babel loader 

- webpack.config.js
    - bundle all js file into one file
    - serves the one file to the browser
    - need to determine where is the entry js file and where to output
    - snippets = `webpack.config`
    - entry: where the js file will be read from
    - output: where the js files will be output to
    - optimization: minimize = smaller = faster browser load
    - plugings: sommething like optimization

- edit `package.json`
    - add to script
    - snippets = `dev`
    - dev: run webpack in development mode and watch mode that will watch for changes
        - recompile the js file to the output file
    - build: production mode
    - remove the `"type": "commonjs"`


### add templates for React to fill in
- add html file to the `templates > frontend` folder
    - add necessary items (bootstrap, csrf token, js and css file)
    - snippets = `html-react`

### render the html file in the views

### add the js files
- `index.js` in the src folder
    - create root and render App component 
- `App.s` in the src > components folder
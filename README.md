### deta-crud
`deta-crud` is a sample code to demonstrate connection to MONGO DB and doing some CRUD operations.

In this example you can deploy your own copy of this example, provide the necessary MONGO DB credentials and extend its use for your own purpose.

This API is deployed on a [deta micro](https://www.deta.sh/) and uses easy to python library - [FastAPI](https://fastapi.tiangolo.com/)

#### Deploy a copy of this code to your own deta micro

To deploy it to a [deta micro](https://deta.sh) push 

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/ugmurthy/deta-crud)


#### Database
The database in this sample code consists of two collections
* a `header` collection
* and a `readings` collection
* every document in the `header` collection has one or more documents in `reading` collection
* the reading are fictious and represent 3 axis accelerometer  readings

#### deta.json

`deta.json` facilitates specifying metadata and environment variables - for details look [here](https://docs.deta.sh/docs/micros/deploy_to_deta_button/#metadata-environment-variables-and-cron)
```
{
    "name": "deta-crud",
    "description": "API for MONGO DB CRUD operations",
    "runtime": "python3.",
    "env": [
        {
            "key": "DB_USER",
            "description": "Mongo DB Username",
            "value": "",
            "required": true
        },
        {
            "key": "DB_PWD",
            "description": "Mongo DB Password",
            "value": "",
            "required": true
        },
        {
            "key": "DB_HOST",
            "description": "MONGO DB HOST name",
            "value": " ",
            "required": true
        }

    ]
}
```

#### Installation Instructions

##### Install on your deta micro

Note: Assumues you have deta cli - otherwise [look here for details](https://docs.deta.sh/docs/cli/install)

OPTION 1: Hit [![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/ugmurthy/deta-crud)

OPTION 2: The path where you will learn something if you are new to deta
```
## STEP 1 - clone the repo
$ git clone https://github.com/ugmurthy/deta-crud
$ cd deta-crud

## STEP 2 - login and create a new micro - keep a note of the endpoint
$ deta login
$ deta new

## STEP 3
## use a text editor to create .env file with following environment variables
## DB_USER=db_user_name
## DB_PWD=db_password
## DB_HOST=db_hostname

## STEP 4 update the environment variables on deta micro
$ deta update --env .env

## depluy your code
$ deta deploy
```

##### Install on your local machine

```
## Create a virual environment if needed
$ git clone https://github.com/ugmurthy/deta-crud
$ cd deta-crud
$ pip install -r requirements.txt
## use a text editor to create .env file with following environment variables
## DB_USER=db_user_name
## DB_PWD==db_password
## DB_HOST=db_hostname

$ uvicorn main:app --reload
```

Once done use a browser to browse the endpoint/docs for the list of APIs



    

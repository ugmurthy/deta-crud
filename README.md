### deta-crud
`deta-crud` is a sample code to demonstrate connection to MONGO DB and doing some CRUD operations.

In this example you can deploy your own copy of this example, provide the necessary MONGO DB credentials and extemd its use for your own purpose.

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


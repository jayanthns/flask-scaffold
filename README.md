# flask-mysql-blueprints-marshmallow-sqlalchemy.

#####Scaffold of `Flask` `Mysql` `Blueprints` `Marshmallow` `SQLAlchemy` `flask cli`

## Requirements
### Recommended editor:
Download from this link ---> [Visual Studio Code](https://code.visualstudio.com/Download)

### Prerequisite knowledge:
`VS Code` `Python` `Flask` `Rest API` `MySQL` `marshmallow` `SQLAlchemy`

### System requirements:
* `Python 3.6+`
* `mysql`

## Getting started

#### Create virtual environment
`python3 -m venv env`

#### Activate the environment
`source env/bin/activate`


```cd <project_root>```

##### Create `.env` file
###### ***`Copy env variables from .sample.env file and insert in the .env file.`

##### For Dubug mode
`export FLASK_DEBUG=1` 0: off, 1: on

##### Creation of migrations folder
`flask db init`

#### For migrations
`flask db migrate`

#### Applying the migrations
`flask db upgrade`

#### Running the project
`flask run`
or
`python manage.py`
or
`gunicorn --bind 0.0.0.0 wsgi:app --log-level DEBUG --reload`

-----Project setup completed-----

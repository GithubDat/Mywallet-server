[![CircleCI](https://circleci.com/gh/CognizantStudio/lp02-team-s-server.svg?style=svg&circle-token=d55eb10724c9030b8c45112ba3935b69c6cab5e2)](https://circleci.com/gh/CognizantStudio/lp02-team-s-server)

# LP02 Team S Risk Adjustment Server

The server has these dependencies:
 * Python
 * Flask
 * GraphQL
 * Postgres

### Getting Started
Clone this repo

Make sure you have Python up to date; this was built with Python 3.6.4

You'll need to setup the virtual environment for this application and setup the database.
To setup the virtual environment:
Install `virtualenv` through `pip`
    - `pip install virtualenv`

Create a virtual environment in the root directory of this project with `virtualenv venv`

Activate the virtual environment with the following command:
    - `. ./venv/Scripts/activate`

## Installation
Use `pip install -r requirements.txt` to install all required libraries
`pip install -e .`


This Flask application is setup akin to what is described (here)[http://flask.pocoo.org/docs/0.12/patterns/packages/] so if you have not run `pip install -e .` you might need to prefix the `flask` commands with `python -m`. This (page)[https://stackoverflow.com/questions/7610001/what-is-the-purpose-of-the-m-switch] has more information on the `-m` option.

Then when you run the application make sure you have initialized the following shell environment variables:

```bash
export FLASK_APP=server/__init__.py
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_server"
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_servertest"
```

Server is installed.
One plugin(autopep8) needs to be installed. Run the below command:
./run_tests_windows.sh

The next sections cover setting up the database.


## Database Setup

### Create Database

```bash
createdb lp02_team_s_server
```

### Create test Database

```bash
createdb lp02_team_s_servertest
```

### Export test Database

```bash
export DATABASE_URL="postgresql://$(whoami)@localhost/lp02_team_s_servertest"
```

### Initialize Database Migration

This is a one-time setup - if there is no `migrations` folder in this directory then run this command:

```bash
flask db init
```

### Generate/Regenerate Migration Files

When the data model changes, you will need to regenerate the migration files with the following command:
```bash
flask db migrate
```

### Execute Database Migration

```bash
flask db upgrade
```

### Seed Database
Run the following to seed the database with data:
```bash
./init_db.py '--runseed'
```

## S3 for Local Development

You will need to setup configuration to pull from Amazon S3 (contact Chad McKenna or Balakrishna Jahagirdar). Please set the following environment variables:
```bash
export S3_ACCESS_KEY='<our_access_key>'
export S3_SECRET_KEY='<our_secret_key>'
```

## Start the Server

The startup activates the virtual environment and initializes variables.

```bash
For linux:
./start_server.sh
For windows:
./start_server_windows.sh
```

Once the server has started, you can try GraphQL queries here: http://127.0.0.1:5000/graphql-debug


## Run Tests

The scripts to run tests also activate the virtual environment and initialize variables.

```bash
For linux:
./run_tests.sh
For windows:
./run_tests_windows.sh
```

Can also run: `python setup.py test`

`py.test -s` - Run tests and see output from print statements

`py.test -x` - Run tests and stop on the first test failure

### GraphQL testing
In following the advice of <http://docs.graphene-python.org/en/latest/testing/>, we have snapshot testing for
our GraphQL endpoints. `test_schema.py` contains an example of how to write a graphene snapshot test.

To update a snapshot for a given test-file:
```bash
py.test --snapshot-update ./path/to/the_test_file.py
```

NOTE: You MUST update all snapshots for the entire file, there's no way to do it more granularly than that.
You were warned.git


## Run Lint

```bash
flake8
```

To add a local git hook for yourself, run:
```bash
flake8 --install-hook git
```
After adding above hook you will be able to see lint errors while git commit.
#   M y w a l l e t - s e r v e r c o d e  
 
# Intro to Prefect

This project is meant as an Introduction to Data Engineering through Prefect.


## Setup

```shell
python3 -m venv .venv
source .venv/bin/activate
pip3 install -e '.[dev]'
pre-commit install
docker compose up -d
prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
prefect server start
```

**Note:** Pre-commit hooks might not work as expected if folder structure is as in this whole repo. Instead, just use this learming module folder as the repo content so that toml file is in root directory and can be used to configure some of the pre-commit hooks.

## Run Prefect Pipeline

Go to the project folder 'Intro to Prefect' and activate venv. Then, run pipeline (already set in toml file to run main function with script call as 'pipeline')
```shell
cd 'Intro to Prefect'
source .venv/bin/activate
pipeline
```

Open Prefect UI in browser (http://localhost:4200/) and trigger a run for the flow from deployment tab. 'Quick Run' will use default parameters and 'Custom Run' provides options to modify the parameters.

## Check Database

Open Adminer UI hosted on http://localhost:8080/ and login with below details:
```
System: PostgreSQL
Server: database (not localhost because db service is inside docker)
Username: root
Password: root
Database: petstore
```
Once logged in, 'inventory_history' table can be seen here.

## Teardown

```shell
docker compose down
deactivate      # to exit virtual environment .venv
```

**Note:** Depending on docker installation process used, `docker-compose` might be available to use instead of `docker compose` in above commands.


## Description

**Setup virtual environment:** `python -m venv .venv`
- This command creates a virtual environment using Python's venv module.
- venv is a tool for creating isolated Python environments to manage project-specific dependencies.
- .venv: This specifies the directory name for the virtual environment. In this case, it creates a folder named .venv in the current directory.

**Setup virtual environment:** `source .venv/bin/activate`
- This activates the newly created virtual environment (.venv).
- On Unix-like systems (Linux, macOS), the source command runs the activate script located in the .venv/bin/ directory.
- Once activated, any Python packages installed using pip will be contained within this virtual environment, and the Python version used will be the one from .venv.

**Install development dependencies:** `pip install -e '.[dev]'`
- This installs the Python project's dependencies in "editable" mode using pip.
- -e: The "editable" flag allows you to make changes to the source code without having to reinstall the package every time.
- .[dev]: This is a special notation to install development dependencies. The dot (.) refers to the current directory, and [dev] refers to extra dependencies specified in the setup.py or pyproject.toml file, typically for development purposes (e.g., testing libraries, linters, etc.).

**Install Git pre-commit hooks:** `pre-commit install`
- This installs Git pre-commit hooks for the repository. Pre-commit hooks are scripts that run automatically before committing code changes.
- These hooks typically ensure that code is formatted, linted, and checked for errors before it can be committed to the version control system (Git).
- pre-commit is a popular Python tool for managing and running these hooks.

**Start services via Docker:** `docker-compose up -d`
- This command starts Docker containers using the docker-compose tool.
- docker-compose uses a docker-compose.yml file to define and configure multiple Docker containers for a project.
- up: This starts all the services defined in the docker-compose.yml file.
- -d: This flag runs the containers in the background ("detached" mode).
- It typically starts services such as databases, API servers, or other dependencies required by your project.

**Configure Prefect server:** `prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"`
- This sets the Prefect configuration to point to a specific Prefect API URL.
- Prefect is a workflow orchestration tool used to manage, monitor, and schedule tasks and data pipelines.
- PREFECT_API_URL="http://127.0.0.1:4200/api": This sets the API endpoint for the Prefect server to http://127.0.0.1:4200/api, where 127.0.0.1 is the local machine's IP address (localhost) and port 4200 is where the Prefect API is running.

**Start Prefect server:** `prefect server start`
- This starts the Prefect server, which is the orchestration backend for Prefect workflows.
- It typically launches services like the Prefect API, UI, and other components required to run and manage workflows.
- After running this command, the Prefect server will be available at the URL set in the previous step (http://127.0.0.1:4200/api), and you can interact with it to schedule and monitor tasks.


## More Information

**Details of venv:** Once `source .venv/bin/activate` has been used terminal should show (.venv) in the beginning to indicate its inside virtual environment. Below commands can be used to know more details of this virtual env using terminal:
```bash
pip list                # List installed packages
echo $VIRTUAL_ENV       # Check the virtual environment's location
python --version        # Check the Python version

# Check the virtual environment's status
echo "In virtual environment: $(python -c 'import sys; print(sys.prefix)')"
```

<hr><hr>

TODO: Add test functions and pytest functionality

The initial version of project is based on a youtube video live coding: https://www.youtube.com/watch?v=FxRZ9zo6GmI

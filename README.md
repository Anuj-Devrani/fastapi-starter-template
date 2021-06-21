# FastAPI Starter Template

## Description
Simple template for quickly starting a backend project on FastAPI.

FASTAPI + MYSQL + SQLALCHEMY + ALEMBIC + POETRY
## Features

* Python <a href="https://github.com/tiangolo/fastapi" class="external-link" target="_blank">**FastAPI**</a> backend:
    * **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic).
    * **Intuitive**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging.
    * **Easy**: Designed to be easy to use and learn. Less time reading docs.
    * **Short**: Minimize code duplication. Multiple features from each parameter declaration.
    * **Robust**: Get production-ready code. With automatic interactive documentation.
    * **Standards-based**: Based on (and fully compatible with) the open standards for APIs: <a href="https://github.com/OAI/OpenAPI-Specification" class="external-link" target="_blank">OpenAPI</a> and <a href="http://json-schema.org/" class="external-link" target="_blank">JSON Schema</a>.
* **SQLAlchemy** models (independent of Flask extensions, so they can be used with Celery workers directly).
* **Automatic migrations** with **Alembic**
* **CORS** (Cross Origin Resource Sharing).
* **Poetry** for dependency management.  
* Sample model with examples.

## Directory Structure
```shell
├── alembic.ini
├── app
│   ├── apis
│   │   ├── api.py
│   │   ├── deps.py
│   │   ├── __init__.py
│   │   └── item
│   │       ├── api.py
│   │       ├── crud.py
│   │       ├── __init__.py
│   │       ├── models.py
│   │       └── schemas.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── db
│   │   ├── base.py
│   │   ├── __init__.py
│   │   └── session.py
│   ├── __init__.py
│   ├── main.py
│   └── routes
│       └── __init__.py
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       └── d277b5881619_create_starter_models.py
├── poetry.lock
├── pyproject.toml
└── README.md
```

## How to use it
1. Clone the repo.
```shell
git clone git@github.com:Anuj-Devrani/fastapi-starter-template.git
```

2. Install requirements.
```shell
poetry install
poetry shell
```

3. Put values as per your configuration in .env

4. Run alembic migrations.
```shell
alembic upgrade head 
```

5. Run with:
```shell
uvicorn app.main:app --reload
```

Access docs at [http://localhost:8000/docs](http://localhost:8000/docs).

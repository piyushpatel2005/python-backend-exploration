# Social API

In this section, we will build a simple social media API using FastAPI. The API will allow users to create posts, like posts, and follow other users.


## Running Locally

```shell
cd examples/fastapi
```

Create `.env` file inside `socialapi` directory with the following content based on `.env.example` file.

```shell
pip install -r requirements.txt
uvicorn socialapi.main:app --reload
```

### Developing Locally

```shell
pip install -r requirements-dev.txt
```


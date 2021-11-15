# Music Genre Classifier

## Objective

The objective of this project is to learn about approaches to classification of music genres. 
The main method explored in this project id is K-nearest neighbours.

K-nearest neighbours is popularly used for regression and classification. The predictions on the data points are based
on a similarity score, which is computed based on how far the points are from one another.

## Background



## Develop

The project can be bootstrapped locally using docker-compose. A Makefile is included in the repository for ease of use.

### Build

To build the project you can run the following Makefile target.

```bash
make build ARGS="--build-arg 'POETRY_PYPI_TOKEN_PYPI=<azure artifact token here>'"
```

### Environment variables

The local project makes use of 2 files for environment variables.

- .private.env
- .public.env

The `.private.env` variables should include all variables which should **not** be checked into version control.

The `.public.env` file is checked into version control as it must only contain non sensitive variables required for local development. `.public.env` is included merely for the developer experience as sourcing the appropriate values for the required variables is cumbersome.

In spite of the above there are certain private variables required to run the project locally. These should be kept out of version control in the `.private.env` file as explained above and include:

```bash

```
### Run

To bring up the containers you can run one of the following Makefile targets.

```bash
make up
make upd # Run as a daemon process
```

### Manually Invoking Functions

You can manually invoke non HTTP trigger functions by making the following POST request.


```python
import requests


requests.post(
    "http://localhost:8082/admin/functions/knack_data_loader/",
    json={},
    headers={"x-functions-key": "MASTER_KEY"}
)
```

Or run the `invoke-<function>` targets available in the Makefile.

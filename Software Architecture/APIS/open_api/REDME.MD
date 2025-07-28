OpenAPI
=======


```bash
brew install openapi-generator

# Generate a Python client from the OpenAPI YAML file: bash Copy
openapi-generator generate -i /path/to/your/openapi-spec.yaml -g python -o ./generated-client
# Generate a Node.js client from the OpenAPI YAML file: bash Copy
openapi-generator generate -i /path/to/your/openapi-spec.yaml -g javascript -o ./generated-client

```

Example app

```bash
├── client
│   ├── __init__.py
│   ├── custom.py
│   └── generated-client
│       └── __init__.py
├── my_app
│   ├── __init__.py
│   └── main.py
└── openapi_spec.yaml

```

**commands:**

```bash
openapi-generator generate -i openapi_spec.yaml -g python -o client/generated-client

openapi-generator generate -i openapi_spec.yaml -g python -o client/generated-client --library httpx --poetry1

```

### openapi-python-generator

* https://pypi.org/project/openapi-python-generator/
* https://marcomuellner.github.io/openapi-python-generator/quick_start/

```bash
openapi-python-generator generate ./openapi_spec.yaml --output client/generated-client --library httpx --poetry

```
# Application Bootstrap Documentation

This document outlines the bootstrapping process for the PyService application, including database initialization and FastAPI application setup.

## Functions

### bootstrap_database

```python
def bootstrap_database() -> None:
```

#### Description
Creates database tables schematics if they don't exist at application startup.

#### Functionality
- Calls `create_score_table()` to initialize the score table in the database.

#### Return Value
None

#### Side Effects
- May create or modify database tables.

### bootstrap_application

```python
def bootstrap_application() -> FastAPI:
```

#### Description
Initializes and configures the FastAPI application.

#### Functionality
1. Configures basic logging.
2. Creates a new FastAPI instance with title and description.
3. Collects and includes routers using `collect_and_include_routers`.

#### Return Value
- `FastAPI`: Configured FastAPI application instance.

#### Side Effects
- Sets up logging configuration.
- Modifies the FastAPI application by including routers.

## Application Setup

```python
app = bootstrap_application()
bootstrap_database()
```

#### Description
Initializes the FastAPI application and sets up the database.

#### Functionality
1. Calls `bootstrap_application()` to create and configure the FastAPI app.
2. Calls `bootstrap_database()` to initialize the database tables.

## Dependencies

- `FastAPI` from `fastapi`
- `basicConfig`, `INFO` from `logging`
- `collect_and_include_routers` from `pyservice.api.builder`
- `create_score_table` from `pyservice.infrastructure.mapping.score_table`

## Configuration Details

- **Logging**: Set to INFO level with format "%(asctime)s - %(levelname)s - %(message)s"
- **FastAPI App**:
  - Title: "PyService Template"
  - Description: "This is an internal template for fastapi microservices"

## Notes

- The `collect_and_include_routers` function is used to dynamically include routers in the FastAPI application.
- There's a TODO comment suggesting future implementation of a Redis Enable/Disable mechanism.

## Usage

This code is typically used as the entry point for the PyService application. To use:

1. Ensure all dependencies are installed.
2. Run this script to start the FastAPI application with the configured settings and initialized database.

## Potential Improvements

1. Implement the Redis Enable/Disable mechanism mentioned in the TODO comment.
2. Add error handling for database initialization.
3. Consider making the logging configuration customizable through environment variables or a config file.
4. Add health check endpoints or startup/shutdown event handlers if needed.
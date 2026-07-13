# Practice Codespace - FastAPI Starter Project

A scalable FastAPI starter project with comprehensive features including database integration, exception handling, logging, and lifespan management.

## Project Overview

This is a production-ready FastAPI application demonstrating best practices for building modern Python APIs. The project is structured to be modular, testable, and easy to maintain.

## Project Structure

```
practice-codespace/
├── main.py                 # Application entry point
├── test.py                 # Test suite
├── Dockerfile              # Docker configuration for containerization
├── app.db                  # SQLite database file
│
├── app/
│   ├── api/
│   │   ├── routes.py       # API endpoints and routing logic
│   │   ├── schemas.py      # Pydantic models for request/response validation
│   │   └── dependencies.py # Database session management
│   │
│   ├── core/
│   │   ├── exceptions.py   # Global exception handlers
│   │   ├── lifespan.py     # Application lifecycle management
│   │   └── logging.py      # Logging configuration
│   │
│   └── db/
│       ├── database.py     # Database configuration and session setup
│       └── models.py       # SQLAlchemy ORM models
```

## Code Workflow

### 1. **Application Initialization** (`main.py`)

The application starts by creating a FastAPI instance through the `create_app()` function:

- **App Setup**: Creates a FastAPI instance with metadata (title, version, description)
- **Logging**: Initializes logging configuration
- **Exception Handlers**: Registers custom exception handlers globally
- **Routes**: Includes all API routes
- **Lifespan**: Manages startup and shutdown events

```python
app = create_app()  # Creates and returns the configured FastAPI app
```

### 2. **Core Components**

#### **Logging Setup** (`app/core/logging.py`)
- Configures basic logging with INFO level
- Format: `timestamp - level - logger_name - message`
- Used throughout the application for debugging and monitoring

#### **Exception Handling** (`app/core/exceptions.py`)
- **HTTP Exception Handler**: Returns JSON responses for HTTP errors
- **Validation Exception Handler**: Handles Pydantic validation errors with 422 status
- **Unhandled Exception Handler**: Catches unexpected errors with 500 status
- All exceptions are converted to consistent JSON error responses

#### **Application Lifespan** (`app/core/lifespan.py`)
- **Startup**: 
  - Logs "Application startup" message
  - Sets `app.state.started = True`
  - Initializes `AppResource` and marks it as initialized
- **Shutdown**: 
  - Performs cleanup by shutting down resources
  - Sets initialization flag to False
  - Logs "Application shutdown" message

### 3. **Database Layer** (`app/db/`)

#### **Database Configuration** (`app/db/database.py`)
- Uses SQLite database (`app.db`)
- Creates a connection engine with thread-safety disabled (suitable for development)
- Creates a session factory for database operations
- Sets up SQLAlchemy's declarative base for model definition

#### **Database Models** (`app/db/models.py`)
- **Item Model**: ORM model representing items table
  - `id`: Primary key (Integer, auto-increment)
  - `name`: Item name (String, non-nullable)

### 4. **API Layer** (`app/api/`)

#### **Schemas** (`app/api/schemas.py`)
- **ItemCreate**: Pydantic model for creating items
  - `name`: Required string field for item name
  - Provides request validation

#### **Dependencies** (`app/api/dependencies.py`)
- **get_db()**: Dependency function that provides database sessions
  - Creates a new session for each request
  - Ensures proper cleanup in finally block
  - Used with FastAPI's `Depends()` mechanism

#### **Routes** (`app/api/routes.py`)
- **GET `/`**: User endpoint that returns a success message
- **GET `/health`**: Health check endpoint for monitoring
- **POST `/items`**: Create a new item in the database
  - Accepts `ItemCreate` schema
  - Uses database session dependency
  - Returns created item with ID
- **GET `/items`**: Retrieve all items from the database
  - Returns list of items with id and name

### 5. **Testing** (`test.py`)

Comprehensive test suite using FastAPI's TestClient:

- **test_root_endpoint()**: Verifies root endpoint works
- **test_health_endpoint()**: Verifies health check endpoint
- **test_not_found_returns_json_error()**: Validates error handling for non-existent routes
- **test_lifespan_sets_app_state()**: Confirms lifespan events execute properly
- **test_items_endpoints_work_with_sqlalchemy()**: Tests database integration with CRUD operations

## API Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|------------|
| GET | `/` | User endpoint | 200 |
| GET | `/health` | Health check | 200 |
| POST | `/items` | Create item | 201 |
| GET | `/items` | List all items | 200 |

## Running the Application

### Local Development

```bash
# Install dependencies
pip install fastapi uvicorn sqlalchemy

# Run the application
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Using Docker

```bash
# Build the Docker image
docker build -t practice-codespace .

# Run the container
docker run -p 8000:8000 practice-codespace
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest test.py -v
```

## Key Features

✅ **Modular Architecture**: Organized by concerns (api, core, db)
✅ **Database Integration**: SQLAlchemy ORM with SQLite
✅ **Error Handling**: Centralized exception handling with JSON responses
✅ **Logging**: Configured logging for debugging and monitoring
✅ **Lifespan Management**: Proper startup and shutdown event handling
✅ **Request Validation**: Pydantic schemas for type safety
✅ **Dependency Injection**: FastAPI's dependency system for loose coupling
✅ **Containerization**: Docker support for easy deployment
✅ **Testing**: Comprehensive test coverage
✅ **Production-Ready**: Follows FastAPI best practices

## Technology Stack

- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI web server
- **Docker**: Containerization

## Development Workflow

1. **Define Models**: Add new models in `app/db/models.py`
2. **Create Schemas**: Define request/response schemas in `app/api/schemas.py`
3. **Add Routes**: Implement endpoints in `app/api/routes.py`
4. **Handle Errors**: Add custom exception handlers if needed
5. **Write Tests**: Add test cases in `test.py`
6. **Deploy**: Use Docker or standard Python deployment methods

---

**Created**: July 2026  
**Language**: Python 3.11  
**Framework**: FastAPI 0.100+  
**License**: MIT

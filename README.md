![API Tests](https://github.com/Harryl3ivers/api-integration-testing-framework/actions/workflows/tests.yml/badge.svg)
# API Integration Testing Framework

An automated API testing framework built with Python, Pytest and Requests.  
The project validates REST API functionality through automated CRUD, authentication, negative and integration tests.

The framework also includes SQL validation using SQLite and a Postman collection for manual API testing.

## Technologies

- Python
- Pytest
- Requests
- Faker
- SQLite
- SQL
- Postman
- GitHub Actions

## Testing Coverage

The framework includes tests for:

### Authentication Testing
- Successful authentication
- Token generation
- Invalid credentials

### Booking API Testing
- Create bookings
- Retrieve bookings
- Update bookings
- Delete bookings

### Negative Testing
- Invalid booking IDs
- Invalid requests
- Failed authentication scenarios

### Data Validation
- Response structure validation
- API response value validation
- API data compared against SQLite database records

## Framework Structure
api/
├── client.py
├── config.py
└── validators.py

database/
├── connection.py
└── queries.py

tests/
├── test_auth.py
├── test_bookings.py
└── test_database.py

postman/
├── Restful Booker.postman_collection.json
└── Restful Booker.postman_environment.json


## Running Tests

Create a virtual environment:


python -m venv venv


Activate:

Windows:


venv\Scripts\activate


Install dependencies:


pip install -r requirements.txt


Run tests:


pytest -v


Generate HTML report:


pytest -v --html=reports/test-report.html --self-contained-html


Generate coverage report:


pytest --cov=api --cov=database --cov-report=html


## CI/CD

Tests are automatically executed using GitHub Actions whenever changes are pushed to the repository.

## Postman Collection

A Postman collection is included for manual API testing and exploratory testing.

The collection covers:

- Authentication
- CRUD operations
- Negative test scenarios
- Environment variables
# AI Usage Notes

## AI Tools Used

- ChatGPT

## AI-Assisted Work

- Generated the initial FastAPI project structure.
- Helped create CRUD endpoint boilerplate.
- Suggested the pytest structure.

## Changes I Made

- Implemented automatic ID generation.
- Added category filtering.
- Added total expense calculation.
- Added delete functionality with 404 handling.
- Fixed JSON serialization for Python date objects using `default=str`.
- Improved Swagger documentation with tags and status codes.

## Validation

- Manually tested all endpoints using Swagger UI.
- Wrote and executed automated tests using pytest.
- Verified JSON file persistence across operations.

## AI Suggestions Not Used

- SQLite database implementation.

Reason:
The assignment explicitly allowed JSON file storage, so I chose a lightweight JSON-based implementation.
# Simplified API Sample

This is a simplified version of the original project, containing only one sample endpoint from each category:

- One API endpoint: Health check at `/health_check/`
- One user endpoint: User profile at `/user/profile/{user_id}`
- One test file: Testing both endpoints

## Project Structure

```
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── health_check.py  # Simple health check endpoint
│   │       └── user.py          # User profile endpoint
│   └── main.py                  # FastAPI application setup
├── tests/
│   └── test_api.py              # Tests for the endpoints
├── main.py                      # Entry point
└── requirements.txt             # Dependencies
```

## Setup and Installation

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8100 --reload
```

The API will be available at http://localhost:8100

## API Endpoints

- `GET /health_check/` - Check if the API is running
- `GET /user/profile/{user_id}` - Get a user profile by ID

## Running Tests

```bash
pytest tests/
```

## License

Distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

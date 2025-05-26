# Deployment: Tree of Life Cladogram

## Local Deployment (Docker)

1. Build and run backend:
    ```bash
    cd scripts
    docker build -t tol-backend .
    docker run -p 5001:5001 tol-backend
    ```

2. Serve frontend as before (`python -m http.server 8000` in `web/`).

## Cloud/Production

- Deploy backend on any Python 3.8+ host (Heroku, AWS, etc).
- Configure CORS as needed.
- Frontend can be served as static files.

## Requirements

- Python 3.8+ for backend. Node.js (optional) for frontend JS tests.
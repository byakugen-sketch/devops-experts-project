# Phase 1 — Flask Application & Docker

A simple Python Flask application containerized with Docker and published to Docker Hub.

---

## Application

Built with Flask, the app exposes two endpoints:

| Endpoint | Method | Response |
|----------|--------|----------|
| `/` | GET | `Hello, Doron!` |
| `/health` | GET | `{"status": "healthy"}` |

The `/health` endpoint is used by Kubernetes liveness and readiness probes in Phase 2.

---

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

---

## Docker Hub

The image is published at:

**`docker.io/uzumaki420/devops-experts-project:latest`**

Pull and run directly without building locally:
```bash
docker run -p 5000:5000 uzumaki420/devops-experts-project:latest
```

---

## Build and Run Locally

### 1. Build the image
```bash
docker build -t devops-experts-project .
```

### 2. Run the container
```bash
docker run -p 5000:5000 devops-experts-project
```

### 3. Open in browser
Visit: [http://localhost:5000](http://localhost:5000)

---

## Run with Docker Compose

```bash
docker-compose up
```

To stop:
```bash
docker-compose down
```

Enable debug mode:
```bash
FLASK_DEBUG=true docker-compose up
```

---

## Run Locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```

---

## Project Structure

```
Phase 1/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Docker Compose configuration
└── .dockerignore        # Files excluded from the Docker build context
```

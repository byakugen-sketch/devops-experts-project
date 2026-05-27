# devops-experts-project

A simple Python Flask application that returns a "Hello, Doron!" message.

---

## Requirements

- [Docker](https://www.docker.com/products/docker-desktop)

---

## Pull from Docker Hub

```bash
docker run -p 5000:5000 uzumaki420/devops-experts-project:latest
```

---

## Run with Docker

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

---

## Run Locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```

Enable debug mode:
```bash
FLASK_DEBUG=true python app.py
```

# Phase 2 — Kubernetes with Minikube

Deploys the Flask app from Phase 1 onto a local Kubernetes cluster using Minikube.

---

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

---

## Start the Cluster

```bash
minikube start --driver=docker
```

---

## Deploy the App

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify everything is running:
```bash
kubectl get pods
kubectl get services
```

---

## Access the App

The NodePort URL is not directly reachable on Mac with the Docker driver. Use the Minikube tunnel instead:

```bash
minikube service flask-service
```

This opens a tunnel and provides a local URL to access the app (e.g. http://127.0.0.1:58117). The port changes each time the tunnel is started.

---

## Tear Down

```bash
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
minikube stop
```

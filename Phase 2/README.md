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
minikube addons enable metrics-server
```

---

## Deploy the App

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Verify everything is running:
```bash
kubectl get pods
kubectl get services
kubectl get hpa
```

---

## Access the App

The LoadBalancer IP requires a Minikube tunnel to be reachable on Mac:

```bash
minikube tunnel
```

App is then available at: **http://127.0.0.1:80**

---

## Horizontal Pod Autoscaling (HPA)

The HPA automatically scales the number of pods between 2 and 10 based on CPU usage. It triggers when average CPU across all pods exceeds 50% of their requested CPU (`100m`).

To verify HPA is working:
```bash
kubectl get hpa
kubectl top pods
```

To watch pods scale in real time:
```bash
kubectl get pods -w
```

---

## Tear Down

```bash
kubectl delete -f hpa.yaml
kubectl delete -f deployment.yaml
kubectl delete -f service.yaml
minikube stop
```

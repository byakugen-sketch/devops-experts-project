# Phase 3 — Helm & CI/CD with Jenkins

Packages the Kubernetes manifests from Phase 2 into a Helm chart and automates build, test, and deployment through a Jenkins pipeline.

---

## Structure

```
Phase 3/
├── Chart.yaml
├── values.yaml
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── hpa.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── cronjob-healthcheck.yaml
│   └── cronjob-cleanup.yaml
├── jenkins/
│   ├── Dockerfile
│   └── docker-compose.yml
└── README.md
```

---

## Helm Chart

The chart templates all Phase 2 Kubernetes manifests. All configurable values are in `values.yaml` — no need to edit individual manifests.

### Install

```bash
helm install flask-app ./Phase\ 3 --set secret.secretKey=<your-secret>
```

### Upgrade

```bash
helm upgrade flask-app ./Phase\ 3 --set secret.secretKey=<your-secret>
```

### Uninstall

```bash
helm uninstall flask-app
```

---

## Jenkins CI/CD Pipeline

### Prerequisites

- Docker Desktop
- Minikube running (`minikube start --driver=docker`)
- Minikube tunnel running (`minikube tunnel`)

### Starting Jenkins

```bash
cd Phase 3/jenkins
docker-compose up -d
```

Jenkins runs at **http://localhost:8080**.

On first launch, retrieve the admin password with:
```bash
docker exec jenkins-jenkins-1 cat /var/jenkins_home/secrets/initialAdminPassword
```

### Required Jenkins Setup

**Plugins:** Git, Docker Pipeline, Credentials Binding (install via suggested plugins on first launch)

**Credentials:**
- Go to Manage Jenkins → Credentials → Global → Add Credentials
- Kind: `Username with password`
- ID: `dockerhub-credentials`
- Username: Docker Hub username
- Password: Docker Hub access token (generate at hub.docker.com → Account Settings → Security → Access Tokens)

**Pipeline job:**
- New Item → `flask-app` → Pipeline
- Definition: Pipeline script from SCM
- SCM: Git → `https://github.com/byakugen-sketch/devops-experts-project.git`
- Branch: `*/main`
- Script Path: `Jenkinsfile`

### Pipeline Stages

| Stage | What it does |
|-------|-------------|
| Checkout | Pulls latest code from GitHub |
| Build | Builds Docker image from Phase 1 |
| Test | Runs pytest inside the built image |
| Push | Pushes image to Docker Hub |
| Deploy | Runs `helm upgrade --install` against the Minikube cluster |

Push and Deploy only run if all previous stages pass.

---

## Issues Encountered

**Branch mismatch**
Jenkins defaulted to `master` but the repo uses `main`. Fixed by updating the branch specifier in the job configuration to `*/main`.

**Docker socket permissions**
Jenkins container couldn't connect to the Docker daemon inside the container. Fixed by running `chmod 666 /var/run/docker.sock` on startup via the `entrypoint` in `docker-compose.yml`.

**Kubernetes unreachable from Jenkins container**
The kubeconfig referenced `127.0.0.1` which inside the Jenkins container points to itself, not the host. Fixed by replacing `127.0.0.1` with `host.docker.internal` in the kubeconfig.

**TLS certificate mismatch**
Minikube's certificate is issued for `localhost`, not `host.docker.internal`. Fixed by removing `certificate-authority-data` from the kubeconfig and setting `insecure-skip-tls-verify: true`. Acceptable for a local development cluster.

**Docker Hub authentication**
A password reset invalidated the existing credentials. Resolved by generating a Docker Hub access token and using that instead of the account password — access tokens are the recommended approach regardless.

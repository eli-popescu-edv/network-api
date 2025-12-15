Got it — here’s a more professional **English README**, with a structure similar to the template style (intro → description → getting started → help), and **without embedding your YAML**, since you already have it in the repo.

---

# Network API

A **FastAPI** service that provides an **IP Subnet Calculator** and a small set of **network utilities**.
Designed to run in **Kubernetes** (local development via **Minikube**).

---

## Description

`network-api` exposes REST endpoints for:

* subnet calculation (mask, network, broadcast, usable host range)
* IP membership checks (does an IP belong to a network?)
* container/pod network information (local IP, default gateway)

It is containerized with Docker and can be deployed locally to Kubernetes using Minikube.

---

## Getting Started

### Dependencies

Make sure you have the following installed:

* **Docker**
* **kubectl**
* **Minikube**

(Optional, but helpful)

* **curl** (for quick API testing)

---

### Installing

Clone the repository:

```bash
git clone https://github.com/eli-popescu-edv/network-api
cd network-api
```

---

### Executing program (Kubernetes / Minikube)

#### 1) Start Minikube

```bash
minikube start --driver=docker
```

Verify cluster is healthy:

```bash
minikube status
kubectl cluster-info
```

#### 2) Build the Docker image

From the project root (where the Dockerfile is):

```bash
docker build -t network-api:latest .
```

#### 3) Load the image into Minikube

```bash
minikube image load network-api:latest
```

#### 4) Deploy to Kubernetes

Apply your Kubernetes manifests (use your actual paths/filenames):

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Check status:

```bash
kubectl get pods -o wide
kubectl get svc
```

#### 5) Access the API

Option A — **Minikube service URL**:

```bash
minikube service network-api-service --url
```

Option B — **Port-forward** (recommended for debugging):

```bash
kubectl port-forward deployment/network-api 8000:8000
```

Then open:

* Swagger UI: `http://127.0.0.1:8000/docs`

---

## API Endpoints

### Subnet Calculator

* `GET /subnet/{ip}/{bits}`
* `POST /subnet/calculate`
* `GET /subnet/mask/{bits}`
* `GET /subnet/addresses/{ip}/{bits}`

Example (browser):

```
/subnet/192.168.1.10/24
```

### Network Tools

* `GET /net/belongs/{ip}/{network_ip}/{bits}`
* `POST /net/belongs`
* `GET /net/local-ip`
* `GET /net/gateway`

Example (browser):

```
/net/belongs/192.168.1.50/192.168.1.0/24
```

---

## Help

### Common issue: changes don’t show up in Kubernetes

Kubernetes will not automatically pick up local code changes unless you rebuild and redeploy:

```bash
docker build -t network-api:latest .
minikube image load network-api:latest
kubectl rollout restart deployment/network-api
```

### Common issue: CrashLoopBackOff

Check pod logs:

```bash
kubectl get pods
kubectl logs <pod-name> --previous --tail=200
```

---

## Notes

* `/net/local-ip` returns the **pod/container IP**, not a public internet IP.
* `/net/gateway` returns the container network’s **default gateway** (useful in Docker/Minikube environments).

---

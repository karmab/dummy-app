This repository contains a sample app for communicating between two endpoints

# How to run

## as a container

```
podman run -p 7000:7000 -e DUMMY_URL=http://10.19.32.57:7000/message  --rm quay.io/karmab/dummy-app:latest
```

## on kubernetes

```
kubectl create -f deployment.yaml
```

## POSTING

```
curl --json '{"tool": "curloid"}' http://127.0.0.1:7000/message
```

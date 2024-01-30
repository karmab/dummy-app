This repository contains a sample app for communicating between two endpoints

# How to run

## as a container

```
podman run -p 7000:7000 -e DUMMY_URL=10.19.32.57:7000  --rm quay.io/karmab/dummy-app:latest
```

## on kubernetes

```
kubectl create -f deployment.yaml
```

## Posting a message

```
curl -H "Content-Type: application/json" -X POST --data '{"tool":"curloid"}' http://127.0.0.1:7000/echo
```

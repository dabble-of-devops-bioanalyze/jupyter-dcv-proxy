#!/usr/bin/env bash

echo "========================================================="
echo "Creating DCV Session:"
echo "dcv create-session --owner ${NB_USER} ${SESSION_ID}"

dcv create-session --owner ${NB_USER} ${SESSION_ID}

echo "Listing DCV Sessions"
dcv list-sessions

configurable-http-proxy --port ${PORT} --default-target=https://localhost:8443 --insecure --log-level=debug

echo "========================================================="

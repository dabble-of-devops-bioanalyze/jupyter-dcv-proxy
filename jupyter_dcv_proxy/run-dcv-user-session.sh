#!/usr/bin/env bash

dcv create-session --owner ${NB_USER} ${SESSION_ID}
configurable-http-proxy --port ${PORT} --default-target=https://localhost:8443 --insecure --log-level=debug

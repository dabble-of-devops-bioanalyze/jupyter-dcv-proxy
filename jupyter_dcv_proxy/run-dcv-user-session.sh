#!/usr/bin/env bash

echo "========================================================="
echo "Creating DCV Session:"

export SESSION_ID=$(uuidgen)
echo "dcv create-session --owner ${USER} ${SESSION_ID}"
dcv create-session --owner ${USER} ${SESSION_ID}

echo "Listing DCV Sessions"
dcv list-sessions

configurable-http-proxy --port ${PORT} --default-target=https://localhost:8443 --insecure --log-level=debug &


while true; do

    dcv describe-session "${SESSION_ID}" || {
        echo >&2 "DCV session ${SESSION_ID} exited unexpectedly. Starting new session"
        SESSION_ID=$(openssl rand -hex 12)
        dcv create-session --owner $USER ${SESSION_ID}
    }
    sleep 10

done

echo "========================================================="

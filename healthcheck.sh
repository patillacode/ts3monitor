#!/bin/bash
curl --head --request GET 127.0.0.1:${DOCKER_INTERNAL_PORT}/status | grep '200 OK'

#!/bin/bash

BIN=$( dirname "$0")
PREFIX=$(dirname "$BIN" )
VENV_DIR="${PREFIX}/main.py"

fastapi dev $VENV_DIR --host 0.0.0.0 --port 8001
#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

if [ ! -d ${DIR}/venv ]; then
    setup.sh
fi
${DIR}/venv/bin/python3 ${DIR}/Nestor/main.py

#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

python3 -m virtualenv -p python3 ${DIR}/venv
${DIR}/venv/bin/pip install -r ${DIR}/requirements.txt

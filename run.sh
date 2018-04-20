#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

if [ ! -d ${DIR}/venv ]; then
    setup.sh
fi

MODE_RASPBERRY=$(uname -a | grep 'raspberry')
if [ "${MODE_RASPBERRY}" != "" ]; then
    export DRY_RUN=true
fi

${DIR}/venv/bin/python3 ${DIR}/Nestor/main.py

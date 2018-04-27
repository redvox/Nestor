#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

if [ ! -d ${DIR}/venv ]; then
    setup.sh
fi

set +e
MODE_RASPBERRY=$(uname -a | grep 'raspberry')
set -e
if [ "${MODE_RASPBERRY}" == "" ]; then
    echo "DRY RUN"
    export DRY_RUN=true
    ${DIR}/venv/bin/python3 ${DIR}/Nestor/main.py --dry
else
    echo "RUN"
    ${DIR}/venv/bin/python3 ${DIR}/Nestor/main.py
fi

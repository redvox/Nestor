#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e
TARGET_IP=${1}
MODE_ALL=${2}

if [ "${MODE_ALL}" == "true" ]; then
    scp -pr ./Nestor pi@${TARGET_IP}:/home/pi/
    scp -pr ./config pi@${TARGET_IP}:/home/pi/
    scp -pr ./requirements.txt pi@${TARGET_IP}:/home/pi/
    scp -pr ./run.sh pi@${TARGET_IP}:/home/pi/
    scp -pr ./setup.sh pi@${TARGET_IP}:/home/pi/

else
    scp -pr ./Nestor/*.py pi@${TARGET_IP}:/home/pi/Nestor
fi

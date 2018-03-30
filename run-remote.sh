#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

TARGET_IP=192.168.178.42

./copy.sh
ssh pi@${TARGET_IP} ./run.sh

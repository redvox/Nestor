#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

MODE_SETUP="false"

usage() {   echo -e "${CB}Usage:${CC}"
            echo    " copy.sh [-s][-h]"
            echo
            echo    "Copies your py files from Nestor to remote."
            echo
            echo -e "${CB}Options:${CC}"
            echo    "   -s      copy all files"
            exit 1; }

while getopts "sh-:" opt; do
  case ${opt} in
    s)
      MODE_SETUP="true"
      ;;
    h)
      usage
      ;;
    *)
      echo -e "${CR}Invalid option:${CC} -$OPTARG"
      usage
      ;;
  esac
done

TARGET_IP=192.168.178.42

if [ "${MODE_SETUP}" == "true" ]; then
    scp -pr ./Nestor pi@${TARGET_IP}:/home/pi/
    scp -pr ./config pi@${TARGET_IP}:/home/pi/
    scp -pr ./requirements.txt pi@${TARGET_IP}:/home/pi/
    scp -pr ./run.sh pi@${TARGET_IP}:/home/pi/
    scp -pr ./setup.sh pi@${TARGET_IP}:/home/pi/

else
    scp -pr ./Nestor/*.py pi@${TARGET_IP}:/home/pi/Nestor
fi

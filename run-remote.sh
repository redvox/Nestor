#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
set -e

TARGET_IP=192.168.178.42

MODE_ALL="false"
MODE_SETUP="false"

usage() {   echo -e "${CB}Usage:${CC}"
            echo    " run-remote.sh [-s][-a][-h]"
            echo
            echo    "Copies your py files from Nestor to remote and execute them"
            echo
            echo -e "${CB}Options:${CC}"
            echo    "   -a      copy all files"
            echo    "   -s      run setup"
            exit 1; }

while getopts "ash-:" opt; do
  case ${opt} in
    a)
      MODE_ALL="true"
      ;;
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

if [ "${MODE_ALL}" == "true" ]; then
    ./copy.sh ${TARGET_IP} true
else
    ./copy.sh ${TARGET_IP}
fi

if [ "${MODE_SETUP}" == "true" ]; then
    ssh pi@${TARGET_IP} ./setup.sh
fi

ssh pi@${TARGET_IP} ./run.sh

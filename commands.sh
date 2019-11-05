#!/bin/bash
# ./commands.sh
# source commands.sh

function setup_pandakids() {
    apt-get install python3-dev
    pip3 install -U Flask
    pip3 install redislite
    pip3 install flask-socketio
}

function run_pandakids() {
    export FLASK_APP=ui_setup.py
    export FLASK_DEBUG=1
    python3 channel_logic.py &
    python3 ui_setup.py
    kill %1
}

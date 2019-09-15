#!/bin/bash
# ./commands.sh
# source commands.sh

function setup_pandakids() {
    apt-get install python3-dev
    pip3 install -U Flask
    pip3 install redislite
}

function run_pandakids() {
    export FLASK_APP=ui_setup.py
    export FLASK_DEBUG=1
    python3 -m flask run
}
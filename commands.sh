#!/bin/bash
# ./commands.sh
# source commands.sh

# Run with argument 'true' to install non-python dependencies
function setup_pandakids() {
    local non_python_install="${1:false}"
    if [ "$non_python_install" == "true" ]; then
        sudo apt-get install python3-dev
        sudo apt-get install espeak
	sudo apt-get install libpulse-dev
	sudo apt-get install portaudio19-dev
	sudo apt-get install swig
    fi
    pip3 install -U Flask
    pip3 install redislite
    pip3 install flask-socketio
    pip3 install PyAudio
    pip3 install pocketsphinx
    pip3 install SpeechRecognition
    pip3 install pyttsx3
    pip3 install gevent
    pip3 install gevent-websocket
    export PYTHONPATH=`pwd`:$PYTHONPATH
}

function run_pandakids() {
    export FLASK_APP=ui_setup.py
    export FLASK_DEBUG=1
    export PYTHONPATH=`pwd`:$PYTHONPATH
    python3 logic/channel_logic.py &
    sleep 2
    python3 speech_recog/recognition.py &
    sleep 2
    python3 emotion_detection/webcam_recognition.py &
    sleep 2
    python3 ui/ui_setup.py
    killall -9 redis-server
}

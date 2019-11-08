import speech_recognition as sr
import TTS.wrapper as w


def get_mic(mic_name):
    """
    Get the index of the given microphone in our list of microphones.
    If it's not found, instead set the index to be the first microphone found.
    :param mic_name: The given name of the microphone to get
    :return: The microphone index.
    """
    mic = sr.Microphone # (sample_rate=44100, chunk_size=4096)
    mic_list = mic.list_microphone_names()
    print("Microphone List:")
    print(mic_list)
    to_return = -1
    for i in range(0, len(mic_list)):
        mic_entry = mic_list[i]
        if mic_entry[:len(mic_name)] == mic_name:
            return i
        elif mic_entry[:10] == 'Microphone' and to_return == -1:
            to_return = i
    print(to_return)
    return to_return


def get_text(mic_obj):
    """
    Recognize the phrase said into the mic using a Google Speech API
    :param mic_obj: The microphone object we're using as the input audio fee
    :return: The phrase the user said.
    """
    recog = sr.Recognizer()
    # recog.energy_threshold = 600
    with mic_obj as mic:
        print("Say something")
        data = recog.listen(mic, phrase_time_limit=1.5)
    print("Got mic phrase")
    text = recog.recognize_google(data)
    print(text)
    return text


def main():
    # Microphone we're using
    # **Replace this with the name of your mic (trimmed if needed)**
    mic_name = "Microphone (Realtek High Defini"

    # Run the process
    mic_ind = get_mic(mic_name)
    mic_obj = sr.Microphone(device_index=mic_ind)
    text = get_text(mic_obj)
    w.audio_input_process_wrapper(text)
    return

main()

import speech_recognition as sr


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


def get_text(mic_obj, keyword_entries=None):
    """
    Recognize the phrase said into the mic
    :param mic_obj: The microphone object we're using as the input audio feed
    :param keyword_entries: The entries we're using to get phrases from.
                            Set to None by default, so that it pulls from all English words.
    :return: The phrase the user said.
    """
    recog = sr.Recognizer()
    # recog.energy_threshold = 600
    with mic_obj as mic:
        print("Say something")
        data = recog.listen(mic, phrase_time_limit=1.5)
    print("Got mic phrase")
    text = recog.recognize_sphinx(data, keyword_entries=keyword_entries)
    print(text)
    return text


def main():
    # Microphone we're using
    mic_name = "Microphone (Realtek High Defini"

    # Set up the phrases we're using if desired
    # Commented out because it was creating weird results before.
    """
    phrases = ["yes", "no", "help", "happy", "sad", "video"]
    sensitivity = 0
    keyword_entries = []
    for phrase in phrases:
        keyword_entries.append((phrase, sensitivity))
    print(keyword_entries)
    """
    keyword_entries = None
    # Run the process
    mic_ind = get_mic(mic_name)
    mic_obj = sr.Microphone(device_index=mic_ind)
    text = get_text(mic_obj, keyword_entries)
    print("Given response: " + text)
    return

main()

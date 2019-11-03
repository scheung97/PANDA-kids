#import libraries
import pyttsx3 as tts
import time

#initialisation
"""
Defaults to best available drive.
Options:
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on MAC OS # X
espeak - all other platforms
"""
def Speech(output):
    engine = tts.init()


    #phrase = input("Enter phrase for Text2Speech: ") #replace with response from speech2text work

    """Voices

    can update age, gender, languages, name
    """

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #male voice
    #engine.setProperty('voice', voices[1].id) #female voice

    """Rate

    """
    #rate = engine.getProperty('rate')
    #engine.setProperty('rate', 60) #speech rate

    """Volume"""
    #volume = engine.getProperty('volume')
    #engine.setProperty('volume', 25) #volume level

    print(output)
    engine.say(output)
    engine.runAndWait()
    time.sleep(1) #program waits for x-amount of seconds
    engine.stop()

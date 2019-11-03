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
def Speech(*argv): #*argv = multiple inputs (do we need multiple inputs??) 
    for text in argv:
        engine = tts.init()

        #phrase = input("Enter phrase for Text2Speech: ") #replace with response from speech2text work

        """Voices

        can update age, gender, languages, name
        """

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) #male voice
        #engine.setProperty('voice', voices[1].id) #female voice

        """Rate

        speech rate
        """
        #rate = engine.getProperty('rate')
        #engine.setProperty('rate', 60) #speech rate

        """Volume

        volume level of speech
        """
        #volume = engine.getProperty('volume')
        #engine.setProperty('volume', 25) #volume level

        print(text) #for error checking
        engine.say(text)
        engine.runAndWait()

    time.sleep(1) #program waits for x-amount of seconds
    engine.stop()

#import library
import pyttsx3 as tts
import time

#initialisation
system = tts.init()

phrase = input("Enter phrase for Text2Speech: ") #replace with response from speech2text work

"""Voices"""
voices = system.getProperty('voices')
system.setProperty('voice', voices[0].id) #male voice
#system.setProperty('voice', voices[1].id) #female voice

"""Rate"""
#rate = system.getProperty('rate')
#system.setProperty('rate', 60) #speech rate

"""Volume"""
#volume = system.getProperty('volume')
#system.setProperty('volume', 25) #set volume

print(phrase)
system.say(phrase)
system.runAndWait()
time.sleep(2)
system.stop()

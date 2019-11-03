"""Pseudocode for handling things"""
import twilio_work as tw
import tts


"""
@param speech2text.input   result of speech2text process

@returns twilio           text or text to speech prompt
@returns speech           audio output of tts code
"""

def audio_input_process_wrapper(input): #speech2text.input):
    try:
        #replace with function objects
        if (input == 'help'):
            print("twilio")
            #tw.twilio_work('Help required')
        elif(input == 'bored'):
            print("tts")
            tts.Speech('Would you like to watch a video?')
        else:
            print('neither')

    except:
        print('error detected')

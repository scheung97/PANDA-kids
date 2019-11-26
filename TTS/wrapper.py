"""Pseudocode for handling things"""
#import TTS.twilio_work as tw
import TTS.tts as tts


"""
@param speech2text.input   result of speech2text process

@returns twilio           text or text to speech prompt
@returns speech           audio output of tts code
"""

def audio_input_process_wrapper(input): #speech2text.input):
    #try:
        #replace with function objects
        if input.__contains__('help'):
            print("twilio")
            tw.twilio('Help required')
        elif input.__contains__('bored'):
            print("tts")
            tts.Speech('Would you like to watch a video?')
        else:
            print('neither')
    except Exception as e:
        print('error detected: {}'.format(e))

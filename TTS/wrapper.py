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
        switch(input){
            case'help':
                print("twilio")
                #tw.twilio_work('Help required')
            case 'bored':
                print("tts")
                tts.Speech('Would you like to watch a video?')
            default:
                print('neither')
            }
    except:
        print('error detected')

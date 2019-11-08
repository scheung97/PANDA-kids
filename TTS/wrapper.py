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
<<<<<<< HEAD
        if input.__contains__('help'):
            print("twilio")
            #tw.twilio_work('Help required')
        elif input.__contains__ ('bored'):
            print("tts")
            tts.Speech('Would you like to watch a video?')
        else:
            print('neither')

=======
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
>>>>>>> c02385faa595f20d74f7dd9f8a1e307c6c31e213
    except:
        print('error detected')

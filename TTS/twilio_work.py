from twilio.rest import Client

def twilio(text_content):
    account_sid = 'AC9e086a1bb6fe2cc10891a5f544f02c44'
<<<<<<< HEAD
    auth_token = '703fbb843f0b04ebceb5f7cd6efe6916' #don't make this public
=======
    auth_token = XXXXXXXXXXXXXXX #get twilio key from site
>>>>>>> b3593361748a8394e4e0dc5e1c3b4cfeda42102a
    client = Client(account_sid, auth_token)

    #text_content = text_message

    message = client.messages.create(
                                  from_='+17172832424',
                                  to='+18573030125',
                                  body= text_content
                              )

    #print(message.sid)
    print(text_content)

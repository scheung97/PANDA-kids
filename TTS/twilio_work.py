from twilio.rest import Client

def twilio(text_content):
    account_sid = 'AC9e086a1bb6fe2cc10891a5f544f02c44'
    auth_token = '22a64710613f78922fa9979313efe373' #don't make this public
    client = Client(account_sid, auth_token)

    #text_content = text_message

    message = client.messages.create(
                                  from_='+17172832424',
                                  to='+18573030125',
                                  body= text_content
                              )

    #print(message.sid)
    print(text_content)

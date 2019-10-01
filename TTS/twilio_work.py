from twilio.rest import Client

account_sid = 'AC9e086a1bb6fe2cc10891a5f544f02c44'
auth_token = '[Auth Token]' 
client = Client(account_sid, auth_token)

text_content = 'Spenser is baby and needs your help'

message = client.messages.create(
                              from_='+17172832424',
                              to='+19082297439',
                              body= text_content 
                          )

print(message.sid)

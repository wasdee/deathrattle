from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC04317ad3070ade6116edca682096209e"
# Your Auth Token from twilio.com/console
auth_token  = "824e5400c8380c7844ab0bdf708aed41"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+66992866936", 
    from_=''.join("+1 240 743 2139".split()),
    body="Hello from Python!")
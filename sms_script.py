from twilio.rest import TwilioRestClient

test = True
account = "ACa9da0578d7e255ad317b5c1771ce18f3"
test_account = "ACf145369caae51d6d46198e06d5a76cf8"
token = "2d7b7fcdc00ce77d1e3b7a6b04a1e8c2"
test_token = "fa1d49bce50cfa51ec5f1aa4f09199ee"
if test:
    client = TwilioRestClient(test_account, test_token)
else:
    client = TwilioRestClient(account, token)

message = client.messages.create(to="+972526019037", from_="+97254-372-9006",
                                             body="Hello there!, you are on avocado duty.")

# curl -X POST http://textbelt.com/text  -d number=972526019037  -d "message=I sent this message for free with textbelt.com"
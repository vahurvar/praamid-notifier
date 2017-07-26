from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "sid"
# Your Auth Token from twilio.com/console
auth_token = "token"

client = Client(account_sid, auth_token)


def send_message(list_trips):
    client.messages.create(
        to="fill",
        from_="fill",
        body=get_message_string(list_trips))


def get_message_string(list_trips):
    ans = "Free spots available for following trips:\n\n"
    for trip in list_trips:
        ans += trip + "\n"
    ans += "Hurry up to https://www.praamid.ee"
    return ans

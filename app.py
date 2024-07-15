from flask import Flask
from twilio.rest import Client
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
# A .env file is a simple text file used to store environment variables in key-value pairs. These files are commonly used in development environments to keep configuration values such as database credentials, API keys, and other sensitive information out of your source code. Using a .env file helps in separating configuration from the codebase and provides a way to manage environment-specific settings.
load_dotenv()

# Retrieve Twilio credentials from environment variables
# A client instance in the context of APIs like Twilio or Azure refers to an object that acts as a gateway to interact with the respective services. It is a part of the SDK (Software Development Kit) provided by these services and abstracts the underlying complexity, making it easier to perform operations such as sending messages, managing storage, etc.
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

# Initialize Twilio client
client = Client(account_sid, auth_token)

@app.route("/", methods=['GET'])
def make_outbound_call():
    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to="+6597487943",
        from_="+12512921238"
    )
    print(call.sid)
    return "Outbound call initiated"

if __name__ == "__main__":
    app.run(debug=True)

#Currently hosted on a local network, must be hosted globally
#Must be able to change phone number
#Must have dialogue and a timeout
#Make notes
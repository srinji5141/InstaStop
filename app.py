from flask import Flask
from twilio.rest import Client
from dotenv import load_dotenv
import os
from twilio.twiml.voice_response import VoiceResponse, Say

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
        url="https://hello-voice-5480-udkzsk.twil.io/sacrifice", #Check out Twilio studio
        to="+6597487943",
        from_="+12512921238"
    )
    print(call.sid)
    return "Outbound call initiated"

if __name__ == "__main__":
    app.run(debug=True)

#Must host globally
#Must call only while opening
#Get the dialogue to work
#https://console.twilio.com/us1/service/functions/ZSf4b7b4c367e67255adcf6c916b6cf8de/runtime-functions-editor?frameUrl=%2Fconsole%2Ffunctions%2Feditor%2FZSf4b7b4c367e67255adcf6c916b6cf8de%2Fenvironment%2FZE0460a2fe0be41b8fa13888b09d372c8a%2Fconfig%2Fvariables%3Fapp_title%3Dhello-voice%26x-target-region%3Dus1&currentFrameUrl=%2Fconsole%2Ffunctions%2Feditor%2FZSf4b7b4c367e67255adcf6c916b6cf8de%2Fenvironment%2FZE0460a2fe0be41b8fa13888b09d372c8a%2Ffunction%2FZHb9555efe3ebd432e74bad943d7b1b79f%3F__override_layout__%3Dembed%26bifrost%3Dtrue%26x-target-region%3Dus1
#Must be able to download shortcut, change phone number
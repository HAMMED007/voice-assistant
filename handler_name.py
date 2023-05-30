import user_takecommand
from main import speak


def username():
    speak("What should I call you sir?")
    uname = user_takecommand.takeCommand()
    speak("Welcome " + uname)
    global assistant_name
    assistant_name = "Cherry"  # Change the name of the assistant here
    speak("How can I help you " + uname)

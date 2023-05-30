import datetime

import pyttsx3


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        pyttsx3.speak("Good Morning Sir !")
    elif 12 <= hour < 18:
        pyttsx3.speak("Good Afternoon Sir !")
    else:
        pyttsx3.speak("Good Evening Sir !")
    ass_name = "my name is cherry"
    pyttsx3.speak("I am your Assistant")
    pyttsx3.speak(ass_name)

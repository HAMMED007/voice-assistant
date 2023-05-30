import speech_recognition as sr


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        confidence = r.recognize_google(audio, show_all=True)['alternative'][0]['confidence']
        if confidence < 0.7:
            raise sr.UnknownValueError
    except sr.UnknownValueError:
        print("Voice not recognized.")
        return "None"
    except Exception as e:
        print(e)
        print("Unable to recognize your voice.")
        return "None"
    return query

import speech_recognition as sr
from engine.features import openCommand, playYoutube, findContact, whatsApp, makeCall, sendMessage, capture, video
from engine.voice import speak

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        speak("Say that again please...")
        return ""

def allcommand():
    query = takecommand()
    if "send message" in query or "phone call" in query or "video call" in query:
        flag = ""
        contact_no, name = findContact(query)
        if contact_no != 0:
            speak("Which mode you want to use whatsapp or mobile")
            preferance = take()
            print(preferance)
            if "mobile" in preferance:
                if "send message" in query or "send sms" in query:
                    speak("what message to send")
                    message = take()
                    sendMessage(message, contact_no, name)
                elif "phone call" in query:
                    makeCall(name, contact_no)
                else:
                    speak("please try again")
            elif "whatsapp" in preferance:
                message = ""
                if "send message" in query:
                    message = 'message'
                    speak("what message to send")
                    query = takecommand()

                elif "phone call" in query:
                    message = 'call'
                else:
                    message = 'video call'

                whatsApp(contact_no, query, message, name)

    elif "open" in query:
        openCommand(query)
    elif "on youtube" in query:
        playYoutube(query)
    elif "capture photo" in query:
        capture()
    elif "capture video" in query:
        speak("Time to capture video")
        x = take()
        video(x)
    else:
        speak("Sorry, I don't understand that")

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 5,
                         6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        speak("Say that again please...")
        return ""
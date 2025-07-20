from shlex import quote
import subprocess
from engine.voice import speak
from engine.db_utils import get_connection
import pywhatkit as kit
import sqlite3
import webbrowser
import pyautogui
from engine.helper import extract_yt_term, replace_spaces_with_percent_s, goback, keyEvent, tapEvents, adbInput
import os
import time

con = sqlite3.connect('database.db')
cur = con.cursor()

def openCommand(query):
    query = query.replace("open", "").strip().lower()
    app_name = query

    if not app_name:
        speak("App name not found.")
        return

    try:
        with get_connection() as con:
            cur = con.cursor()

            # Check for system app
            cur.execute("SELECT path FROM sys_command WHERE LOWER(name) = ?", (app_name,))
            result = cur.fetchone()
            if result:
                speak(f"Opening {app_name}")
                os.startfile(result[0])
                return

            # Check for website
            cur.execute("SELECT path FROM web_command WHERE LOWER(name) = ?", (app_name,))
            result = cur.fetchone()
            if result:
                speak(f"Opening {app_name}")
                webbrowser.open(result[0])
                return

        # Fallback
        speak(f"Opening {app_name}")
        os.system("start " + app_name)

    except Exception as e:
        speak("Something went wrong.")
        print("❌ Error:", e)


def playYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Could not understand what to play on YouTube.")


def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string


# Whatsapp Message Sending
def findContact(query):
    words_to_remove = ['make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)

    try:
        query = query.strip().lower()
        cur.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
                       ('%' + query + '%', query + '%'))
        results = cur.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0


def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 12
        jarvis_message = "message send successfully to " + name

    elif flag == 'call':
        target_tab = 7
        message = ''
        jarvis_message = "calling to " + name

    else:
        target_tab = 6
        message = ''
        jarvis_message = "staring video call with " + name

    # Encode the message for URL
    encoded_message = quote(message)

    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(jarvis_message)

def makeCall(name, mobileNo):
    mobileNo =mobileNo.replace(" ", "")
    speak("Calling "+name)
    command = 'adb shell am start -a android.intent.action.CALL -d tel:'+mobileNo
    os.system(command)

# to send message
def sendMessage(message, mobileNo, name):
    message = replace_spaces_with_percent_s(message)
    mobileNo = replace_spaces_with_percent_s(mobileNo)
    speak("sending message")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open sms app
    tapEvents(730, 2950)
    #start chat
    tapEvents(1100, 2900)
    # search mobile no
    adbInput(mobileNo)
    #tap on name
    tapEvents(430, 770)
    # tap on input
    tapEvents(430, 2960)
    #message
    adbInput(message)
    #send
    tapEvents(1310, 1990)
    speak("message send successfully to "+name)

def capture():
    speak("Capturing photo")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open cam app
    tapEvents(1250, 2950)
    # tap to capture
    tapEvents(700, 2750)
    speak("Captured photo")

def video(x):
    speak("Capturing video")
    goback(4)
    time.sleep(1)
    keyEvent(3)
    # open cam app
    tapEvents(1250, 2950)
    # move to video option
    tapEvents(454, 2450)
    # tap to start video
    tapEvents(720, 2730)
    # time to take video
    time.sleep(x)
    # tap to end video
    tapEvents(720, 2730)
    speak("Captured video")

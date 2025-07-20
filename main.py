from engine.auto_adb import connect_device
from engine.voice import speak
from engine.command import allcommand

if __name__ == "__main__":
    if not connect_device():  # You can pass IP if needed
        speak("Could not connect to mobile. Exiting.")
        exit()

    speak("Mobile connected successfully. Ready for commands.")
    allcommand()

import queue
import sounddevice as sd
import vosk
import subprocess
import json
import os

model_path = "model/vosk-model-small-en-us-0.15"

if not os.path.exists(model_path):
    print("❌ Vosk model not found!")
    exit()

model = vosk.Model(model_path)
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print("⚠️", status)
    q.put(bytes(indata))

def listen_for_wake_word():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("🔊 Listening for 'jarvis'...")

        rec = vosk.KaldiRecognizer(model, 16000)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                print(f"🗣️ Heard: {text}")

                if "jarvis" in text:
                    print("🚀 Wake word detected! Launching main.py...")
                    subprocess.Popen(["python", "main.py"])
                    break  # Remove this line if you want it to stay running

if __name__ == "__main__":
    listen_for_wake_word()

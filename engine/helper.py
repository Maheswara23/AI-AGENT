import re
import os
import time

def extract_yt_term(query):
    """
    Extracts the content between 'play' and 'on YouTube' from voice query.
    Example: 'play rrr on YouTube' → 'rrr'
    """
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, query, re.IGNORECASE)
    return match.group(1).strip() if match else None

# key events like receive call, stop call, go back
def keyEvent(key_code):
    command =  f'adb shell input keyevent {key_code}'
    os.system(command)
    time.sleep(1)

# Tap event used to tap anywhere on screen
def tapEvents(x, y):
    command =  f'adb shell input tap {x} {y}'
    os.system(command)
    time.sleep(1)

# Input Event is used to insert text in mobile
def adbInput(message):
    command =  f'adb shell input text "{message}"'
    os.system(command)
    time.sleep(1)

# to go complete back
def goback(key_code):
    for i in range(6):
        keyEvent(key_code)

# To replace space in string with %s for complete message send
def replace_spaces_with_percent_s(input_string):
    return input_string.replace(' ', '%s')
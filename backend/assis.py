import subprocess
import datetime
import webbrowser
import os
import pyjokes # type: ignore
import ctypes
# import requests
import json
import random
# import pywhatkit
# from urllib.request import urlopen


def wishMe():
    """Function to wish the user based on current time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        greet = "Good Morning Sir!"

    elif 12 <= hour < 18:
        greet = "Good Afternoon Sir!"

    else:
        greet = "Good Evening Sir!"

    assname = "Friday"
    return f"{greet} I am your Assistant {assname}. How can I help you, Sir?"


def choice(query):
    query = query.lower()
    greetings = [
    "Hello",
    "Hi there",
    "Hey",
    "Good morning",
    "Good afternoon",
    "Good evening",
    "Greetings",
    "Howdy",
    "Nice to see you",
    "Hiya",
    "What's up",
    "how are you",
    " how's it going",
    "Yoo",
    "Hii",
    "good to see you",
    "what's happening",
    "Hi there, how can I help you",
    "Hello there",
    "Hi, nice to meet you",
    "hi",
    "Hi"
    ]
    for greeting in greetings:
        if greeting.lower() in query:
            return "Hello How can i help you"
            
    if "open youtube" in query:
        webbrowser.open("https://www.youtube.com")
        return "Here you go to Youtube"

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Here you go to Google"

    elif "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Here you go to Google"

    elif "open stackoverflow" in query:
        webbrowser.open("https://stackoverflow.com")
        return "Here you go to Stack Overflow. Happy coding!"

    elif any(keyword in query for keyword in ["play music", "play song"]):
        music_dir = "S:\\Music\\ShareMe\\SnapTube Audio\\Alexander rybak - fairy tale (lyrics) trending song(MP3_320K).mp3"
        songs = os.listdir(music_dir)
        random_song = os.startfile(os.path.join(music_dir, random.choice(songs)))
        return "Here you go with music"

    elif "open" in query:
        sub = query.split("open ")[-1]
        sub = sub.replace("%20", "").replace(" ", "")
        url = f"http://www.{sub}"
        webbrowser.open(url)
        return "Opening, sir"

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Sir, the time is {strTime}"

    elif "open browser" in query:
        codePath = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk"
        os.startfile(codePath)
        return "Opening browser"

    elif "how are you" in query:
        return "I am fine, Thank you. How are you, Sir?"

    elif any(greeting in query.lower() for greeting in ["fine", "good"]):
        return "It's good to know that you're fine"

    elif "change my name to" in query:
        global assname
        assname = query.replace("change my name to", "").strip()
        return f"Thanks for naming me {assname}"

    elif any(question in query.lower() for question in ["what's your name", "what is your name"]):
        return f"My friends call me {assname}"

    elif any(question in query.lower() for question in ["who made you", "who created you"]):
        return "I have been created by Satwik."

    elif "joke" in query:
        return pyjokes.get_joke()

    elif any(keyword in query for keyword in ["search", "play"]):
        query = query.replace("search", "").replace("play", "")
        webbrowser.open(query)
        return "Performing search/play action"

    elif "who i am" in query:
        return "If you talk then definitely you're human."

    elif "why you came to world" in query:
        return "Thanks to Satwik. It's a secret"

    elif "power point presentation" in query:
        power = r"C:\\Users\\satwi\\Documents\\satwik.pptx"
        os.startfile(power)
        return "Opening Power Point presentation"

    elif "is love" in query:
        return "It is the 7th sense that destroys all other senses"

    elif "who are you" in query:
        return "I am your virtual assistant created by Satwik"

    elif "reason for you" in query:
        return "I was created as a minor project by Mister Satwik"

    elif "change background" in query:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper", 0)
        return "Background changed successfully"

    elif "open bluestack" in query:
        appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
        os.startfile(appli)
        return "Opening Bluestacks"

    elif "lock window" in query:
        ctypes.windll.user32.LockWorkStation()
        return "Locking the device"

    elif "shutdown system" in query:
        subprocess.call("shutdown /p /f")
        return "Hold On a Sec ! Your system is on its way to shut down"

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])
        return "Restarting system"

    elif any(keyword in query.lower() for keyword in ["hibernate", "sleep"]):
        subprocess.call("shutdown /h")
        return "Hibernating"

    elif any(keyword in query.lower() for keyword in ["log off", "sign out"]):
        subprocess.call(["shutdown", "/l"])
        return "Logging off"


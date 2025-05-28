import pyttsx3
import os
import pyautogui
import webbrowser
import datetime
from time import sleep

engine=pyttsx3.init("sapi5")
voice=engine.getProperty("voices")
engine.setProperty("voice",voice[0].id)
# print(voice[0])
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"command prompt":"cmd","word":"winword","excel":"excel","chrome":"Chrome","powerpoint":"powerpnt"}
values=dictapp.keys()

def openappweb(query):
    # speak("launching sir")
    if ".com" in query or ".in" in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("jarvis","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://www.{query}")

    else:
        # keys=list(dictapp.keys())
        for app in values:
            if app in  query:
                os.system(f"start {dictapp[app]}")

def closappweb(query):
    # speak("closing sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "two tab" in query or "2 tabs" or "to tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        # speak("two tabs closed")

    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f'taskkill /f /im {dictapp[app]}.exe')



# def shutdown(query):
#     if "shut down the system" in query:
#         speak("shutting down the system")
#         pyautogui.hotkey("windows","x","u","u")







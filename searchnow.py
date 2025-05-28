import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
# from bs4 import BeautifulSoup
def takecommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,5)
    try:
        print("understanding...")
        query=r.recognize_google(audio)
        print(query)

    except Exception as e:
        print("say that again...")
        return 'None'
    
    return query

query=takecommand().lower()

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    pass

        

def searchyoutube(query): 
    pass

   
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import streamlit as st

# Initialize pyttsx3 globally
st.write("initalization takes some time")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
    """Function to speak text"""
    engine.say(text)
    engine.runAndWait()

def takecommand():
    """Function to recognize speech"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        st.write("Listening...")

        try:
            audio = r.listen(source, timeout=5)
        except Exception:
            print("Please speak within timeout '5 seconds'")
            return "None"

    try:
        print("Understanding...")
        st.write("Understanding...")
        query = r.recognize_google(audio)
        print("you said :"+query)
        st.write("you said :"+query)
        return query.lower()
    except sr.UnknownValueError:
        print("Couldn't recognize speech.")
        return "None"

if __name__ == "__main__":
    st.title('Voice assistant')
    speak("Hello! Voice assistant activated.")

    while True:
        query = takecommand()
        if "activate" in query:
            speak("How can I help you?")
            print("How can I help you?")
            st.write("How can I help you?")
            while True:
                query = takecommand()
                if "ok jarvis sleep now" in query:
                    speak("Call me whenever you need.")
                    st.write("Call me whenever you need.")
                    break
                elif "hello" in query:
                    speak("Hello, how are you?")
                    st.write("Hello, how are you?")
                elif "google search" in query:
                    search_term = query.replace("google search", "").strip()
                    webbrowser.open(f"https://www.google.com/search?q={search_term}")
                elif "youtube search" in query:
                    search_term = query.replace("youtube search", "").strip()
                    pywhatkit.playonyt(search_term)
                elif "what's the time now" in query:
                    strtime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strtime}")
                    st.write(f"The time is {strtime}")
                elif "turn off" in query:
                    speak("Have a great day! Turning off.")
                    print("Turned off!")
                    st.write("Turned off!")
                    exit()
                elif "open" in query: 
                    from apps import openappweb 
                    openappweb(query) 
                elif "close" in query: 
                    from apps import closappweb 
                    closappweb(query)
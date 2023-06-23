import os

import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime

speaker = win32com.client.Dispatch("SAPI.spVoice")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"Darshan said: {query}")
            return query
        except Exception as e:
            return "Sorry Could You Repeat That I Didn't catch that"


speaker.speak("Good Evening Mr. Darshan, i am Jarvis At Your Service, what can i do for you?")
while True:
    print("Listening")
    query = takeCommand()
    # speaker.Speak(query)
    sites = [["Youtube", "https://youtube.com"], ["Wikipedia", "https://wikipedia.com"], ["Google", "https://google.com"] ]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.speak(f"Opening {site[0]}, Mr. Darshan")
            webbrowser.open(site[1])
    if "open music"in query:
        musicpath = "C:/Users/Learnvern/PycharmProjects/ai/song.mp3"
        os.startfile(musicpath)
    if "Time".lower() in query.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.speak(f"Sir The Time Is{time}")


    # elif "Open Google".lower() in query.lower():
    #     speaker.Speak("Opening Google, Mr. Darshan")
    #     webbrowser.open("https://www.google.com")
    # elif "Open Zoom".lower() in query.lower():
    #     speaker.Speak("Opening Zoom, Mr. Darshan")
    #     webbrowser.open("https://us05web.zoom.us/j/7632297551?pwd=bUhzMHM0L1BpUjQxYmM4UVVPSUZCZz09")

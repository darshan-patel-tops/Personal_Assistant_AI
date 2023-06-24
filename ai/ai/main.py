import os
import random
import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import os
import datetime
from config import apikey

speaker = win32com.client.Dispatch("SAPI.spVoice")

chats = ""
def chat(query):
    global chats
    # print(chats)
    openai.api_key = apikey
    chats += f"Darshan:{query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chats,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        speaker.speak(response["choices"][0]["text"])
        # text += response["choices"][0]["text"]
        chats += f"{response['choices'][0]['text']}\n"
        return response["choices"][0]["text"]
        # if not os.path.exists("ai files"):
        #     os.mkdir("ai files")

        # with open(f"ai files/prompt- {random.randint(1,999999999)}", "w")as f:
        with open(f"ai files/{''.join(query.split('Jarvis')[1:]).strip()}.txt", "w") as f:
             f.write(query)

        speaker.speak(response["choices"][0]["text"])
    except Exception as e:
        # speaker.speak("Sorry Could You Repeat That I Didn't catch that")
        return "Sorry Could You Repeat That I Didn't catch that"

def ai(prompt):
    openai.api_key = apikey
    text = f"AI Response:{prompt}\n\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("ai files"):
            os.mkdir("ai files")

        # with open(f"ai files/prompt- {random.randint(1,999999999)}", "w")as f:
        with open(f"ai files/{''.join(prompt.split('Jarvis')[1:]).strip()}.txt", "w")as f:
            f.write(text)

        speaker.speak(response["choices"][0]["text"])
    except Exception as e:
        # speaker.speak("Sorry Could You Repeat That I Didn't catch that")
        return "Sorry Could You Repeat That I Didn't catch that"


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
            # speaker.speak("Sorry Could You Repeat That I Didn't catch that")
            return "Sorry Could You Repeat That I Didn't catch that"


speaker.speak("Good Evening Mr. Darshan, i am Jarvis At Your Service, what can i do for you?")
while True:
    print("Listening")
    query = takeCommand()
    # speaker.Speak(query)
    sites = [["Youtube", "https://youtube.com"], ["Wikipedia", "https://wikipedia.com"],
             ["Google", "https://google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.speak(f"Opening {site[0]}, Mr. Darshan")
            webbrowser.open(site[1])
    if "open music" in query:
        musicpath = "C:/Users/Learnvern/PycharmProjects/ai/song.mp3"
        os.startfile(musicpath)
    elif "Time".lower() in query.lower():
        time = datetime.datetime.now().strftime("%H Hours %M Minutes %S Seconds")
        speaker.speak(f"Sir The Time Is{time}")
    elif "Jarvis".lower() in query.lower():
        ai(prompt=query)
    elif "see you later".lower() in query.lower():
        exit()
    elif "Reset".lower() in query.lower():
        chats = ""

    else:
        print("Talking")
        chat(query)
        print("Talking later")


    # elif "Open Google".lower() in query.lower():
    #     speaker.Speak("Opening Google, Mr. Darshan")
    #     webbrowser.open("https://www.google.com")
    # elif "Open Zoom".lower() in query.lower():
    #     speaker.Speak("Opening Zoom, Mr. Darshan")
    #     webbrowser.open("https://us05web.zoom.us/j/7632297551?pwd=bUhzMHM0L1BpUjQxYmM4UVVPSUZCZz09")

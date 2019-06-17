from gtts import gTTS
import playsound
import speech_recognition as sr
import time
from time import ctime
import os
import webbrowser
import sys

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    playsound.playsound("audio.mp3",True)
    os.remove("audio.mp3")

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)

        data = ""
        try:
            data = r.recognize_google(audio)
            print("You Said: " + data)
        except sr.UnknownValueError:
            print("Alice Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request result from Alexa Speech Recognition Service; {0}".format(e))

        return data

def alice(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[1]
        speak("Hold on Eric, I will show you where " + location + " is .")
        webbrowser.open("https://www.google.com/maps/place/" + location + "/&amp;")

    if "open browser" in data:
        webbrowser.open("https://www.google.com")

    if "open YouTube" in data:
        webbrowser.open("https://www.youtube.com")

    if "open Facebook" in data:
        webbrowser.open("https://www.facebook.com")

    if "hello Alice" in data:
        speak("Hello")

    if "what is your name" in data:
        speak("My Name is Alice, iam a Virtual Assistant")

    if "thank you" in data:
        speak("Your Welcome")

    if "good morning" in data:
        speak("Good Morning")

    if "good night" in data:
        speak("Good Night")

    if "goodbye" in data:
        speak("Ok goodbye")
        sys.exit()

    if "open Steam" in data:
        speak("Ok Open Steam")
        os.startfile('C:\\Program Files (x86)\Steam\Steam.exe')

time.sleep(2)
speak("Hi Eric, what can I do for you?")
while 1:
    data = recordAudio()
    alice(data)

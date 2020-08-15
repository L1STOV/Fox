import speech_recognition as sr
import datetime
import webbrowser
import time
from gtts import gTTS
import playsound
import os
import random

r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            fox_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            fox_speak("Sorry, didn't get that")
        except sr.RequestError:
            fox_speak("Check your Internet connection")
        return voice_data


def fox_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    now = datetime.datetime.now()
    if 'what is your name' in voice_data:
        fox_speak("My name is Fox")
    if 'what time is now' in voice_data:
        fox_speak("Now " + str(now.hour) + ":" + str(now.minute))
    if 'what date is today' in voice_data:
        fox_speak("Today is " + str(now.day) + " of " + str(now.month))
    if 'search' in voice_data:
        search = record_audio("What do you want to search")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        fox_speak("Here is what i found for " + search)
    if 'find location' in voice_data:
        location = record_audio("What's the location")
        url = "https://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        fox_speak("Here is the location " + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
fox_speak("How can i help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)

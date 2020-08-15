import speech_recognition as sr
import datetime
import webbrowser
import time
from gtts import gTTS
import playsound
import os
import random

r = sr.Recognizer()


def words_exists(options):
    for opt in options:
        if opt in voice_data:
            return True


def record_audio(ask=False):
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
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
        print(f">> {voice_data.lower()}")
        return voice_data


def fox_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    ran = random.randint(1, 10000000)
    audio_file = 'audio-' + str(ran) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    now = datetime.datetime.now()
    if words_exists(['what is your name', 'please remember your name', 'your name is', 'remember your name']):
        fox_speak("My name is Fox")

    if words_exists(['what time is now', 'current time', 'what time', 'whats the time now']):
        fox_speak("Now " + str(now.hour) + " hours " + str(now.minute) + " minutes")

    if 'what date is today' in voice_data:
        fox_speak("Today is " + str(now.day) + " of " + str(now.strftime("%B")))

    if words_exists(['search', 'find', 'search in google', 'find in google']):
        search = record_audio("What do you want to search")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        fox_speak("Here is what i found for " + search)

    if words_exists(['find location', 'find the location', 'i need location']):
        location = record_audio("What's the location")
        url = "https://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        fox_speak("Here is the location " + location)

    if words_exists(['how are you', 'what\'s up', 'whats up', 'how you doing', 'what\'s new', 'whats new']):
        answers = ["I am fine and always ready to work. Let\'s start",
                   "I'm just wonderful. I missed you very much",
                   "Excellent, I am rested and ready to work",
                   "Cool. Today is a great day"
                   ]
        answer = answers[random.randint(0, len(answers)-1)]
        fox_speak(answer)
        
    if 'exit' in voice_data:
        fox_speak("See you soon, master")
        exit()


time.sleep(1)
fox_speak("How can i help you?")
while True:
    voice_data = record_audio()
    respond(voice_data)

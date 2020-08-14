import speech_recognition as sr
import datetime
import webbrowser

r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, didn't get that")
        except sr.RequestError:
            print("Check your Internet connection")
        return voice_data


def respond(voice_data):
    now = datetime.datetime.now()
    if 'what is your name' in voice_data:
        print("My name is Fox")
    if 'what time is now' in voice_data:
        print("Now " + str(now.hour) + ":" + str(now.minute))
    if 'what date is today' in voice_data:
        print("Today is " + str(now.day) + " of " + str(now.month))
    if 'search' in voice_data:
        search = record_audio("What do you want to search")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Here is what i found for " + search)
    if 'find location' in voice_data:
        location = record_audio("What's the location'")
        url = "https://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        print("Here is the location " + location)


print("How can i help you?")
voice_data = record_audio()
respond(voice_data)

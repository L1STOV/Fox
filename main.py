import speech_recognition as sr

r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:
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
    if 'what is your name' in voice_data:
        print("My name is Fox")


print("How can i help you?")
voice_data = record_audio()
respond(voice_data)

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Listening...")
    # record audio data for 5 seconds
    audio_data = r.record(source, duration=5)
    print("Processing...")
    # convert speech to text
    text = r.recognize_google(audio_data, language="ru-RU")
    print(text)

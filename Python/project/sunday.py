import wikipedia
import pyttsx3
import speech_recognition
import pywhatkit

engine = pyttsx3.init()
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    speak("My name is veronica ai , i am here to assist you")
    print("Listining...")
    audio = r.listen(source)
    print("Understanding...")
    query = r.recognize_google(audio)
    print(query)
    speak(query)
    a = wikipedia.summary(query)
    print(a) 
    speak(a)
    # if "google in query" in query:
    #     pywhatkit.search("What is Bgmi")

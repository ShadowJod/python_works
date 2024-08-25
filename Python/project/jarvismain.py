import webbrowser
import speech_recognition
import pyttsx3

recognizer  = speech_recognition.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ =="__main__":
    speak("Initialising Sunday AI")
    while True:
        
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Listining")
            audio = r.listen(source)

        try:
            command = r.recognize_sphinx(audio)
            print(command)
        except Exception as e:
            print(e)

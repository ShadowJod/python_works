import speech_recognition 
import webbrowser
import pyttsx3
import wikipedia


a = (wikipedia.summary(" what is iron man"))
print(a)

recognizer = speech_recognition.Recognizer()
# while True:
#     try:
#         with speech_recognition.Microphone() as source:
#             print("Say Something Good")
#             audio = recognizer.listen(source)
#              text = recognizer.recognize_google(audio)
#             text = text.lower()

#             print(f"Recoginized text :{text}")            

#     except:
#         print("You were trying to funny")
#         recognizer = speech_recognition.Recognizer()
#         continue

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak(a)

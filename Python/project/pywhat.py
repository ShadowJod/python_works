import pywhatkit
import pyttsx3 
import speech_recognition


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("listining....")
    audio = r.listen(source)
    print("Understanding...")
    query = r.recognize_google(audio)
    print(f" seraching{query} on Google")
    speak(f" seraching {query} on Google")
    # pywhatkit.playonyt(query)
    pywhatkit.search(query)





# # # pywhatkit.sendwhatmsg("8700883040", "Hi")

# pywhatkit.sendwhatmsg_to_group_instantly("Bhai log 🫂🦾", "Prince ki ma ka bhosda")
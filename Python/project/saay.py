import pyttsx3 

engine = pyttsx3.init()
engine.say(input("Enter your name\n"))
engine.runAndWait()
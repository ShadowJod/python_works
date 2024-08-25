import speech_recognition 

def speechtotext():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index=1) as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)
     
    print("Recoginizng...")
    query = r.recognize_google(audio, language = 'en-in')
    print(f"User said : {query}\n")
    return query

speechtotext()
    


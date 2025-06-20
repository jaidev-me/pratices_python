import functions as f

f.speak("Let me check you are my boss or not. I am opening camera")
valid = f.face_valid()
if valid:
    f.speak("Welcome sir, how can I help you")
    while True:
        query = f.listen()
        print(query)
        if query:
            print(query)
            query = query.lower()
            if "quit" in query or "quite" in query or query == "stop":
                break
            f.speak(f.response(query))
    f.speak("Have a nice day! See you later sir")
else:
    f.speak("Sorry, I can't help you, you are not my boss")

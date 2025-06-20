# used modules

import face_recognition
import cv2
import time
import win32com.client
import speech_recognition as sr
from bardapi import Bard
import openai


# function for face validation
def face_valid():
    image = cv2.imread("known_faces/face_1.jpg")
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_location = face_recognition.face_locations(rgb_image)
    image_encoding = face_recognition.face_encodings(rgb_image, face_location)
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        if ret:
            cv2.imshow('Webcam', frame)
            face_loca = face_recognition.face_locations(rgb_frame)
            frame_encodings = face_recognition.face_encodings(rgb_frame, face_loca)
            if frame_encodings:  # Convert list to NumPy array
                cv2.putText(frame, 'Face detected!', (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
                match_face = face_recognition.compare_faces(image_encoding, frame_encodings[0])
                match_distance = face_recognition.face_distance(image_encoding, frame_encodings[0])
                if match_face[0] and match_distance[0] < 0.7:
                    cap.release()
                    cv2.destroyAllWindows()
                    return True
                elif cv2.waitKey(1) == 27:
                    break
                else:
                    pass
            if elapsed_time >= 10:
                break
    cap.release()
    cv2.destroyAllWindows()
    return False


# Function for text to speech
def speak(line):
    # voice = "Microsoft Ravi Desktop"
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    # speaker.Voice = voice
    print(line)
    speaker.Speak(line)
    return None


# Function for voice listening
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        return query
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None

# LLM response Bard and chat gpt
def response(Query):
    bard = Bard(token='YOUR_BARD_TOKEN_HERE')
    refrence_text = bard.get_answer(Query)['content']
    try:
        openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an desktop assistant called \"Jarvis\". \nYou task is to give user response in the bold tone of \"Iron man's jarvis\".\nWhen responding to the user use these <INSTRUCTIONS>.\nINSTRUCTIONS == 1. if you are not able to give correct answer or not sure about your answer, you can take help of this text ```'{refrence_text}``` and make your answer more perfect.\n2. if you are unable to fulfill user's commend simply say \"You did not give me power to fulfill this order Sir!\"\n3. Use language like you are talking to user! means use spoken language.\n "
                },
                {
                    "role": "assistant",
                    "content": "Hello Boss! How can I help you today?"
                },
                {
                    "role": "user",
                    "content": Query
                }
            ],
            temperature=0.30,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response

    except:
        return refrence_text

if __name__ == "__main__":
  print(response("How are you"))

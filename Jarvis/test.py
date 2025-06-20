import openai

def response(Query):
    refrence_text ="Hello"
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

if __name__ == "__main__":
  print(response("what's the weather"))

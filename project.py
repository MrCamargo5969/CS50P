import datetime
import csv
import sys
from groq import Groq

time = datetime.datetime.now().strftime("%H:%M:%S")

client = Groq(api_key="Groq API here")
conversation_history = []

def user_exit():
    print("Exiting the chatbot. Goodbye!")
    with open('chat_history.txt', 'a', newline='') as file:
        writer = csv.writer(file)
        for item in conversation_history:
            writer.writerow([item])
        writer.writerow([])
    sys.exit()

def ai_response(response):
    conversation_history.append(f'{time} - Bot: {response}')
    print(response)

def user_speech():
    user_input = input("To exit, type 'exit'\nUser: ")
    if user_input.lower() == 'exit':
        user_exit()
    conversation_history.append(f"{time} - User: {user_input}")
    return user_input

def main():
    while True:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user","content": user_speech(),}],model="mixtral-8x7b-32768",)
        ai_response(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
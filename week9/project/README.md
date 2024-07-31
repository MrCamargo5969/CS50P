# ChatBot Home Office
#### GitHub username: MrCamargo5969
#### edX username: Mr_Camargo
#### Video Demo:  <https://youtu.be/e0EKkHwUAWk>
#### Description:
ChatBot Home Office is a Python chatbot project designed to assist users in a remote work environment. This chatbot uses the Groq API to provide automated responses and can store the conversation history.

## Features
- **Main Function (`main`):** The main function that starts the chatbot and maintains interaction with the user.
- **Function `user_exit`:** Function that allows the user to exit the chatbot, saving the conversation history in a CSV file.
- **Function `ai_response`:** Function that processes and displays the chatbot's response.
- **Function `user_speech`:** Function that captures the user's input and adds it to the conversation history.

## Project Files
- **`project.py`:** Contains the main code of the chatbot.
- **`test_project.py`:** Contains unit tests for the project functions.
- **`requirements.txt`:** List of dependencies needed to run the project.
- **`chat_history.txt`:** (Optional) Stores the chatbot's conversation history.

## Design Decisions
- **Use of Groq API:** We chose to use the Groq API due to its ability to provide accurate and fast responses.
- **History Storage:** We decided to store the conversation history in a CSV file to facilitate auditing and tracking user interactions.

## Execution Instructions
1. Install the necessary dependencies listed in `requirements.txt`.
2. Run `project.py` to start the chatbot.
3. Use `test_project.py` to run the tests and ensure that all functions are working correctly.

# Basic Rule-Based Chatbot
# Internship Task 4

def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if user_input == "hello" or user_input == "hi":
        return "Hi! Nice to meet you."
    
    elif user_input == "what's your favorite color":
        return "I like blue. It's a calming color."
    
    elif user_input == "what's the weather like":
        return "I don't have access to real-time weather data, but I hope it's nice where you are!"
    
    elif user_input == "tell me a joke":
        return "Why did the computer go to the doctor? Because it caught a virus!"
    
    elif user_input == "what is python":
        return "Python is a popular programming language known for its simplicity and readability."
    
    elif user_input == "fine":
        return "ok,thanks!"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "what can you do":
        return "I can respond to some basic predefined messages."
    
    elif user_input == "what is used for creating chat bots":
        return "Chatbots can be created using various programming languages and frameworks, including Python, JavaScript, and more."
    
    elif user_input == "what we use the topics in python":
        return "In Python, we can use topics like variables, data types, loops, functions, and libraries to create chatbots."

    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    elif user_input == "thank you":
        return "You're welcome! If you have any more questions, feel free to ask."
    elif user_input == "what is your purpose":
        return "My purpose is to assist users by."
    elif user_input == "im great":
        return "That's wonderful to hear! Keep up the positive vibes!"
    elif user_input == "what about you":
        return "I'm just a chatbot, but I'm here to help you with any questions or information you need."

    else:
        return "Sorry, I don't understand that."



print("=" * 45)
print("          BASIC PYTHON CHATBOT")
print("=" * 45)

print("Type 'bye' to exit the chatbot.\n")

while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower().strip() == "bye":
        break

print("\nChatbot ended. Thank you!")
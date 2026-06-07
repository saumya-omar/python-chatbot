print("Namaste! Welcome to your Chatbot")
print("Type 'bye' to exit")

responses = {
    "hello": "Hii, welcome! How can I help you?",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug makes you better developer",
    "happy": "Great to hear that"
}

def getResponseBot(userQuestion):
    for eachKey in responses:
        if eachKey in userQuestion.lower():
            return responses[eachKey]

    return "I am still learning"

while True:

    userInput = input("Please ask your question: ")

    if "bye" in userInput.lower():
        print("Goodbye!")
        break

    reply = getResponseBot(userInput)

    print("Bot Response:", reply)

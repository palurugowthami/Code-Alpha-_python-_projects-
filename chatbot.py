def chatbot():
    print("🤖 Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")
        elif user == "how are you":
            print("Bot: I'm fine, thank you!")
        elif user == "what is your name":
            print("Bot: I am a simple Python Chatbot.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
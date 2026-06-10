# A program that listens to user input and replies using fixed rules (if-else conditions).

def chatbot():
    print("🤖 Chatbot: Hello! I'm a simple chatbot. How can I help you today? Type 'exit' to stop.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hello! How can I help you?")

        elif user_input in ["how are you", "how are you doing"]:
            print("Chatbot: I'm just code, but I'm doing great!")

        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day 👋")
            break

        elif user_input in ["help"]:
            print("Chatbot: You can say hello, ask my name, ask how I am, or type exit.")

        elif user_input in ["what is your name"]:
            print("Chatbot: I'm a rule-based chatbot.")

        else:
            print("Chatbot: I don't understand that yet.")

chatbot()

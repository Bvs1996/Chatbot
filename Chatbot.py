import random
responses = {
    "Hello": ["Hello","Hi","How are you","How may i Help You"],
    "How are you": ["Iam fine,what about you","doing well"],
    "i need a help": ["Yes,what kind of help do you want","Yes, tell me","Sure,I will help you"],
    "contact": ["9716663111","53567829","945625245"],
    "no response": ["sorry for that, Let me check","I will check with my team"],
    "thanks": ["Thank you","Thanks,Good bye","Thanks, Have a nice day"],
    "default": ["iam not sure","Please reffer to contact"],
    "bye": ["Good Bye","See you later"]
    
}
def chatbot_response (user_input):
    user_input = user_input.lower()
    for key in responses:
        if key.lower() in user_input:
            return random.choice(responses[key])
    return random.choice(responses["danaefault"])

while True:
    user_input = input("you: ")
    if user_input.lower() in ["quit","exit","Bye"]:
        print("chatbot:goodbye")
        break
    print("chatbot:",chatbot_response(user_input))
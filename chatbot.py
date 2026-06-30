from knowledge_base import chatbot_data
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return chatbot_data["greetings"]
    elif "internship" in user_input:
        return chatbot_data["internship_info"]
    elif "benefit" in user_input:
        return chatbot_data["benefits"]
    elif "skill" in user_input:
        return chatbot_data["skills"]
    elif "apply" in user_input:
        return chatbot_data["apply"]
    elif "interview" in user_input:
        return chatbot_data["interview"]
    elif "resume" in user_input:
        return chatbot_data["resume_tips"]
    elif "bye" in user_input:
        return chatbot_data["exit"]
    else:
        return chatbot_data["unknown"]
def start_chatbot():
    print("Internship Help Chatbot is running...")
    print("Type 'bye' to exit")
    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)
        if "bye" in user_input.lower():
            break
start_chatbot()
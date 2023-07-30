import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List


# Load your OpenAI API key
models.OpenAI.api_key = "OPENAI KEY"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Hi my name is Akshay"""




@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1
    user_input = message_history[-1].content.strip().lower()

    openai_instance = models.OpenAI()
    inputVal = ['generate','create']

    if ('generate' in user_input and 'picture' in user_input) or ('create' in user_input and 'picture' in user_input) :
        bot_response = openai_instance.newimage(
        system_prompt=user_input,
    )
    else:
        # # Generate GPT-3.5 Turbo response
        bot_response = openai_instance.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )
    

    return bot_response, state

# import os
# from langchain.schema import HumanMessage, SystemMessage
# from langchain_openai.chat_models import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# # Simple in-memory conversation storage by chat_id (can be replaced with persistent storage)
# memory_store = {}

# def get_message_history_for_chat(chat_id):
#     return memory_store.get(chat_id, [])

# def save_message_history_for_chat(chat_id, messages):
#     memory_store[chat_id] = messages

# def main(chat_id=None, context_id=None):
#     api_key = os.getenv("OPENAI_API_KEY")
#     if not api_key:
#         print({"ok": False, "error": "API key missing."}, 404)
#         return

#     if chat_id is None:
#         print({"ok": False, "error": "chat_id is required."}, 400)
#         return

#     chat = ChatOpenAI(
#         openai_api_key=api_key,
#         model_name="gpt-4o-mini",
#         max_tokens=500
#     )

#     # Load history or start fresh
#     messages = get_message_history_for_chat(chat_id)
#     if not messages:
#         # Add system message only once at the beginning
#         messages.append(SystemMessage(content="You are a helpful assistant."))

#     # Add new user input
#     user_input = "What is LangChain?"
#     messages.append(HumanMessage(content=user_input))

#     try:
#         # Call the model with the full conversation history
#         response = chat.invoke(messages)
#         # Append AI response to history
#         messages.append(response)
#         # Save updated history
#         save_message_history_for_chat(chat_id, messages)

#         print({"ok": True, "chat_id": chat_id, "context_id": context_id, "completion": response.content}, 200)
#     except Exception as e:
#         print({"ok": False, "error": str(e)}, 500)

# if __name__ == "__main__":
#     main(chat_id="chat123", context_id="contextA")


import os
import json
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Simple in-memory conversation storage by chat_id (can be replaced with persistent storage)
memory_store = {}

def get_message_history_for_chat(chat_id):
    return memory_store.get(chat_id, [])

def save_message_history_for_chat(chat_id, messages):
    memory_store[chat_id] = messages

def main(chat_id=None, context_id=None):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(json.dumps({"ok": False, "error": "API key missing."}))
        return

    if chat_id is None:
        print(json.dumps({"ok": False, "error": "chat_id is required."}))
        return

    chat = ChatOpenAI(
        openai_api_key=api_key,
        model_name="gpt-4o-mini",
        max_tokens=500
    )

    # Load history or start fresh
    messages = get_message_history_for_chat(chat_id)
    if not messages:
        messages.append(SystemMessage(content="You are a helpful assistant."))

    # Add new user input
    user_input = input("Enter your message: ") #Run time querry, avoided hard coding 
    messages.append(HumanMessage(content=user_input))

    try:
        response = chat.invoke(messages)
        messages.append(response)
        save_message_history_for_chat(chat_id, messages)
        print(json.dumps({
            "ok": True,
            "chat_id": chat_id,
            "context_id": context_id,
            "completion": response.content
        }))
    except Exception as e:
        print(json.dumps({
            "ok": False,
            "error": str(e)
        }))

if __name__ == "__main__":
    main(chat_id="chat123", context_id="contextA")

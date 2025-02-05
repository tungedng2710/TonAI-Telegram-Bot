'''
Rename this file to configs.py
'''

MODEL_ID = 'TonAI:chatbot'
BOT_USERNAME = "tonai_chat_bot"
with open("bot_token.txt") as txtfile:
   BOT_TOKEN = txtfile.read()
   
LIMITATION = 20
GREETING = """
I'm TonAI Chatbot
"""
from ollama import chat
from ollama import ChatResponse
from sys import exit as ex

def main():
  while True:
    msg = input("What's your request? ")
    if msg.lower().strip() == "quit":
      ex("Thanks")
    print(chatbot(msg))



def chatbot(message=None):
  response: ChatResponse = chat(model='gemma3', messages=[
    {
      'role': 'user',
      'content': message,
    },

  ])
  print(response['message']['content'])
  # or access fields directly from the response object
  print(response.message.content)

if __name__=="__main__":
  main()
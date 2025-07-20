from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Access the API key using os.getenv
api_key = "YA7pNDjejp9DQT6ySuBdBOQSJl5otcmP"

model = "mistral-large-latest"


client = MistralClient(api_key=api_key)

def chat_mistral(prompt: str):
   messages = [
       ChatMessage(role="user", content=prompt)
   ]

   # No streaming
   chat_response = client.chat(
       model=model,
       messages=messages,
   )

   return chat_response.choices[0].message.content


prompt = """Praca detektywistyczna: kto jest prawdziwym twórca Bitcoina?

proszę przeprowadzic następujące działania:


1. zrób Analizę krytyczną zebranych informacji i napisz wyniki tego analizu.
ocen wiarygodności źródeł, krzyżowego odniesienia
informacji i uwzględnij ewentualną stronniczość lub ukryte motywacje, 
które mogą wpływać na różne poglądy i opinie. napisz wyniki badan a nie instrukcje jak to zrobic

2. Kontekst Historyczny.
Proszę zbadać kontekst historyczny związany z powstaniem Bitcoina, 
włączając w to wydarzenia poprzedzające jego rozwój
 oraz szerszy krajobraz społeczno-gospodarczy w tamtym czasie. 

3. Teorie i Spekulacje
Proszę zbadać różne teorie i spekulacje na temat tożsamości Satoshi Nakamoto. 
Mogą to być osoby, które były proponowane jako potencjalni kandydaci 
na podstawie dowodów poszlakowych lub analizy językowej. """
print(chat_mistral(prompt))

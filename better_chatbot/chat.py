import random
import json

import torch

import pandas as pd

from model import NeuralNet
from nltk_utils import bag_of_words,tokenize

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

intents = pd.read_csv("better_chatbot/preguntas_respuestas.csv",encoding='utf-8',sep=",")

FILE="better_chatbot/dataMejor.pth"
data = torch.load(FILE)

input_size=data["input_size"]
hidden_size=data["hidden_size"]
output_size=data["output_size"]
all_words=data["all_words"]
tags=data["tags"]
model_state=data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name="Sam"
columna_preguntas = intents.iloc[:, 0].tolist()
columna_respuestas = intents.iloc[:, 1].tolist()
print("vamos a charlar! tipea 'salir' para salir")
print("especificar lo mas que se pueda:materia, codigo de materia, dia de cursada y comision")
while True:
    
    sentence = input("you:")
    if sentence =="salir":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model (X)
    _, predicted = torch.max(output,dim=1)
    tag = tags [predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob=probs[0][predicted.item()]

    if prob.item()>0.9999:
        for intent in columna_preguntas:
            if tag == columna_preguntas.index(intent):
                #print(f"{bot_name}: {random.choice(intent['responses'])}")
                respuesta=f"{str(bot_name)}:{str(columna_respuestas[tag])}"
        print (respuesta)
    else:
        print(f"{bot_name}: por favor especificar mas datos") 

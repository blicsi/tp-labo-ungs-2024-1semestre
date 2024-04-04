import json
from nltk_utils import tokenize,stem,bag_of_words
import numpy as np
import pandas as pd
import csv

import torch
import torch.nn as nn
from torch.utils.data import Dataset,DataLoader

from model import NeuralNet

#se guarda en memoria el csv
data = pd.read_csv("better_chatbot/preguntas_respuestas.csv",encoding='utf-8',sep=",")

all_words = []
tags = []
xy = []

for intent in intents["intents"]:
    tag=intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        w= tokenize(pattern)
        all_words.extend(w)
        xy.append((w,tag))
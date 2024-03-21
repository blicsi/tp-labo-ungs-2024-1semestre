import json

with open("data.json","r") as f:
    intent = json.load(f)

all_words = []
tags = []
xy = []
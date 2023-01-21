#!/usr/bin/env python
# coding: utf-8

#Inference Code
import spacy
import json

#Load the model
nlp = spacy.load('model')

#Load the document
with open('./10000344.txt', 'r') as f:
    text = f.read()

#Inference
inference = nlp(text)

#create the output dictionary
output = {}
for ent in inference.ents:
    output[ent.label_] = str(ent.doc)

#save the output dictionary
with open('./output/10000344.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

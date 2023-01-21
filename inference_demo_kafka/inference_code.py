#!/usr/bin/env python
# coding: utf-8

import os
import json

#Inference Code
import spacy
from kafka import KafkaConsumer


#Load the model
nlp = spacy.load('model')
IP = os.getenv('IP')
BOOTSTRAP_SERVER=[IP+":9092"]
print(BOOTSTRAP_SERVER)
consumer = KafkaConsumer('quickstart-events', bootstrap_servers=BOOTSTRAP_SERVER)
for msg in consumer:
    #Inference
    text_msg = msg.value.decode('utf-8')
    inference = nlp(text_msg)

    #create the output dictionary
    output = {}
    for ent in inference.ents:
        output[ent.label_] = str(ent.doc)

    #save the output dictionary
    with open('./output/10000344.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)

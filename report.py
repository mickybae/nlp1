import os
import json
import nltk
import matplotlib.pyplot as plt
import numpy as np
from konlpy.tag import Okt
from pprint import pprint
from matplotlib import font_manager, rc

def read_data(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data

def tokenize(doc):
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_data = read_data('./data/ratings_train.txt')
test_data = read_data('./data/ratings_test.txt')

okt = Okt()

if os.path.isfile('./data/train_docs.json'):
    with open('./data/train_docs.json','r', encoding="utf-8") as f:
        train_docs = json.load(f)
    with open('./data/test_docs.json','r', encoding="utf-8") as f:
        test_docs = json.load(f)
else:
    
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]

    with open('./data/train_docs.json','w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('./data/test_docs.json','w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

pprint(train_docs[0])
for t in train_docs
    for i in t
    
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:28:20 2020

@author: minimilien
"""

from nltk.corpus import stopwords
from gensim.models import Doc2Vec
import pandas as pd
import numpy as np
import nltk

try:
    nltk.download('stopwords')
except:
    pass

stopwords = set(stopwords.words('english'))
s = 300
df=pd.read_csv("tweets.csv",index_col=0)


def traitement(phrase):
    phrase=phrase.lower()
    texte2=(str(phrase).replace(',',' ')).lower()
    texte2=texte2.replace("'",' ')
    texte2=texte2.replace("-",' ')
    texte2=texte2.replace(".",' ')
    texte2=texte2.replace("*",' ')
    texte2=texte2.replace("\\",' ')
    texte2=texte2.replace("\n",' ')
    texte2=texte2.replace("/",' ')
    texte2=texte2.replace("!",' ')
    texte2=texte2.replace("?",' ')
    texte2=texte2.replace("\"",' ')
    texte2=texte2.replace("'",' ')
    texte2=texte2.replace("\#",' ')
    texte2=texte2.split()
    texte2=[token for token in texte2 if len(token) and token.lower() not in stopwords]
    return ' '.join(texte2)

model=Doc2Vec.load('tweetmodel.model')

def norme(vec):
    return np.sqrt(np.sum(vec*vec))
def prediction(vec1,vec2):
    val=np.sum((vec1*vec2))
    val/=(norme(vec1)*norme(vec2))
    if val>1:
        return np.arccos(1)#because of the structure of floats it can appen that the result is almost 1 but superior
    else:
        return np.arccos(val)
        
def taille(vec1,vec2):
    return abs(norme(vec1)-norme(vec2))

def vectorization(word):
    T=word.split(' ')
    vector=sum([vec(i) for i in T])
    return vector

def vec(mot):
    try:
        x=model.wv.get_vector(mot)
        return x
    except:
        return np.array([0]*s,dtype=np.float32)

def similarity(word1,word2):
    w1,w2=traitement(word1),traitement(word2)
    v1,v2=vectorization(w1),vectorization(w2)
    return prediction(v1,v2)

def get_20_best(phrase):
    res={tweet:similarity(phrase,tweet) for tweet in df['text']}
    res=sorted(res, key= lambda A: res[A])
    return res[:20]

#print('\n'.join(get_20_best("Build a wall !!!")))
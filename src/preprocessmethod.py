from joindatasets import *

from ast import literal_eval as le
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def converter(obj):
    glist = []
    for i in le(obj):
        glist.append(i['name'])
    return glist

def converterspecificnums(obj):
    glist = []
    cnt = 0
    for i in le(obj):
        if cnt != 3:
            glist.append(i['name'])
            cnt+=1
        else:
            break
    return glist

def fetch_director(obj):
    glist = []
    for i in le(obj):
        if i['job'] == "Director":
            glist.append(i['name'])
            break
    return glist

def stemwords(text):
    lst = []
    for i in text.split():
        lst.append(ps.stem(i))
    return " ".join(lst)
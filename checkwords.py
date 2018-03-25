import os
import json
import sys

def load_words():
    try:
        filename = os.path.join(os.getcwd(), "words_dictionary.json")
        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

def CheckWord(word,targetword):
    lst = list(targetword)
    for c in list(word):
        if c not in lst:
            return ''
        else:
            lst.remove(c)
    return word

if __name__ == '__main__':
    english_words = load_words()
    word = sys.argv[1]
    length = int(sys.argv[2])
    #lst = [x for x,_ in english_words.items() if (len(x) >= 3) & (len(x) <= 7) & (CheckWord(x,word) != '')]
    lst = [x for x,_ in english_words.items() if (len(x) == length) & (CheckWord(x,word) != '')]
    for allowed in lst:
        print(allowed)
    

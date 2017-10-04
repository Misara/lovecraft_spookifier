import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize.moses import MosesDetokenizer
#from bs4 import BeautifulSoup


def spookify_adjectives(raw):
    """ Replaces all adjectives in provided text with 'spooky' """
    #raw_text = BeautifulSoup(raw).getText()
    d = MosesDetokenizer()
    tok_text = word_tokenize(raw)
    tok_text = nltk.pos_tag(tok_text)
    text = []

    for i in range(len(tok_text)):
        word = tok_text[i]
        if word[1] == 'JJ' or word[1] == 'JJR' or word[1] == 'JJS':
            text += ['spooky']
        else:
            text += [word[0]]
    text = d.detokenize(text)
    return ' '.join(text)



def remove_adjectives(raw):
    """ Removes all adjectives from provided text """
    pass

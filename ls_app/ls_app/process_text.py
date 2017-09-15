import nltk
from nltk.tokenize import word_tokenize
#from bs4 import BeautifulSoup


def spookify_adjectives(raw):
    """ Replaces all adjectives in provided text with 'spooky' """
    #raw_text = BeautifulSoup(raw).getText()
    #tok_text = word_tokenize(raw)
    #for word in range(len(tok_text)):
    #    if nltk.pos_tag(tok_text[word][1], tagset='universal')[1] is 'ADJ':
    #        tok_text[word][0] = 'spooky'
    return "Passed to spookify"


def remove_adjectives(raw):
    """ Removes all adjectives from provided text """
    pass

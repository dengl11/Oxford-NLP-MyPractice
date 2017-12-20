from collections import Counter
import re 

def counter_of_words(sentences_tokenized):
    """return a counter of words
    Args:
        sentences_tokenized: [[word]

    Return: 
    """
    c = Counter()
    for words in sentences_tokenized:
        for w in words:
            c[w] += 1
    return c 


def tokenize_sentences(sentences):
    """return [[word]
    Args:
        sentences:  [sentence]

    Return: 
    """
    tokenized_sentences = []
    for sent_str in sentences:
        tokens = re.sub(r"[^a-z0-9]+", " ", sent_str.lower()).split()
        tokenized_sentences.append(tokens)
    return tokenized_sentences

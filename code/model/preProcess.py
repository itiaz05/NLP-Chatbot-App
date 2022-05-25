import spacy
import numpy as np

nlp = spacy.load("en_core_web_lg")

# Input: Get pattern as -String-
# Output: Return -Array- of pattern after clean stoping words, puncts and add tokens after lemma and lower 
def clean_pattern(sentence):
    doc = nlp(sentence)
    filtered_pattern = []
    
    for token in doc:
        if token.is_stop == False and not token.is_punct:
            token_after_lemma = token.lemma_
            filtered_pattern.append(token_after_lemma.lower())

    return filtered_pattern

# Input: Get all words as array of -Strings-, and sentence as -String- all words without duplicate words
# Output: array of bag of words
def bag_of_words(sentence, all_words):
    sentence_as_string = " ".join(sentence) # "convert" sentence into String because clean_pattern(String) get string as input
    sentence_tokenize = clean_pattern(sentence_as_string)
    bag = np.zeros(len(all_words),dtype=np.float32)

    for index,word in enumerate(all_words):
        if word in sentence_tokenize:
            bag[index] = 1

    return bag

# Output: array of bag of words
def bag_of_words_TF_IDF(sentence, all_words):
    sentence_as_string = " ".join(sentence) # "convert" sentence into String because clean_pattern(String) get string as input
    sentence_tokenize = clean_pattern(sentence_as_string)
    bag = np.zeros(len(all_words),dtype=np.float32)

    for index,word in enumerate(all_words):
        if word in sentence_tokenize:
            bag[index] +=1

    return bag
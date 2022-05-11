from sklearn.feature_extraction.text import TfidfVectorizer
import math

def extract_feature(bagOfWords):
    num_of_words_dict = dict.fromkeys(bagOfWords,0)

    for word in bagOfWords:
        num_of_words_dict[word] += 1


def computeTF(wordDict,bagOfWords):
    tfDict = {}
    bagOfWordsLength = len(bagOfWords)
    for word,count in wordDict.items():
        tfDict[word] = count/float(bagOfWordsLength) 

    return tfDict


# def computeIDF(patterns):
    










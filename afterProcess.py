from asyncio.windows_events import NULL
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_lg")

# Input: get array of identifiers array 
# Output: return a matcher obj that each words {identifier | Number or not | POS -> number }
def create_patterns():
    identifiersArray = ['flow','step','cr','release']
    matcher = Matcher(nlp.vocab)
    for identifier in identifiersArray:
        labelMatcher = [{'LOWER':identifier},{'LOWER':'number','OP':'?'},{'POS':'NUM'}]
        matcher.add(identifier, [labelMatcher])
        
    return matcher


# Input: User Doc, Matcher obj
# Output: return dict that represent each of our Matcher identifiyers
def getNumbers(matches,doc):
    labelsDict = {"cr": NULL, "flow": NULL, "step":NULL, "release": NULL}
    for match_id ,start, end in matches:
        span = doc[start:end]  # The matched span
        for token in span:
            if token.text in labelsDict.keys(): # if the token is one of the keys
                if token.right_edge.like_num:
                    labelsDict[token.text] = token.right_edge
    return labelsDict

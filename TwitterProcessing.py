"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2022

"""

import re
import emoji
import nltk

class TwitterProcessing:
    """
    This class is used to pre-process tweets.  This centralises the processing to one location.  Feel free to add.
    """

    def __init__(self, tokeniser, lStopwords):
        """
        Initialise the tokeniser and set of stopwords to use.

        @param tokeniser:
        @param lStopwords:
        """

        self.tokeniser = tokeniser
        self.lStopwords = lStopwords



    def process(self, text):
        """
        Perform the processing.
        @param text: the text (tweet) to process

        @returns: list of (valid) tokens in text
        """
       
        # covert all to lower case
        text = text.lower()
      
        # convert emoji to text
        text = emoji.demojize(text, delimiters=(" ", " "))
 
        # Remove the mentions  
        text = re.sub('@[^\s]+', '', text)
 
        # Remove the # from strings
        text = text.replace("#", "")
  
        # remove the digits from tweets
        text = ''.join([i for i in text if not i.isdigit()])

        # Remove the single quotes from strings
        text = text.replace("'", "")

        # tokenise
        tokens = self.tokeniser.tokenize(text)
        tokensStripped = [tok.strip() for tok in tokens]
  
        # stem (we use set to remove duplicates)
        stemmer = nltk.stem.PorterStemmer()
        lTokens = set([stemmer.stem(tok) for tok in tokensStripped])
        
        # pattern for digits
        # the list comprehension in return statement essentially remove all strings of digits or fractions, e.g., 6.15
        regexDigit = re.compile("^\d+\s|\s\d+\s|\s\d+$")
        
        # regex pattern for http
        regexHttp = re.compile("^http")
        
        # regex pattern for https
        regexHttps = re.compile("^https")

        return [tok for tok in lTokens if tok not in self.lStopwords and regexDigit.match(tok) == None and regexHttp.match(tok) == None and regexHttps.match(tok) == None]
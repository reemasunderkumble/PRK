#
# COSC2671 Social Media and Network Analytics
# @author Jeffrey Chan, RMIT University, 2022
#

import tweepy 


def twitterClient():
    """
        Setup Twitter API client.

        @returns: tweepy.API object
    """
    API_KEY = "95L6BdhQybmTaEZaaL9xNYQd2"
    API_SECRET = "sw6XZ5eUfQMcm0qOolWWuo3hoQ6TUigEdA7V8Au5cK3kgqIxMn"
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIRShwEAAAAALzIBTorthj1D6Q9ECJsh52Pt334%3DzuswRkEtup8aH1qnFFYTh6xQOYn5M7KbwVtIzK72Vc5sW9cCfI"
    ACCESS_TOKEN = "2623592551-gXRKZDqskkomaLyLgHh29DXCeHjAiXOFjDWb709"
    ACCESS_TOKEN_SECRET = "aTUiBs7XllKXCqT0NlZ2LsFAcH0ZMnfZ3DJwZ2AKkSki4"
    #client = tweepy.Client(API_KEY,API_SECRET,BEARER_TOKEN,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
    client = tweepy.Client(BEARER_TOKEN)
    #return API_KEY,API_SECRET,BEARER_TOKEN,ACCESS_TOKEN,ACCESS_TOKEN_SECRET
    return client

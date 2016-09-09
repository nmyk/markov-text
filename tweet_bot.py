from db import Db
from sql import Sql
from rnd import Rnd
import tweepy
import sqlite3
from markov import WORD_SEPARATOR
from gen import Generator	

NAME = 'fiction'
CONSUMER_KEY = 'AVDFXF3LJZBSPKmiQZvwOYcke'
ACCESS_TOKEN = '282241770-ODWN1cekRcTn7UZkHp6NR6URZUDDttH6mLcbmyO5'

def main():
	consumer_secret = open('consumer_secret.txt').read()[:-1]
	access_token_secret = open('access_token_secret.txt').read()[:-1]
	auth = tweepy.OAuthHandler(CONSUMER_KEY, consumer_secret)
	auth.set_access_token(ACCESS_TOKEN, access_token_secret)
	api = tweepy.API(auth)
	tweet = create_tweet()
	api.update_status(tweet)
	
def create_tweet():
	db = Db(sqlite3.connect(NAME + '.db'), Sql())
	generator = Generator(NAME, db, Rnd())
	tweet_candidate = generator.generate(WORD_SEPARATOR)
	return tweet_candidate if len(tweet_candidate) <= 140 else create_tweet()

if __name__ == '__main__':
	main()
	

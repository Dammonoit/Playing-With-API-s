from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import os
import glob
import twitter_authentication
 

class TwitterStreamer():
    
    def __init__(self):
        pass

    def stream_tweets(self, output_file, Hash_tags):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(output_file)
        auth = OAuthHandler(twitter_authentication.CONSUMER_KEY, twitter_authentication.CONSUMER_SECRET)
        auth.set_access_token(twitter_authentication.ACCESS_TOKEN, twitter_authentication.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=Hash_tags)


class StdOutListener(StreamListener):
    
    def __init__(self, output_file):
        self.output_file = output_file

    def on_data(self, data):
        try:
			
            print(data)
            with open(self.output_file, 'a') as tf:
                tf.write(data)
			return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
    files = glob.glob('/home/dammonoit/Desktop/twitter_app/App2/Output/*')
    for f in files:
		os.remove(f)
    print("The data Collected From the Tweepy API is: \n")
    Hash_tags = ["Trump", "Modi", "BJP", "Liberal"]
    output_file = "Output/tweets.txt"
    

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(output_file, Hash_tags)

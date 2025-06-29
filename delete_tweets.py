import tweepy
import json
import time

# Your API credentials
api_key = "PASTE_YOUR_API_KEY"
api_secret = "PASTE_YOUR_API_SECRET"
access_token = "PASTE_YOUR_ACCESS_TOKEN"
access_secret = "PASTE_YOUR_ACCESS_SECRET"

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)

with open("tweets.js", "r", encoding="utf-8") as file:
    raw_data = file.read()
    json_data = json.loads(raw_data[raw_data.index("["):])  # strips the JS prefix

# === Delete tweets ===
for entry in json_data:
    tweet = entry.get("tweet")
    if not tweet:
        continue
    tweet_id = tweet.get("id")
    tweet_text = tweet.get("full_text", "")[:50]

    try:
        print(f"🗑 Deleting tweet {tweet_id} - {tweet_text}")
        api.destroy_status(tweet_id)
        time.sleep(1)  # to avoid rate limits
    except Exception as e:
        print(f"⚠️ Error deleting tweet {tweet_id}: {e}")
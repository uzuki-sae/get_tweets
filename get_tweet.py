import requests
import datetime
from requests_oauthlib import OAuth1Session
import pandas as pd
import json
from pandas.io.json import json_normalize
def get_tweets(day):
    api_key = "oaFY47Bnpbi8mqfykwejrIMPr"
    api_key_secret = "yHPvrwOQqevkvCX294tRq7WeYln4AEpHkjAqEQoaK3vdcQs83g"
    access_token = "846656552333262848-ZCWB9kJP4M7f5piIXtoBIbPn2PA6Atd"
    access_token_secret = "cbVhOVFHUBDYhU5N2BUM0AkL97nfR7tH5WEkjxCnRNO4Z"
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHndkQEAAAAAtamWY2kbxfW%2FoautUZAMtt8I0ac%3D4OE9DOG9KHpRRpAHR5vsfde81NqBjfgSsGPd2bZTdZb5EsQ4OY"
    api = OAuth1Session(api_key, api_key_secret, access_token, access_token_secret,)
    my_id="739768279758082053"
    url = f"https://api.twitter.com/2/users/{my_id}/tweets"
    sday=datetime.datetime.strftime(day, "%Y-%m-%d")
    day=day+datetime.timedelta(weeks=1)
    print(sday)
    eday=datetime.datetime.strftime(day, "%Y-%m-%d")
    print(eday)
    params = {
        'expansions'  : "author_id,in_reply_to_user_id,referenced_tweets.id.author_id,entities.mentions.username",
        'tweet.fields': "created_at,public_metrics,entities",
        'user.fields' : "name",
        'max_results' : 64,
        'start_time'  : '{}T00:00:01Z'.format(sday),
        'end_time'    : '{}T00:00:01Z'.format(eday)
      }

    tweet = api.get(url, params = params)
    res=json.loads(tweet.text)
    print(res)
    try:
        data=res['data']
    except:
        data=""
    return data

day=datetime.date(2016, 6, 22)
eos=datetime.date(2017, 8, 12)



j=[]
while day < eos:
    res = get_tweets(day)
    print(res)
    if res=="":
        pass
    else:
        j.extend(res)
    day = day + datetime.timedelta(weeks=1)





with open('user_tweets.json', 'w') as f:
    json.dump(j, f, indent=4)
# read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
#df.to_csv("~/Downloads/2017tweet.csv", encoding='utf-8', sep=',', header=True)

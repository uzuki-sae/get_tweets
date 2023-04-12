import json
import pandas as pd
from get_refered import get_refered
from to_list import to_list


with open('user_tweets.json', 'r', encoding="utf8") as dic:
    j=json.load(dic)
column = ["時間","作成者","RT","コメント","いいね","リツイート","テキスト","引用種類","引用先","オリジナル時間", "オリジナル作成者","RT","コメント","いいね","リツイート","テキスト", "type", "username"]
v = []
for t in j:
    rfr=get_refered(t)
    print(rfr)
    value=to_list(t)
    if rfr == "no reference":
        value.extend([None, None, None, None, None, None, None, None, None])
    else:
#        print(to_list(rfr))
        value.extend(to_list(rfr))
#    print(value)
    v.append(value)

dfm=pd.DataFrame(data=v, columns=column)
l=[]
for t in j:
    try:
        for h in t["entities"]["hashtags"]:
            l.append([t["created_at"], h["tag"]])
    except:
        pass
dfh=pd.DataFrame(data=l,columns=["time", "tag"])

dfm.to_csv("mian_tweets.csv")
dfh.to_csv("hashtag_tweets.csv")

import json
def to_list(data):
#    print(data)
#    print(type(data))
    if type(data)==list:
        data=data[0]
    else:
        pass
    ls = [data["created_at"], data["author_id"], data["public_metrics"]["retweet_count"], data["public_metrics"]["reply_count"], data["public_metrics"]["like_count"], data["public_metrics"]["quote_count"], data["text"]]
    try:
        ls.append(data["referenced_tweets"][0]["type"])
    except:
        ls.append(None)
    try:
        ls.append(data["entities"]["mentions"][0]["username"])
    except:
        ls.append(None)
    print(ls)
    return ls

def hash():
    import pandas as pd
    from pandas import json_normalize
    from collections import defaultdict
    df = pd.read_json('data', lines=True)
    import re
    top_hashtags = defaultdict(int)
    regex = "#\w+" 
    for tweet in range(len(df)):
        hashtag = re.findall(regex, df.iloc[tweet, 2])
        for tag in hashtag:
            top_hashtags[tag] += 1
    print(sorted(top_hashtags.items(), key=lambda x: x[1], reverse = True)[0:10])
    
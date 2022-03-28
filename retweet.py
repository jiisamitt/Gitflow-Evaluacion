def retweet():
    import pandas as pd

    df = pd.read_json(r'data.json', lines=True)
    df.sort_values(by=['retweetCount'], inplace=True, ascending=False)
    df.reset_index(inplace=True)
    for i in range(10):
        print("Id del twitter: ", df['id'][i])
        print("Cantidad de veces retwiteado: ", df['retweetCount'][i], "\n")


# def add_tweet():
#     print("agregar")
# 
# for tweet in len(raw_tweets):
#     if tweet["retweetconut"] > min_number:
#         
# 
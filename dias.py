def dias():
    import pandas as pd
    from collections import defaultdict
    df = pd.read_json('data.json', lines=True)

    top_dias = defaultdict(int)
    for tweet in range(len(df)):
        top_dias[df.iloc[tweet, 1].date().strftime('%d/%m/%Y')] += 1
        
    top_dias = sorted(top_dias.items(), key=lambda x: x[1], reverse = True)[0:10]
    print(top_dias)
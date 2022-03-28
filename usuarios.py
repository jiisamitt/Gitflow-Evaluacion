def usuarios():
    import pandas as pd
    from pandas import json_normalize


    from collections import defaultdict

    df = pd.read_json('data.json', lines=True)


    top_usuarios = defaultdict(int)
    for tweet in range(len(df)):
        top_usuarios[df.iloc[tweet, 5]['id']] += 1
    top_usuarios = sorted(top_usuarios.items(), key=lambda x: x[1], reverse = True)[0:10]
    print(top_usuarios)




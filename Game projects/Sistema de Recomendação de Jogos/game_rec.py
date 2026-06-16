import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

data = {
    "Jogo" : ["GTA","FIFA","COD","Minecraft"],
    "Ação" : ["1","0","1","0"],
    "Esporte" : ["0","1","0","0"],
    "Criativo" : ["0","0","0","1"]
}

df = pd.DataFrame(data)

similaridade = cosine_similarity(df.iloc[:,1:])

def recomendar(jogo):
    idx = df[df["Jogo"] == jogo].index[0]
    score = list(enumerate(similaridade[idx]))
    scores = sorted(scores,key=lambda x: x[1],reverse=True)
    return df.iloc[scores[1][0]["Jogo"]]

print(recomendar("GTA"))
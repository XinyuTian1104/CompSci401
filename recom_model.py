import pandas as pd
from fpgrowth_py import fpgrowth

class Model(object):
    def __init__(self) -> None:
        pass
    
    def pre_processing(self, raw_ds):
        ds = raw_ds.groupby('pid')['track_name'].apply(list)
        itemSetList = []

        for i in range(0, len(ds)):
            for j in range(0, len(ds.iloc[i])):
                ds.iloc[i][j] = ds.iloc[i][j].split('-', 1)[0]
                ds.iloc[i][j] = ds.iloc[i][j].split(' (', 1)[0]
            l = []
            for t in ds.iloc[i]:
                if t not in l:
                    l.append(t)
            itemSetList.append(l)

        return itemSetList

    def train(self, raw_ds):
        itemSetList = self.pre_processing(raw_ds)
        # print(len(itemSetList))
        _, rules = fpgrowth(itemSetList, minSupRatio = 0.01, minConf = 0.05)
        # print(freqItemSet, rules)
        self.rules = rules

    def recommend(self, df_songs):
        rules = self.rules
        songs = df_songs['track_name'].unique().tolist()
        for i in range(0, len(songs)):
            songs[i] = songs[i].split('-', 1)[0]
            songs[i] = songs[i].split(' (', 1)[0]

        recommended_songs = []
        for rule in rules:
            if set(rule[0]).issubset(set(songs)):
                if (set(rule[1]).issubset(set(songs)) == 0):
                    if (rule[1] not in recommended_songs):
                        recommended_songs.extend(list(rule[1]))

        recommended_songs = list(set(recommended_songs))
        return recommended_songs
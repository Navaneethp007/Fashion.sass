import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

data=pd.read_csv('Clothes.csv')
def find_similarity(self, data, newCol):
    # insert a new row in the data df
    if newCol not in data.columns:
        data = data.append(newCol, ignore_index=True)

    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    desc = tfidf.fit_transform(data['Description'])
    sim = cosine_similarity(desc) 
    csims = {}
    for i in range(len(sim)):
        sim_ind = sim[i].argsort()[:-50:-1] 
        csims[data['Description'].iloc[i]] = [(sim[i][x], data['Description'][x]) for x in sim_ind]
                                
class Recommender:
    def __init__(self, matrix):
        self.matrix_similar = matrix

    def _print_message(self, des, re_des):
        rec_items = len(re_des)
        
        print(f'The {rec_items} recommended items for {des} are:')
        for i in range(rec_items):
            print(f"Number {i+1}:")
            print(f"{re_des[i][1]} with {round(re_des[i][0], 3)} similarity score")
            print("--------------------")
        
    def recommend(self, recommendation):
        des = recommendation['des']
        number_items = recommendation['number_items']
        re_des = self.matrix_similar[des][:number_items]
        self._print_message(des=des, re_des=re_des)
recommedations = Recommender(csims)
                                         
recommendation = {
    "des": [data['Description'].iloc[4], data['Description'].iloc[5]],
    "number_items": 3 
}

recommedations.recommend(recommendation)

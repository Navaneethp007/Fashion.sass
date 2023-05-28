import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict

data=pd.read_csv('Clothes.csv')
def find_similarity(data, newCol):
    # insert a new column in the data df
    if newCol != '':
        #  data.append(
        # {
        #     'Id': data.iloc[-1][0] +1,
        #     'Description': newCol,
        #     'Category': 'Mixed'
        # }, ignore_index=True
        # )
        data=pd.concat([data, pd.DataFrame({'Id': data.iloc[-1][0] +1, 'Description': newCol, 'Category': 'Mixed'}, index=[0])], ignore_index=True)
    

    tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
    desc = tfidf.fit_transform(data['Description'])
    sim = cosine_similarity(desc) 
    csims = {}
    for i in range(len(sim)):
        sim_ind = sim[i].argsort()[:-50:-1] 
        csims[data['Description'].iloc[i]] = [(sim[i][x], data['Description'][x]) for x in sim_ind]

    return csims

csims = find_similarity(data, '')
        
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
        des = ' '.join(list(set(' '.join(des).split(' '))))
        if(des not in data['Description'].values):

            csims=find_similarity(data, des)
            self.matrix_similar = csims
        # print(self.matrix_similar.last())
        number_items = recommendation['number_items']
        re_des = self.matrix_similar[des][:number_items]
        self._print_message(des=des, re_des=re_des)
recommedations = Recommender(csims)
                                         
recommendation = {
    "des": [data['Description'].iloc[4], data['Description'].iloc[5]],
    "number_items": 3 
}

recommedations.recommend(recommendation)

                                     
recommendation = {
    "des": [data['Description'].iloc[3], data['Description'].iloc[8]],
    "number_items": 3 
}

recommedations.recommend(recommendation)

                                     
recommendation = {
    "des": [data['Description'].iloc[2], data['Description'].iloc[4]],
    "number_items": 3 
}

recommedations.recommend(recommendation)

                                     
recommendation = {
    "des": [data['Description'].iloc[1], data['Description'].iloc[10]],
    "number_items": 3 
}

recommedations.recommend(recommendation)

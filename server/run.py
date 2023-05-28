import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict
from flask import Flask, request  # Import flask

app = Flask(__name__)  # Setup the flask app by creating an instance of Flask
desc_to_id = {}
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
    for i in range(len(data)):
        data['Description'].iloc[i] = ' '.join(sorted(list(set(data['Description'].iloc[i].split(' ')))))
        desc_to_id[data['Description'].iloc[i]] = data['Id'].iloc[i]

    desc = tfidf.fit_transform(data['Description'])
    sim = cosine_similarity(desc) 
    csims = {}
    for i in range(len(sim)):
        sim_ind = sim[i].argsort()[:-50:-1] 
        csims[data['Description'].iloc[i]] = [(sim[i][x], data['Description'][x]) for x in sim_ind]

    return csims

        
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
        des = ' '.join(sorted(list(set(' '.join(des).split(' ')))))
        if(des not in data['Description'].values):

            csims=find_similarity(data, des)
            self.matrix_similar = csims
        # print(self.matrix_similar.last())
        number_items = recommendation['number_items']
        re_des = []
        lis_id = []
        # re_des = self.matrix_similar[des][1:number_items+1]

        for i in range(1, len(self.matrix_similar[des])):
            id = desc_to_id[self.matrix_similar[des][i][1]]
            if id<60:
                re_des.append(self.matrix_similar[des][i])
                lis_id.append(id+1)
        #     if self.matrix_similar[des][i][0] !=1:
        #         id = data.loc[data['Description'] == self.matrix_similar[des][i][1]]['Id'].values[0]
        #         # print(id)
        #         if id>60:
        #             continue
        #         lis_id.append(id)
        #         re_des.append(self.matrix_similar[des][i])

            if(len(re_des) == number_items):
                break

        self._print_message(des=des, re_des=re_des)
        return lis_id


@app.route('/')  # When someone goes to / on the server, execute the following function
def home():
    return 'Hello, World!'  # Return this message back to the browser

@app.route('/dressSelect', methods=['POST'])
def dressSelect():
# if request.method == 'POST':
    list = request.get_json()
    print(list)
                                         
    recommendation = {
        # "ids": [int(i)-1 for i in list],   
        "des": [data['Description'].iloc[int(i)-1] for i in list['dress']],
        "number_items": 4-len(list['dress'])
    }

    lis_id=recommedations.recommend(recommendation)
    # return 'Hello World'
    lis_id = [str(i) for i in lis_id]

    return {
        "id": lis_id
    }  # Return this message back to the browser



if __name__ == '__main__':  # If the script that was run is this script (we have not been imported)
    data=pd.read_csv('Clothes.csv')
    csims = find_similarity(data, '')
    recommedations = Recommender(csims)
    app.run()  # Start the server




    
                                     
# recommendation = {
#     "des": [data['Description'].iloc[3], data['Description'].iloc[8]],
#     "number_items": 3 
# }

# recommedations.recommend(recommendation)

                                     
# recommendation = {
#     "des": [data['Description'].iloc[2], data['Description'].iloc[4]],
#     "number_items": 3 
# }

# recommedations.recommend(recommendation)

                                     
# recommendation = {
#     "des": [data['Description'].iloc[1], data['Description'].iloc[10]],
#     "number_items": 3 
# }

# recommedations.recommend(recommendation)

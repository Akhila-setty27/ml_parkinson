

import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle


from yield_code import yield_fn


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html') 

    

@app.route('/prediction',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    #print(features_list1,features_list)

    int_features = [str(x) for x in request.form.values()]



    print("output from web page  ",int_features)




    
    a=int_features


    print(a)

    output_yield=yield_fn(a)

    if output_yield==0:
      ty="Negative"
    else:
      ty="Possitive"


    return render_template('index2.html',prediction_text='the result of analysis of the data is --------   {}  '.format(ty))


if __name__ == "__main__":
    app.run(debug=True)

import joblib
 
import pickle   

filename = 'rf_model.sav'
#pickle.dump(clf, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
#loaded_model = pickle.load(open(filename, 'rb'))
loaded_model = joblib.load(filename)
#result = loaded_model.score(Xtest, Ytest)
#print(result)


import numpy as np

def yield_fn(features_list):
                int_features2 = np.array(features_list)

                int_features1 = int_features2.reshape(1, -1)


                tested1=loaded_model.predict(int_features1)



                print(tested1)

                return  tested1


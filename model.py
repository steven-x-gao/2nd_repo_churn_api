import pickle
import gzip
#load model

with gzip.open('./ecom-user-churn.pgz', 'r') as f:
        model_lrr = pickle.load(f)

def predict(input):

    pred=model_lrr.predict(input)[0]
    print(pred)
    return pred

"""
python3 predict_model.py \ 
-x_predict='2 0 0 10.5 31 0 1 0 0 1'
"""
import pickle
from os import getenv

import numpy as np
import pandas as pd


def predict_model(pkl: str, x_predict):
    """
    Загрузка модели и предикт
    """
    with open(pkl, 'rb') as fd:
        model = pickle.load(fd)
    return model.predict(x_predict)


if __name__ == "__main__":
    
    print(predict_model("model.pkl", np.array([getenv("X_PREDICT").split()])))



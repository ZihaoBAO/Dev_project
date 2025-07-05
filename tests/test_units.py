import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import joblib
import pandas as pd
from sklearn.datasets import load_digits
import numpy as np

def test_model_loading():
    """test if the model can be loaded correctly"""
    try:
        model = joblib.load("models/random_forest_model/random_forest_model.joblib")
        assert model is not None
        assert hasattr(model, 'predict')
        print("✅ model loading test passed")
    except Exception as e:
        print(f"❌ model loading test failed: {e}")
        assert False

def test_data_loading():
    """test if the data can be loaded correctly"""
    digits = load_digits()
    assert digits.data.shape[0] > 0
    assert digits.target.shape[0] > 0
    assert digits.data.shape[0] == digits.target.shape[0]
    print("✅ data loading test passed")

def test_prediction_format():
    """test if the prediction output format is correct"""
    try:
        model = joblib.load("models/random_forest_model/random_forest_model.joblib")
        digits = load_digits()
        
        # create test data
        test_data = digits.data[:1]  # take the first row data
        prediction = model.predict(test_data)
        
        # test if the prediction result format is correct
        assert isinstance(prediction, np.ndarray)
        assert len(prediction) == 1
        # Check if the prediction value is numeric (int or float)
        assert np.issubdtype(prediction.dtype, np.number)
        print("✅ prediction format test passed")
    except Exception as e:
        print(f"❌ prediction format test failed: {e}")
        assert False

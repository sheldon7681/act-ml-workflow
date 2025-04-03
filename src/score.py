
import json
import joblib
import numpy as np
import pandas as pd
from azureml.core.model import Model

def init():
  global model
  model_path = Model.get_model_path('model')
  model = joblib.load(model_path)

def run(raw_data):
  try: ## Try la predicción.
    data = json.loads(raw_data)['data'][0]
    data = pd.DataFrame(data)

    columns_model = [
      " Borrowing dependency",
      " Current Liability to Current Assets",                       
      " Net Value Per Share (C)",                                  
      " Non-industry income and expenditure/revenue",              
      " Net Value Growth Rate",                                    
      " Continuous interest rate (after tax)",
    ]

    data_dummies = data[columns_model]
    result = model.predict(data_dummies).tolist()

    return json.dumps(result)
  except Exception as e:
    return json.dumps(str(e))

import ast
from fastapi import FastAPI
from .algorithm import make_prediction


app = FastAPI()

@app.get('/predict')

def predict(text: str):
  score,label = make_prediction(text)
  #return pred
  response = {'text_sentiment':label,'score':score}

  return response

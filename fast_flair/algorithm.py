import flair
from flair.models import TextClassifier
from flair.data import Sentence


fast_model = TextClassifier.load('en-sentiment')

def make_prediction(text):
  #Load Model
  model = fast_model
  sentence = Sentence(text)
  model.predict(sentence)
  score = sentence.score
  label = sentence.labels[0].value
  return score,label
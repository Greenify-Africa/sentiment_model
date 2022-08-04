import flair
from flair.models import TextClassifier
from flair.data import Sentence
from .apps import FlairmodelConfig



def make_prediction(text):
  #Load Model
  model = FlairmodelConfig.model
  sentence = Sentence(text)
  model.predict(sentence)
  score = sentence.score
  label = sentence.labels[0].value
  return score,label
from django.apps import AppConfig
from flair.models import TextClassifier



class FlairmodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'flairModel'

    model = TextClassifier.load('en-sentiment')

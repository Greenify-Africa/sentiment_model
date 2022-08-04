from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .algorithm import make_prediction


# Create your views here.
class PredictView(APIView):
  def get(self,request):
    if request.method == 'GET':
      #get the input data
      text = request.GET.get('text')
      #instantiate model
      score,label = make_prediction(text)
      #return pred
      response = {'text_sentiment':label,'score':score}
      return JsonResponse(response)
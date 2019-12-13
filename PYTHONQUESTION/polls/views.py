# Create your views here.

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from .models import Question
from serializers import QuestionSerializer 

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = Question.objects.all()
	if request.method == 'GET':
		serializer = QuestionSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
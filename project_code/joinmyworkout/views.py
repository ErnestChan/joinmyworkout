from django.shortcuts import render
from django.template.context import RequestContext

# Create your views here.


def home(request):
	context = RequestContext(request, 
							{'user': request.user})
	return render(request, 'joinmyworkout/index.html', {'user': request.user})


def create_event(request):
	return render(request, 'joinmyworkout/create_event.html', {})

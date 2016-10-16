from django.shortcuts import render
# from django.http import HttpResponse
from forms import CreateForm
# Create your views here.


def home(request):
    return render(request, 'joinmyworkout/index.html', {})


def create_event(request):
    form = CreateForm()
    return render(request, 'joinmyworkout/create_event.html', {'form': form})

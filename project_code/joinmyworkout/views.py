from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
        return render(request, 'joinmyworkout/index.html', {})


def create_event(request):
        return render(request, 'joinmyworkout/create_event.html', {})

from django.shortcuts import render
from django.shortcuts import redirect
# from django.http import HttpResponse
from forms import CreateForm
# from django.template.context import RequestContext

# Create your views here.


def home(request):
    # context = RequestContext(request, {'user': request.user})
    return render(request, 'joinmyworkout/index.html', {'user': request.user})


def create_event(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # TODO: This needs to redirect to a confirmation page to handle.
            return redirect('index', pk=post.pk)
    else:
        form = CreateForm()
    return render(request, 'joinmyworkout/create_event.html', {'form': form})

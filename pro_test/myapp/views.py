from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest
from django.http import HttpResponse


def index(request):
    context = {
        'name': 'mali'
    }
    # return HttpResponse("Hello,World")
    return render(request, 'index.html', context=context)

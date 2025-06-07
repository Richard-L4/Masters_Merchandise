from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html')


def who_we_are(request):
    return render(request, 'home/who_we_are.html')
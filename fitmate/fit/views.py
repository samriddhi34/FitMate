from django.shortcuts import render
def index(request):
    return render(request, 'fit/index.html')

# Create your views here.

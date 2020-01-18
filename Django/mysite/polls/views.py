from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You'r at the polls index.")

# Create your views here.

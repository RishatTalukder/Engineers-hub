from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'main_app/home.html')    
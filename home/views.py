from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("This is the home page")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("This is the about page")
    return render(request, "about.html")

def contact(request):
    # return HttpResponse("This is the contact page")
    return render(request, "contact.html")

def prediction(request):
    # return HttpResponse("This is the prediction page")
    return render(request, "prediction.html")

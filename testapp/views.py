from django.http import HttpResponse, request
from django.shortcuts import render
from .models import experties, our_products


# Create your views here.
def fun(request):
    obj = experties.objects.all()
    return render(request, 'index.html', {"experties": obj})


def fun1(request):
    obj = our_products.objects.all()
    return render(request, 'index.html', {"results": obj})


def addition(request):
    num1 = int(request.post["num1"])
    num2 = int(request.post["num2"])
    num3 = num1 + num2
    return render(request, 'result.html', {"add": num3})

def details(request,id):
    try:
        details=experties.objects.get(id=id)
    except Exception as e :
        raise e
    return render (request,'components.html', {"details":details})

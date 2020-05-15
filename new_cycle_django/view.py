from django.shortcuts import render

from . import classifier

def home(request):
    return render(request,'form.html')

def contacts(request):
    return render(request,'contacts.html')

def form(request):
    return render(request,'form.html')

def result(request):
    user_input = request.POST.get('experience')
    result = classifier.predictValueModel(user_input)
    return render(request,'result.html',{'salary':result})



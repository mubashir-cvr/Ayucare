from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def about(request):
    return render(request,'aboutus.html')


def branch(request):
    return render(request,'branch.html')

def contact(request):
    return render(request,'contact.html')


def doctor(request):
    return render(request,'doctor.html')
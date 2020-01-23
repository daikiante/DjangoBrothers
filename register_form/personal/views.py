from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'personal/home.html')


def about(request):
    return render(request,'personal/about.html')


def contact(request):
    return render(request,'personal/contact.html')


def service(request):
    return render(request,'personal/service.html')


def testimonials(request):
    return render(request,'personal/testimonials.html')

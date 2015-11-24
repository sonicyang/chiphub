from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def about_us(request):
    return render(request, 'about_us.html')


def exchange(request):
    return render(request, 'exchange.html')


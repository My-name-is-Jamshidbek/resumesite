from django.shortcuts import render


def index(request):
    return render(request, 'user/pages/index.html')


def contact(request):
    return render(request, 'user/pages/contact.html')


def portfolio(request):
    return render(request, 'user/pages/portfolio.html')


def services(request):
    return render(request, 'user/pages/services.html')

def about(request):
    return render(request, 'user/pages/about.html')

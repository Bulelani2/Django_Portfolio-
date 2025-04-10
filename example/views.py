from django.shortcuts import render


def homepage(request):
    # return HttpResponse('Home page')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('About page')
    return render(request, 'aboutme.html')

def services(request):
    # return HttpResponse('Services page')
    return render(request, 'services.html')

def portfolio(request):
    # return HttpResponse('Portfolio page')
    return render(request, 'portfolio.html')

def contact(request):
    # return HttpResponse('Contact page')
    return render(request, 'contact.html')
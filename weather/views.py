import requests
from django.shortcuts import render
from .forms import CityForm

def weather_view(request):
    weather_data = {}
    form = CityForm(request.GET or None)
    
    if form.is_valid():
        city = form.cleaned_data['city']
        api_key = ''
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = {'error': 'City not found or API limit exceeded.'}
    
    context = {
        'form': form,
        'weather': weather_data
    }
    return render(request, 'weather.html', context)

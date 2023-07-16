from django.shortcuts import render
import requests

# Create your views here.
def home(request):

    city = request.GET.get('city', "Kochi")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d56500713e7ed9c0f6c358a9fe87104a'
    data = requests.get(url).json()
    

    payload = {
        'city' : data['name'],
        'country' : data['sys']['country'],
        'weather' : data['weather'][0]['main'],
        'icon' : data['weather'][0]['icon'],
        'kelvin' : int(data['main']['temp']),
        'celsius' : int(data['main']['temp']) - 273,
        'pressure' : data['main']['pressure'],
        'humidity' : data['main']['humidity'],
        'description' : data['weather'][0]['description']
    }

    context = {'data' : payload}
    print(context)


    return render(request, 'home.html', context)
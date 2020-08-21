import requests
from django.shortcuts import render, redirect
from .models import WeatherModel
from .forms import CityForm





def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=dddf7dee42561f049195e8b232679d60'
    err_msg = ''
    message = ''
    message_color = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            city_count = WeatherModel.objects.filter(name=new_city).count()
            if city_count == 0:
                r = requests.get(url.format(new_city)).json()
                if r['cod'] == 200:
                    form.save()
                else:
                    err_msg = "City doesn't exist!>>>"
            else:
                err_msg = 'City is already added!>>>'
        if err_msg :
          message = err_msg
          message_color = 'btn-outline-danger'
        else:
          message = 'City added successfully!>>>'
          message_color = 'btn-outline-success'


    form = CityForm


    cities = WeatherModel.objects.all()
    weather_data = []
    for city in cities:
        r = requests.get(url.format(city)).json()


        city_weather = {
          'city': city.name,
          'temperature': r['main']['temp'],
          'description': r['weather'][0]['description'],
          'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    content = {'city_weather': weather_data,
               'form': form,
               'message': message,
               'message_color': message_color
               }
    return render(request, 'weather.html', content)


def delete(request, city_name):
    WeatherModel.objects.get(name=city_name).delete()
    return redirect('home')



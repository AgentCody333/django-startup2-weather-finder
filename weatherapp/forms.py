from django.forms import ModelForm, TextInput
from .models import WeatherModel


class CityForm(ModelForm):

  class Meta:
    model = WeatherModel
    fields = ['name']
    widgets = {'name':TextInput(attrs={'class':'form-control mr-sm-2', 'placeholder':'Location name'})}
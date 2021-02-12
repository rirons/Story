from django.forms import fields
from .models import Forecast
from django import forms
from django.forms.widgets import Textarea, Widget

class ForecastForm(forms.ModelForm):
    class Meta:
        model = Forecast
        fields = ['roomno','day1lbs','day2lbs','day3lbs','day4lbs','day5lbs','lg5pct','med10pct','sm10pct']
        widgets = { 
                    'roomno': forms.TextInput(attrs={'size': 5}),
                    'day1lbs': forms.TextInput(attrs={'size': 5}),
                    'day2lbs': forms.TextInput(attrs={'size': 5}),
                    'day3lbs': forms.TextInput(attrs={'size': 5}),
                    'day4lbs': forms.TextInput(attrs={'size': 5}),
                    'day5lbs': forms.TextInput(attrs={'size': 5})
        
        
        }
        labels = {
            'roomno': 'Room','day1lbs':'Day 1','day2lbs':'Day 2','day3lbs':'Day 3','day4lbs':'Day 4','day5lbs':'Day 5'
        }


class FcastAllForm(forms.Form):
    roomno = forms.CharField()

class ContactForm(forms.Form):
    full_name = forms.CharField()



from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class LocForm(forms.Form):
    placename = forms.CharField(max_length=100)
    lat = forms.FloatField()
    lon = forms.FloatField()

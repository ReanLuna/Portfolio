from django import forms
from .models import GraphicDesign
from django.forms import ModelForm


class ImageForm(forms.ModelForm):
    caption = forms.TextInput()
    image = forms.ImageField()
    class Meta:
        model = GraphicDesign
        fields = ['image', 'caption']

class UIUXUpdateForm(forms.ModelForm):
    class Meta:
        model = GraphicDesign
        fields = ['image', 'caption']

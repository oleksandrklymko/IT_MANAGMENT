from django import forms

from .models import Toy

class ToyForm(forms.ModelForm):

    class Meta:
        model = Toy
        fields = '__all__'
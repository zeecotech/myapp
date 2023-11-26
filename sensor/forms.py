from django import forms
from sensor.models import sensorinputModel

class sensorinputForm(forms.ModelForm):
    class Meta:
        model = sensorinputModel
        fields = '__all__'
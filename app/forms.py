from django import forms
from app.models import *

class BMI_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']


class BMI_User_form (forms.ModelForm):
    class Meta:
        model=BMI
        fields=['age','height','weight','mobile_number']

        
from django.shortcuts import render
from app.models import *

from django.http import HttpResponse,HttpResponseRedirect

from app.forms import *
# Create your views here.
def Bmi(request):
    Bf=BMI_form()
    Uf=BMI_User_form()
    d={"Bf":Bf,"Uf":Uf}
    if request.method=='POST':
        Bfd=BMI_form(request.POST)
        Ufd=BMI_User_form(request.POST)
        if Bfd.is_valid() and Ufd.is_valid():
            height=Ufd.cleaned_data['height']
            weight=Ufd.cleaned_data['weight']
            
            pw=Bfd.cleaned_data['password']
            USO=Bfd.save(commit=False)
            USO.set_password(pw)
            USO.save()

            UFO=Ufd.save(commit=False)
            UFO.user=USO
            bmi=float(weight)/float(height)/100*float(height)
            UFO.BMI=bmi
            UFO.save()
            if bmi<=16:
                return HttpResponse(f"You are under very  weight {bmi}")
            elif bmi<=18.5:
                return HttpResponse(f"You are under  weight {bmi}")
            elif bmi<=25:
                return HttpResponse(f"you are healthy {bmi}")
            elif bmi<=30:
                return HttpResponse(f"You are overweight {bmi}")


    return render(request,'health.html',d)
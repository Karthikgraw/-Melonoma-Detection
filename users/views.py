from django.shortcuts import render,redirect
from core.core_api import *
import requests
from django.contrib.auth.decorators import login_required
import os
import tempfile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from authentication.models import *
from .models import *
# Create your views here.

@login_required(login_url='login')
def melanoma_prediction(request):
    return render(request,'melanoma_prediction.html')

@login_required(login_url='login')
def get_melanoma_prediction(request):
    doctors = CustomUser.objects.filter(user_type ='3')
    if request.method  == 'POST':
        file = request.FILES.get('data')
        print(file)
        path = default_storage.save('tmp/'+file.name, ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        prediction = predict_melanoma(tmp_file)
        os.remove(tmp_file)
        print(prediction)
        context={
            'prediction':prediction,
            'doctors':doctors,
        }
        return render(request,'melanoma_prediction.html',context)
    return render(request,'melanoma_prediction.html')

@login_required(login_url='login')
def view_doctors(request):
    doctors = CustomUser.objects.filter(user_type ='3')
    context = {
        'doctors':doctors
    }
    return render(request)

def appoint_doctor(request):
    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id')
        predict = request.POST.get('predict')
        doctor = CustomUser.objects.get(id=doctor_id)
        appointment = Appoinment(
            customer = request.user,
            doctor=doctor,
            predict = predict,
        )
        appointment.save()
        # messages.success(request,'Appoinment Added Successfully')
        return redirect('view_appointments')

def view_appointments(request):
    appointments = Appoinment.objects.filter(customer = request.user)
    context ={
        'appointments':appointments
    }
    return render(request,'view_appointments.html',context)



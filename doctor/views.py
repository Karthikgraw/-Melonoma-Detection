from django.shortcuts import render,redirect
from users.models import *
# Create your views here.

def doctor_view_appointments(request):
    appointments = Appoinment.objects.filter(doctor=request.user)
    context = {
        'appointments':appointments
    }
    return render(request,'doctor_view_appointments.html',context)

def appointment_response(request):
    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        appointment = Appoinment.objects.get(id=appointment_id)
        appointment.reply=request.POST.get('reply')
        appointment.save()
        # messages.success(request,'Reply added succesfully')
        return redirect('doctor_view_appointments')

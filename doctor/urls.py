from django.urls import path
from . import views
urlpatterns = [
    path('doctor_view_appointments',views.doctor_view_appointments,name='doctor_view_appointments'),
    path('appointment_response',views.appointment_response,name='appointment_response'),
]

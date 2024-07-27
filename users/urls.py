from django.urls import path
from . import views
urlpatterns = [
    path('melanoma_prediction/',views.melanoma_prediction,name='melanoma_prediction'),
    path('get_melanoma_prediction/',views.get_melanoma_prediction,name='get_melanoma_prediction'),
    path('view_doctors/',views.view_doctors,name='view_doctors'),
    path('appoint_doctor',views.appoint_doctor,name='appoint_doctor'),
    path('view_appointments',views.view_appointments,name='view_appointments'),
]

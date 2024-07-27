from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #login_Path
    path('registration/', views.registration, name='registration'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('login/', views.Login, name='login'),
    path('doLogin', views.dologin2, name='doLogin'),
    path('doLogout', views.DoLogout, name='doLogout'),
    path('checkMail',views.CheckMail,name='checkMail'),
    path('forgotPassword', views.ForgotPassword, name='forgot_password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,get_user_model,authenticate
from django.contrib import messages
from .models import *
from django.db import transaction 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#email verirification
from verify_email.email_handler import send_verification_email

#forms
from .forms import *

#Django Mail
from django.core.mail import send_mail
import datetime

UserModel = get_user_model()

@transaction.atomic
def registration(request):
    cuform=CustomUserInputForm(request.POST, request.FILES)
    if request.method == "POST":
        if cuform.is_valid():
            email=cuform.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request, 'email is already taken')
                return redirect('registration')
            else:
                password=cuform.cleaned_data.get('password')
                user_form=cuform.save(commit=False)
                user_form.set_password(password)
                user_form.user_type='2'
                # user_data=send_verification_email(request,cuform)
                user_form.save()
                return redirect('login')
            
    else:
        cuform=CustomUserInputForm()

    context={
        'custom_user_form':cuform,
    }
    return render(request, 'register.html',context)

def register_doctor(request):
    cuform=CustomUserInputForm(request.POST, request.FILES)
    if request.method == "POST":
        if cuform.is_valid():
            email=cuform.cleaned_data.get('email')
            if CustomUser.objects.filter(email=email).exists():
                messages.warning(request, 'email is already taken')
                return redirect('register_doctor')
            else:
                password=cuform.cleaned_data.get('password')
                user_form=cuform.save(commit=False)
                user_form.set_password(password)
                user_form.user_type='3'
                # user_data=send_verification_email(request,cuform)
                user_form.save()
                return redirect('login')      
    else:
        cuform=CustomUserInputForm()
    context={
        'custom_user_form':cuform,
    }
    return render(request, 'register_doctor.html',context)


def Login(request):
    if request.method == "POST":
        username = request.POST.get('email')
    return render(request, 'login.html')


def dologin2(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user=UserModel.objects.get(email=email)
            print("first try block:",user)
            p2=user.password
            print(p2)
            if user.check_password(password):
                print("password check - true")
                user=authenticate(request,email=email,password=password)
                print("authentication begins",user)
                if user is not None:
                    try:
                        if user.user_type == '1':
                            login(request, user)
                            return redirect('get_current_weather')
                        elif user.user_type == '2':
                            login(request, user)
                            print("user login...")
                            return redirect('melanoma_prediction')
                        elif user.user_type == '3':
                            login(request, user)
                            print("Doctor login...")
                            return redirect('doctor_view_appointments')
                        else:
                            messages.error(request,'Invalid User Credentials (No user found)')
                        return redirect('login')
                    except:
                        pass
                else:
                    messages.error(request,'Email not Verified')
                    return redirect('login')
            else:
                messages.error(request,'Invalid Password')
                return redirect('login')
        except UserModel.DoesNotExist:
            messages.error(request,'No User Found')
            return redirect('login')
    return render(request, 'login.html')


def CheckMail(request):
    check_mail=request.POST.get('email2')
    user=UserModel.objects.get(email=check_mail)
    context={
        'user_data':user
    }
    if user is not None:
        return render(request,'forgot_password.html',context)
    else:
        messages.info(request,"sorry invalid mail id")
        redirect('login')
        
        
@transaction.atomic
def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get('mail')
        password = request.POST.get('password1')
        
        user_model = get_user_model()
        user = user_model.objects.get(email=email)
        user.set_password(password)
        user.save()
        now = datetime.datetime.now()
        mesage=f'Your password has been changed on {now}'
        send_mail(
            "Password Reset",
            f"Your Password Hase been Changed {now}",
            from_email=None,
            recipient_list=[email],
            fail_silently=False,
        )
        messages.success(request, 'Password Reset Successfull !')
        return redirect('login')
    return render(request, 'forgot_password.html')

def DoLogout(request):
    logout(request)
    return redirect('landing')


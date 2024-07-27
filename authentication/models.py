from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

class CustomUserManager(BaseUserManager):
    USER_CHOICES=(
        ('1','Admin'),
        ('2','User'),
    )
    
    def create_user(self,first_name,last_name,email,username,user_type,profile_pic,password=None):
        if not email:
            raise ValueError('The Email Must be set')
        email=self.normalize_email(email)
        user=self.model(first_name=first_name,last_name=last_name,username=username,user_type=user_type,email=email,profile_pic=profile_pic)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractUser):
    USER_CHOICES=(
        ('1','Admin'),
        ('2','User'),
    )
    email = models.EmailField(unique=True)
    user_type=models.CharField(choices=USER_CHOICES, max_length=50, default=1)
    profile_pic=models.ImageField(upload_to='static/templates/media/profile')
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
    def __str__(self):
        return str(self.first_name)



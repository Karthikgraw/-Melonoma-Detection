from django.db import models
from authentication.models import CustomUser
# Create your models here.

class Appoinment(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='customer_appoinments')
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='doctor_appoinments')
    predict = models.CharField(max_length=40)
    reply=models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.first_name}:{self.doctor.first_name}"



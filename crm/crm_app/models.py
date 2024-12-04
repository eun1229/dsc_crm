# crm/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in User model
    phone_number = models.CharField(max_length=15, blank=True)  
    company = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      # Track when the profile was last updated

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.now, blank=True)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True)  
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    condition = models.CharField(
        max_length=100,
        choices=[('schizophrenia', 'Schizophrenia Spectrum and Other Psychotic Disorders'), ('bipolar', 'Bipolar and Related Disorders'), ('depression', 'Depressive Disorders'), 
        ('anxiety', 'Anxiety Disorders'), ('ocd', 'Obsessive Compulsive and Related Disorders'), ('ptsd', 'Trauma and Stress Related Disorders'),],
        default='schizophrenia'
    )  
    diagnosis = models.CharField(
        max_length=100,
        choices=[('self', 'Self-Diagnosed'), ('clinical', 'Clinically Diagnosed'), ('evaulation', 'Not Diagnosed but Seeking Evaluation')],
        default='self'
    )
    insurance = models.CharField(
        max_length=100,
        choices=[('medicare', 'Medicare'), ('private', 'Private Insurance'), ('none', 'No Insurance')],
        default='none'
    )                                                           
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      # Track when the profile was last updated

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")

# crm/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to built-in User model
    phone_number = models.CharField(max_length=15, blank=True)  
    company = models.CharField(max_length=100, blank=True)      
    position = models.CharField(max_length=50, blank=True)      # Position in company
    address = models.CharField(max_length=255, blank=True)      # Physical address
    notes = models.TextField(blank=True)                        # Any notes or details about the client
    status = models.CharField(
        max_length=20,
        choices=[('lead', 'Lead'), ('customer', 'Customer'), ('inactive', 'Inactive')],
        default='lead'
    )                                                           # CRM-specific status, like lead, customer, or inactive
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      # Track when the profile was last updated

    def __str__(self):
        return f"{self.user.username}'s Profile"

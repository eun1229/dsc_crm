from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Record
from django.contrib.admin.widgets import AdminDateWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, max_length=15)
    company = forms.CharField(required=False, max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                company=self.cleaned_data['company']
            )
        return user

class AddPatientForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control form-field", "name":"patient-name"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control form-field", "name":"patient-last-name"}), label="")
    birthday = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date", "class":"form-control form-field", "name":"patient-bday"}), input_formats=["%Y-%m-%d"], label="Date of Birth")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control form-field contact-card", "name":"patient-email"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control form-field contact-card", "name":"patient-phone"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control form-field address-card", "name":"patient-address"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control form-field address-card", "name":"patient-city"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control form-field address-card", "name":"patient-state"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control form-field address-card", "name":"patient-zipcode"}), label="")

    class Meta:
        model = Record
        exclude = ("user",)
        labels = {
            'condition': "Disorder category that best describes the patient's condition.",
            'diagnosis': "What is the patient's diagnosis status?",
            'insurance': "Patient's insurance information",
        }

class UploadForm(forms.Form):
    csv_file = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder':
        'Upload "patients.csv"'}))
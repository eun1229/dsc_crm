from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, AddPatientForm, UploadForm
from django.views.generic.base import View, TemplateView
from .models import Record
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import io
import csv
from django.http import HttpResponseRedirect
from .models import Record

# Create your views here.

def index(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "Invalid login. Please try again.")
            return redirect('index')
    else:
        return render(request, 'crm_app/index.html', {'records' : records})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user and profile
            login(request, user)  # Log the user in after registration
            messages.success(request, "You have been successfully registered. Welcome!")
            return redirect('index')  # Redirect to a home page or dashboard
        else:
            form = CustomUserCreationForm()
            messages.success(request, "Failed to register")
            return render(request, 'crm_app/register.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'crm_app/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def patient_record(request, pk):
	if request.user.is_authenticated:
		patient_record = Record.objects.get(id=pk)
		return render(request, 'crm_app/patient_record.html', {'patient_record':patient_record})
	else:
		messages.success(request, "You must be logged in to view that page.")
		return redirect('view_patients')

def delete_patient(request, pk):
	if request.user.is_authenticated:
		patient_record = Record.objects.get(id=pk)
		patient_record.delete()
		messages.success(request, "Successfully deleted record.")
		return redirect('view_patients')
	else:
		messages.success(request, "You must be logged in to view that page.")
		return redirect('view_patients')

def add_patient(request):
    form = AddPatientForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_patient = form.save()
                messages.success(request, "Successfully added new patient.")
                return redirect("view_patients")
        return render(request, 'crm_app/add_patient.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('index')


def view_patients(request):
    if request.user.is_authenticated:
        patient_records = Record.objects.all()
        return render(request, 'crm_app/view_patients.html', {'patient_records':patient_records})
    else:
        messages.success(request, "You must be logged in to view that page.")
        return redirect('index')

# Function to upload the form, parse it, save to database
def decode_utf8(line_iterator):
    for line in line_iterator:
        yield line.decode('utf-8')


    
def create_upload(request):
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'crm_app/create_upload.html', {'form': form})

    form = UploadForm(request.POST, request.FILES)

    # Validate the form
    if form.is_valid():

        # Get the correct type string instead of byte without reading full file into memory with a generator to decode line by line
        patients_file = csv.reader(decode_utf8(request.FILES['sent_file']))
        next(patients_file)  # Skip header row

        for counter, line in enumerate(patients_file):
            first_name = line[1]
            last_name = line[2]
            email = line[3]
            phone = line[4]
            address = line[5]
            city = line[6]
            state = line[7]
            zipcode = line[8]
            birthday = line[11]
            condition = line[12]
            diagnosis = line[13]
            insurance = line[14]

            p = Record()
            p.first_name = first_name
            p.last_name = last_name
            p.email = email
            p.phone = phone
            p.address = address
            p.city = city
            p.state = state
            p.zipcode = zipcode
            p.birthday = birthday
            p.condition = condition
            p.diagnosis = diagnosis
            p.insurance = insurance

            p.save()

        messages.success(request, 'Saved successfully!')

        return redirect("view_patients")
        

# @login_required
# def user_list(request):
#     model = User  
#     template_name = 'crm_app/user_list.html'  
#     context_object_name = 'users'  # The name to use for the list of users in the template
#     paginate_by = 10  # Optional: adds pagination if there are many users

#     return User.objects.all().order_by('username')  # Adjust ordering as needed

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()  # Save the user and profile
#             login(request, user)  # Log the user in after registration
#             return redirect('index')  # Redirect to a home page or dashboard
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'crm_app/user_list.html', {'form': form})

# @method_decorator(login_required, name='dispatch')  # Ensures that only logged-in users can view the list
# class UserListView(ListView):
#     model = User  
#     template_name = 'crm_app/user_list.html'  
#     context_object_name = 'users'  # The name to use for the list of users in the template
#     paginate_by = 10  # Optional: adds pagination if there are many users

#     def get_queryset(self):
#         # Customize the queryset if needed (e.g., filtering or ordering)
#         return User.objects.all().order_by('username')  # Adjust ordering as needed
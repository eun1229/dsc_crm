from django.contrib import admin
from django.urls import path
from crm_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name="logout"),
    path('view_patients/', views.view_patients, name="view_patients"),
    path('patient_record/<int:pk>', views.patient_record, name="patient_record"),
    path('delete_patient/<int:pk>', views.delete_patient, name="delete_patient"),
    path('add_patient/', views.add_patient, name="add_patient"),
    path('create_upload/', views.create_upload, name="create_upload"),
]

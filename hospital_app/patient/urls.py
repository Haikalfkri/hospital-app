from django.urls import path
from patient import views

urlpatterns = [
    path("patient-dashboard", views.PatientDashboard, name="patient-dashboard"),
]

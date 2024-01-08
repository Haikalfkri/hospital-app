from django.shortcuts import render

# Create your views here.
def PatientDashboard(request):
    return render(request, "patient/base.html")
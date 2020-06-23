from django.contrib import admin
from .models import Prescription, Patient, PatientDetail


# Register your models here.
# todo: register Patient model
# admin.site.register(Patient)
# admin.site.register(PatientDetail)
admin.site.register(Prescription)

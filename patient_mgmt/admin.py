from django.contrib import admin

# Register your models here.

from patient_mgmt.models import Patient
admin.site.register(Patient)
#class PatientAdmin(admin.ModelAdmin):
#   fields = ['first_name', 'last_name', 'ssn']
#admin.site.register(Patient, PatientAdmin)

from patient_mgmt.models import Labs
admin.site.register(Labs)
from patient_mgmt.models import Diagnosis
admin.site.register(Diagnosis)
from patient_mgmt.models import Drug
admin.site.register(Drug)
from patient_mgmt.models import Drug_Interaction
admin.site.register(Drug_Interaction)
from patient_mgmt.models import Allergy
admin.site.register(Allergy)
from patient_mgmt.models import Personnel
admin.site.register(Personnel)
from patient_mgmt.models import Ownership
admin.site.register(Ownership)
from patient_mgmt.models import Doctor
admin.site.register(Doctor)
from patient_mgmt.models import Prescription
admin.site.register(Prescription)
from patient_mgmt.models import Appointment
admin.site.register(Appointment)
from patient_mgmt.models import Bed
admin.site.register(Bed)
from patient_mgmt.models import Corporation
admin.site.register(Corporation)
from patient_mgmt.models import Surgeon
admin.site.register(Surgeon)
from patient_mgmt.models import Procedure
admin.site.register(Procedure)
from patient_mgmt.models import Surgery_Type
admin.site.register(Surgery_Type)
from patient_mgmt.models import Nurse
admin.site.register(Nurse)
from patient_mgmt.models import Surgery
admin.site.register(Surgery)
from patient_mgmt.models import Nurse_Skill
admin.site.register(Nurse_Skill)
from patient_mgmt.models import Surgeon_Skill
admin.site.register(Surgeon_Skill)
from patient_mgmt.models import Admission
admin.site.register(Admission)

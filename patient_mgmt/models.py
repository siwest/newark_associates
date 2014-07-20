from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Diagnosis(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Diagnoses"

    def __unicode__(self):
        return self.code + " - " + self.description

class Patient(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    ssn = models.CharField(max_length=9)
    dob = models.DateField('Date of Birth')
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    diagnosis = models.ManyToManyField(Diagnosis)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    # def clean(self):
    #     if self.nurse_set.object.count > 1:
    #         raise ValidationError('A patient cannot have more than 1 nurse')
    #     if self.diagnosis_set.object.count < 1:
    #         raise ValidationError('A Patient must have at least one diagnosis')
    #     if self.appointment_set.object.count < 1 and self.admission_set.object.count < 1:
    #         raise ValidationError('A Patient must have at least one appointment or admission to be diagnosed')


class Labs(models.Model):
    patient = models.ForeignKey(Patient)
    blood_type = models.CharField(max_length=3)
    HDL = models.IntegerField()
    LDL = models.IntegerField()
    triglycerides = models.IntegerField()
    blood_sugar = models.IntegerField()
    is_high_risk_heart_disease = models.BooleanField()

    class Meta:
        verbose_name_plural = "Labs"


    def __unicode__(self):
        return self.patient.first_name + " " + self.patient.last_name


    def total_cholestorol(self):
        return self.HDL + self.LDL + (0.2 * self.triglycerides)

    def heart_disease_index(self):
        return self.total_cholestorol() / self.HDL

    def heart_disease_category(self):
        if self.is_high_risk_heart_disease:
            return "H"
        elif self.heart_disease_index() < 4:
            return "N"
        elif self.heart_disease_index() <= 5:
            return "L"
        elif self.heart_disease_index() > 5:
            return "M"
        else:
            return "unknown"






class Drug(models.Model):
    name = models.CharField(max_length=10)
    quantity_on_hand = models.IntegerField(max_length=10)
    quantity_on_order = models.IntegerField(max_length=10)
    year_to_date_usage = models.IntegerField(max_length=10)
    unit_cost = models.DecimalField(max_digits=3, decimal_places=2)

    def __unicode__(self):
        return self.name



class Drug_Interaction(models.Model):
    drug = models.ManyToManyField(Drug)
    interaction = models.CharField(max_length=30)
    severity_of_interaction = models.CharField(max_length=1)

    class Meta:
        verbose_name = "Drug Interaction"

    def __unicode__(self):
        return self.drug.name + ": " + self.interaction + " (" + self.severity_of_interaction + ")"



class Allergy(models.Model):
    patient = models.ManyToManyField(Patient)
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Allergies"

    def __unicode__(self):
        return self.patient.first_name + " " + self.patient.last_name + ", Allergy: " + self.name


class Personnel(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    ssn = models.CharField(max_length=9)
    dob = models.DateField('Date of Birth')
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    salary = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Personnel"

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Ownership(models.Model):
    percent_ownership = models.DecimalField(max_digits=5, decimal_places=2)

    def __unicode__(self):
        return unicode(self.percent_ownership)


    def clean(self):
        existing_total_percent = 0
        for ownership in Ownership.objects.all():
            existing_total_percent += ownership.percent_ownership
        if existing_total_percent + self.percent_ownership > 100:
            raise ValidationError('Total ownership of clinic cannot exceed 100%')


class Doctor(models.Model):
    personnel = models.ForeignKey(Personnel)
    ownership = models.ForeignKey(Ownership)

    def __unicode__(self):
        return "Dr. " + self.personnel.last_name

    # def clean(self):
    #     if self.patient_set.object.count not in range(7, 21):
    #         raise ValidationError('A Doctor must have between 7 and 20 patients')


class Prescription(models.Model):
    drug = models.ForeignKey(Drug)
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    dosage = models.CharField(max_length=10)
    frequency = models.CharField(max_length=10)

    def __unicode__(self):
        return self.patient.first_name + " " + self.patient.last_name + " is taking " + self.drug.name + " prescribed by Dr. " + self.doctor.personnel.last_name

    def clean(self):
        #check to see if patient already has a prescription for this drug by a different doctor
        if self.patient.prescription_set.filter(drug=self.drug).exclude(doctor=self.doctor).count() > 1:
            raise ValidationError('No two doctors can prescribe the same medication to a patient.')



class Appointment(models.Model):
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)
    time = models.DateTimeField('date')

    def __unicode__(self):
        return "Dr. " + self.doctor.personnel.last_name + " appointment with " + self.patient.first_name + " " + self.patient.last_name + " at " + unicode(self.time)


class Bed(models.Model):
    unit = models.CharField(max_length=5)
    room = models.CharField(max_length=5)
    bed = models.CharField(max_length=1)

    def __unicode__(self):
        return self.unit + " " + self.room + self.bed


class Corporation(models.Model):
    name = models.CharField(max_length=20)
    headquarters_city = models.CharField(max_length=20)
    headquarters_state = models.CharField(max_length=2)
    ownership = models.ForeignKey(Ownership)

    def __unicode__(self):
        return self.name

class Nurse_Skill(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Nurse Skill"

    def __unicode__(self):
        return self.name 

class Surgeon_Skill(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Surgeon Skill"

    def __unicode__(self):
        return self.name 

class Surgeon(models.Model):
    personnel = models.ForeignKey(Personnel)
    contract_type = models.CharField(max_length=30)
    contract_length = models.IntegerField(max_length=2)
    skills = models.ManyToManyField(Surgeon_Skill)
    def __unicode__(self):
        return "Dr. " + self.personnel.last_name


class Procedure(models.Model):
    name = models.CharField(max_length=70)
    date_time = models.DateTimeField('date')
    patient = models.ForeignKey(Patient)
    doctor = models.ForeignKey(Doctor)

    def __unicode__(self):
        return self.name + " procedure at " + unicode(self.date_time) + " on " + self.patient.first_name + " " + self.patient.last_name + " by Dr. " + self.doctor.personnel.last_name


class Surgery_Type(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=1)
    required_surgeon_skills = models.ManyToManyField(Surgeon_Skill)
    required_nurse_skills = models.ManyToManyField(Nurse_Skill)

    class Meta:
        verbose_name = "Surgery Type"

    def __unicode__(self):
        return self.name + "/" + self.category

    # def clean(self):
    #     if self.nurse_set.objects.count < 2:
    #         raise ValidationError('A surgery type cannot have less than 2 nurses.')


class Nurse(models.Model):
    personnel = models.ForeignKey(Personnel)
    grade = models.CharField(max_length=20)
    years_experience = models.IntegerField(max_length=2)
    skills = models.ManyToManyField(Nurse_Skill)

    def __unicode__(self):
        return "Nurse " + self.personnel.last_name

    # def clean(self):
    #     if self.patient_set.object.count < 5:
    #         raise ValidationError('A nurse cannot have less than 5 patients.')


class Surgery(models.Model):
    procedure = models.ForeignKey(Procedure)
    surgery_type = models.ForeignKey(Surgery_Type)
    anatomical_location = models.CharField(max_length=20)
    special_needs = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Surgeries"

    def __unicode__(self):
        return self.procedure.name + "/" + self.surgery_type.name + "/" + self.anatomical_location + " procedure at " + unicode(self.procedure.date_time) + " on " + self.procedure.patient.first_name + " " + self.procedure.patient.last_name + " by Dr. " + self.procedure.doctor.personnel.last_name



class Admission(models.Model):
    procedure = models.ManyToManyField(Procedure)
    unit = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    bed = models.CharField(max_length=10)
    start_stay = models.DateTimeField('date')
    end_stay = models.DateTimeField('date')

    def __unicode__(self):
        return "Dr. " + self.procedure.doctor.personnel.last_name + " appointment with " + self.procedure.patient.first_name + " " + self.procedure.patient.last_name + " at " + self.start_time + " " + self.end_time





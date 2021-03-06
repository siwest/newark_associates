# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Admission.unit'
        db.delete_column(u'patient_mgmt_admission', 'unit')

        # Deleting field 'Admission.room'
        db.delete_column(u'patient_mgmt_admission', 'room')


        # Renaming column for 'Admission.bed' to match new field type.
        db.rename_column(u'patient_mgmt_admission', 'bed', 'bed_id')
        # Changing field 'Admission.bed'
        db.alter_column(u'patient_mgmt_admission', 'bed_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Bed']))
        # Adding index on 'Admission', fields ['bed']
        db.create_index(u'patient_mgmt_admission', ['bed_id'])


    def backwards(self, orm):
        # Removing index on 'Admission', fields ['bed']
        db.delete_index(u'patient_mgmt_admission', ['bed_id'])

        # Adding field 'Admission.unit'
        db.add_column(u'patient_mgmt_admission', 'unit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Adding field 'Admission.room'
        db.add_column(u'patient_mgmt_admission', 'room',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


        # Renaming column for 'Admission.bed' to match new field type.
        db.rename_column(u'patient_mgmt_admission', 'bed_id', 'bed')
        # Changing field 'Admission.bed'
        db.alter_column(u'patient_mgmt_admission', 'bed', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        u'patient_mgmt.admission': {
            'Meta': {'object_name': 'Admission'},
            'bed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Bed']"}),
            'end_stay': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Procedure']", 'symmetrical': 'False'}),
            'start_stay': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'patient_mgmt.allergy': {
            'Meta': {'object_name': 'Allergy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reaction': ('django.db.models.fields.CharField', [], {'default': "'anaphylaxis'", 'max_length': '100'})
        },
        u'patient_mgmt.appointment': {
            'Meta': {'object_name': 'Appointment'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Patient']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'patient_mgmt.bed': {
            'Meta': {'object_name': 'Bed'},
            'bed': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'patient_mgmt.corporation': {
            'Meta': {'object_name': 'Corporation'},
            'headquarters_city': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'headquarters_state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ownership': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Ownership']"})
        },
        u'patient_mgmt.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'patient_mgmt.doctor': {
            'Meta': {'object_name': 'Doctor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ownership': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Ownership']"}),
            'personnel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Personnel']"})
        },
        u'patient_mgmt.drug': {
            'Meta': {'object_name': 'Drug'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'quantity_on_hand': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'quantity_on_order': ('django.db.models.fields.IntegerField', [], {'max_length': '10'}),
            'unit_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'year_to_date_usage': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'patient_mgmt.drug_interaction': {
            'Meta': {'object_name': 'Drug_Interaction'},
            'drug': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Drug']", 'symmetrical': 'False'}),
            'effect': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'severity_of_interaction': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'patient_mgmt.labs': {
            'HDL': ('django.db.models.fields.IntegerField', [], {}),
            'LDL': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Labs'},
            'blood_sugar': ('django.db.models.fields.IntegerField', [], {}),
            'blood_type': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_high_risk_heart_disease': ('django.db.models.fields.BooleanField', [], {}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Patient']"}),
            'triglycerides': ('django.db.models.fields.IntegerField', [], {})
        },
        u'patient_mgmt.nurse': {
            'Meta': {'object_name': 'Nurse'},
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personnel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Personnel']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Nurse_Skill']", 'symmetrical': 'False'}),
            'years_experience': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        u'patient_mgmt.nurse_skill': {
            'Meta': {'object_name': 'Nurse_Skill'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'patient_mgmt.ownership': {
            'Meta': {'object_name': 'Ownership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_ownership': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'patient_mgmt.patient': {
            'Meta': {'object_name': 'Patient'},
            'allergy': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Allergy']", 'symmetrical': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'diagnosis': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Diagnosis']", 'symmetrical': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'patient_mgmt.personnel': {
            'Meta': {'object_name': 'Personnel'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'patient_mgmt.prescription': {
            'Meta': {'object_name': 'Prescription'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Doctor']"}),
            'dosage': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'drug': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Drug']"}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Patient']"})
        },
        u'patient_mgmt.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Doctor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Patient']"})
        },
        u'patient_mgmt.surgeon': {
            'Meta': {'object_name': 'Surgeon'},
            'contract_length': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'contract_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personnel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Personnel']"}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Surgeon_Skill']", 'symmetrical': 'False'})
        },
        u'patient_mgmt.surgeon_skill': {
            'Meta': {'object_name': 'Surgeon_Skill'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'patient_mgmt.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'anatomical_location': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Procedure']"}),
            'special_needs': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'surgery_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['patient_mgmt.Surgery_Type']"})
        },
        u'patient_mgmt.surgery_type': {
            'Meta': {'object_name': 'Surgery_Type'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'required_nurse_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Nurse_Skill']", 'symmetrical': 'False'}),
            'required_surgeon_skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Surgeon_Skill']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['patient_mgmt']
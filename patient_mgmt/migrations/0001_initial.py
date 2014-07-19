# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table(u'patient_mgmt_patient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Patient'])

        # Adding model 'Labs'
        db.create_table(u'patient_mgmt_labs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Patient'])),
            ('blood_type', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('HDL', self.gf('django.db.models.fields.IntegerField')()),
            ('LDL', self.gf('django.db.models.fields.IntegerField')()),
            ('triglycerides', self.gf('django.db.models.fields.IntegerField')()),
            ('blood_sugar', self.gf('django.db.models.fields.IntegerField')()),
            ('is_high_risk_heart_disease', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'patient_mgmt', ['Labs'])

        # Adding model 'Diagnosis'
        db.create_table(u'patient_mgmt_diagnosis', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Diagnosis'])

        # Adding M2M table for field patient on 'Diagnosis'
        m2m_table_name = db.shorten_name(u'patient_mgmt_diagnosis_patient')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('diagnosis', models.ForeignKey(orm[u'patient_mgmt.diagnosis'], null=False)),
            ('patient', models.ForeignKey(orm[u'patient_mgmt.patient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['diagnosis_id', 'patient_id'])

        # Adding model 'Drug'
        db.create_table(u'patient_mgmt_drug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('quantity_on_hand', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('quantity_on_order', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('year_to_date_usage', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('unit_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Drug'])

        # Adding model 'Drug_Interaction'
        db.create_table(u'patient_mgmt_drug_interaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interaction', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('severity_of_interaction', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Drug_Interaction'])

        # Adding M2M table for field drug on 'Drug_Interaction'
        m2m_table_name = db.shorten_name(u'patient_mgmt_drug_interaction_drug')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('drug_interaction', models.ForeignKey(orm[u'patient_mgmt.drug_interaction'], null=False)),
            ('drug', models.ForeignKey(orm[u'patient_mgmt.drug'], null=False))
        ))
        db.create_unique(m2m_table_name, ['drug_interaction_id', 'drug_id'])

        # Adding model 'Allergy'
        db.create_table(u'patient_mgmt_allergy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Allergy'])

        # Adding M2M table for field patient on 'Allergy'
        m2m_table_name = db.shorten_name(u'patient_mgmt_allergy_patient')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('allergy', models.ForeignKey(orm[u'patient_mgmt.allergy'], null=False)),
            ('patient', models.ForeignKey(orm[u'patient_mgmt.patient'], null=False))
        ))
        db.create_unique(m2m_table_name, ['allergy_id', 'patient_id'])

        # Adding model 'Personnel'
        db.create_table(u'patient_mgmt_personnel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('salary', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Personnel'])

        # Adding model 'Ownership'
        db.create_table(u'patient_mgmt_ownership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('percent_ownership', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Ownership'])

        # Adding model 'Doctor'
        db.create_table(u'patient_mgmt_doctor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('personnel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Personnel'])),
            ('ownership', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Ownership'])),
        ))
        db.send_create_signal(u'patient_mgmt', ['Doctor'])

        # Adding model 'Prescription'
        db.create_table(u'patient_mgmt_prescription', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Drug'])),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Doctor'])),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Patient'])),
            ('dosage', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Prescription'])

        # Adding model 'Appointment'
        db.create_table(u'patient_mgmt_appointment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Patient'])),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Doctor'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'patient_mgmt', ['Appointment'])

        # Adding model 'Bed'
        db.create_table(u'patient_mgmt_bed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('bed', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Bed'])

        # Adding model 'Corporation'
        db.create_table(u'patient_mgmt_corporation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('headquarters_city', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('headquarters_state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ownership', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Ownership'])),
        ))
        db.send_create_signal(u'patient_mgmt', ['Corporation'])

        # Adding model 'Nurse_Skill'
        db.create_table(u'patient_mgmt_nurse_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Nurse_Skill'])

        # Adding model 'Surgeon_Skill'
        db.create_table(u'patient_mgmt_surgeon_skill', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Surgeon_Skill'])

        # Adding model 'Surgeon'
        db.create_table(u'patient_mgmt_surgeon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('personnel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Personnel'])),
            ('contract_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('contract_length', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Surgeon'])

        # Adding M2M table for field skills on 'Surgeon'
        m2m_table_name = db.shorten_name(u'patient_mgmt_surgeon_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('surgeon', models.ForeignKey(orm[u'patient_mgmt.surgeon'], null=False)),
            ('surgeon_skill', models.ForeignKey(orm[u'patient_mgmt.surgeon_skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['surgeon_id', 'surgeon_skill_id'])

        # Adding model 'Procedure'
        db.create_table(u'patient_mgmt_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Patient'])),
            ('doctor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Doctor'])),
        ))
        db.send_create_signal(u'patient_mgmt', ['Procedure'])

        # Adding model 'Surgery_Type'
        db.create_table(u'patient_mgmt_surgery_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Surgery_Type'])

        # Adding M2M table for field required_surgeon_skills on 'Surgery_Type'
        m2m_table_name = db.shorten_name(u'patient_mgmt_surgery_type_required_surgeon_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('surgery_type', models.ForeignKey(orm[u'patient_mgmt.surgery_type'], null=False)),
            ('surgeon_skill', models.ForeignKey(orm[u'patient_mgmt.surgeon_skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['surgery_type_id', 'surgeon_skill_id'])

        # Adding M2M table for field required_nurse_skills on 'Surgery_Type'
        m2m_table_name = db.shorten_name(u'patient_mgmt_surgery_type_required_nurse_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('surgery_type', models.ForeignKey(orm[u'patient_mgmt.surgery_type'], null=False)),
            ('nurse_skill', models.ForeignKey(orm[u'patient_mgmt.nurse_skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['surgery_type_id', 'nurse_skill_id'])

        # Adding model 'Nurse'
        db.create_table(u'patient_mgmt_nurse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('personnel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Personnel'])),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('years_experience', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Nurse'])

        # Adding M2M table for field skills on 'Nurse'
        m2m_table_name = db.shorten_name(u'patient_mgmt_nurse_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nurse', models.ForeignKey(orm[u'patient_mgmt.nurse'], null=False)),
            ('nurse_skill', models.ForeignKey(orm[u'patient_mgmt.nurse_skill'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nurse_id', 'nurse_skill_id'])

        # Adding model 'Surgery'
        db.create_table(u'patient_mgmt_surgery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Procedure'])),
            ('surgery_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patient_mgmt.Surgery_Type'])),
            ('anatomical_location', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('special_needs', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'patient_mgmt', ['Surgery'])

        # Adding model 'Admission'
        db.create_table(u'patient_mgmt_admission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bed', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('start_stay', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_stay', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'patient_mgmt', ['Admission'])

        # Adding M2M table for field procedure on 'Admission'
        m2m_table_name = db.shorten_name(u'patient_mgmt_admission_procedure')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('admission', models.ForeignKey(orm[u'patient_mgmt.admission'], null=False)),
            ('procedure', models.ForeignKey(orm[u'patient_mgmt.procedure'], null=False))
        ))
        db.create_unique(m2m_table_name, ['admission_id', 'procedure_id'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table(u'patient_mgmt_patient')

        # Deleting model 'Labs'
        db.delete_table(u'patient_mgmt_labs')

        # Deleting model 'Diagnosis'
        db.delete_table(u'patient_mgmt_diagnosis')

        # Removing M2M table for field patient on 'Diagnosis'
        db.delete_table(db.shorten_name(u'patient_mgmt_diagnosis_patient'))

        # Deleting model 'Drug'
        db.delete_table(u'patient_mgmt_drug')

        # Deleting model 'Drug_Interaction'
        db.delete_table(u'patient_mgmt_drug_interaction')

        # Removing M2M table for field drug on 'Drug_Interaction'
        db.delete_table(db.shorten_name(u'patient_mgmt_drug_interaction_drug'))

        # Deleting model 'Allergy'
        db.delete_table(u'patient_mgmt_allergy')

        # Removing M2M table for field patient on 'Allergy'
        db.delete_table(db.shorten_name(u'patient_mgmt_allergy_patient'))

        # Deleting model 'Personnel'
        db.delete_table(u'patient_mgmt_personnel')

        # Deleting model 'Ownership'
        db.delete_table(u'patient_mgmt_ownership')

        # Deleting model 'Doctor'
        db.delete_table(u'patient_mgmt_doctor')

        # Deleting model 'Prescription'
        db.delete_table(u'patient_mgmt_prescription')

        # Deleting model 'Appointment'
        db.delete_table(u'patient_mgmt_appointment')

        # Deleting model 'Bed'
        db.delete_table(u'patient_mgmt_bed')

        # Deleting model 'Corporation'
        db.delete_table(u'patient_mgmt_corporation')

        # Deleting model 'Nurse_Skill'
        db.delete_table(u'patient_mgmt_nurse_skill')

        # Deleting model 'Surgeon_Skill'
        db.delete_table(u'patient_mgmt_surgeon_skill')

        # Deleting model 'Surgeon'
        db.delete_table(u'patient_mgmt_surgeon')

        # Removing M2M table for field skills on 'Surgeon'
        db.delete_table(db.shorten_name(u'patient_mgmt_surgeon_skills'))

        # Deleting model 'Procedure'
        db.delete_table(u'patient_mgmt_procedure')

        # Deleting model 'Surgery_Type'
        db.delete_table(u'patient_mgmt_surgery_type')

        # Removing M2M table for field required_surgeon_skills on 'Surgery_Type'
        db.delete_table(db.shorten_name(u'patient_mgmt_surgery_type_required_surgeon_skills'))

        # Removing M2M table for field required_nurse_skills on 'Surgery_Type'
        db.delete_table(db.shorten_name(u'patient_mgmt_surgery_type_required_nurse_skills'))

        # Deleting model 'Nurse'
        db.delete_table(u'patient_mgmt_nurse')

        # Removing M2M table for field skills on 'Nurse'
        db.delete_table(db.shorten_name(u'patient_mgmt_nurse_skills'))

        # Deleting model 'Surgery'
        db.delete_table(u'patient_mgmt_surgery')

        # Deleting model 'Admission'
        db.delete_table(u'patient_mgmt_admission')

        # Removing M2M table for field procedure on 'Admission'
        db.delete_table(db.shorten_name(u'patient_mgmt_admission_procedure'))


    models = {
        u'patient_mgmt.admission': {
            'Meta': {'object_name': 'Admission'},
            'bed': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'end_stay': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Procedure']", 'symmetrical': 'False'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_stay': ('django.db.models.fields.DateTimeField', [], {}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'patient_mgmt.allergy': {
            'Meta': {'object_name': 'Allergy'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'patient': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Patient']", 'symmetrical': 'False'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['patient_mgmt.Patient']", 'symmetrical': 'False'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interaction': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
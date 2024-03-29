# Generated by Django 2.2.4 on 2019-10-21 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(default='', max_length=100)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('middlename', models.CharField(default='', max_length=100)),
                ('suffix', models.CharField(default='', max_length=100)),
                ('prefix', models.CharField(default='', max_length=100)),
                ('sex', models.CharField(default='', max_length=100)),
                ('birthdate', models.CharField(default='', max_length=100)),
                ('birthplace', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='profile_pics')),
                ('userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('room', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('symptom', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'appointment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ClinicSchedule',
            fields=[
                ('clinic_schedule_id', models.AutoField(primary_key=True, serialize=False)),
                ('clinic_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('day', models.CharField(max_length=100)),
                ('first_start_hour', models.IntegerField()),
                ('first_start_minute', models.IntegerField()),
                ('first_end_hour', models.IntegerField()),
                ('first_end_minute', models.IntegerField()),
                ('second_start_hour', models.IntegerField()),
                ('second_start_minute', models.IntegerField()),
                ('second_end_hour', models.IntegerField()),
                ('second_end_minute', models.IntegerField()),
                ('third_start_hour', models.IntegerField()),
                ('third_start_minute', models.IntegerField()),
                ('third_end_hour', models.IntegerField()),
                ('third_end_minute', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'clinic_schedule',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Consulation',
            fields=[
                ('consulation_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationAssessment',
            fields=[
                ('consulation_assessment_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('diagnosis', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_assessment',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationAssessmentRemark',
            fields=[
                ('consulation_assessment_remark_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('remark', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_assessment_remark',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationObjective',
            fields=[
                ('consulation_objective_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('vitals_wt', models.CharField(max_length=100)),
                ('vitals_hr', models.CharField(max_length=100)),
                ('vitals_rr', models.CharField(max_length=100)),
                ('vitals_bmi', models.CharField(max_length=100)),
                ('vitals_ht', models.CharField(max_length=100)),
                ('vitals_bt', models.CharField(max_length=100)),
                ('vitals_spo2', models.CharField(max_length=100)),
                ('vitals_bp', models.CharField(max_length=100)),
                ('vision_r', models.CharField(max_length=100)),
                ('vision_l', models.CharField(max_length=100)),
                ('pupils', models.CharField(max_length=100)),
                ('glasses_lenses', models.CharField(max_length=100)),
                ('hearing', models.CharField(max_length=100)),
                ('physical_exam', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_objective',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationObjectiveFile',
            fields=[
                ('consulation_objective_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_objective_id', models.IntegerField()),
                ('file_path', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_objective_file',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationObjectiveImage',
            fields=[
                ('consulation_objective_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_objective_id', models.IntegerField()),
                ('file_path', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_objective_image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationObjectiveRemark',
            fields=[
                ('consulation_objective_remark_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_objective_id', models.IntegerField()),
                ('remark', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_objective_remark',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationPlan',
            fields=[
                ('consulation_plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('plan', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_plan',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationPlanPrescription',
            fields=[
                ('consulation_plan_test_prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('prescription_id', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_plan_prescription',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationPlanRemark',
            fields=[
                ('consulation_plan_remark_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('remark', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_plan_remark',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationPlanTestRequest',
            fields=[
                ('consulation_plan_test_request_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('test_request', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_plan_test_request',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ConsulationSubjective',
            fields=[
                ('consulation_subjective_id', models.AutoField(primary_key=True, serialize=False)),
                ('consulation_id', models.IntegerField()),
                ('chief_complaint', models.CharField(max_length=100)),
                ('history_present_illness', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'consulation_subjective',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('suffix', models.CharField(max_length=100)),
                ('prefix', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('birthdate', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'doctor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('laboratory_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('lab_name', models.CharField(max_length=100)),
                ('result_date', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('allowed', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'laboratory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LaboratoryImage',
            fields=[
                ('laboratory_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('image_path', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'laboratory_image',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalNote',
            fields=[
                ('medical_note_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('allowed', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'medical_note',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalNoteMedicalCertificate',
            fields=[
                ('medical_note_medical_certificate_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('hospital_no', models.CharField(max_length=100)),
                ('complete_address', models.CharField(max_length=100)),
                ('first_date', models.CharField(max_length=100)),
                ('second_date', models.CharField(max_length=100)),
                ('third_date', models.CharField(max_length=100)),
                ('complete_diagnosis', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'medical_note_medical_certificate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalNoteMedicalClearance',
            fields=[
                ('medical_note_medical_clearance_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('first_date', models.CharField(max_length=100)),
                ('second_date', models.CharField(max_length=100)),
                ('remark', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'medical_note_medical_clearance',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MedicalNoteText',
            fields=[
                ('medical_note_text_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'medical_note_text',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('generic_name', models.CharField(max_length=100)),
                ('dose', models.CharField(max_length=100)),
                ('form', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'medicine',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('prescription_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('allowed', models.IntegerField()),
                ('deleted', models.IntegerField()),
            ],
            options={
                'db_table': 'prescription',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PrescriptionChild',
            fields=[
                ('prescription_child_id', models.AutoField(primary_key=True, serialize=False)),
                ('prescription_id', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('clinic_id', models.IntegerField()),
                ('generic_name', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('dose', models.IntegerField()),
                ('form', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('frequency_sig', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('favorite', models.IntegerField()),
                ('timestamp', models.IntegerField()),
            ],
            options={
                'db_table': 'prescription_child',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_id', models.IntegerField()),
                ('lastname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('suffix', models.CharField(max_length=100)),
                ('prefix', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('birthdate', models.CharField(max_length=100)),
                ('birthplace', models.CharField(max_length=100)),
                ('blood_type', models.CharField(max_length=100)),
                ('id_no', models.CharField(default='', max_length=100)),
                ('civil_status', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('tel_no', models.CharField(max_length=100)),
                ('home_address', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('employer_name', models.CharField(max_length=100)),
                ('employer_no', models.CharField(max_length=100)),
                ('employer_address', models.CharField(max_length=100)),
                ('emergency_name', models.CharField(max_length=100)),
                ('emergency_address', models.CharField(max_length=100)),
                ('emergency_no', models.CharField(max_length=100)),
                ('emergency_relationship', models.CharField(max_length=100)),
                ('referring_physician', models.CharField(max_length=100)),
                ('primarycare_physician', models.CharField(max_length=100)),
                ('other_physician', models.CharField(max_length=100)),
                ('hmo', models.TextField(db_column='HMO')),
                ('hmo_card', models.TextField(db_column='HMO_card')),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('doctor', models.ManyToManyField(to='projectMain.Account')),
                ('userName', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'patient',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deleted', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectMain.Account')),
            ],
            options={
                'db_table': 'clinic',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.IntegerField(choices=[(1, 'Doctor'), (2, 'Patient'), (3, 'Laboratory Specialist'), (4, 'Nurse'), (5, 'Encoder')], default=0)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'account_type',
                'managed': True,
            },
        ),
    ]

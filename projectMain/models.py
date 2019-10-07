# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    email_address = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'account'


class AccountType(models.Model):
    account_type_id = models.AutoField(primary_key=True)
    access = models.TextField()

    class Meta:
        managed = False
        db_table = 'account_type'


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    room = models.TextField()
    date = models.TextField()
    symptom = models.TextField()
    note = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'appointment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    name = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clinic'


class ClinicSchedule(models.Model):
    clinic_schedule_id = models.AutoField(primary_key=True)
    clinic_id = models.IntegerField()
    doctor_id = models.IntegerField()
    day = models.TextField()
    first_start_hour = models.IntegerField()
    first_start_minute = models.IntegerField()
    first_end_hour = models.IntegerField()
    first_end_minute = models.IntegerField()
    second_start_hour = models.IntegerField()
    second_start_minute = models.IntegerField()
    second_end_hour = models.IntegerField()
    second_end_minute = models.IntegerField()
    third_start_hour = models.IntegerField()
    third_start_minute = models.IntegerField()
    third_end_hour = models.IntegerField()
    third_end_minute = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clinic_schedule'


class Consulation(models.Model):
    consulation_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation'


class ConsulationAssessment(models.Model):
    consulation_assessment_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    diagnosis = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_assessment'


class ConsulationAssessmentRemark(models.Model):
    consulation_assessment_remark_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    remark = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_assessment_remark'


class ConsulationObjective(models.Model):
    consulation_objective_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    vitals_wt = models.TextField()
    vitals_hr = models.TextField()
    vitals_rr = models.TextField()
    vitals_bmi = models.TextField()
    vitals_ht = models.TextField()
    vitals_bt = models.TextField()
    vitals_spo2 = models.TextField()
    vitals_bp = models.TextField()
    vision_r = models.TextField()
    vision_l = models.TextField()
    pupils = models.TextField()
    glasses_lenses = models.TextField()
    hearing = models.TextField()
    physical_exam = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_objective'


class ConsulationObjectiveFile(models.Model):
    consulation_objective_file_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    file_path = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_objective_file'


class ConsulationObjectiveImage(models.Model):
    consulation_objective_image_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    file_path = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_objective_image'


class ConsulationObjectiveRemark(models.Model):
    consulation_objective_remark_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    remark = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_objective_remark'


class ConsulationPlan(models.Model):
    consulation_plan_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    plan = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_plan'


class ConsulationPlanPrescription(models.Model):
    consulation_plan_test_prescription_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    prescription_id = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_plan_prescription'


class ConsulationPlanRemark(models.Model):
    consulation_plan_remark_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    remark = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_plan_remark'


class ConsulationPlanTestRequest(models.Model):
    consulation_plan_test_request_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    test_request = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_plan_test_request'


class ConsulationSubjective(models.Model):
    consulation_subjective_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    chief_complaint = models.TextField()
    history_present_illness = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'consulation_subjective'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    lastname = models.TextField()
    firstname = models.TextField()
    middlename = models.TextField()
    suffix = models.TextField()
    prefix = models.TextField()
    sex = models.TextField()
    birthdate = models.TextField()
    birthplace = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doctor'


class Laboratory(models.Model):
    laboratory_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    type = models.TextField()
    lab_name = models.TextField()
    result_date = models.TextField()
    remark = models.TextField()
    allowed = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'laboratory'


class LaboratoryImage(models.Model):
    laboratory_image_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    image_path = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'laboratory_image'


class MedicalNote(models.Model):
    medical_note_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    allowed = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medical_note'


class MedicalNoteMedicalCertificate(models.Model):
    medical_note_medical_certificate_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    hospital_no = models.TextField()
    complete_address = models.TextField()
    first_date = models.TextField()
    second_date = models.TextField()
    third_date = models.TextField()
    complete_diagnosis = models.TextField()
    remark = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medical_note_medical_certificate'


class MedicalNoteMedicalClearance(models.Model):
    medical_note_medical_clearance_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    first_date = models.TextField()
    second_date = models.TextField()
    remark = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medical_note_medical_clearance'


class MedicalNoteText(models.Model):
    medical_note_text_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    title = models.TextField()
    date = models.TextField()
    text = models.TextField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medical_note_text'


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    generic_name = models.TextField()
    dose = models.TextField()
    form = models.TextField()
    price = models.FloatField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medicine'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    clinic_id = models.IntegerField()
    doctor_id = models.IntegerField()
    lastname = models.TextField()
    firstname = models.TextField()
    middlename = models.TextField()
    suffix = models.TextField()
    prefix = models.TextField()
    sex = models.TextField()
    birthdate = models.TextField()
    birthplace = models.TextField()
    blood_type = models.TextField()
    id_no = models.TextField()
    civil_status = models.TextField()
    nationality = models.TextField()
    religion = models.TextField()
    contact_no = models.TextField()
    tel_no = models.TextField()
    home_address = models.TextField()
    province = models.TextField()
    occupation = models.TextField()
    employer_name = models.TextField()
    employer_no = models.TextField()
    employer_address = models.TextField()
    emergency_name = models.TextField()
    emergency_address = models.TextField()
    emergency_no = models.TextField()
    emergency_relationship = models.TextField()
    referring_physician = models.TextField()
    primarycare_physician = models.TextField()
    other_physician = models.TextField()
    hmo = models.TextField(db_column='HMO')  # Field name made lowercase.
    hmo_card = models.TextField(db_column='HMO_card')  # Field name made lowercase.
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'patient'


class Prescription(models.Model):
    prescription_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    allowed = models.IntegerField()
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prescription'


class PrescriptionChild(models.Model):
    prescription_child_id = models.AutoField(primary_key=True)
    prescription_id = models.IntegerField()
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    generic_name = models.TextField()
    brand_name = models.TextField()
    dose = models.IntegerField()
    form = models.TextField()
    quantity = models.IntegerField()
    frequency_sig = models.TextField()
    duration = models.IntegerField()
    deleted = models.IntegerField()
    favorite = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prescription_child'

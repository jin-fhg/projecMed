# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    #account_id = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=100)
    #password = models.CharField(max_length=100)
    userName = models.OneToOneField(User, on_delete=models.CASCADE)
    #email_address = models.CharField(max_length=100)
    accType = models.CharField(max_length=100,  default="")
    lastname = models.CharField(max_length=100,  default="")
    firstname = models.CharField(max_length=100,  default="")
    middlename = models.CharField(max_length=100,  default="")
    suffix = models.CharField(max_length=100,  default="")
    prefix = models.CharField(max_length=100,  default="")
    sex = models.CharField(max_length=100,  default="")
    birthdate = models.CharField(max_length=100, default='')
    birthplace = models.CharField(max_length=100, default='')
    image = models.ImageField(default='', upload_to='profile_pics', blank=True)
    #deleted = models.IntegerField()
    #timestamp = models.IntegerField()

    def __str__(self):
        return f'{self.userName.username} Profile'

    class Meta:
        managed = True
        db_table = 'account'


class AccountType(models.Model):
    #account_type_id = models.AutoField(primary_key=True)
    access = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.access} AccountType'

    class Meta:
        managed = True
        db_table = 'account_type'


class Appointment(models.Model):
    #appointment_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    room = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    symptom = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'appointment'


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    name = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'clinic'


class ClinicSchedule(models.Model):
    clinic_schedule_id = models.AutoField(primary_key=True)
    clinic_id = models.IntegerField()
    doctor_id = models.IntegerField()
    day = models.CharField(max_length=100)
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
        managed = True
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
        managed = True
        db_table = 'consulation'


class ConsulationAssessment(models.Model):
    consulation_assessment_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    diagnosis = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_assessment'


class ConsulationAssessmentRemark(models.Model):
    consulation_assessment_remark_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    remark = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_assessment_remark'


class ConsulationObjective(models.Model):
    consulation_objective_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    vitals_wt = models.CharField(max_length=100)
    vitals_hr = models.CharField(max_length=100)
    vitals_rr = models.CharField(max_length=100)
    vitals_bmi = models.CharField(max_length=100)
    vitals_ht = models.CharField(max_length=100)
    vitals_bt = models.CharField(max_length=100)
    vitals_spo2 = models.CharField(max_length=100)
    vitals_bp = models.CharField(max_length=100)
    vision_r = models.CharField(max_length=100)
    vision_l = models.CharField(max_length=100)
    pupils = models.CharField(max_length=100)
    glasses_lenses = models.CharField(max_length=100)
    hearing = models.CharField(max_length=100)
    physical_exam = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_objective'


class ConsulationObjectiveFile(models.Model):
    consulation_objective_file_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    file_path = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_objective_file'


class ConsulationObjectiveImage(models.Model):
    consulation_objective_image_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    file_path = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_objective_image'


class ConsulationObjectiveRemark(models.Model):
    consulation_objective_remark_id = models.AutoField(primary_key=True)
    consulation_objective_id = models.IntegerField()
    remark = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_objective_remark'


class ConsulationPlan(models.Model):
    consulation_plan_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    plan = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_plan'


class ConsulationPlanPrescription(models.Model):
    consulation_plan_test_prescription_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    prescription_id = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_plan_prescription'


class ConsulationPlanRemark(models.Model):
    consulation_plan_remark_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    remark = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_plan_remark'


class ConsulationPlanTestRequest(models.Model):
    consulation_plan_test_request_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    test_request = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_plan_test_request'


class ConsulationSubjective(models.Model):
    consulation_subjective_id = models.AutoField(primary_key=True)
    consulation_id = models.IntegerField()
    chief_complaint = models.CharField(max_length=100)
    history_present_illness = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'consulation_subjective'




class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'doctor'


class Laboratory(models.Model):
    laboratory_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    type = models.CharField(max_length=100)
    lab_name = models.CharField(max_length=100)
    result_date = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    allowed = models.IntegerField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'laboratory'


class LaboratoryImage(models.Model):
    laboratory_image_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    image_path = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
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
        managed = True
        db_table = 'medical_note'


class MedicalNoteMedicalCertificate(models.Model):
    medical_note_medical_certificate_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    hospital_no = models.CharField(max_length=100)
    complete_address = models.CharField(max_length=100)
    first_date = models.CharField(max_length=100)
    second_date = models.CharField(max_length=100)
    third_date = models.CharField(max_length=100)
    complete_diagnosis = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'medical_note_medical_certificate'


class MedicalNoteMedicalClearance(models.Model):
    medical_note_medical_clearance_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    first_date = models.CharField(max_length=100)
    second_date = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'medical_note_medical_clearance'


class MedicalNoteText(models.Model):
    medical_note_text_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'medical_note_text'


class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    generic_name = models.CharField(max_length=100)
    dose = models.CharField(max_length=100)
    form = models.CharField(max_length=100)
    price = models.FloatField()
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'medicine'


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    account_id = models.IntegerField()
    clinic_id = models.IntegerField()
    doctor_id = models.IntegerField()
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    birthdate = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=100)
    id_no = models.CharField(max_length=100)
    civil_status = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    tel_no = models.CharField(max_length=100)
    home_address = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    employer_name = models.CharField(max_length=100)
    employer_no = models.CharField(max_length=100)
    employer_address = models.CharField(max_length=100)
    emergency_name = models.CharField(max_length=100)
    emergency_address = models.CharField(max_length=100)
    emergency_no = models.CharField(max_length=100)
    emergency_relationship = models.CharField(max_length=100)
    referring_physician = models.CharField(max_length=100)
    primarycare_physician = models.CharField(max_length=100)
    other_physician = models.CharField(max_length=100)
    hmo = models.TextField(db_column='HMO')  # Field name made lowercase.
    hmo_card = models.TextField(db_column='HMO_card')  # Field name made lowercase.
    deleted = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
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
        managed = True
        db_table = 'prescription'


class PrescriptionChild(models.Model):
    prescription_child_id = models.AutoField(primary_key=True)
    prescription_id = models.IntegerField()
    account_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_id = models.IntegerField()
    clinic_id = models.IntegerField()
    generic_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    dose = models.IntegerField()
    form = models.CharField(max_length=100)
    quantity = models.IntegerField()
    frequency_sig = models.CharField(max_length=100)
    duration = models.IntegerField()
    deleted = models.IntegerField()
    favorite = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'prescription_child'

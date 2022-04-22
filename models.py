# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ConsultationCharges(models.Model):
    doc_id = models.IntegerField()
    loc_id = models.IntegerField()
    video_consultation_charges = models.CharField(max_length=10)
    physical_consultation_charges = models.CharField(max_length=10)
    currency_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'consultation_charges'


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
    id = models.BigAutoField(primary_key=True)
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


class DoctorLicense(models.Model):
    doc_id = models.IntegerField()
    license_name = models.CharField(max_length=100)
    license_issue_date = models.DateField()
    license_expiry_date = models.DateField()
    license_authority = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'doctor_license'


class DoctorSchedule(models.Model):
    doc_id = models.CharField(max_length=20)
    loc_id = models.CharField(max_length=20)
    from_field = models.DateTimeField(db_column='from')  # Field renamed because it was a Python reserved word.
    to = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'doctor_schedule'


class MyAppCustomer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=200)
    family_code = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    email_id = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.CharField(max_length=100)
    primary_member = models.IntegerField()
    date_of_birth = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_customer'


class MyAppDoctor(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=20, blank=True, null=True)
    speciality = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_id = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=10000, blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, blank=True, null=True)
    location_id = models.CharField(max_length=50, blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.CharField(max_length=100)
    signature_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'my_app_doctor'


class MyAppDoctorConsaltanciesCharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    doctor_id = models.CharField(max_length=200, blank=True, null=True)
    location_id = models.CharField(max_length=1000, blank=True, null=True)
    video_consultancy_fees = models.CharField(max_length=1000, blank=True, null=True)
    physical_consultancy_fees = models.CharField(max_length=1000, blank=True, null=True)
    currency_type = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_doctor_consaltancies_charge'


class MyAppDoctorLicense(models.Model):
    id = models.BigAutoField(primary_key=True)
    doctor_id = models.CharField(max_length=30, blank=True, null=True)
    license_no = models.CharField(max_length=100, blank=True, null=True)
    license_issue_date = models.CharField(max_length=100, blank=True, null=True)
    license_issuing_authority = models.CharField(max_length=100, blank=True, null=True)
    license_expiry_date = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_doctor_license'


class MyAppDoctorLoccation(models.Model):
    doc_id = models.CharField(max_length=30, blank=True, null=True)
    loc_id = models.CharField(primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'my_app_doctor_loccation'


class MyAppDoctorSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    doctor_id = models.CharField(max_length=200, blank=True, null=True)
    location_id = models.CharField(max_length=1000, blank=True, null=True)
    day = models.CharField(max_length=100, blank=True, null=True)
    field_from = models.CharField(db_column='_from', max_length=100, blank=True, null=True)  # Field renamed because it started with '_'.
    to = models.CharField(max_length=100, blank=True, null=True)
    time_zone_offset = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_doctor_schedule'


class MyAppDoctorsLocation(models.Model):
    location_id = models.CharField(primary_key=True, max_length=256)
    doc_user_id = models.CharField(max_length=256, blank=True, null=True)
    clinic_name = models.CharField(max_length=256, blank=True, null=True)
    building_name = models.CharField(max_length=256, blank=True, null=True)
    area = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.CharField(max_length=256, blank=True, null=True)
    longitude = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=256, blank=True, null=True)
    state = models.CharField(max_length=256, blank=True, null=True)
    pin_code = models.CharField(max_length=256, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_doctors_location'


class MyAppDoctorsSpecialitie(models.Model):
    id = models.BigAutoField(primary_key=True)
    speciality = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_doctors_specialitie'


class MyAppInsuranceCompanyMaster(models.Model):
    insurance_company_name = models.CharField(db_column='Insurance Company Name', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'my_app_insurance_company_master'


class MyAppMedicalConditionDisease(models.Model):
    id = models.BigAutoField(primary_key=True)
    icd_code = models.CharField(max_length=200, blank=True, null=True)
    disease = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_medical_condition_disease'


class MyAppMedicalConditionsMaster(models.Model):
    icd_code = models.CharField(max_length=7, blank=True, null=True)
    disease = models.CharField(max_length=228, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_medical_conditions_master'


class MyAppPatientMedicalCondition(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_code = models.CharField(max_length=200, blank=True, null=True)
    condition_name = models.CharField(max_length=200, blank=True, null=True)
    since_how_long = models.CharField(max_length=200, blank=True, null=True)
    medicine = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_patient_medical_condition'


class MyAppPatientMedicalReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_code = models.CharField(max_length=200, blank=True, null=True)
    report_name = models.CharField(max_length=200, blank=True, null=True)
    report_image = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_app_patient_medical_report'


class MyAppTpaNameMaster(models.Model):
    tpa_name = models.CharField(db_column='TPA Name', max_length=57, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'my_app_tpa_name_master'

from django.db import models

# Create your models here.
class Doctor(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True,null=False,blank=False)
    name = models.CharField(max_length=20, default='', blank=True, null=True)
    speciality = models.CharField(max_length=50, default='', blank=True, null=True)
    date_of_birth = models.CharField(max_length=50, default='', blank=True, null=True)
    location_id = models.CharField(max_length=50,default='',blank=True,null=True)
    qualification = models.CharField(max_length=100,default='',blank=True,null=True)
    phone_number = models.CharField(max_length=20, default='', blank=True, null=True)
    email_id = models.EmailField(max_length=50, default='', blank=True, null=True)
    password = models.CharField(max_length=10000, default='', blank=True, null=True)
    profile_image = models.ImageField(default='',upload_to="media-files/doctors_profile_images")
    signature_image = models.ImageField(default='',upload_to="media-files/doctors_signature_images")

    @staticmethod
    def get_doctor(username):
        try:
            return Doctor.objects.get(user_id = username)
        except:
            return False

class Doctor_schedule(models.Model):
    doctor_id = models.CharField(max_length=200,default='',blank=True,null=True)
    location_id = models.CharField(max_length=1000, default='', blank=True, null=True)
    day = models.CharField(max_length=100, default='', blank=True,null=True)
    _from = models.CharField(max_length=100, default='', blank=True,null=True)
    to = models.CharField(max_length=100, default='', blank=True,null=True)
    time_zone_offset = models.CharField(max_length=100, default='', blank=True,null=True)

class Doctor_license(models.Model):
    doctor_id = models.CharField(max_length=30,blank=True, null=True,default='')
    license_no = models.CharField(max_length=100,default='',blank=True,null=True)
    license_issue_date = models.CharField(max_length=100,default='',blank=True,null=True)
    license_issuing_authority = models.CharField(max_length=100,default='',blank=True,null=True)
    license_expiry_date = models.CharField(max_length=100,default='',blank=True,null=True)

class Doctor_loccation(models.Model):
    doc_id = models.CharField(max_length=30,blank=True, null=True,default='')
    loc_id = models.CharField(primary_key=True,max_length=30,blank=False, null=False,default='')

    @staticmethod
    def get_doc(doct_id):
        try:
            return Doctor_loccation.objects.filter(doc_id = doct_id)
        except:
            return False

class Doctors_location(models.Model):
    location_id = models.CharField(primary_key=True,max_length=4294967295,blank=False, null=False)
    clinic_name=models.CharField(max_length=30,blank=True, null=True,default='')
    building_name = models.CharField(max_length=30,blank=True, null=True,default='')
    area = models.CharField(max_length=30,blank=True, null=True,default='')
    latitude = models.CharField(max_length=30,blank=True, null=True,default='')
    longitude = models.CharField(max_length=30,blank=True, null=True,default='')
    city = models.CharField(max_length=30,blank=True, null=True,default='')
    state = models.CharField(max_length=30,blank=True, null=True,default='')
    pin_code = models.IntegerField(null=True)
    country = models.CharField(max_length=30,blank=True, null=True,default='')


class Doctors_specialitie(models.Model):
    speciality=models.CharField(max_length=200,blank=True, null=True)

# class Doctor_profile(models.Model):
#     doctor_user_id = models.CharField(max_length=200,default='',blank=True,null=True)
#     image = models.FileField(default='',upload_to='media-files/doctors_profile_images')
# class Doctor_signature(models.Model):
#     doctor_user_id = models.CharField(max_length=200,default='',blank=True,null=True)
#     image = models.FileField(default='',upload_to='media-files/doctors_signature_images')

class Doctor_consaltancies_charge(models.Model):
    doctor_id = models.CharField(max_length=200,default='',blank=True,null=True)
    location_id = models.CharField(max_length=1000, default='', blank=True, null=True)
    video_consultancy_fees = models.CharField(max_length=1000, default='', blank=True, null=True)
    physical_consultancy_fees = models.CharField(max_length=1000, default='', blank=True, null=True)
    currency_type = models.CharField(max_length=1000, default='', blank=True, null=True)    # location_fees

# class Doctor_location_consaltancie(models.Model):
#     doctor_id = models.CharField(max_length=200,default='',blank=True,null=True)



# class Provider(models.Model):
#   user_id = models.CharField(max_length=20,primary_key=True,null=False,blank=False)
#   name = models.CharField(max_length=20)
#   speciality = models.CharField(max_length=50)
#   phone_number = models.CharField(max_length=20)
#   email_id = models.EmailField(max_length=50)
#   password = models.CharField(max_length=50)
#   typeOfProvider = models.CharField(max_length=50)
#   dateOfBirth = models.CharField(max_length=50)
#   gender = models.CharField(max_length=20)

# -------------------patients
class Customer(models.Model):
    customer_id = models.CharField(max_length=200, primary_key=True)
    family_code = models.CharField(max_length=200,default='',blank=True,null=True)
    name = models.CharField(max_length=200,default='',blank=True,null=True)
    phone_number = models.CharField(max_length=200,default='',blank=True,null=True)
    gender = models.CharField(max_length=200,default='',blank=True,null=True)
    date_of_birth = models.CharField(max_length=200,default='',blank=True,null=True)
    email_id = models.CharField(max_length=200,default='',blank=True,null=True)
    password = models.CharField(max_length=200,default='',blank=True,null=True)
    primary_member = models.BooleanField(default=False)
    profile_picture = models.ImageField(default='',upload_to='media-files/patients_profile_images')

    @staticmethod
    def get_latest_save_patient_customer_id(cus_id):
        try:
            return Customer.objects.latest('customer_id')
        except:
            return False

class Medical_condition_disease(models.Model):
    icd_code = models.CharField(max_length=200,default='',blank=True,null=True)
    disease = models.CharField(max_length=200,default='',blank=True,null=True)

class Patient_medical_condition(models.Model):
    customer_code = models.CharField(max_length=200,default='',blank=True,null=True)
    condition_name = models.CharField(max_length=200,default='',blank=True,null=True)
    since_how_long = models.CharField(max_length=200,default='',blank=True,null=True)
    medicine = models.CharField(max_length=200,default='',blank=True,null=True)

class Patient_medical_report(models.Model):
    customer_code = models.CharField(max_length=200,default='',blank=True,null=True)
    report_name = models.CharField(max_length=200,default='',blank=True,null=True)
    report_image = models.ImageField(upload_to='media-files/patients_report_images')
    description = models.CharField(max_length=200,default='',blank=True,null=True)

# class MyAppInsuranceCompanyMaster(models.Model):
    # insurance_company_name = models.CharField(default='', max_length=40, blank=True, null=True)
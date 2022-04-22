from django.contrib import admin
from .models import Doctor, Doctors_location, Doctors_specialitie,\
    Doctor_loccation, Doctor_schedule, Doctor_license, Doctor_consaltancies_charge
    # , A_doctor_locations
    # A_doctor_specialities
# from my_app.models import
from .models import Customer\
    , Medical_condition_disease, Patient_medical_condition, Patient_medical_report
    # MyAppInsuranceCompanyMaster

# Register your models here.

class For_Doctor(admin.ModelAdmin):
    list_display = ['user_id','name','speciality', 'date_of_birth', 'phone_number','email_id','password']

class For_Doctor_location(admin.ModelAdmin):
    list_display = ['location_id','clinic_name','building_name','area',
                    'latitude','longitude','city','state','pin_code']

class For_Doc_loc(admin.ModelAdmin):
    list_display = ['doc_id', 'loc_id']

class For_Doctor_speciality(admin.ModelAdmin):
    list_display = ['speciality']

class For_Doctor_consaltancy_charges(admin.ModelAdmin):
    list_display = ['doctor_id','location_id','video_consultancy_fees', "physical_consultancy_fees","currency_type"]

# class For_Doctor_profile_images(admin.ModelAdmin):
#     list_display = ['doctor_user_id','image']
# class For_Doctor_signature_images(admin.ModelAdmin):
#     list_display = ['doctor_user_id','image']

class For_Doctor_schedule(admin.ModelAdmin):
    list_display = ['doctor_id','location_id','day','_from','to']

class For_doctor_license(admin.ModelAdmin):
    list_display = ['doctor_id','license_no','license_issue_date','license_issuing_authority','license_expiry_date']
# class For_Doctor_specialities(admin.ModelAdmin):
#     list_display = ['doctor_user_id']


class For_Patients(admin.ModelAdmin):
    list_display = ['customer_id','family_code','name','phone_number','gender',
                    'email_id','password','profile_picture']

class For_Patients_medical_condition(admin.ModelAdmin):
    list_display = ['customer_code','condition_name','since_how_long','medicine']

class For_Patients_medical_report(admin.ModelAdmin):
    list_display = ['customer_code','report_name','report_image','description']

class For_Diseaes(admin.ModelAdmin):
    list_display = ['icd_code','disease']

class For_insurance(admin.ModelAdmin):
    list_display = ['insurance_company_name']

admin.site.register(Customer, For_Patients)
admin.site.register(Patient_medical_condition, For_Patients_medical_condition)
admin.site.register(Patient_medical_report, For_Patients_medical_report)
admin.site.register(Medical_condition_disease, For_Diseaes)
# admin.site.register(MyAppInsuranceCompanyMaster, For_insurance)


admin.site.register(Doctor,For_Doctor)

admin.site.register(Doctors_location,For_Doctor_location)
admin.site.register(Doctor_loccation,For_Doc_loc)
# admin.site.register(A_doctor_locations,For_Doctor_locations)

admin.site.register(Doctors_specialitie,For_Doctor_speciality)

admin.site.register(Doctor_consaltancies_charge,For_Doctor_consaltancy_charges)

admin.site.register(Doctor_schedule,For_Doctor_schedule)

admin.site.register(Doctor_license, For_doctor_license)


# --------------------patients




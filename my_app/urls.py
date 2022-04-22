from django.contrib import admin
from django.urls import path
from .views import Adduser, Doc_loc, Doc_speciality, Login_doc, Fetch_doc_loc, Delete_doc_location,\
    Get_doc_qua, Add_doc_qua, Get_doc_spe, Add_doc_spe, Get_doctor_con, Add_Doctor_con,\
    Get_doc_pro ,Add_doc_pro, Get_doc_licence, Add_doc_licence, Get_doc_schedule, Add_doc_schedule, Get_doc_lic,\
    Add_doc_lic, Get_doc_sign, Add_doc_sign, Patient_regis\
    , Disease_list, Patient_login, Get_patient_med_cond, Add_patient_med_cond, Get_patient_med_report, Add_patient_med_report, Get_schedule

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('add', Adduser.as_view(), name = 'homepage'),
    path('add_patient', Patient_regis.as_view(), name = 'patient_registration'),
    path('disease_list', Disease_list.as_view(), name = 'disease_list'),
    path('patient_login', Patient_login.as_view(), name = 'patient_login'),
    path('get_patient_condition/<str:customer_code>', Get_patient_med_cond.as_view(), name = 'get_patient_condition'),
    path('add_patient_condition', Add_patient_med_cond.as_view(), name = 'add_patient_condition'),

    path('get_patient_report/<str:customer_code>', Get_patient_med_report.as_view(), name = 'get_patient_report'),
    path('add_patient_report', Add_patient_med_report.as_view(), name = 'add_patient_report'),
    # path('addProvider', addProvider, name = 'Add Provider'),
    path('add_loc', Doc_loc.as_view(), name='add_location'),
    path('all_speciality', Doc_speciality.as_view(), name='add_speciality'),

    path('fetch_doc_loc', Fetch_doc_loc.as_view(), name='fetch_doc_loc'),
    path('delete_doc_loc', Delete_doc_location.as_view(), name='delete_doc_loc'),

    path('get_doc_consultancy/<str:doct_id>', Get_doctor_con.as_view(), name='get_doc_consultancy'),
    path('add_doc_consultancy', Add_Doctor_con.as_view(), name='add_doc_consultancy'),

    path('get_doc_qualification/<str:doct_id>', Get_doc_qua.as_view(), name='get_doc_qualification'),
    path('add_doc_qualification', Add_doc_qua.as_view(), name='add_doc_qualification'),

    path('get_doc_licence/<str:doct_id>', Get_doc_licence.as_view(), name='get_doc_licence'),
    path('add_doc_licence', Add_doc_licence.as_view(), name='add_doc_licence'),

    path('get_doc_speciality/<str:doct_id>', Get_doc_spe.as_view(), name='get_doc_speciality'),
    path('add_doc_speciality', Add_doc_spe.as_view(), name='add_doc_speciality'),

    path('get_doc_profile/<str:doct_id>', Get_doc_pro.as_view(), name='get_doc_pro'),
    path('add_doc_profile', Add_doc_pro.as_view(), name='add_doc_pro'),
    # path('add_doc_speciality', Add_doc_spe.as_view(), name='add_doc_speciality'),

    path('get_doc_signature/<str:doct_id>', Get_doc_sign.as_view(), name='get_doc_sign'),
    path('add_doc_signature', Add_doc_sign.as_view(), name='add_doc_sign'),

    path('get_doc_schedule/<str:doct_id>', Get_doc_schedule.as_view(), name='get_doc_schedule'),
    path('get_schedule/', Get_schedule.as_view(), name='get_schedule'),
    path('add_doc_schedule', Add_doc_schedule.as_view(), name='add_doc_schedule'),

    path('get_doc_license/<str:doct_id>', Get_doc_lic.as_view(), name='get_doc_license'),
    path('add_doc_license', Add_doc_lic.as_view(), name='add_doc_license'),

    path('doctor_login/<str:username>/<str:password>',Login_doc.as_view(), name='doctor_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

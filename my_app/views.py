from pydoc import doc
from django.shortcuts import render, HttpResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import DoctorSerializer, DoctorLocationSerializer, DoctorSpecialitySerializer,\
    PatientSerializer\
    , DiseaseSerializer
from .models import Doctor, Doctors_location, Doctors_specialitie, Doctor_loccation, Doctor_schedule,\
    Doctor_license, Doctor_consaltancies_charge
# Create your views here.
from django.views import View

#all done
class Adduser(APIView):
    def get(self,request, format=None):
        print("mille la hai re be")
        doctor = Doctor.objects.all()
        print(doctor)
        serializer = DoctorSerializer(doctor, many=True)
        return Response(serializer.data)

    def post(self,request):
        self.http_method_names.append("GET")
        request.data['password'] = make_password(request.data['password'])
        serializer = DoctorSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print("sahi hia")
        return Response(serializer.data)

#all done
class Get_doc_qua(APIView):
    def get(self,request,doct_id):
        print("yeh chal raha hai kya")
        doc_id = doct_id
        try:
            get_doc = Doctor.get_doctor(doc_id)
        except:
            get_doc = False
        if get_doc:
            return Response({'Qualification':get_doc.qualification})
class Add_doc_qua(APIView):
    def post(self,request):
        doc_id = request.data['doc_id']
        quali = request.data['qualification']
        print(doc_id)
        try:
            get_doc = Doctor.get_doctor(doc_id)
        except:
            get_doc = False
        if get_doc:
            print("getting doctor bhai")
            get_doc.qualification = quali
            get_doc.save()
            return Response("Doctor Qualification saved Successfully")

#all done
class Get_doc_licence(APIView):
    def get(self,request,doct_id):
        print("yeh chal raha hai kya")
        doc_id = doct_id
        try:
            get_doc = Doctor_license.objects.filter(doctor_id = doc_id)
        except:
            get_doc = False
        if get_doc:
            licenses = []
            for lic in get_doc:
                license = {
                    'license_no': lic.license_no,
                    'license_issue_date': lic.license_issue_date,
                    'license_expiry_date': lic.license_expiry_date,
                    'license_issuing_authority': lic.license_issuing_authority}
                licenses.append(license)
            return Response(licenses)
class Add_doc_licence(APIView):
    def post(self,request):
        doc_id = request.data['doc_id']
        lic_no = request.data['license_no']
        issue_date = request.data['license_issue_date']
        expity_date = request.data['license_expiry_date']
        issuing_author = request.data['license_issuing_authority']
        print(doc_id,lic_no,issue_date,expity_date,issuing_author)
        try:
            get_doc = Doctor.get_doctor(doc_id)
        except:
            get_doc = False
        if doc_id and lic_no and issue_date and expity_date and issuing_author:
            add_license = Doctor_license(
                doctor_id = doc_id,
                license_no = lic_no,
                license_issue_date = issue_date,
                license_expiry_date = expity_date,
                license_issuing_authority = issuing_author
            )
            add_license.save()
            return Response("Doctor Qualification saved Successfully")
        else:
            return Response("Something went wrong")

#all done
class Get_doc_spe(APIView):
    def get(self,request,doct_id):
        doc_id = doct_id
        try:
            get_doc = Doctor.get_doctor(doc_id)
        except:
            get_doc = False
        if get_doc:
            return Response({'Speciality':get_doc.speciality})
class Add_doc_spe(APIView):
    def post(self,request):
        doc_id = request.data['doc_id']
        spec = request.data['speciality']
        try:
            get_doc = Doctor.get_doctor(doc_id)
        except:
            get_doc = False
        if get_doc:
            get_doc.speciality = f'{get_doc.speciality}, {spec}'
            get_doc.save()
            return Response("Doctor Speciality saved Successfully")

#all done
class Fetch_doc_loc(APIView):
    def post(self,request):
        # self.http_method_names.append("GET")
        doc_id = request.data['doc_id']
        get_doc_loc_id = Doctor_loccation.objects.filter(doc_id = doc_id)
        print(get_doc_loc_id)
        if get_doc_loc_id:
            location_ids = []
            for id in get_doc_loc_id:
                # locations = {}
                # print(get_doc_loc.clinic_name)
                location = id.loc_id
                location_ids.append(location)
                # locations = location.copy()
                # locations.update(location)
            print(location_ids)
            get_all_locations = Doctors_location.objects.filter(location_id__in = location_ids)
            if get_all_locations:
                all_locations = []
                for get_doc_loc in get_all_locations:
                    location = {
                        'location_id': get_doc_loc.location_id,
                        'clinic_name':get_doc_loc.clinic_name,
                        'building_name' : get_doc_loc.building_name,
                        'area':get_doc_loc.area,
                        'latitude' : get_doc_loc.latitude,
                        'longitude': get_doc_loc.longitude,
                        'city': get_doc_loc.city,
                        'state': get_doc_loc.state,
                        'pin_code': get_doc_loc.pin_code,
                        'country': get_doc_loc.country
                    }
                    all_locations.append(location)
                return Response(all_locations)
            else:
                return Response("Locations not found")
        else:
            return Response("Invalid_username")
        return Response("getting it bro")

#all done
class Delete_doc_location(APIView):
    def post(self,request):
        doctor_id = request.data['doc_id']
        location_id = request.data['loc_id']
        print(type(location_id))
        print(doctor_id)
        if doctor_id:
            get_doc = Doctor_loccation.get_doc(doctor_id)
            print(get_doc)
            if get_doc:
                loc_id_list = []
                for loc_ids in get_doc:
                    loca_id = loc_ids.loc_id
                    loc_id_list.append(loca_id)
                if location_id in loc_id_list:
                    try:
                        Doctor_loccation.objects.get(loc_id = location_id).delete()
                        return Response("deleted successfully")
                    except:
                        return Response("can't delete")
            else:
                print("none")

#all done
class Doc_loc(APIView):
    def get(self,request):
        doctor_loc = Doctors_location.objects.all()
        print(doctor_loc)
        serializer = DoctorLocationSerializer(doctor_loc,many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self,request):
        d_id = request.data['doc_id']
        l_id = request.data['loc_id']
        clinic_name = request.data['clinic_name']
        building_name = request.data['building_name']
        area = request.data['area']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        city = request.data['city']
        state = request.data['state']
        pin_code = request.data['pin_code']
        country = request.data['country']
        try:
            chech_exist = Doctors_location.objects.filter(location_id = l_id)
        except:
            chech_exist = False
        if chech_exist:
            doc_inner_loc = Doctor_loccation(doc_id=d_id, loc_id=l_id)
            doc_inner_loc.save()
            return Response('New Doctor location added successfully')
        else:
            doc_loc = Doctors_location(
                location_id = l_id,
                clinic_name = clinic_name,
                building_name = building_name,
                area = area,
                latitude = latitude,
                longitude = longitude,
                city = city,
                state = state,
                pin_code = pin_code,
                country = country
            )
            doc_loc.save()
            doc_inner_loc = Doctor_loccation(doc_id=d_id, loc_id=l_id)
            doc_inner_loc.save()
            return Response('New Doctor location added successfully')

# all done
class Doc_speciality(APIView):
    def get(self,request):
        doctor_spec = Doctors_specialitie.objects.all()
        print(doctor_spec)
        serializer = DoctorSpecialitySerializer(doctor_spec,many=True)
        print(serializer)
        # doctor = Doctor.objects.get('true1')
        return Response(serializer.data)

    def post(self,request):
        serializer = DoctorSpecialitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)



# all done
class Get_doctor_con(APIView):
    def get(self, request,doct_id):
        doc_id = doct_id
        try:
            get_doctor = Doctor_consaltancies_charge.objects.filter(doctor_id = doc_id)
        except:
            get_doctor = False
        if get_doctor:
            charges = []
            for fee in get_doctor:
                charge = {
                    'doctor_id': fee.doctor_id,
                    'location_id': fee.location_id,
                    'video_consultancy_fees': fee.video_consultancy_fees,
                    'physical_consultancy_fees': fee.physical_consultancy_fees,
                    'currency_type': fee.currency_type
                }
                charges.append(charge)
            return Response(charges)
        else:
            return Response("Can't find user")
class Add_Doctor_con(APIView):
    def post(self, request):
        print("yeh kaam nahi kar araha hia")
        doc_id = request.data['doc_id']
        loc_id = request.data['loc_id']
        video_consultancy_fees = request.data['video_consultancy_fees']
        physical_consultancy_fees = request.data['physical_consultancy_fees']
        currency_type = request.data['currency_type']
        if doc_id and loc_id and video_consultancy_fees and physical_consultancy_fees and currency_type:
            charges = Doctor_consaltancies_charge(doctor_id = doc_id, location_id = loc_id,
                                                  video_consultancy_fees = video_consultancy_fees,
                                                  physical_consultancy_fees = physical_consultancy_fees,
                                                  currency_type = currency_type)
            charges.save()
            return Response('Doctor video consaltancy fees added successfully')
        else:
            return Response("Something went wrong provide full details")

# class Get_doctor_location_con(APIView):
#     def get(self, request,doct_id):
#         doc_id = doct_id
#         print('doing it baba')
#         try:
#             get_doctor = Doctor_location_consaltancie.objects.filter(doctor_id = doc_id)
#         except:
#             get_doctor = False
#         if get_doctor:
#             location_fees = []
#             for doc in get_doctor:
#
#                 location_fee = {
#                     'doctor_id': doc.doctor_id,
#                     'location_id': doc.location_id,
#                     'fees': doc.fees,
#                     'currency_type': doc.currency_type
#                 }
#                 location_fees.append(location_fee)
#             return Response(location_fees)
# class Add_Doctor_location_con(APIView):
#     def post(self, request):
#         print("yeh kaam nahi kar araha hia")
#         doc_id = request.data['doc_id']
#         loc_id = request.data['loc_id']
#         fees = request.data['fees']
#         currency_type = request.data['currency_type']
#         print(doc_id,loc_id,fees)
#         Doctor_location_consaltancie(doctor_id = doc_id, location_id = loc_id, fees = fees, currency_type = currency_type).save()
#         return Response('Doctor location consaltancy fees added successfully')

# all done
class Get_doc_pro(APIView):
    def get(self, request, doct_id):
        doc_id = doct_id
        try:
            get_doc = Doctor.objects.get(user_id = doc_id)
        except:
            get_doc = False
        if get_doc:
            try:
                image = get_doc.profile_image.url
            except:
                image = False
            print(image)
            if image:
                return Response({"doctor_id":get_doc.user_id,"image":image})
            else:
                return Response("No Profile Image is there")
        else:
            return Response("Something went wrong")
class Add_doc_pro(APIView):
    def post(self, request):
        print("yeh kaam nahi kar araha hia")
        doc_id = request.data['doc_id']
        image = request.FILES['image']
        try:
            get_doc = Doctor.objects.get(user_id = doc_id)
        except:
            get_doc = False
        if doc_id and image:
            if get_doc:
                get_doc.profile_image = image
                get_doc.save()
                return Response("Doctor Profile uploaded successfully")
            else:
                return Response("Something went wrong")
        else:
            return Response("Something went wrong")

#all done
class Get_doc_sign(APIView):
    def get(self, request, doct_id):
        doc_id = doct_id
        try:
            get_doc = Doctor.objects.get(user_id = doc_id)
        except:
            get_doc = False
        if get_doc:
            # print(get_doc.profile_image)
            try:
                image = get_doc.signature_image.url
            except:
                image = False
            if image:
                return Response({"doctor_id":get_doc.user_id,"profile_image":image})
            else:
                return Response("No Signature is there")
        else:
            return Response("Something went wrong")
class Add_doc_sign(APIView):
    def post(self, request):
        doc_id = request.data['doc_id']
        image = request.FILES['image']
        if doc_id and image:
            try:
                get_doc = Doctor.objects.get(user_id=doc_id)
            except:
                get_doc = False
            if get_doc:
                get_doc.signature_image = image
                get_doc.save()
            return Response("Doctor Signature uploaded successfully")
        else:
            return Response("Something went wrong")

#all done
class Get_doc_schedule(APIView):
    def get(self,request,doct_id):
        doc_id = doct_id
        try:
            get_doc = Doctor_schedule.objects.filter(doctor_id=doc_id)
        except:
            get_doc = False
        if get_doc:
            get_location_ids = []
            for loc in get_doc:
                location_id = loc.location_id
                get_location_ids.append(location_id)
            try:
                get_loc_id = Doctors_location.objects.filter(location_id__in = get_location_ids)
            except:
                get_loc_id = False
            # print(get_loc_id)
            if get_loc_id:
                final_schedule = []
                get_sche = Doctor_schedule.objects.filter(doctor_id=doc_id)
                for i in get_sche:
                    l_id = i.location_id
                    try:
                        get_loc = Doctors_location.objects.get(location_id = l_id)
                    except:
                        get_loc = False
                    if get_loc:
                        doc_sche = {
                            'location_id' : l_id,
                            'clinic_name' : get_loc.clinic_name,
                            'building_name': get_loc.building_name,
                            'area': get_loc.area,
                            'latitude': get_loc.latitude,
                            'longitude': get_loc.longitude,
                            'city': get_loc.city,
                            'state': get_loc.state,
                            'pin_code' : get_loc.pin_code,
                            'country': get_loc.country,
                            'schedule' : {
                                'day' : i.day,
                                '_from' : i._from,
                                'to' : i.to,
                                'time_zone_offset' : i.time_zone_offset
                            }
                        }
                        final_schedule.append(doc_sche)
                    else:
                        return Response("Something went wrong")
                return Response(final_schedule)
            else:
                return Response("Something went wrong")
class Add_doc_schedule(APIView):
    def post(self,request):
        doc_id = request.data['doctor_id']
        loc_id = request.data['location_id']
        day = request.data['day']
        _from = request.data['from']
        to = request.data['to']
        time_zone = request.data['time_zone_offset']
        if doc_id and loc_id and day and _from and to and time_zone:
            Doctor_schedule(
                doctor_id = doc_id,
                location_id = loc_id,
                day = day,
                _from = _from,
                to = to,
                time_zone_offset = time_zone
            ).save()
            return Response("Doctor Schedule have been saved")
        else:
            return Response("Something went wrong")


# all done
class Login_doc(APIView):
    def post(self,request, username,password):
        print(username)
        pass_word = str(password)
        doc = Doctor.get_doctor(username)
        print(doc)
        if doc:
            doc_pass = doc.password
            flag = check_password(pass_word,doc_pass)
            print(flag)
            if flag:
                doctor_all_things = {
                    'user_id':doc.user_id,
                    'name' : doc.name,
                    'speciality':doc.speciality,
                    'DOB' : doc.date_of_birth,
                    'location': doc.location_id,
                    'phone_num': doc.phone_number,
                    'email_id': doc.email_id,
                    'password': doc.password

                }
                return Response(doctor_all_things)
            else:
                print(doc.password)
                return Response("Incorrect Password!")
        else:
            return Response("Invalid username!")

#all done
class Get_doc_lic(APIView):
    def get(self,request,doct_id):
        print("yeh chal raha hai kya")
        doc_id = doct_id
        try:
            get_doc = Doctor_license.objects.filter(doctor_id = doc_id)
        except:
            get_doc = False
        if get_doc:
            licenses = []
            for lic in get_doc:
                license = {
                    'doctor_id':lic.doctor_id,
                    'license_no': lic.license_no,
                    'license_issue_date': lic.license_issue_date,
                    'license_issuing_authority': lic.license_issuing_authority,
                    'license_expiry_date' : lic.license_expiry_date
                }
                licenses.append(license)
            return Response(licenses)
        else:
            return Response('Something went wrong !')
class Add_doc_lic(APIView):
    def post(self,request):
        doc_id = request.data['doctor_id']
        lic_no = request.data['license_no']
        lic_is_d = request.data['license_issue_date']
        lic_is_auth = request.data['license_issuing_authority']
        lic_ex_da = request.data['license_expiry_date']
        if doc_id and lic_no and lic_is_d and lic_is_auth and lic_ex_da:
            doctor_license_add = Doctor_license(
                doctor_id = doc_id,
                license_no = lic_no,
                license_issue_date = lic_is_d,
                license_issuing_authority = lic_is_auth,
                license_expiry_date = lic_ex_da
            )
            doctor_license_add.save()
            return Response("Doctor License saved Successfully")
        else:
            return Response("Something went wrong !")

# @api_view(['POST'])
# def addProvider(request):
#     serializer = ProviderSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class Get_schedule(APIView):
    def post(self,request):
        doc_id = request.data['doctor_id']
        weekday = request.data['weekday']
        try:
            get_doc = Doctor_schedule.objects.filter(doctor_id=doc_id, day = weekday)
        except:
            get_doc = False
        if get_doc:
            get_location_ids = []
            for loc in get_doc:
                location_id = loc.location_id
                get_location_ids.append(location_id)
            try:
                get_loc_id = Doctors_location.objects.filter(location_id__in = get_location_ids)
            except:
                get_loc_id = False
            # print(get_loc_id)
            if get_loc_id:
                final_schedule = []
                get_sche = Doctor_schedule.objects.filter(doctor_id=doc_id,day=weekday)
                for i in get_sche:
                    l_id = i.location_id
                    try:
                        get_loc = Doctors_location.objects.get(location_id = l_id)
                    except:
                        get_loc = False
                    if get_loc:
                        doc_sche = {
                            'location_id' : l_id,
                            'clinic_name' : get_loc.clinic_name,
                            'building_name': get_loc.building_name,
                            'area': get_loc.area,
                            'schedule' : {
                                'day' : i.day,
                                '_from' : i._from,
                                'to' : i.to,
                                'time_zone_offset' : i.time_zone_offset
                            }
                        }
                        final_schedule.append(doc_sche)
                    else:
                        return Response("Something went wrong")
                return Response(final_schedule)
            else:
                return Response("Something went wrong")


class Get_doc_schedule(APIView):
    def get(self,request,doct_id):
        doc_id = doct_id
        try:
            get_doc = Doctor_schedule.objects.filter(doctor_id=doc_id)
        except:
            get_doc = False
        if get_doc:
            get_location_ids = []
            for loc in get_doc:
                location_id = loc.location_id
                get_location_ids.append(location_id)
            try:
                get_loc_id = Doctors_location.objects.filter(location_id__in = get_location_ids)
            except:
                get_loc_id = False
            # print(get_loc_id)
            if get_loc_id:
                final_schedule = []
                get_sche = Doctor_schedule.objects.filter(doctor_id=doc_id)
                for i in get_sche:
                    l_id = i.location_id
                    try:
                        get_loc = Doctors_location.objects.get(location_id = l_id)
                    except:
                        get_loc = False
                    if get_loc:
                        doc_sche = {
                            'location_id' : l_id,
                            'clinic_name' : get_loc.clinic_name,
                            'building_name': get_loc.building_name,
                            'area': get_loc.area,
                            'latitude': get_loc.latitude,
                            'longitude': get_loc.longitude,
                            'city': get_loc.city,
                            'state': get_loc.state,
                            'pin_code' : get_loc.pin_code,
                            'country': get_loc.country,
                            'schedule' : {
                                'day' : i.day,
                                '_from' : i._from,
                                'to' : i.to,
                                'time_zone_offset' : i.time_zone_offset
                            }
                        }
                        final_schedule.append(doc_sche)
                    else:
                        return Response("Something went wrong")
                return Response(final_schedule)
            else:
                return Response("Something went wrong")



from my_app.models import Customer\
    , Medical_condition_disease, Patient_medical_condition, Patient_medical_report

class Patient_regis(APIView):
    def get(self,request, format=None):
        patient = Customer.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

    def post(self,request):
        self.http_method_names.append("GET")
        try:
            latest_cus = Customer.objects.latest('customer_id')
        except:
            latest_cus = False
        print(latest_cus)
        if latest_cus:
            cus_id = str(latest_cus.customer_id)
            cus_index = cus_id.find('_')
            cus_num = int(cus_id[cus_index + 1:])
            last_cus_id = f'CC_{cus_num + 1}'
        if not latest_cus:
            last_cus_id = 'CC_1'

        try:
            latest_fam = Customer.objects.latest('family_code')
        except:
            latest_fam = False
        print(latest_fam)
        if latest_fam:
            fam_id = str(latest_fam.family_code)
            fam_index = fam_id.find('_')
            fam_num = int(fam_id[fam_index + 1:])
            last_fam_id = f'FC_{fam_num + 1}'
        if not latest_fam:
            last_fam_id = "FC_1"

        request.data['customer_id'] = last_cus_id
        request.data['family_code'] = last_fam_id
        request.data['password'] = make_password(request.data['password'])
        serializer = PatientSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            print("sahi hia")
        return Response(serializer.data)

class Get_patient_med_cond(APIView):
    def get(self,request,customer_code):
        cus_code = customer_code
        try:
            get_customer = Patient_medical_condition.objects.filter(customer_code = cus_code)
        except:
            get_customer = False
        if get_customer:
            conditions_list = []
            for a in get_customer:
                conditions = {
                    'customer_code':a.customer_code,
                    'condition_name':a.condition_name,
                    'since_how_long':a.since_how_long,
                    'medicine':a.medicine,
                }
                conditions_list.append(conditions)
            return Response(conditions_list)
        else:
            return Response('Patient Not Found !')
class Add_patient_med_cond(APIView):
    def post(self,request):
        cus_code = request.data['customer_code']
        condition_name = request.data['condition_name']
        since_how_long = request.data['since']
        medicine = request.data['medicine']
        if cus_code and condition_name and since_how_long and medicine:
            condition = Patient_medical_condition(
                customer_code = cus_code,
                condition_name = condition_name,
                since_how_long = since_how_long,
                medicine = medicine
            )
            condition.save()
            return  Response('Patient conditions have been saved')
        else:
            return Response('Something went wrong !')


class Get_patient_med_report(APIView):
    def get(self,request,customer_code):
        cus_code = customer_code
        try:
            get_customer = Patient_medical_report.objects.filter(customer_code = cus_code)
        except:
            get_customer = False
        # print(get_customer)
        if get_customer:
            conditions_list = []
            for a in get_customer:
                conditions = {
                    'customer_code':a.customer_code,
                    'report_name':a.report_name,
                    'report_image':a.report_image.url,
                    'description':a.description,
                }
                print(conditions)
                conditions_list.append(conditions)
            return Response(conditions_list)
        else:
            return Response('Patient Not Found !')
class Add_patient_med_report(APIView):
    def post(self,request):
        cus_code = request.data['customer_code']
        report_name = request.data['report_name']
        report_image = request.data['report_image']
        description = request.data['description']
        print(cus_code,report_name,report_image,description)
        if cus_code and report_name and report_image and description:
            condition = Patient_medical_report(
                customer_code = cus_code,
                report_name = report_name,
                report_image = report_image,
                description = description
            )
            condition.save()
            return  Response('Patient Report have been saved')
        else:
            return Response('Something went wrong !')


class Disease_list(APIView):
    # def get(self,request, format=None):
    #     disease_list = Medical_condition_disease.objects.all()
    #     # print(disease_list)
    #
    #     # disease = Medical_condition_master.objects.all()
    #     # print(disease)
    #     serializer = DiseaseSerializer(disease_list, many=True)
    #     return Response(serializer.data)

    def post(self,request):
        name = request.data['disease']
        try:
            disease_name = Medical_condition_disease.objects.filter(disease__icontains = name)
        except:
            disease_name = False
        if disease_name:
            disease_name_list = []
            for a in disease_name:
                # print(a)
                disease = a.disease
                disease_name_list.append(disease)
            print("ho toh rha hia")
        return Response({'diseases_found':disease_name_list})

class Patient_login(APIView):
    def post(self,request):
        phone_no = request.data['phone_num']
        password = request.data['password']
        print(phone_no,password)
        if phone_no and password:
            try:
                get_patient = Customer.objects.get(phone_number = phone_no)
            except:
                get_patient = False
            print(get_patient)
            if get_patient:
                get_patient_password = get_patient.password
                print(get_patient_password)
                flag = check_password(password,get_patient_password)
                print(flag)
                # print(get_patient.name)
                if flag:
                    image = get_patient.profile_picture
                    if image:
                        image = image.url
                    else:
                        image = str(image)
                    patient = {
                        'customer_id':get_patient.customer_id,
                        'family_code': get_patient.family_code,
                        'name': get_patient.name,
                        'phone_number': get_patient.phone_number,
                        'gender': get_patient.gender,
                        'date_of_birth': get_patient.date_of_birth,
                        'email_id': get_patient.email_id,
                        'password': get_patient.password,
                        'primary_member': get_patient.primary_member,
                        'profile_picture': image
                    }
                    print(patient)
                    return Response({'patient':patient})
                else:
                    return Response('Incorrect Password')
            else:
                return Response('Invalid Phone Number')
        else:
            return Response("Please Enter Both Phone Number and Password")
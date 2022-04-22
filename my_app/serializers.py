from rest_framework import serializers
from .models import Doctor, Doctors_location, Doctors_specialitie, Customer\
    , Medical_condition_disease


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = '__all__'
    class Meta2:
        model = Doctor
        fields = ('user_id','password')
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields = '__all__'
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medical_condition_disease
        fields = '__all__'

class DoctorLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors_location
        fields = '__all__'

class DoctorSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors_specialitie
        fields = '__all__'

class DoctorSpecialityListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors_specialitie
        fields = '__all__'


# class ProviderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Provider
#         fields = '__all__'

# from rest_framework.serializers import Serializer, FileField
# class Doctorprofileupload(serializers.ModelSerializer):
#     file_uploaded = FileField()
#     class Meta:
#         model = Doctor_profile
#         fields = '__all__'
from rest_framework.serializers import ModelSerializer
from .models import CiscoData


class CiscoDataModelSerializer(ModelSerializer):


    class Meta:
        model=CiscoData
        fields=['id','sapid','hostname','macaddress','loopback']
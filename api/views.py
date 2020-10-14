from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import CiscoData
from .serializers import CiscoDataModelSerializer
from rest_framework.response import Response
# Create your views here.
def check(request):
    return HttpResponse('working')




class CiscoDataModelViewSet(ModelViewSet):
    queryset=CiscoData.objects.filter(flag=True)
    serializer_class=CiscoDataModelSerializer


    def destroy(self,request,*args,**kwargs):
        print('priniting ----->',args,kwargs)
        pk=kwargs['pk']
        csob=CiscoData.objects.get(id=pk)
        csob.flag=False
        csob.save()
        return Response('Deleted')
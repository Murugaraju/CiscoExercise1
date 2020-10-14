
from django.urls import path,include
from .views import check
from rest_framework.routers import DefaultRouter
from .views import CiscoDataModelViewSet

router = DefaultRouter()

router.register(r'',CiscoDataModelViewSet)

urlpatterns = [
    
    path('check/',check),
    path('',include(router.urls))

]


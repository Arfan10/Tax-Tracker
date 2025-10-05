from django.urls import path, include
from rest_framework import routers 
from .views import InvestmentViewSet,TaxRecordViewSet,PortforlioViewSet

router = routers.DefaultRouter()
router.register(r'investments',InvestmentViewSet)
router.register(r'taxrecords',TaxRecordViewSet)
router.register(r'portfolio',PortforlioViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
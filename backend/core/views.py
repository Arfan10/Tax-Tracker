from rest_framework import viewsets 
from .models import Investment,TaxRecord,Portfolio
from .Serializer import InvestmentSerializer,TaxRecordSerializer,PortfolioSerializer
from rest_framework.permissions import AllowAny

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [AllowAny]

class TaxRecordViewSet(viewsets.ModelViewSet):
    queryset = TaxRecord.objects.all()
    serializer_class = TaxRecordSerializer

class PortforlioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    
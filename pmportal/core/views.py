from rest_framework import generics
from .models import Address
from .serializers import AddressSerializer

# Create your views here.

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
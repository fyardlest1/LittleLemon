from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from .serializers import MenuSerializer, BookingSerializer

from .models import Booking, Menu

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

    # def get_permissions(self):
    #     if (self.request.method == 'GET'):
    #         return []
    #     return [IsAdminUser()]


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView ):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # def get_permissions(self):
    #     if (self.request.method == 'GET'):
    #         return []
    #     return [IsAdminUser()]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]


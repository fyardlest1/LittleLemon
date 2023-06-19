from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import MenuSerializer, BookingSerializer, UserSerializer

from .models import Booking, Menu

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filterset_fields = ['price', 'inventory']
    search_fields = ['title']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView ):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


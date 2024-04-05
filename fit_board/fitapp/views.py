from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .models import *
from .serializers import *


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym_name.objects.all()
    serializer_class = GymSerializer
    filter_backends = [filters.SearchFilter]
    search_field = ['name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    filter_backends = [filters.SearchFilter]
    search_field = ['full_name', 'gym', 'sport']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_field = ['client_name']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


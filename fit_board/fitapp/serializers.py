from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym_name
        fields = '__all__'


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    trainer_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'phone_num', 'user', 'trainer_name']

    def get_trainer_name(self, obj):
        return obj.trainer_name.full_name if obj.trainer_name else None


class ScheduleSerializer(serializers.ModelSerializer):
    trainer = serializers.SerializerMethodField()
    gym = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = ['id', 'trainer', 'day', 'start_time', 'finish_time', 'gym']

    def get_trainer(self, obj):
        return obj.trainer.full_name if obj.trainer else None

    def get_gym(self, obj):
        return obj.gym.name if obj.gym else None


class BookingSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    schedule = ScheduleSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'client_name', 'schedule']

    def get_client_name(self, obj):
        return obj.client.client_name if obj.client else None


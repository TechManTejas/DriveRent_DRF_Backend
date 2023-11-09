from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Car
        fields = '__all__'

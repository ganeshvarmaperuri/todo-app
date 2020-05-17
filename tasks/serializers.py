from rest_framework import serializers
from .models import *

class taskserializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'
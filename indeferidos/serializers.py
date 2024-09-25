from rest_framework import serializers
from .models import Indeferidos

class IndeferidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indeferidos
        fields = '__all__'

from rest_framework import serializers
from .models import Tarea
from apps.persona.serializers import PersonaSerializer

class TareaSerializer(serializers.ModelSerializer):

    person = PersonaSerializer()

    class Meta:
        model = Tarea
        fields = '__all__'
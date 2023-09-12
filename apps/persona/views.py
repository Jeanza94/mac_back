from django.shortcuts import render
from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer


# Create your views here.
class PersonaView(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Persona
from .serializers import PersonaSerializer


# Create your views here.
class PersonaView(viewsets.ModelViewSet):
    serializer_class = PersonaSerializer
    
    def get_queryset(self):
        
        document_number = self.request.query_params.get('document_number')
        document_type = self.request.query_params.get('document_type')
        if document_number != None and document_number.isnumeric() and document_type != None and document_type.isnumeric():
            return Persona.objects.get_persons_by_document(document_type, document_number)
            
        return Persona.objects.get_all_persons()
         
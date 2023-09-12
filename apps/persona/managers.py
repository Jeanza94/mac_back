from django.db import models
from django.db.models import Q

class PersonaManger(models.Manager):

    def get_all_persons(self):
        return self.all()
    
    def get_persons_by_search(self, search):
        return self.filter(
            Q(firstname__icontains=search) | Q(middle_name__icontains=search) | Q(surname__icontains=search) |
            Q(birth__icontains=search) | Q(country__icontains=search) | Q(gender__icontains=search) | 
            Q(status__icontains=search) | Q(document_type__icontains=search) | Q(document_number__icontains=search)
        )

    def get_persons_by_document(self, document_type, document_number):
        return self.filter(
            document_type = document_type,
            document_number=document_number,
        )


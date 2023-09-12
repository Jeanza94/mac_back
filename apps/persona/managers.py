from django.db import models

class PersonaManger(models.Manager):

    def get_all_persons(self):
        return self.all()
    
    def get_persons_by_document(self, document_type, document_number):
        return self.filter(
            document_type = document_type,
            document_number=document_number,
        )
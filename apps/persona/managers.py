from django.db import models

class PersonaManger(models.Manager):

    def get_all_persons(self):
        return self.all()
    
    def get_persons_by_document_number(self, document_number):
        print(int(document_number))
        return self.filter(document_number=document_number)
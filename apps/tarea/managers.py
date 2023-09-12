
from django.db import models


class TareaManager(models.Manager):

    def get_all_taks(self):
        return self.all()
    
    def get_tasks_by_limit_date(self, limit_date):
        return self.filter(
            limit_date__lte = limit_date
        )
    
    def get_tasks_by_date_range(self, start_date, end_date):
        return self.filter(
            limit_date__range = (start_date, end_date)
        )
    
    def get_tasks_by_document(self, document_type, document_number):
        return self.filter(
            person__document_type = document_type,
            person__document_number = document_number
        )

from datetime import datetime
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

# Create your views here.
class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    
    def get_queryset(self):

        limit_date = self.request.query_params.get('limit_date')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        document_type = self.request.query_params.get('document_type')
        document_number = self.request.query_params.get('document_number')


        if limit_date:
            try:
                limit_date = datetime.strptime(limit_date, '%Y-%m-%d')
                return Tarea.objects.get_tasks_by_limit_date(limit_date) 
            except:
                pass
        
        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                return Tarea.objects.get_tasks_by_date_range(start_date, end_date)
            except:
                pass

        if document_type and document_type.isnumeric() and document_number and document_number.isnumeric():
            # return Tarea.objects.get_tasks_by_document('1', 1323343) 
            return Tarea.objects.get_tasks_by_document(document_type, document_number) 
                

        return Tarea.objects.get_all_taks()
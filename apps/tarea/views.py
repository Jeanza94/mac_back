from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer

# Create your views here.
class TareaView(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    queryset = Tarea.objects.all()

from django.urls import path, include
from rest_framework import routers
from .views import TareaView

router = routers.DefaultRouter()
router.register('tareas', TareaView, 'tareas')

urlpatterns = [
    path('api/', include(router.urls))
]
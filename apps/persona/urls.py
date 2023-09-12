
from django.urls import path, include
from rest_framework import routers
from .views import PersonaView

router = routers.DefaultRouter()
router.register(f'personas', PersonaView, 'personas')

urlpatterns = [
    path('api/', include(router.urls))
]
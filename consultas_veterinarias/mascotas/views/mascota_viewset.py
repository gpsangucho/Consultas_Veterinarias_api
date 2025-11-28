from rest_framework import viewsets
from mascotas.models import Mascota
from mascotas.serializers.mascota_serializer import MascotaSerializer

#from rest_framework.permissions import IsAuthenticated
#from rest_framework_simplejwt.authentication import JWTAuthentication

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    
    #authentication_classes = [JWTAuthentication]
    #permission_classes = [IsAuthenticated]

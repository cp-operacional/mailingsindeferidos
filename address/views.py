from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Municipios, Estados

class FiltrarMunicipios(APIView):
    def post(self, request):
        codigo_uf = request.data.get('codigo_uf')
        if codigo_uf is None:
            return Response({"error": "codigo_uf é obrigatório."}, status=status.HTTP_400_BAD_REQUEST)

        municipios = Municipios.objects.filter(codigo_uf=codigo_uf)
        return Response({"municipios": list(municipios.values_list('nome', flat=True))}, status=status.HTTP_200_OK)

class ListarUfs(APIView):
    def get(self, request):
        ufs = Estados.objects.values('codigo_uf', 'uf')
        return Response(list(ufs), status=status.HTTP_200_OK)

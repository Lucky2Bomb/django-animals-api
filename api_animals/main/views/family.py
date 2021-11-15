from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models, serializers


class FamilyView(APIView):
    def get(self, request):
        families = models.Family.objects.all()
        serializer = serializers.FamilySerializer(families, many=True)
        return Response({"families": serializer.data})

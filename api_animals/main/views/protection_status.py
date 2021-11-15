from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models, serializers


class ProtectionStatusView(APIView):
    def get(self, request):
        protection_statuses = models.ProtectionStatus.objects.all()
        serializer = serializers.ProtectionStatusSerializer(
            protection_statuses, many=True)
        print(serializer.data)
        return Response({"protection_statuses": serializer.data})

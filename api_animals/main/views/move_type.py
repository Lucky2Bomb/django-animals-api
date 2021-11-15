from rest_framework import generics

from .. import models, serializers


# class MoveTypeView(APIView):
#     def get(self, request):
#         move_types = models.MoveType.objects.all()
#         serializer = serializers.MoveTypeSerializer(move_types, many=True)
#         return Response({"move_types": serializer.data})

class MoveTypeList(generics.ListCreateAPIView):
    queryset = models.MoveType.objects.all()
    serializer_class = serializers.MoveType

    def create(self, validated_data):
        return models.MoveType.objects.create(**validated_data)

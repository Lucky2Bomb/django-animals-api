from functools import partial
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class AnimalView(APIView):
    def get(self, request):
        animals = models.Animal.objects.all()
        serializer = serializers.AnimalSerializer(animals, many=True)
        return Response({"animals": serializer.data})

    def post(self, request):
        animal = request.data.get('animal')

        serializer = serializers.AnimalSerializer(data=animal)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()

        return Response({"success": "Animal '{}' created successfully".format(animal_saved.name)})

    def put(self, request, pk):
        saved_animal = get_object_or_404(models.Animal.objects.all(), pk=pk)
        data = request.data.get('animal')
        serializer = serializers.AnimalSerializer(instance=saved_animal, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()

        return Response({
            "success": f"Animal {animal_saved.name} updated successfully"
        })

    def delete(self, request, pk):
        animal = get_object_or_404(models.Animal.objects.all(), pk=pk)
        animal.delete()
        return Response({
            "success": f"Animal with id {pk} has been deleted"
        }, status=204)

class FamilyView(APIView):
    def get(self, request):
        families = models.Family.objects.all()
        serializer = serializers.FamilySerializer(families, many=True)
        return Response({"families": serializer.data})

class MoveTypeView(APIView):
    def get(self, request):
        move_types = models.MoveType.objects.all()
        serializer = serializers.MoveTypeSerializer(move_types, many=True)
        return Response({"move_types": serializer.data})

class ProtectionStatusView(APIView):
    def get(self, request):
        protection_statuses = models.ProtectionStatus.objects.all()
        serializer = serializers.ProtectionStatusSerializer(protection_statuses, many=True)
        print(serializer.data)
        return Response({"protection_statuses": serializer.data})

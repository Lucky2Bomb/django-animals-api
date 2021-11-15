from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .. import models
from .. import serializers


class AnimalView(APIView):
    def get(self, request):
        animals = models.Animal.objects.all()
        serializer = serializers.Animal(animals, many=True)
        return Response({"animals": serializer.data})

    def post(self, request):
        animal = request.data.get('animal')

        serializer = serializers.Animal(data=animal)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()

        return Response({"success": "Animal '{}' created successfully".format(animal_saved.name)})

    def put(self, request, pk):
        saved_animal = get_object_or_404(models.Animal.objects.all(), pk=pk)
        data = request.data.get('animal')
        serializer = serializers.Animal(
            instance=saved_animal, data=data, partial=True)

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

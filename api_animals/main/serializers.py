from rest_framework import serializers

from . import models


class AnimalSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    domesticated = serializers.BooleanField()
    lifetime = serializers.DecimalField( max_digits=10, decimal_places=2, coerce_to_string=False, allow_null=True,)
    weight = serializers.DecimalField( max_digits=10, decimal_places=2, coerce_to_string=False, allow_null=True,)
    height = serializers.DecimalField( max_digits=10, decimal_places=2, coerce_to_string=False, allow_null=True,)
    number_of_individuals = serializers.IntegerField()
    description = serializers.CharField(allow_null=True, allow_blank=True)
    
    image = serializers.ImageField(allow_null=True,)

    protection_status_id = serializers.IntegerField()
    move_type_id = serializers.IntegerField()
    family_id = serializers.IntegerField()

    def create(self, validated_data):
        return models.Animal.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.domesticated = validated_data.get('domesticated', instance.domesticated)
        instance.lifetime = validated_data.get('lifetime', instance.lifetime)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.number_of_individuals = validated_data.get('number_of_individuals', instance.number_of_individuals)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.protection_status = validated_data.get('protection_status', instance.protection_status)
        instance.move_type = validated_data.get('move_type', instance.move_type)
        instance.family = validated_data.get('family', instance.family)

        instance.save()
        return instance
        # return super().update(instance, validated_data)

    # protection_status
    # move_type
    # family

class MoveTypeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)

class ProtectionStatusSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    abbreviation = serializers.CharField(max_length = 100, allow_null=True, allow_blank=True)

class FamilySerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    
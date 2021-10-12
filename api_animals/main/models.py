from django.db import models


class MoveType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class ProtectionStatus(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name + f" ({self.abbreviation})"

class Family(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=255)
    domesticated = models.BooleanField(default=False)
    lifetime = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    weight = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    height = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=2)
    number_of_individuals = models.BigIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField("Image", upload_to="animal_images/", null=True, blank=True)

    protection_status = models.ForeignKey(ProtectionStatus, on_delete=models.PROTECT, null=True, blank=True)
    move_type = models.ForeignKey(MoveType, on_delete=models.PROTECT, null=True, blank=True)
    family = models.ForeignKey(Family, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

from django.db import models


class ProtectionStatus(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name + f" ({self.abbreviation})"

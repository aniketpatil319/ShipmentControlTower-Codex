from django.db import models
from accounts.models import Company


class InboundShipment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='inbound_shipments')
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    expected_date = models.DateField()

    def __str__(self) -> str:
        return self.reference


class OutboundShipment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='outbound_shipments')
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    expected_date = models.DateField()

    def __str__(self) -> str:
        return self.reference

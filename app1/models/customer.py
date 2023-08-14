from django.db import models
import datetime
from django.utils.timezone import now


class Customer(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    customer_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    def isExists(self):
        if Customer.objects.filter(customer_id=self.customer_id):
            return True
        else:
            return False


class SupportRepresentative(models.Model):
    support_representive = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.support_representive


class Service_request(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField()
    attachment = models.FileField(upload_to="attachments/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    submitted_at = models.DateTimeField(
        default=datetime.datetime.now(), blank=True, null=True
    )
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.customer)

    def isExists(self):
        if Service_request.objects.filter(customer=self.customer):
            return True
        else:
            return False

    @staticmethod
    def getdata(mu_user):
        try:
            return Service_request.objects.get(customer=mu_user)
        except:
            return False


# default=datetime.datetime.now ,blank=True,null=True


class SupportTicket(models.Model):
    service_request = models.OneToOneField(Service_request, on_delete=models.CASCADE)
    support_representative = models.ForeignKey(
        SupportRepresentative, on_delete=models.CASCADE
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(
        default=datetime.datetime.now(), blank=True, null=True
    )

    def __str__(self) -> str:
        return str(self.service_request)

    
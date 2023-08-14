from django.contrib import admin
from app1.models.customer import (
    Customer,
    SupportRepresentative,
    Service_request,
    SupportTicket,
)


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "customer_id")


admin.site.register(Customer, CustomerAdmin)


class SupportRepresentativeAdmin(admin.ModelAdmin):
    list_display = ("support_representive",)


admin.site.register(SupportRepresentative, SupportRepresentativeAdmin)


class Service_requestAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "type",
        "details",
        "attachment",
        "status",
        "submitted_at",
        "resolved_at",
    )


admin.site.register(Service_request, Service_requestAdmin)


class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ("service_request", "support_representative", "notes", "created_at")


admin.site.register(SupportTicket, SupportTicketAdmin)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app1.models.customer import Customer, Service_request

from datetime import datetime, timedelta
import json


def base(request):
    return render(request, "app1/base.html")


def create_request(request):
    today = datetime.now()
    ten_days_later = today + timedelta(days=10)

    if request.method == "GET":
        return render(request, "app1/create_request.html")

    post = request.POST
    customer2 = post.get("customer_id")
    type = post.get("type")
    details = post.get("details")
    attachment = request.FILES.get("attachment")

    print(customer2, type, details, attachment)
    my_user = Customer(customer_id=customer2)

    if my_user.isExists():
        customer3 = Customer.objects.all()
        for customer in customer3:
            # breakpoint()
            create = Service_request(
                customer=customer,
                type=type,
                details=details,
                attachment=attachment,
                resolved_at=str(ten_days_later),
            )
            create.save()

    else:
        return HttpResponse({"customer id wrong"})
    return render(request, "app1/create_request.html")


# Create your views here.


def get(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")

        print("customer_id", customer_id)

        customer = Customer.objects.get(customer_id=customer_id)
        if customer:
            service_requests = Service_request.objects.filter(customer=customer)  #

            return render(request, "app1/data.html", {"pi": service_requests})
    return render(
        request,
        "app1/login.html",
    )

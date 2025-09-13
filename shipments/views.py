from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import InboundShipment, OutboundShipment


@login_required
def dashboard(request):
    company = request.user.company
    inbound = InboundShipment.objects.filter(company=company)
    outbound = OutboundShipment.objects.filter(company=company)
    return render(request, 'shipments/dashboard.html', {
        'inbound': inbound,
        'outbound': outbound,
    })

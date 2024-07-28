from django.shortcuts import render
from .models import Identity, Registered, RegisteredToSaved

# Create your views here.
def index(request):
    return render(request, "identities/index.html", {
        "identities": Identity.objects.all(),
        "registered": Registered.objects.all(),
        "registered_to_saved": RegisteredToSaved.objects.all()
    })
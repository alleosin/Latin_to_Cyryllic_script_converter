from django.shortcuts import render, get_object_or_404
from .models import Acceptor, Donation

# Create your views here.
def view_page(requsest, username):
    owner = get_object_or_404(Acceptor, username)
    if requsest.user == username:
        donations = Donation.objects.filter(acceptor = owner).order_by("-created_date")
    context = {
        "owner": owner,
        "donations": donations,
    }
    return render(requsest, "user_page.html", context)

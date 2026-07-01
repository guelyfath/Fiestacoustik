from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactRequestForm
from .models import Feature, SiteSettings, Testimonial, VideoItem

def home_view(request):
    # Le meme endpoint affiche la home en GET et enregistre une demande en POST.
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre demande a bien ete envoyee.")
            return redirect("/#contact")
    else:
        form = ContactRequestForm()

    # Seuls les contenus actifs remontent sur la page publique.
    testimonials = Testimonial.objects.filter(is_active=True)
    context = {
        "site_settings": SiteSettings.objects.first(),
        "features": Feature.objects.filter(is_active=True),
        "videos": VideoItem.objects.filter(is_active=True),
        "testimonials": testimonials,
        # JSON consomme par static/js/main.js pour paginer les avis sans recharger la page.
        "testimonials_data": [
            {
                "text": testimonial.text,
                "name": testimonial.author_name,
                "event": testimonial.event_label,
            }
            for testimonial in testimonials
        ],
        "contact_form": form,
    }
    return render(request, "index.html", context)

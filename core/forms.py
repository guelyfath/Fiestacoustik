from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    EVENT_TYPE_CHOICES = (
        ("", "Type d'evenement"),
        ("Mariage", "Mariage"),
        ("Anniversaire", "Anniversaire"),
        ("Comite des fetes", "Comite des fetes"),
        ("Restaurant / bar", "Restaurant / bar"),
        ("Soiree privee", "Soiree privee"),
        ("Autre", "Autre"),
    )

    event_type = forms.ChoiceField(choices=EVENT_TYPE_CHOICES, required=False)

    class Meta:
        model = ContactRequest
        fields = ("name", "email", "phone", "event_type", "event_date", "location", "message")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nom complet"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "phone": forms.TelInput(attrs={"placeholder": "Telephone"}),
            "event_date": forms.DateInput(attrs={"type": "date"}),
            "location": forms.TextInput(attrs={"placeholder": "Lieu de l'evenement"}),
            "message": forms.Textarea(attrs={"placeholder": "Votre message"}),
        }

    def save(self, commit=True):
        # La liste du formulaire est fixe ; on stocke seulement son libelle dans la demande.
        contact_request = super().save(commit=False)
        contact_request.event_type_label = self.cleaned_data.get("event_type") or ""

        if commit:
            contact_request.save()

        return contact_request

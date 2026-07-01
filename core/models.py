from django.db import models


class OrderedActiveModel(models.Model):
    # Base commune pour les contenus affiches en liste dans la home.
    order = models.PositiveIntegerField("ordre", default=0)
    is_active = models.BooleanField("actif", default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class SiteSettings(models.Model):
    # Configuration interne du site : non exposee dans l'admin client.
    site_name = models.CharField("nom du site", max_length=120, default="Fiestacoustik")
    logo = models.FileField("logo", upload_to="site/", blank=True)
    phone = models.CharField("telephone", max_length=30, blank=True)
    email = models.EmailField("email", blank=True)
    location = models.CharField("zone geographique", max_length=180, blank=True)
    instagram_url = models.URLField("Instagram", blank=True)
    facebook_url = models.URLField("Facebook", blank=True)
    youtube_url = models.URLField("YouTube", blank=True)
    quote_button_text = models.CharField(
        "texte du bouton devis",
        max_length=80,
        default="Demander un devis",
    )
    contact_eyebrow = models.CharField(
        "accroche contact",
        max_length=120,
        default="Parlons de votre projet",
    )
    contact_title = models.CharField(
        "titre contact",
        max_length=160,
        default="Un evenement en preparation ?",
    )
    contact_text = models.TextField(
        "texte contact",
        default="Remplissez le formulaire, je vous reponds rapidement pour en discuter.",
    )
    footer_company = models.CharField("entreprise footer", max_length=120, default="Maguely")
    footer_text = models.CharField(
        "texte footer",
        max_length=220,
        default="Creation de sites vitrines et experiences web sur mesure.",
    )

    class Meta:
        verbose_name = "reglage du site"
        verbose_name_plural = "reglages du site"

    def __str__(self):
        return self.site_name


class Feature(OrderedActiveModel):
    # Petits arguments sous le hero : icone, chiffre/titre et libelle.
    icon_name = models.CharField(
        "icone Lucide",
        max_length=80,
        default="music",
        help_text="Exemples : music, users, volume-2, star.",
    )
    title = models.CharField("titre ou chiffre", max_length=80)
    text = models.CharField("texte", max_length=120)

    class Meta(OrderedActiveModel.Meta):
        verbose_name = "argument hero"
        verbose_name_plural = "arguments hero"

    def __str__(self):
        return f"{self.title} {self.text}".strip()


class VideoItem(OrderedActiveModel):
    # Une video geree par le client : URL externe et miniature optionnelle.
    title = models.CharField("titre", max_length=120)
    subtitle = models.CharField("sous-titre", max_length=140, blank=True)
    video_url = models.URLField("URL de la video", blank=True)
    thumbnail = models.FileField("image miniature", upload_to="videos/", blank=True)

    class Meta(OrderedActiveModel.Meta):
        verbose_name = "video"
        verbose_name_plural = "videos"

    def __str__(self):
        return self.title


class Testimonial(OrderedActiveModel):
    # Avis clients affiches dans le carousel de la page d'accueil.
    text = models.TextField("avis")
    author_name = models.CharField("nom", max_length=120)
    event_label = models.CharField("evenement", max_length=120, blank=True)

    class Meta(OrderedActiveModel.Meta):
        verbose_name = "avis client"
        verbose_name_plural = "avis clients"

    def __str__(self):
        return self.author_name


class ContactRequest(models.Model):
    # Demandes envoyees depuis le formulaire public, consultables dans l'admin.
    class Status(models.TextChoices):
        NEW = "new", "Nouveau"
        READ = "read", "Lu"
        DONE = "done", "Traite"
        ARCHIVED = "archived", "Archive"

    name = models.CharField("nom complet", max_length=120)
    email = models.EmailField("email")
    phone = models.CharField("telephone", max_length=30, blank=True)
    event_type_label = models.CharField("type d'evenement saisi", max_length=120, blank=True)
    event_date = models.DateField("date de l'evenement", null=True, blank=True)
    location = models.CharField("lieu de l'evenement", max_length=180, blank=True)
    message = models.TextField("message")
    status = models.CharField(
        "statut",
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    created_at = models.DateTimeField("date de creation", auto_now_add=True)
    updated_at = models.DateTimeField("date de modification", auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "demande de contact"
        verbose_name_plural = "demandes de contact"

    def __str__(self):
        return f"{self.name} - {self.created_at:%d/%m/%Y}"

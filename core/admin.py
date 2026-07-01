from django.contrib import admin

from .models import (
    ContactRequest,
    Feature,
    Testimonial,
    VideoItem,
)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    # Elements autorises : la barre d'arguments sous le hero.
    list_display = ("title", "text", "icon_name", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "text")


@admin.register(VideoItem)
class VideoItemAdmin(admin.ModelAdmin):
    # Elements autorises : les cartes videos.
    list_display = ("title", "subtitle", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "subtitle", "video_url")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # Elements autorises : les avis clients.
    list_display = ("author_name", "event_label", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("author_name", "event_label", "text")


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    # Ce model n'est pas un contenu de page : il sert a suivre les demandes recues.
    list_display = ("name", "email", "phone", "event_type_label", "event_date", "status", "created_at")
    list_editable = ("status",)
    list_filter = ("status", "event_type_label", "created_at")
    search_fields = ("name", "email", "phone", "location", "message")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    fieldsets = (
        ("Contact", {"fields": ("name", "email", "phone")}),
        ("Evenement", {"fields": ("event_type_label", "event_date", "location")}),
        ("Demande", {"fields": ("message", "status")}),
        ("Suivi", {"fields": ("created_at", "updated_at")}),
    )


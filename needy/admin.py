from django.contrib import admin
from .models import Needy

@admin.register(Needy)
class NeedyAdmin(admin.ModelAdmin):
    list_display = ("full_name", "national_code", "phone_number", "path", "created_by", "birth_date")
    list_filter = ("path", "marital_status", "is_covered", "religion")
    search_fields = ("full_name", "national_code", "phone_number")
    ordering = ("full_name",)
    list_editable = ("path",)
    list_per_page = 20

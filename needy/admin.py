from django.contrib import admin
from .models import Street, NeedyPath, Needy


class StreetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class NeedyPathAdmin(admin.ModelAdmin):
    list_display = ('street', 'name')
    search_fields = ('street__name', 'name')
    list_filter = ('street',)


class NeedyAdmin(admin.ModelAdmin):
    list_display = (
    'full_name', 'national_code', 'phone_number', 'street', 'path', 'is_covered', 'marital_status', 'religion')
    search_fields = ('full_name', 'national_code', 'phone_number', 'street__name', 'path__name')
    list_filter = ('is_covered', 'marital_status', 'religion', 'street', 'path')
    list_per_page = 20

    # نمایش اطلاعات اضافی
    def has_add_permission(self, request):
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return super().has_delete_permission(request, obj)


admin.site.register(Street, StreetAdmin)
admin.site.register(NeedyPath, NeedyPathAdmin)
admin.site.register(Needy, NeedyAdmin)

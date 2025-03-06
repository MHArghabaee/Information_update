from django.contrib import admin
from .models import Needy
from .models import Street

admin.site.register(Street)
@admin.register(Needy)
class NeedyAdmin(admin.ModelAdmin):
    list_display = ("full_name", "national_code", "phone_number", "path", "created_by", "birth_date")
    list_filter = ("path", "marital_status", "is_covered", "religion")
    search_fields = ("full_name", "national_code", "phone_number")
    ordering = ("full_name",)
    list_editable = ("path",)
    list_per_page = 20


from django.contrib import admin
from .models import NeedyPath, Street

class NeedyPathAdmin(admin.ModelAdmin):
    list_display = ('street', 'name')  # فیلدهایی که در لیست نمایش داده شوند
    search_fields = ('name',)  # امکان جستجو بر اساس نام مسیر
    list_filter = ('street',)  # فیلتر کردن بر اساس خیابان
    ordering = ('street', 'name')  # ترتیب پیش‌فرض بر اساس خیابان و سپس نام مسیر

    # اضافه کردن گزینه برای فیلدهای انتخابی در فرم و صفحه ویرایش
    fieldsets = (
        (None, {
            'fields': ('street', 'name')
        }),
    )

# ثبت مدل و پنل ادمین
admin.site.register(NeedyPath, NeedyPathAdmin)

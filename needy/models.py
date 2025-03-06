from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import BooleanField

User = get_user_model()

from django.db import models


class Street(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="نام خیابان")

    def __str__(self):
        return self.name


class NeedyPath(models.Model):
    street = models.ForeignKey(Street, on_delete=models.SET_NULL, null=True, related_name="paths",
                               verbose_name="خیابان مربوطه")
    name = models.CharField(max_length=255, verbose_name="نام مسیر")

    def __str__(self):
        return f"{self.street.name} - {self.name}"


class Needy(models.Model):
    PATH_CHOICES = [("تعریف نشده", "تعریف نشده")] + [(str(i), f"مسیر {i}") for i in range(1, 11)]
    COVERAGE_CHOICES = [
        ('بدون پوشش', 'بدون پوشش'),
        ('کمیته امداد', 'کمیته امداد'),
        ('بهزیستی', 'بهزیستی'),
        ('کمیته امداد و بهزیستی', 'کمیته امداد و بهزیستی'),
    ]
    MARITAL_STATUS_CHOICES = [
        ("مجرد", "مجرد"),
        ("متاهل", "متاهل"),
        ("متارکه", "متارکه"),
    ]
    RELIGION_CHOICES = [
        ("شیعه", "شیعه"),
        ("سنی", "سنی"),
    ]
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="کاربر ایجاد کننده")

    introducer_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی معرف", null=True, blank=True)
    introducer_phone = models.CharField(max_length=15, verbose_name="شماره تلفن معرف", null=True, blank=True)
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی", null=True, blank=True)
    father_name = models.CharField(max_length=100, verbose_name="نام پدر", null=True, blank=True)
    family_members = models.IntegerField(verbose_name="تعداد اعضای تحت سرپرستی", null=True, blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", null=True, blank=True)
    marital_status = models.CharField(
        max_length=20,
        verbose_name="وضعیت تاهل",
        choices=MARITAL_STATUS_CHOICES,
        null=True,
        blank=True
    )
    religion = models.CharField(
        max_length=50,
        verbose_name="مذهب",
        choices=RELIGION_CHOICES,
        null=True,
        blank=True
    )
    job = models.CharField(max_length=100, verbose_name="شغل", null=True, blank=True)
    is_covered = models.CharField(max_length=100, choices=COVERAGE_CHOICES, verbose_name="تحت پوشش", null=True,
                                  blank=True)
    national_code = models.CharField(max_length=10, verbose_name="کد ملی", null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس", null=True, blank=True)
    street = models.ForeignKey(
        Street,
        verbose_name="خیابان",
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL
    )
    path = models.ForeignKey(
        NeedyPath,
        verbose_name="مسیر",
        null=True,
        blank=True,
        default=1,
        on_delete=models.SET_NULL
    )
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    house_number = models.CharField(max_length=12, verbose_name="پلاک", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    latitude = models.FloatField(
        null=True, blank=True, verbose_name="عرض جغرافیایی",
    )

    longitude = models.FloatField(
        null=True, blank=True, verbose_name="طول جغرافیایی",
    )

    location = models.CharField(max_length=255, null=True, blank=True, verbose_name="موقعیت جغرافیایی")
    location_link = models.CharField(
        max_length=500,
        null=True, blank=True,
        verbose_name="لینک موقعیت مکانی در نشان"
    )

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.location = f"Latitude: {self.latitude}, Longitude: {self.longitude}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

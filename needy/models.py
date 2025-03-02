from django.db import models

class Needy(models.Model):
    introducer_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی معرف", null=True, blank=True)
    introducer_phone = models.CharField(max_length=15, verbose_name="شماره تلفن معرف", null=True, blank=True)
    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی", null=True, blank=True)
    father_name = models.CharField(max_length=100, verbose_name="نام پدر", null=True, blank=True)
    family_members = models.IntegerField(verbose_name="تعداد اعضای تحت سرپرستی", null=True, blank=True)
    birth_date = models.DateField(verbose_name="تاریخ تولد", null=True, blank=True)
    marital_status = models.CharField(max_length=20, verbose_name="وضعیت تاهل", null=True, blank=True)
    religion = models.CharField(max_length=50, verbose_name="مذهب", null=True, blank=True)
    job = models.CharField(max_length=100, verbose_name="شغل", null=True, blank=True)
    is_covered = models.CharField(max_length=100, verbose_name="تحت پوشش", null=True, blank=True)
    national_code = models.CharField(max_length=10, verbose_name="کد ملی", null=True, blank=True)
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس", null=True, blank=True)
    street = models.CharField(max_length=100, verbose_name="خیابان", null=True, blank=True)
    address = models.TextField(verbose_name="آدرس", null=True, blank=True)
    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)

    def __str__(self):
        return self.full_name
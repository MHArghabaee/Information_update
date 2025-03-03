from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Needy
import jdatetime
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from openpyxl.styles import Alignment, Border, Side, Font
from openpyxl import Workbook
from .models import Needy

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from openpyxl.styles import Alignment, Border, Side, Font
from openpyxl import Workbook
from .models import Needy
from datetime import datetime
import jdatetime  # کتابخانه‌ی تبدیل تاریخ به شمسی


def convert_persian_to_gregorian(persian_date):
    try:
        persian_date_obj = jdatetime.datetime.strptime(persian_date, "%Y/%m/%d")
        gregorian_date = persian_date_obj.togregorian()
        return gregorian_date.strftime("%Y-%m-%d")  # تبدیل به فرمت میلادی YYYY-MM-DD
    except ValueError:
        return None


def convert_gregorian_to_jalali(date_string):
    # تبدیل رشته ورودی به تاریخ میلادی
    gregorian_date = datetime.strptime(str(date_string), "%Y-%m-%d")

    # تبدیل تاریخ میلادی به شمسی
    jalali_date = jdatetime.date.fromgregorian(
        year=gregorian_date.year,
        month=gregorian_date.month,
        day=gregorian_date.day
    )

    # فرمت‌دهی تاریخ شمسی به صورت YYYY/MM/DD
    formatted_jalali_date = jalali_date.strftime("%Y/%m/%d")

    return formatted_jalali_date
def add_needy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        user = request.user
        path_choices = Needy.PATH_CHOICES
        selected_path = request.POST.get('path',
                                         'تعریف نشده')  # اگر هیچ مسیری انتخاب نشده باشد، "تعریف نشده" پیش‌فرض می‌شود.

        has_introducer = request.POST.get('has_introducer')
        introducer_name = request.POST.get('introducer_name')
        introducer_phone = request.POST.get('introducer_phone')
        full_name = request.POST.get('full_name')
        father_name = request.POST.get('father_name')
        family_members = request.POST.get('family_members')
        birth_date = request.POST.get('birth_date')
        marital_status = request.POST.get('marital_status')
        religion = request.POST.get('religion')
        job = request.POST.get('job')
        is_covered = request.POST.get('is_covered')
        national_code = request.POST.get('national_code')
        phone_number = request.POST.get('phone_number')
        street = request.POST.get('street')
        address = request.POST.get('address')
        description = request.POST.get('description')
        birth_date = convert_persian_to_gregorian(birth_date)

        if has_introducer == None:
            introducer_name = user.get_full_name()
            introducer_phone = user.username
        try:
            Needy.objects.create(
                created_by=user,
                introducer_name=introducer_name,
                introducer_phone=introducer_phone,
                full_name=full_name,
                father_name=father_name,
                family_members=family_members,
                birth_date=birth_date,
                marital_status=marital_status,
                religion=religion,
                job=job,
                is_covered=is_covered,
                national_code=national_code,
                phone_number=phone_number,
                street=street,
                address=address,
                description=description,
                path=selected_path  # ذخیره مسیر انتخابی
            )
            return redirect('success_view')
        except Exception as e:
            print(str(e))


    return render(request, 'needy/add_needy.html',
                  {'path_choices': Needy.PATH_CHOICES, 'selected_path': request.POST.get('path', 'undefined')})


def success_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # پیدا کردن آخرین نیازمند ثبت شده توسط کاربر جاری
    last_needy = Needy.objects.filter(created_by=request.user).last()

    if last_needy is None:
        # اگر نیازمندی وجود نداشت، کاربر را به صفحه‌ی ثبت هدایت می‌کنیم
        return redirect('register_needy')

    # ارسال اطلاعات نیازمند به تمپلیت
    return render(request, 'needy/success.html', {'needy': last_needy})



def needy_list(request):
    needy = Needy.objects.all()
    context = {'needy': needy}
    return render(request, 'needy/needy_list.html', context)







def export_needy_to_excel(request):
    # دریافت تمامی نیازمندان از دیتابیس
    needy_list = get_list_or_404(Needy)

    # ایجاد یک DataFrame از لیست نیازمندان
    data = {
        'کاربر ایجاد کننده': [needy.created_by.get_full_name() if needy.created_by else 'نامشخص' for needy in needy_list],
        'نام و نام خانوادگی معرف': [needy.introducer_name for needy in needy_list],
        'شماره تلفن معرف': [needy.introducer_phone for needy in needy_list],
        'نام و نام خانوادگی': [needy.full_name for needy in needy_list],
        'نام پدر': [needy.father_name for needy in needy_list],
        'تعداد اعضای تحت سرپرستی': [needy.family_members for needy in needy_list],
        'تاریخ تولد': [convert_gregorian_to_jalali(needy.birth_date) if needy.birth_date else '' for needy in needy_list],  # تبدیل تاریخ به شمسی
        'وضعیت تاهل': [needy.marital_status for needy in needy_list],
        'مذهب': [needy.religion for needy in needy_list],
        'شغل': [needy.job for needy in needy_list],
        'تحت پوشش': [needy.is_covered for needy in needy_list],
        'کد ملی': [needy.national_code for needy in needy_list],
        'شماره تماس': [needy.phone_number for needy in needy_list],
        'مسیر': [needy.path for needy in needy_list],
        'خیابان': [needy.street for needy in needy_list],
        'آدرس': [needy.address for needy in needy_list],
        'توضیحات': [needy.description for needy in needy_list],
    }

    df = pd.DataFrame(data)

    # ایجاد یک Workbook جدید با openpyxl
    wb = Workbook()
    ws = wb.active

    # تنظیم جهت صفحه به راست‌به‌چپ
    ws.sheet_view.rightToLeft = True

    # اضافه کردن تیترهای ستون‌ها
    for col_num, column_title in enumerate(df.columns, 1):
        cell = ws.cell(row=1, column=col_num, value=column_title)
        cell.font = Font(bold=True)  # تیترهای ستون‌ها را پررنگ می‌کنیم
        cell.alignment = Alignment(horizontal='right')  # تراز راست برای تیترها

    # اضافه کردن داده‌های DataFrame به Worksheet
    for r_idx, row in enumerate(df.itertuples(index=False), start=2):  # شروع از ردیف ۲ به بعد
        for c_idx, value in enumerate(row, start=1):
            ws.cell(row=r_idx, column=c_idx, value=value)

    # تنظیم تراز متن به راست برای تمام سلول‌ها
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(horizontal='right')

    # اعمال Border برای تمام سلول‌ها
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    for row in ws.iter_rows():
        for cell in row:
            cell.border = thin_border

    # ایجاد یک پاسخ HTTP با نوع محتوای اکسل
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="needy_list.xlsx"'

    # ذخیره Workbook در فایل اکسل و ارسال آن به عنوان پاسخ
    wb.save(response)

    return response
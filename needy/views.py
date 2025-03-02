from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Needy
import jdatetime


def convert_persian_to_gregorian(persian_date):
    try:
        persian_date_obj = jdatetime.datetime.strptime(persian_date, "%Y/%m/%d")
        gregorian_date = persian_date_obj.togregorian()
        return gregorian_date.strftime("%Y-%m-%d")  # تبدیل به فرمت میلادی YYYY-MM-DD
    except ValueError:
        return None


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


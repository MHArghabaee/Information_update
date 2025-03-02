from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Needy


def add_needy(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
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

        try:
            Needy.objects.create(
                created_by=request.user,
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
                description=description
            )
            messages.success(request, 'اطلاعات نیازمند با موفقیت ثبت شد.')
            return redirect('register_needy')
        except Exception as e:
            messages.error(request, f'خطا در ثبت اطلاعات: {str(e)}')

    return render(request, 'needy/add_needy.html')

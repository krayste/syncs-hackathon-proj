from django.shortcuts import render
from assessments.models import DB_Unit


def assessments(request):
    test_db = DB_Unit.objects.get(code="MECH2400")
    test_obj = test_db.obj()
    print(test_obj)

    unit_qs = DB_Unit.objects.filter()
    context = {"unit_list": unit_qs}
    return render(request, 'assessments.html', context)

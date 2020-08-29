from django.shortcuts import render
from assessments.models import DB_Unit
from django.http import HttpResponse


def assessments(request):
    test_db = DB_Unit.objects.get(code="MECH2400")
    test_obj = test_db.obj()
    print(test_obj)

    unit_qs = DB_Unit.objects.filter()
    context = {"unit_list": unit_qs}
    return render(request, 'assessments.html', context)


def generate(request):

    if request.method == "POST":
        # Create list of unit objects according to website input
        list_of_units = []
        unit_codes = request.POST.getlist('units')
        # If no units are selected, do nothing
        if not unit_codes:
            return HttpResponse(status=204)

        for unit_code in unit_codes:
            unit_db = DB_Unit.objects.get(code=unit_code)
            unit_obj = unit_db.obj()
            list_of_units.append(unit_obj)

        return HttpResponse('')

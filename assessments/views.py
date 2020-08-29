from django.shortcuts import render
from assessments.models import DB_Unit
from django.http import HttpResponse
from utils.unit import Assessment
from django.template.loader import render_to_string


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
        list_of_assessments = []
        unit_codes = request.POST.getlist('units')
        # If no units are selected, do nothing
        if not unit_codes:
            return HttpResponse(status=204)

        for unit_code in unit_codes:
            unit_db = DB_Unit.objects.get(code=unit_code)
            unit_obj = unit_db.obj()
            list_of_units.append(unit_obj)

        for unit in list_of_units:
            list_of_assessments.extend(unit.list_of_assessments)

        assessments_dict = Assessment.create_dictionary(
            list_of_assessments)
        unit_codes = [unit.code for unit in list_of_units]

        context = {
            "assessments_dict": assessments_dict,
            "unit_codes": unit_codes,
        }
        assessments_html = render_to_string(
            'assessment_disp.html', context)

        return HttpResponse(assessments_html)

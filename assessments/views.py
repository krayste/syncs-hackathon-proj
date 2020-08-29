from django.shortcuts import render
from assessments.models import DB_Unit
from django.http import HttpResponse
from utils.unit import Assessment
from django.template.loader import render_to_string

import os
from wsgiref.util import FileWrapper


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

        context = {"assessments_dict": assessments_dict}
        assessments_html = render_to_string(
            'assessment_disp.html', context)

        return HttpResponse(assessments_html)


def send_pdf_file(request):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    filename = "static_files/output.pdf"  # Select your file here.
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper, content_type='application/pdf/force-download')
    response['Content-Length'] = os.path.getsize(filename)
    return response

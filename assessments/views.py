from django.shortcuts import render
from assessments.models import DB_Unit
from django.http import HttpResponse
from utils.unit import Assessment
import utils.identify_finals as i_f
from django.template.loader import render_to_string

import os
from wsgiref.util import FileWrapper

import utils.md2pdf as pdf
import utils.event_generator as event

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

        for a in list_of_assessments:
            i_f.identify_finals(a)
        assessments_dict = Assessment.create_dictionary(
            list_of_assessments)
        print(assessments_dict)

        context = {
            "assessments_dict": assessments_dict,
            "list_of_units": list_of_units,
        }
        assessments_html = render_to_string(
            'assessment_disp.html', context)

        # Save a pdf to static files
        assessment_list = pdf.order_ass(list_of_units)
        md_string = pdf.create_md_string(assessment_list)
        print(md_string)
        # pdf.string_to_pdf(md_string)

        # Save an ics to static files
        event.event_generator(list_of_units)

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

def send_ics_file(request):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    filename = "static_files/calendar.ics"  # Select your file here.
    wrapper = FileWrapper(open(filename, 'rb'))
    response = HttpResponse(wrapper, content_type='application/ics/force-download')
    response['Content-Length'] = os.path.getsize(filename)
    return response

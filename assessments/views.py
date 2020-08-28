from django.shortcuts import render
from assessments.models import DB_Unit


def assessments(request):
    unit_qs = DB_Unit.objects.filter()
    context = {"unit_list": unit_qs}
    return render(request, 'assessments.html', context)

from django.shortcuts import render

def assessments(request):
    return render(request, 'assessments.html', {})

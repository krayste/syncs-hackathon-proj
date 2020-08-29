from django.urls import path
from assessments import views

urlpatterns = [
    path('', views.assessments, name='assessments'),
    path('generate', views.generate, name='generate'),
    path('output.pdf', views.send_pdf_file, name='send_pdf_file'),
    path('calendar.ics', views.send_ics_file, name='send_ics_file'),
]

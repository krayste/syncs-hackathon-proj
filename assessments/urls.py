from django.urls import path
from assessments import views

urlpatterns = [
    path('', views.assessments, name='assessments'),
]

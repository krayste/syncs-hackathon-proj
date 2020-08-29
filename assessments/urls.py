from django.urls import path
from assessments import views

urlpatterns = [
    path('', views.assessments, name='assessments'),
    path('generate', views.generate, name='generate'),
]

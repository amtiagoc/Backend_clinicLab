from django.urls import path
from django.views.generic import TemplateView

app_name = 'crud_exams'

urlpatterns = [
    path('', TemplateView.as_view(template_name='crud_exams/index.html'), name='index'),
]
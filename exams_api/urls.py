from django.urls import path, include
from .views import ExamsList, ExamsDetail

app_name = 'exams_api'

urlpatterns = [
    path('', ExamsList.as_view(), name='list'),
    path('<int:pk>/', ExamsDetail.as_view(), name='detail'),
]
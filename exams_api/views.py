from rest_framework import generics
from crud_exams.models import Exams
from .serializers import ExamsSerializer

class ExamsList(generics.ListCreateAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    pass

class ExamsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    pass


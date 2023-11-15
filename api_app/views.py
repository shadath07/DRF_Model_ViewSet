from .models import *
from .serializers import *
from rest_framework import viewsets

# using this will get all the CRUd operations built in by django restframework
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer



# ReadOnlyModelViewSet -------------------->

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
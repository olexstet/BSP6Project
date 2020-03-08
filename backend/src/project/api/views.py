from rest_framework.generics import ListAPIView, RetrieveAPIView
from project.models import Question1 
from .serializers import Question1Serializer


class Question1ListView(ListAPIView):
    queryset = Question1.objects.all()
    serializer_class = Question1Serializer 

class Question1DetailView(RetrieveAPIView):
    queryset = Question1.objects.all()
    serializer_class = Question1Serializer 


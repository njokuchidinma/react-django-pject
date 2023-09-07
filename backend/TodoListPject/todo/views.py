from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer



class Todolist(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class Tododetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

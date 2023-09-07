from django.urls import path
from .views import Todolist, Tododetail


urlpatterns = [
    path('<int:pk>/', Tododetail.as_view()),
    path('', Todolist.as_view()),
]
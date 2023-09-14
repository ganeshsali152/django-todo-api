from django.urls import path

from todo.views import ToDoDetail, ToDoList

urlpatterns = [
    path("todos", ToDoList.as_view()),
    path("todos/<int:pk>", ToDoDetail.as_view()),
]

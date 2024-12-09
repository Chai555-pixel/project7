# todo/urls.py
from django.urls import path
from .views import home, TaskList, TaskDetail, TaskCreate

urlpatterns = [
    path('', home, name='home'),  # Home page route
    path('tasks/', TaskList.as_view(), name='tasks'),  # Task list route
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),  # Task detail route
    path('task/create/', TaskCreate.as_view(), name='task-create'),  # Create task route
]

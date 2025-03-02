from django.urls import path
from .views import task_list, mark_done, delete_task, edit_task  # Import edit_task!

urlpatterns = [
    path('', task_list, name='task-list'),
    path('done/<int:task_id>/', mark_done, name='mark-done'),
    path('delete/<int:task_id>/', delete_task, name='delete-task'),
    path('edit/<int:task_id>/', edit_task, name='edit-task'),  # Make sure this line is correct
]

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from datetime import datetime

def task_list(request):
    """View to display all tasks and add a new one with a due date."""
    if request.method == "POST":
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        importance = request.POST.get("importance", "medium")  # Default to 🍦 Normal
        tag = request.POST.get("tag")
        annoying = request.POST.get("annoying") == "on"

        # ✅ Fix: Only create the task once!
        new_task = Task(
            title=title,
            completed=False,  # ✅ Ensures all new tasks start as "Not Done"
            due_date=datetime.strptime(due_date, "%Y-%m-%d").date() if due_date else None,
            importance=importance,
            tag=tag,
            annoying=annoying
        )
        new_task.save()

        return redirect('task-list')  # Refresh the page after adding a task

    # ✅ Fix: Ensure both "Not Done" and "Done" lists are correctly fetched
    tasks_not_done = Task.objects.filter(completed=False).order_by('due_date')
    tasks_done = Task.objects.filter(completed=True).order_by('due_date')

    return render(request, 'myapp/task_list.html', {
        'tasks_not_done': tasks_not_done,
        'tasks_done': tasks_done
    })

def mark_done(request, task_id):
    """Mark a task as done and move it to the Done list"""
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('task-list')  # ✅ Ensure it redirects correctly

def delete_task(request, task_id):
    """View to delete a task."""
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task-list')

def edit_task(request, task_id):
    """Edit an existing task instead of creating a duplicate."""
    task = get_object_or_404(Task, id=task_id)  # Get the correct task

    if request.method == "POST":
        # Update task fields
        task.title = request.POST.get("title")
        task.importance = request.POST.get("importance", "medium")
        task.tag = request.POST.get("tag")
        task.annoying = request.POST.get("annoying") == "on"
        task.completed = request.POST.get("completed") == "on"

        # Update the due date correctly
        due_date_str = request.POST.get("due_date")
        if due_date_str:
            try:
                task.due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            except ValueError:
                task.due_date = None  # Prevent errors if the date is invalid
        else:
            task.due_date = None  # Allow clearing the date

        task.save()  # Save the task update
        return redirect('task-list')  # Refresh the page after saving

    return redirect('task-list')




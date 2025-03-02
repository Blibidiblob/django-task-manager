# Generated by Django 5.1.6 on 2025-03-02 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_task_due_date_alter_task_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="annoying",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="task",
            name="importance",
            field=models.CharField(
                choices=[
                    ("high", "🦄 Very Important"),
                    ("medium", "🍦 Normal Importance"),
                    ("low", "🦡 Not So Important"),
                ],
                default="medium",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="tag",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

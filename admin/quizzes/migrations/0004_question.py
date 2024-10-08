# Generated by Django 5.0.7 on 2024-09-05 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_remove_question_quiz_alter_quiz_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('choices', models.JSONField()),
                ('is_required', models.BooleanField(default=False)),
                ('question_type', models.CharField(choices=[('radio', 'Single Answer'), ('checkbox', 'Multiple Answers')], max_length=20)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quizzes.quiz')),
            ],
        ),
    ]

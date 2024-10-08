# Generated by Django 5.0.7 on 2024-09-14 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='question',
            name='is_required',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='Default question text', max_length=500),
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('radio', 'Single Choice'), ('checkbox', 'Multiple Choice')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.TextField(default='No description available'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='quizzes.question')),
            ],
        ),
    ]

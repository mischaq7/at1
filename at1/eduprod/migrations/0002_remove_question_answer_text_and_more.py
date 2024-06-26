# Generated by Django 5.0.2 on 2024-03-31 22:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.TextField(default='', help_text='Enter the correct answer'),
        ),
        migrations.AddField(
            model_name='question',
            name='sentence',
            field=models.TextField(default=django.utils.timezone.now, help_text='Enter the sentence without punctuation'),
            preserve_default=False,
        ),
    ]

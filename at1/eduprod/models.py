from django.db import models

class Question(models.Model):
    sentence = models.TextField(help_text="Enter the sentence without punctuation")
    correct_answer = models.TextField(help_text="Enter the correct answer", default='')  # Default value set to an empty string

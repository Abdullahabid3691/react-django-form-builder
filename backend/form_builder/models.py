from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Question(models.Model):
    class QuestionTypes(models.TextChoices):
        TEXT = 'TEXT', _('Text Field')
        EMAIL = 'EMAIL', _('Email Field')
        MULTIPLE = 'MULTIPLE', _('Multiple Choices')
        DROPDOWN = 'DROPDOWN', _('Dropdown')

    question_type = models.CharField(
        max_length=10,
        choices=QuestionTypes.choices,
        default=QuestionTypes.TEXT,
    )
    question = models.CharField(max_length=10000)
    choices = models.JSONField()
    form = models.ForeignKey(Form, related_name="questions", on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_to")


class Responses(models.Model):
    response_to = models.ForeignKey(Form, on_delete=models.CASCADE, related_name="response_to")
    responder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="responder", blank=True,
                                  null=True)
    response = models.ManyToManyField(Answer, related_name="response")

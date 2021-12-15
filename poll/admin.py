from django.contrib import admin
from poll.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

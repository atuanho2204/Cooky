from django.contrib import admin
from django.contrib.auth.models import User
from .models import Choice, Question, Food, Weekly
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Food)
admin.site.register(Weekly)


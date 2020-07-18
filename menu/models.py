from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    introduction = models.TextField(max_length=300, default='')
    description = models.TextField(default='')
    picture = models.ImageField(upload_to='photo', blank=True)




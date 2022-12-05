from datetime import date, datetime
from django.db import models
from matplotlib import widgets
from django.utils import timezone
from .input_param import plate_appearance, hand, ball_type, mph, result, season
# Create your models here.
from django.db import models
from datetime import date

#モデルクラスを定義
class Information(models.Model):
    date = models.DateField(default= date.today())
    season = models.CharField(choices=season,max_length=200)
    plate_appearance = models.CharField(choices=plate_appearance, max_length=200)
    first_runner = models.BooleanField(default=False)
    second_runner = models.BooleanField(default=False)
    third_runner = models.BooleanField(default=False)
    hand = models.CharField(choices=hand, max_length=200)
    ball_type = models.CharField(choices=ball_type, max_length=200)
    mph = models.CharField(choices=mph, max_length=200, default="90")
    result = models.CharField(choices=result, max_length=200)

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    mail = models.EmailField()

    def __str__(self):
        return str(self.age)
    
from django.db import models
from django.db.models.enums import Choices

class Forecast(models.Model):
    def __str__(self):
        return self.roomno
    
    roomno = models.CharField(null = True,max_length=5)
    day1lbs = models.IntegerField(default=0)
    day2lbs = models.IntegerField(default=0)
    day3lbs = models.IntegerField(default=0)
    day4lbs = models.IntegerField(default=0)
    day5lbs = models.IntegerField(default=0)
    lg5pct = models.IntegerField(default=0)
    med10pct = models.IntegerField(default=0)
    sm10pct = models.IntegerField(default=0)
    updated = models.DateField(auto_now_add=True)


# class Forecast1(models.Model):
#     models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)


from django.db import models
from datetime import datetime

class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group_name',
        db_column='group_name'
    )

    group_start_date = models.DateField(default=datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))

    group_finish_date = models.DateField(default="22/04/2023")
    
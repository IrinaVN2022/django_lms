from django.db import models
from datetime import datetime

class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group_name',
        db_column='group_name'
    )

    group_start_date = models.DateField(default='06/12/2022')

    group_finish_date = models.DateField(default='06/04/2023')
    
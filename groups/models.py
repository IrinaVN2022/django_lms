from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group_name',
        db_column='group_name'
    )

    group_start_date = models.DateField(default='22/01/2023')
    group_finish_date = models.DateField(default="22/04/2023")
    
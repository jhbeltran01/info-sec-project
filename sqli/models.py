from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )
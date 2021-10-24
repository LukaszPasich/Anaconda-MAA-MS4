from django.db import models
from django.core.validators import MaxValueValidator


class Membership(models.Model):
    """ Model for Memberships"""

    membership_no = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=32)
    small_name = models.CharField(max_length=32, null=True, blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    pay_interval = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

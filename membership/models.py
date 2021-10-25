from django.db import models
from django.core.validators import MaxValueValidator


class Discipline(models.Model):
    """ Model for Disciplines"""

    name = models.CharField(max_length=32)
    friendly_name = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Membership(models.Model):
    """ Model for Memberships"""

    discipline = models.ForeignKey('Discipline', null=True, blank=True, on_delete=models.SET_NULL)
    membership_no = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=32)
    small_name = models.CharField(max_length=32, null=True, blank=True)
    all_classes = models.BooleanField(default=False)
    price = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    pay_interval = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

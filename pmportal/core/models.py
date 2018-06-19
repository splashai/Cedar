from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    unit                = models.CharField(max_length=10)
    street_no           = models.CharField(max_length=10)
    street              = models.CharField(max_length=100)
    city                = models.CharField(max_length=100)
    province            = models.CharField(max_length=100)
    country             = models.CharField(max_length=100)
    postal_code         = models.CharField(max_length=10)

    def __str__(self):
        return '{} , {}, {}'.format(self.unit, self.street_no, self.street)


class Site(models.Model):
    site_name                = models.CharField(max_length=100)
    site_address             = models.ForeignKey(Address, on_delete=models.PROTECT)
    site_total_units         = models.IntegerField()
    site_floors              = models.IntegerField()
    site_manager             = models.ForeignKey(User, on_delete=models.PROTECT, related_name='manager')
    site_supervisor          = models.ForeignKey(User, on_delete=models.PROTECT, related_name='supervisor')
    site_agent               = models.ForeignKey(User, on_delete=models.PROTECT, related_name='agent')
    site_prime               = models.IntegerField()

    def __str__(self):
        return self.site_name


class Unit(models.Model):
    unit_number              = models.IntegerField()
    unit_floor               = models.IntegerField()
    unit_site                = models.ForeignKey(Site, on_delete=models.PROTECT, related_name='site')
    unit_address             = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='address')
    unit_type                = models.IntegerField()
    unit_details             = models.TextField()

    def __str__(self):
        return self.unit_number

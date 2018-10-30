from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class ChemicalItem(models.Model):
    """

        One chemical item is one entry to the excel item list from Tongyu

        args:
            See the excel form from  Tongyu

        These arguments cannot be blank (You can choose empty values, however):
            chemical_name
            storage_location
            quantity
            unit
    """
    chemical_name = models.CharField(max_length=200)
    storage_location = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10)
    company_name = models.CharField(max_length=200, default="")
    catalog_number = models.CharField(max_length=50, default="")
    order_date = models.DateField(null=True, blank=True)
    expiration_date = models.DateField('date of expiration', null=True, blank=True)
    comment = models.TextField(default="", blank=True)

    def __str__(self):
        return "{} at {}\n".format(self.chemical_name, self.storage_location)

    def expired_yet(self):
        return timezone.now() >= self.expiration_date

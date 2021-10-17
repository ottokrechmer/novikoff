from django.db import models


class Organization(models.Model):

    name = models.CharField(max_length=600, null=True, blank=True, db_index=True)
    activity_type = models.CharField(max_length=600, null=True, blank=True, db_index=True)
    address_region = models.CharField(max_length=200, null=True, blank=True, db_index=True)
    full_name_licensee = models.CharField(max_length=600, null=True, blank=True)
    address = models.CharField(max_length=1200, null=True, blank=True, db_index=True)
    ogrn = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    inn = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    number = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

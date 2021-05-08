# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pstr19(models.Model):
    area = models.CharField(db_column='Area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    building = models.BigIntegerField(db_column='Building', blank=True, null=True)  # Field name made lowercase.
    tourist = models.FloatField(db_column='Tourist', blank=True, null=True)  # Field name made lowercase.
    expenditure = models.FloatField(db_column='Expenditure', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pstr_19'

    def __str__(self):
        return self.area, self.building, self.tourist, self.expenditure


class Pstr20(models.Model):
    area = models.CharField(db_column='Area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    building = models.IntegerField(db_column='Building', blank=True, null=True)  # Field name made lowercase.
    tourist = models.FloatField(db_column='Tourist', blank=True, null=True)  # Field name made lowercase.
    expenditure = models.FloatField(db_column='Expenditure', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pstr_20'

    def __str__(self):
        return self.area, self.building, self.tourist, self.expenditure


class TourismExpenditure(models.Model):
    area = models.CharField(db_column='Area', max_length=100, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, blank=True, null=True)  # Field name made lowercase.
    expenditure_19 = models.FloatField(db_column='Expenditure_19', blank=True, null=True)  # Field name made lowercase.
    expenditure_20 = models.FloatField(db_column='Expenditure_20', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tourism_expenditure'
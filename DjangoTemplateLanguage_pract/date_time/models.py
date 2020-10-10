from django.db import models

class Date_filter(models.Model):
    filter_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.filter_name}'

class Day(models.Model):
    format_char = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'

class Week(models.Model):
    format_char = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'

class Month(models.Model):
    format_char = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'

class Year(models.Model):
    format_char = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'

class TimeFilter(models.Model):
    format_char = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'

class Predefined_format(models.Model):
    format_char = models.CharField(max_length=40, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    example = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.format_char}'
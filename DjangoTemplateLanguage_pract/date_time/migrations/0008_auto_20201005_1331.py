# Generated by Django 3.0.8 on 2020-10-05 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date_time', '0007_predefined_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predefined_format',
            name='format_char',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

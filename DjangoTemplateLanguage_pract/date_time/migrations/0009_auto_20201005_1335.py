# Generated by Django 3.0.8 on 2020-10-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date_time', '0008_auto_20201005_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predefined_format',
            name='format_char',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]

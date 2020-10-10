# Generated by Django 3.0.8 on 2020-10-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date_time', '0002_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_char', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('example', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
# Generated by Django 2.1 on 2020-02-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picosage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='installer',
            name='age',
        ),
        migrations.AddField(
            model_name='installer',
            name='date_started',
            field=models.DateField(null=True),
        ),
    ]

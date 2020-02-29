# Generated by Django 2.1 on 2020-02-29 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picosage', '0002_auto_20200229_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='installer',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='picosage.USAddress'),
        ),
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='picosage.USAddress'),
        ),
    ]
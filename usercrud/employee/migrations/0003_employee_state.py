# Generated by Django 2.2.6 on 2019-10-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employee_edescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='state',
            field=models.IntegerField(choices=[(0, 'Gujarat'), (1, 'Maharashtra'), (2, 'Punjab')], default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 2.2.24 on 2021-11-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_tessio_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='name',
        ),
    ]

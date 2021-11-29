# Generated by Django 3.2.8 on 2021-11-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tessio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tejido',
                'verbose_name_plural': 'Tejidos',
            },
        ),
    ]
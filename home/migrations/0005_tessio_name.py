# Generated by Django 2.2.24 on 2021-11-29 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211129_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='tessio',
            name='name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Paciente'),
            preserve_default=False,
        ),
    ]
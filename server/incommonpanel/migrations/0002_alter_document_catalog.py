# Generated by Django 4.1.4 on 2022-12-16 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incommonpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='catalog',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='incommonpanel.catalog'),
        ),
    ]
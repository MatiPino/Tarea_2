# Generated by Django 3.2.3 on 2021-06-07 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categoria.categoria'),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-05 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0005_auto_20201230_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-31 02:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0004_auto_20201230_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
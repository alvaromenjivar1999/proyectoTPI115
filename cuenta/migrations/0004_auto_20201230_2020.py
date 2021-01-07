# Generated by Django 3.1.4 on 2020-12-31 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0003_auto_20201220_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='token',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenimo'), ('Masculino', 'Masculino')], default='Femenino', max_length=10),
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchAll', '0003_lista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favoritos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.ManyToManyField(to='watchAll.Video')),
            ],
        ),
        migrations.CreateModel(
            name='VerMasTarde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.ManyToManyField(to='watchAll.Video')),
            ],
        ),
        migrations.DeleteModel(
            name='Lista',
        ),
    ]

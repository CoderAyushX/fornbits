# Generated by Django 4.0 on 2022-01-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.CharField(max_length=10)),
                ('stars2', models.CharField(max_length=10)),
                ('stars3', models.CharField(max_length=10)),
                ('stars4', models.CharField(max_length=10)),
                ('stars5', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Rateus',
        ),
    ]

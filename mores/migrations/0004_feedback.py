# Generated by Django 4.0 on 2022-01-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mores', '0003_remove_rate_stars2_remove_rate_stars3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]

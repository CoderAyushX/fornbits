# Generated by Django 4.0 on 2022-01-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='sno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]

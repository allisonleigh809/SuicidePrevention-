# Generated by Django 3.0.9 on 2020-08-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suicideprevent', '0009_moodtracker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodtracker',
            name='date_added',
            field=models.DateField(blank=True, null=True),
        ),
    ]
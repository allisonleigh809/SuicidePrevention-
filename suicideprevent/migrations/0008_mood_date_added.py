# Generated by Django 3.1 on 2020-08-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suicideprevent', '0007_auto_20200811_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='mood',
            name='date_added',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

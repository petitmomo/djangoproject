# Generated by Django 3.0.6 on 2020-06-22 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20200616_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cour',
            name='updated_on',
        ),
    ]
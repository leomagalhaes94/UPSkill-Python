# Generated by Django 4.2.6 on 2023-10-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_alter_contact_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
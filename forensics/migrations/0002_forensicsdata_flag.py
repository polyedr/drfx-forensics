# Generated by Django 3.0.4 on 2021-08-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forensics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forensicsdata',
            name='flag',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
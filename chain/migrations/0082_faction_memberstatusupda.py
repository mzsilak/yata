# Generated by Django 2.2.7 on 2019-12-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0081_faction_memberstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='memberStatusUpda',
            field=models.IntegerField(default=0),
        ),
    ]

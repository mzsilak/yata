# Generated by Django 2.0.5 on 2019-10-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0060_faction_createlive'),
    ]

    operations = [
        migrations.AddField(
            model_name='wall',
            name='breakdown',
            field=models.TextField(blank=True, default='[]', null=True),
        ),
    ]

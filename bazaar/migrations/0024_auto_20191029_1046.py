# Generated by Django 2.0.5 on 2019-10-29 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0023_preference_territoryts'),
    ]

    operations = [
        migrations.CreateModel(
            name='BazaarData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nItems', models.IntegerField(default=10)),
                ('lastScanTS', models.IntegerField(default=0)),
                ('itemType', models.TextField(default='{}')),
            ],
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]

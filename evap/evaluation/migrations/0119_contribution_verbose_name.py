# Generated by Django 3.0.10 on 2021-02-01 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0118_remove_last_modified_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'ordering': ['order'], 'verbose_name': 'contribution', 'verbose_name_plural': 'contributions'},
        ),
    ]

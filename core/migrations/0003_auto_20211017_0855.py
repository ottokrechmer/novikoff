# Generated by Django 3.2.8 on 2021-10-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_organization_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='inn',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ogrn',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
    ]
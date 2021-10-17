# Generated by Django 3.2.8 on 2021-10-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_organization_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='activity_type',
            field=models.CharField(blank=True, db_index=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='full_name_licensee',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=600, null=True),
        ),
    ]

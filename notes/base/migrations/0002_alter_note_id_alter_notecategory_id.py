# Generated by Django 5.1.7 on 2025-03-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notecategory',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]

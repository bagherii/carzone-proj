# Generated by Django 4.1.3 on 2023-01-16 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_description_alter_car_features_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='is_feachured',
            new_name='is_featured',
        ),
    ]

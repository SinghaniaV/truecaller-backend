# Generated by Django 5.0.7 on 2024-07-27 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identities', '0008_alter_identity_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeredtosaved',
            old_name='phone',
            new_name='registered_user',
        ),
    ]

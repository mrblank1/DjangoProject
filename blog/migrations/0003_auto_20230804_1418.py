# Generated by Django 3.2.20 on 2023-08-04 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230804_1217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='counted_viws',
            new_name='counted_views',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='updated_date',
        ),
    ]

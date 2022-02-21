# Generated by Django 4.0.2 on 2022-02-21 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='detail',
        ),
        migrations.AddField(
            model_name='exam',
            name='is_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='testcases',
            field=models.TextField(null=True),
        ),
    ]

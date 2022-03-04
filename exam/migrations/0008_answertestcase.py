# Generated by Django 4.0.2 on 2022-03-04 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_rename_autograded_points_answer_name_autograde_points_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase', models.TextField(default='')),
                ('expected', models.TextField(default='')),
                ('actual', models.TextField(default='')),
                ('points_autograde', models.FloatField(default=0)),
                ('point_manual', models.FloatField(default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.answer')),
            ],
        ),
    ]
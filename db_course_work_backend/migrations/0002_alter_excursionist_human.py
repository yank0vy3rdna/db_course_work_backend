# Generated by Django 4.0 on 2022-01-19 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_course_work_backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursionist',
            name='HUMAN',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.personal_data'),
            preserve_default=False,
        ),
    ]

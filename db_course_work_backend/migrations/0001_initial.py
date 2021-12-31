# Generated by Django 4.0 on 2021-12-31 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EXCURSION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=90)),
                ('DESCRIPTION', models.CharField(default='Самая незабываемая и интересная экскурсия, которую можно посетить.', max_length=400)),
                ('DURATION', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EXCURSIONIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MOBILE_NUMBER', models.CharField(max_length=45)),
                ('EMAIL', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='EXHIBIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(default='МАДОННА С МЛАДЕНЦЕМ', max_length=90)),
                ('DATE_CREATION', models.DateTimeField()),
                ('DIRECTION', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='EXHIBITION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='PASSPORT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SERIES_PASSPORT', models.IntegerField()),
                ('NUMBER_PASSPORT', models.IntegerField(null=True)),
                ('SURNAME', models.CharField(max_length=45)),
                ('NAME', models.CharField(max_length=45)),
                ('PATRONYMIC', models.CharField(max_length=45)),
                ('GENDER', models.BooleanField()),
                ('DATE_BIRTHDAY', models.DateTimeField()),
                ('PASSPORT_ISSUE', models.CharField(max_length=200)),
                ('DATE_ISSUE', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PERSONAL_DATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SURNAME', models.CharField(max_length=45)),
                ('NAME', models.CharField(max_length=45)),
                ('PATRONYMIC', models.CharField(max_length=45)),
                ('GENDER', models.BooleanField()),
                ('DATE_BIRTHDAY', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PLACE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COUNTRY', models.CharField(max_length=90)),
                ('CITY', models.CharField(max_length=90)),
                ('STREET', models.CharField(max_length=90)),
                ('HOUSE', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MUSEUM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=90)),
                ('LOCATION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.place')),
                ('exhibition', models.ManyToManyField(to='db_course_work_backend.EXHIBITION')),
            ],
        ),
        migrations.CreateModel(
            name='GUIDE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MOBILE_NUMBER', models.BigIntegerField()),
                ('EMAIL', models.CharField(max_length=45, unique=True)),
                ('PASSPORT_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.passport')),
            ],
        ),
        migrations.CreateModel(
            name='GROUP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TIME', models.DateTimeField()),
                ('COST', models.IntegerField()),
                ('NUMBER_SEATS', models.IntegerField()),
                ('EXHIBITION_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.excursion')),
                ('GUIDE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.guide')),
                ('PLACE_GATHERING', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PLACE_GATHERING', to='db_course_work_backend.place')),
                ('PLACE_TERMINATION', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PLACE_TERMINATION', to='db_course_work_backend.place')),
                ('excursionist', models.ManyToManyField(to='db_course_work_backend.EXCURSIONIST')),
            ],
        ),
        migrations.AddField(
            model_name='exhibition',
            name='LOCATION',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.place'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='OWNER',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='db_course_work_backend.personal_data'),
        ),
        migrations.AddField(
            model_name='exhibition',
            name='exhibit',
            field=models.ManyToManyField(to='db_course_work_backend.EXHIBIT'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='AUTHOR',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_course_work_backend.personal_data'),
        ),
        migrations.AddField(
            model_name='exhibit',
            name='LOCATION',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='db_course_work_backend.place'),
        ),
        migrations.AddField(
            model_name='excursionist',
            name='HUMAN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db_course_work_backend.personal_data'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='exhibit',
            field=models.ManyToManyField(to='db_course_work_backend.EXHIBIT'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='exhibition',
            field=models.ManyToManyField(to='db_course_work_backend.EXHIBITION'),
        ),
        migrations.AddField(
            model_name='excursion',
            name='museum',
            field=models.ManyToManyField(to='db_course_work_backend.MUSEUM'),
        ),
        migrations.CreateModel(
            name='DOCUMENT_STATUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INSTITUTION', models.CharField(max_length=180, null=True)),
                ('NAME', models.CharField(max_length=180)),
                ('DATE_ISSUE', models.DateTimeField()),
                ('DATE_CANCELLATION', models.DateTimeField()),
                ('excursionist', models.ManyToManyField(to='db_course_work_backend.EXCURSIONIST')),
            ],
        ),
        migrations.CreateModel(
            name='DOCUMENT_ACCREDITATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INSTITUTION', models.CharField(max_length=180, null=True)),
                ('NAME', models.CharField(max_length=180)),
                ('DATE_ISSUE', models.DateTimeField()),
                ('DATE_CANCELLATION', models.DateTimeField()),
                ('guide', models.ManyToManyField(to='db_course_work_backend.GUIDE')),
            ],
        ),
    ]

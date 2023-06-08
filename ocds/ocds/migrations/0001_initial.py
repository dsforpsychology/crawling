# Generated by Django 4.2.2 on 2023-06-08 06:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureInfo',
            fields=[
                ('lecture', models.BigAutoField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(default='강의명', max_length=100)),
                ('recommended', models.FloatField(default=0)),
                ('lecture_url', models.CharField(default='https://example.com/default-url', max_length=250)),
                ('lecture_length', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='TutorInfo',
            fields=[
                ('tutor', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=0, max_length=50)),
                ('tutor_name', models.CharField(default='박선생', max_length=50)),
                ('email', models.CharField(default='default@example.com', max_length=100)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user', models.BigAutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(default=0, max_length=50)),
                ('user_name', models.CharField(default='김학생', max_length=50)),
                ('email', models.CharField(default='default@example.com', max_length=100)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ResultInfo',
            fields=[
                ('result', models.BigAutoField(primary_key=True, serialize=False)),
                ('capture_start', models.TimeField(default=django.utils.timezone.now)),
                ('capture_end', models.TimeField(default=django.utils.timezone.now)),
                ('start_log', models.TimeField(default=django.utils.timezone.now)),
                ('end_log', models.TimeField(default=django.utils.timezone.now)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.lectureinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.userinfo')),
            ],
        ),
        migrations.AddField(
            model_name='lectureinfo',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.tutorinfo'),
        ),
        migrations.CreateModel(
            name='EventInfo',
            fields=[
                ('event', models.BigAutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sleepNum', models.FloatField(default=0.0)),
                ('awakeNum', models.FloatField(default=0.0)),
                ('stateNo', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.lectureinfo')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.resultinfo')),
            ],
        ),
        migrations.CreateModel(
            name='EnrollInfo',
            fields=[
                ('enroll', models.BigAutoField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(default='강의명', max_length=100)),
                ('tutor_name', models.CharField(default='박선생', max_length=50)),
                ('lecture_length', models.IntegerField(default=0)),
                ('registration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocds.userinfo')),
            ],
        ),
    ]

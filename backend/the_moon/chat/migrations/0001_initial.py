# Generated by Django 5.1.2 on 2024-11-26 03:00

import chat.models
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=255)),
                ('user_profile', models.ForeignKey(default=chat.models.get_default_user_profile, on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_title', models.CharField(max_length=255)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('activity', models.CharField(max_length=255)),
                ('user_profile', models.ForeignKey(default=chat.models.get_default_user_profile, on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OneOnOneChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_email', models.CharField(max_length=255)),
                ('receiver_phone_number', models.CharField(max_length=15)),
                ('message', models.JSONField()),
                ('user_profile', models.ForeignKey(default=chat.models.get_default_user_profile, on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='NoteOnFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=60)),
                ('user_profile', models.ForeignKey(default=chat.models.get_default_user_profile, on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ImageOnFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateField(default=datetime.date.today)),
                ('image', models.BinaryField(default=b'\x08')),
                ('user_profile', models.ForeignKey(default=chat.models.get_default_user_profile, on_delete=django.db.models.deletion.CASCADE, to='chat.userprofile')),
            ],
        ),
        migrations.AddConstraint(
            model_name='userprofile',
            constraint=models.UniqueConstraint(fields=('phone_number', 'email'), name='UserProfilePK'),
        ),
        migrations.AddConstraint(
            model_name='school',
            constraint=models.UniqueConstraint(fields=('school_title', 'start_time'), name='SchoolPK'),
        ),
    ]

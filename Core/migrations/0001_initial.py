# Generated by Django 4.2.1 on 2023-05-25 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('education_country', models.CharField(max_length=100)),
                ('university_name', models.CharField(max_length=100)),
                ('education_year_start', models.IntegerField()),
                ('certification_award_name', models.CharField(max_length=100)),
                ('certification_from', models.CharField(max_length=100)),
                ('certification_year', models.IntegerField()),
                ('experience_position', models.CharField(max_length=100)),
                ('experience_company', models.CharField(max_length=100)),
                ('experience_start_date', models.DateField()),
                ('experience_end_date', models.DateField(blank=True, null=True)),
                ('experience_currently_working', models.BooleanField(default=False)),
                ('job_done', models.IntegerField()),
                ('personal_website', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

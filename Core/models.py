from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    education_country = models.CharField(max_length=100)
    university_name = models.CharField(max_length=100)
    education_year_start = models.IntegerField()
    certification_award_name = models.CharField(max_length=100)
    certification_from = models.CharField(max_length=100)
    certification_year = models.IntegerField()
    experience_position = models.CharField(max_length=100)
    experience_company = models.CharField(max_length=100)
    experience_start_date = models.DateField()
    experience_end_date = models.DateField(null=True, blank=True)
    experience_currently_working = models.BooleanField(default=False)
    job_done = models.IntegerField()
    personal_website = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username

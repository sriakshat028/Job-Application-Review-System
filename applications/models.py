from email.policy import default
from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    address=models.TextField()
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    postal_code=models.CharField(max_length=10)
    phone=models.IntegerField()
    gender=models.CharField(max_length=20,default=None)
    email=models.EmailField()
    status=models.CharField(max_length=10,default="applied")
    applied_on=models.DateField(default=timezone.now())
    role=models.TextField(default=None)
    resume=models.FileField(upload_to="resume/",null=False,blank=False,default=None)
  
class Education(models.Model):
    candidate=models.ForeignKey(Candidate,related_name='education',on_delete=models.CASCADE)
    institute=models.TextField()
    degree=models.CharField(max_length=20)
    course=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()

class Experience(models.Model):
    candidate=models.ForeignKey(Candidate,related_name='experience',on_delete=models.CASCADE)
    company=models.TextField()
    role=models.TextField(default=None)
    start_date=models.DateField()
    end_date=models.DateField()
    responsibilities=models.TextField()

class Skills(models.Model):
    candidate=models.ForeignKey(Candidate,related_name='skills',on_delete=models.CASCADE)
    skill=models.CharField(max_length=30)



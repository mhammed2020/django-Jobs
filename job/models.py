from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils.text import slugify

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def imageUpload(instance, filename):
    imageNmae, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)


class Job(models.Model):
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE )
    title = models.CharField(max_length=80)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    # image = models.ImageField(upload_to="jobs/")
    image = models.ImageField(upload_to=imageUpload)

    slug = models.SlugField(blank=True, null=True)


    def save(self,*args,**kwargs):
        #logic
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    coverLetter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



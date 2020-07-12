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

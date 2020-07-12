# Generated by Django 3.0.8 on 2020-07-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_auto_20200712_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('coverLetter', models.TextField(max_length=500)),
            ],
        ),
    ]
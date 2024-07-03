from django.db import models

# Create your models here.


class CONTACT(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SKILL(models.Model):
    disc = models.CharField(max_length=100)


class EXPERIENCE(models.Model):
    achieve = models.CharField(max_length=100)


class PROJECT(models.Model):
    name = models.CharField(max_length=35)
    disc = models.CharField(max_length=100)


class EDUCATION(models.Model):
    level = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    year = models.CharField(max_length=20)

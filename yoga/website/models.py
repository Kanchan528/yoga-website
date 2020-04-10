from django.db import models
from datetime import datetime
# Create your models here.


class Banner(models.Model):
    image = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    video = models.CharField(max_length=300, null=True, blank=True)

class BannerHeading(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)


class MiddleImage(models.Model):
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default = 'describe here')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.heading

class YogaBenefits(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default = 'describe here')
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.heading


class MoreYogaBenefits(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default = 'describe here')   
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.heading


class AboutClasses(models.Model):
    description = models.TextField(default = 'describe here')

    def __str__(self):
        return self.description

class Testomonial(models.Model):
    name = models.CharField(max_length=100, null = True, blank=True)
    posted_by = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default = 'describe here')
    image = models.ImageField(null= True, blank= True)

    def __str__(self):
        return self.name

class Features(models.Model):
    icon_name = models.CharField(max_length=100, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default = 'describe here')

    def __str__(self):
        return self.heading


class AboutBlog(models.Model):
    description = models.TextField(default = 'describe here')

    def __str__(self):
        return self.description

class SubscribeDescription(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class TrainerSectionHeading(models.Model):
    description = models.TextField(default = 'describe here')

    def __str__(self):
        return self.description


class Trainers(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default='describe here')

    def __str__(self):
        return self.name


class AboutUs(models.Model):
    image = models.ImageField(null=True, blank=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(default = 'describe here')

    def __str__(self):
        return self.heading


class OurInformation(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    telephone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(default='describe here')

    def __str__(self):
        return self.about

class ClassType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ClassDetails(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    time = models.TimeField(default=datetime.now, blank = True)
    description = models.TextField(default='describe here')
    image = models.ImageField(null=True, blank=True)
    type = models.ForeignKey(ClassType, on_delete=models.CASCADE,related_name='class_details', null=True, blank=True)

    def __str__(self):
        return self.heading

class BlogSingle(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(default=datetime.now, blank = True)
    image = models.ImageField(null=True, blank=True)
    image_title = models.TextField(default= 'title')
    description = models.TextField(default = 'describe here')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.heading

class PostComment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank =True)
    email = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(default= 'describe here')
    blog = models.ForeignKey( BlogSingle, on_delete=models.CASCADE, related_name='post_comment', null =True, blank=True)

    def __str__(self):
        return self.name








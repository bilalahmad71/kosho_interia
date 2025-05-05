from django.db import models
from django.utils.text import slugify
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Project(models.Model):
    project_heading=models.CharField(max_length=255,unique=True)
    project_description_1=models.TextField()
    project_description_2=models.TextField()
    primary_image=models.ImageField(upload_to='project_images/')
    project_video = models.FileField(upload_to='project_videos/', null=True, blank=True)
    project_url=models.CharField(max_length=255,null=True,blank=True,editable=False)

    

    def __str__(self):
        return str(self.project_heading)
    
    def save(self, *args, **kwargs):
        try:
            old = Project.objects.get(pk=self.pk)
            if old.primary_image and old.primary_image != self.primary_image:
                old.primary_image.delete(save=False)
        except :
            pass

        if not self.project_url:
            self.project_url = slugify(self.project_heading)
        else:
            self.project_url = slugify(self.project_url)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.primary_image:
            self.primary_image.delete(save=False)
        super().delete( *args, **kwargs)

@receiver(post_delete, sender=Project)
def delete_project_image_on_delete(sender, instance, **kwargs):
    if instance.primary_image:
        instance.primary_image.delete(save=False) 

class ProjectGallery(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project_images/')
    def __str__(self):
        return str(self.project.project_heading)
    
    def save(self, *args, **kwargs):
        try:
            old = ProjectGallery.objects.get(pk=self.pk)
            if old.image and old.image != self.image:
                old.image.delete(save=False)
        except :
            pass
        super().save( *args, **kwargs)

@receiver(post_delete, sender=ProjectGallery)
def delete_project_gallery_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False) 

class Blog(models.Model):
    title=models.CharField(max_length=255,unique=True)
    sub_title=models.CharField(max_length=255,null=True,blank=True)
    blog_description_1=models.TextField()
    blog_description_2=models.TextField()
    blog_description_3=models.TextField(null=True,blank=True)
    primary_image=models.ImageField(upload_to='blog_images/')
    blog_url=models.CharField(max_length=255,null=True,blank=True,editable=False)
    def __str__(self):
        return str(self.title)
    def save(self, *args, **kwargs):
        try:
            old = Blog.objects.get(pk=self.pk)
            if old.primary_image and old.primary_image != self.primary_image:
                old.primary_image.delete(save=False)
        except :
            pass

        if not self.blog_url:
            self.blog_url = slugify(self.title)
        else:
            self.blog_url = slugify(self.blog_url)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete primary image if it exists
        if self.primary_image :
            self.primary_image.delete(save=False)  # This uses Django's storage backend properly
        super().delete(*args, **kwargs)


@receiver(post_delete, sender=Blog)
def delete_blog_image_on_delete(sender, instance, **kwargs):
    if instance.primary_image:
        instance.primary_image.delete(save=False)

class BlogGallery(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog_images/')
    def __str__(self):
        return str(self.blog.title) + " image => " + str(self.image.url)
    def delete(self, *args, **kwargs):
        try:
                old = BlogGallery.objects.get(pk=self.pk)
                if old.image and old.image != self.image:
                    old.image.delete(save=False)
        except :
            pass
        super().save( *args, **kwargs)

    def delete( self, *args, **kwargs):
        # Delete image if it exists
        if self.image :
            self.image.delete(save=False)  # This uses Django's storage backend properly
        super().delete( *args, **kwargs)
    
@receiver(post_delete, sender=BlogGallery)
def delete_blog_gallery_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)


class Testimonial(models.Model):
    testimonial_text=models.TextField()
    name=models.CharField(max_length=255)
    address_or_company_name=models.CharField(max_length=255)
    image=models.ImageField(upload_to='testimonial_images/',null=True,blank=True)
    def __str__(self):
        return str(self.name) + " => " + str(self.address_or_company_name)
    
class Lead(models.Model):
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.CharField(max_length=255,null=True,blank=True)
    phone=models.CharField(max_length=255,null=True,blank=True)
    project_budget=models.CharField(max_length=255,null=True,blank=True)
    project_type= models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    zipcode=models.TextField(max_length=200,null=True,blank=True)
    city= models.CharField(max_length=255,null=True,blank=True)
    remark= models.TextField(null=True,blank=True)


    def __str__(self):
        return str(self.name)


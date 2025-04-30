from django.db import models
from django.utils.text import slugify

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
        if not self.project_url:
            self.project_url = slugify(self.project_heading)
        else:
            self.project_url = slugify(self.project_url)
        super().save(*args, **kwargs)

class ProjectGallery(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='project_images/')
    def __str__(self):
        return str(self.project.project_heading)
    

class Blog(models.Model):
    blog_heading=models.CharField(max_length=255,unique=True)
    blog_description_1=models.TextField()
    blog_description_2=models.TextField()
    primary_image=models.ImageField(upload_to='blog_images/')
    blog_url=models.CharField(max_length=255,null=True,blank=True,editable=False)
    def __str__(self):
        return str(self.blog_heading)
    def save(self, *args, **kwargs):
        if not self.blog_url:
            self.blog_url = slugify(self.blog_heading)
        else:
            self.blog_url = slugify(self.blog_url)
        super().save(*args, **kwargs)

class BlogGallery(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog_images/')
    def __str__(self):
        return str(self.blog.blog_heading) + " image => " + str(self.image.url)
    

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
    service=models.CharField(max_length=255,null=True,blank=True)
    message=models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)


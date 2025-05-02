from django.contrib import admin
from home.models import *

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    search_fields=['project_heading','project_url','project_description_1','project_description_2']
    
@admin.register(ProjectGallery)
class AdminProjectGallery(admin.ModelAdmin):
    search_fields=['project__project_heading','project__project_url']
    autocomplete_fields=['project']


@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display=('id','blog_heading','blog_description_1','blog_description_2','primary_image')
    search_fields=['id','blog_heading','blog_description_1','blog_description_2']
 

@admin.register(BlogGallery)
class AdminBlogGallery(admin.ModelAdmin):
    search_fields=['blog__blog_heading','blog__blog_description_1','blog__blog_description_2']


@admin.register(Testimonial)
class AdminTestimonial(admin.ModelAdmin):
    search_fields=['testimonial_test','name','address_or_company_name']
    
@admin.register(Lead)
class AdminLead(admin.ModelAdmin):
    list_display=('id','name','email','phone','service','message')
    search_fields=['id','name','email','phone','service','message']
    list_filter=['service']
    

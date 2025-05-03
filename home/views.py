from django.shortcuts import render,redirect
from home.models import Project,ProjectGallery,Testimonial,Lead,Blog,BlogGallery
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home_view(request):
    all_projects=Project.objects.all()[:6]
    all_testimonials=Testimonial.objects.all()[:10]
    return render(request, 'index.html',{"all_projects":all_projects,"all_testimonials":all_testimonials})


def projects_view(request,project_url=None):
    if project_url:
        current_project=Project.objects.filter(project_url__iexact=project_url).first()
        project_gallery=ProjectGallery.objects.filter(project=current_project)
        if not current_project:
            return redirect('/projects')
        return render(request, 'project_detail.html',{"current_project":current_project,"project_gallery":project_gallery})
    all_projects=Project.objects.all().order_by('-id')
    return render(request, 'projects.html',{"all_projects":all_projects})

import json

@csrf_exempt
def handle_lead_submit(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))  
            contact_name=data.get('contact_name')
            contact_email=data.get('contact_email')
            contact_phone=data.get('contact_phone')
            contact_service=data.get('contact_service')
            contact_message=data.get('contact_message')
            Lead.objects.create(name=contact_name,email=contact_email,phone=contact_phone,service=contact_service,message=contact_message)
            return JsonResponse({"status": 1, 'message': 'Thank you | we will get back to you soon'})
        except Exception as e:
            print(e)
            return JsonResponse({"status": 0, 'message': 'Something went wrong'})
    return JsonResponse({"status": 0, "message": "Something went wrong"})



def contact_view(request):
    return render(request,'contact.html')

def about_view(request):
    all_testimonials=Testimonial.objects.all()[:10]
    return render(request,'about.html',{"all_testimonials":all_testimonials})

def blogs_view(request,blog_url=None):
    if blog_url:
        current_blog=Blog.objects.filter(blog_url=blog_url).first()
        blog_gallery=BlogGallery.objects.filter(blog=current_blog)
        if not current_blog:
            return redirect('/blogs')
        return render(request,'blog_detail.html',{"current_blog":current_blog,'blog_gallery':blog_gallery})
    all_blogs=Blog.objects.all()
    return render(request,'blogs.html',{"all_blogs":all_blogs})
        
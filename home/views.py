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
            project_budget=data.get('project_budget')
            project_type= data.get('project_type')
            contact_message=data.get('contact_message')
            zip_code=data.get('zip_code')
            city=data.get('city')
            Lead.objects.create(name=contact_name,email=contact_email,phone=contact_phone,project_type=project_type,project_budget=project_budget,message=contact_message,zipcode=zip_code,city=city)
            return JsonResponse({"status": 1, 'message': 'Thank you | we will get back to you soon'})
        except Exception as e:
            # print(e)
            return JsonResponse({"status": 0, 'message': 'Something went wrong'})
    return JsonResponse({"status": 0, "message": "Something went wrong"})

@csrf_exempt
def book_consultation(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))  
            contact_name=data.get('form_name')
            contact_email=data.get('form_email')
            contact_phone=data.get('form_phone')
            project_budget=data.get('form_budget')
            city=data.get('form_city')
            Lead.objects.create(name=contact_name,email=contact_email,phone=contact_phone,project_budget=project_budget,city=city)
            return JsonResponse({"status": 1, 'message': 'Thank you | we will get back to you soon'})
        except Exception as e:
            # print(e)
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
        
def luxury_interior(request):
    return render(request,'landing_page.html')

def custom_page_not_found_view(request, exception):
    return redirect('/')

def privary_policy(request):
    return render(request,'privacy_policy.html')
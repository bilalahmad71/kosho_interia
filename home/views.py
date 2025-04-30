from django.shortcuts import render,redirect
from home.models import Project,ProjectGallery,Testimonial
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

@csrf_exempt
def handle_lead_submit(request):
    try:
        pass
    except:
        return JsonResponse({"status":1,'message':'we have recieved your response'})

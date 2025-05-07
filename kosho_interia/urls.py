
from django.contrib import admin
from django.urls import path
from home.views import (
    home_view,projects_view,handle_lead_submit,contact_view,about_view,blogs_view,privary_policy,luxury_interior
)
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header="Kosho Interia"
admin.site.index_title="Kosho Interia"
admin.site.site_title="Kosho Interia"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('projects/', projects_view),
    path('projects/<project_url>/', projects_view),
    path('contact/',contact_view),
    path('about/',about_view),
    path('blogs/',blogs_view),
    path('blogs/<blog_url>/',blogs_view),
    path('book-consultation/',luxury_interior),


    path('submit-lead/', handle_lead_submit),
    path('know-us/', about_view),
    path('enquire/', contact_view),
    path('privacy-policy/',privary_policy)

]
# handler404 = 'home.views.custom_page_not_found_view'


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


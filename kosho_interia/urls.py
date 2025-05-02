
from django.contrib import admin
from django.urls import path
from home.views import (
    home_view,projects_view,handle_lead_submit
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
    path('submit-lead/', handle_lead_submit),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
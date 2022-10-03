
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page, name='Home'),
    path('thanks/', views.thanks, name='thanks_first')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

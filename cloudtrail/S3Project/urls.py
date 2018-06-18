"""S3Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from home.views import DocumentCreateView
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', DocumentCreateView.as_view(template_name="form.html"), name="upload"),

   # url(r'^create_bucket/', views.return_data)
    url(r'^bucket_logs/', views.return_logs)
]
"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from page.views import home_page, affiche_maladie, SNP_search, phenotype_details, snp_details, logout_view
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

# Tous les urls accessibles
# A chaque url est associé une fonction dans (views.py) pour afficher la page
urlpatterns = [
        path('', home_page),
	url('admin/', admin.site.urls),
        path('login/', auth_views.login),
        path('logout/', logout_view),
	url('home/$', home_page),
        url(r'maladies/$', affiche_maladie),
        url(r'SNPsearch/$', SNP_search),
        path(r'phenotype_details/<int:pheno>/', phenotype_details),
        path(r'snp_details/<int:rsid>/', snp_details)
        ]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

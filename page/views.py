from django.shortcuts import render, render_to_response, HttpResponse
from page.models import *
from page.forms import snpform
# loginform, snpdetailform
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.
# Fonctions qui permettent d'afficher les pages selon l'url (définies dans urls.py)
def home_page(request):
     return render(request, "home_page.html")

def logout_view(request):
     logout(request)
     return HttpResponseRedirect('/home')

@login_required(login_url='/login/')
def affiche_maladie(request,):
     list_pheno = sorted(list(TableDisease.objects.values_list('disease_trait')))
     list_pheno2 = []
     for l in list_pheno:
          list_pheno2.append(l[0])         
     return render_to_response("phenotype_list_page.html",
                             {"lines" : list(TableDisease.objects.order_by('disease_trait')) })
#                             {"lines" : list_pheno2 })

@login_required(login_url='/login/')
def phenotype_details(request, pheno):
     objet1 = Snp2Phenotype2Ref.objects.filter(disease_trait_id=pheno)
     disease = TableDisease.objects.filter(rowid=pheno).values('disease_trait')[0]['disease_trait']
     objet2 = Article.objects.all()
     objet3 = Snp.objects.all()
     return render(request,'phenotype_detail_page.html',{'disease':disease, 'obj1':objet1,'obj2':objet2,'obj3':objet3})

@login_required(login_url='/login/')
def SNP_search(request):
           if len(request.POST)>0:
                   form = snpform(request.POST)
                   if form.is_valid() :
                           rs_search = form.cleaned_data['rs_search']
                           chrom_search = form.cleaned_data['chrom']
                           if rs_search == None and chrom_search== None:
                                return render(request, 'snp_search_page.html', {'form':form})
                           elif rs_search :
                                objet = Snp.objects.filter(rsid_current__contains=rs_search)
                           elif chrom_search : 
                                objet = Snp.objects.filter(chr_id=chrom_search)
                           return render(request,'snp_result_page.html',{'obj':objet })
                   else:
                           form = snpform(request.POST)
                           return render(request,'snp_search_page.html',{'form':form})
           else:
                   form = snpform(request.POST)
                   return render(request,'snp_search_page.html',{'form':form})

@login_required(login_url='/login/')
def snp_details(request, rsid):
     snp_qs = Snp.objects.filter(rsid_current=rsid)
     snpid = Snp.objects.filter(rsid_current=rsid).values('rowid')[0]['rowid']
     Snp2Phenotype2Ref_qs = Snp2Phenotype2Ref.objects.filter(snp_id=snpid)
     disease_id = Snp2Phenotype2Ref.objects.filter(snp_id=snpid).values('disease_trait_id')[0]['disease_trait_id']
     disease_table = TableDisease.objects.all()
     #disease = TableDisease.objects.filter(rowid=disease_id).values('disease_trait')[0]['disease_trait']

     return render(request,'snp_detail_page.html',{'rs_id':rsid, 'res_snp':snp_qs, 'Snp2Phenotype2Ref_res': Snp2Phenotype2Ref_qs, 'disease_table': disease_table })
# 


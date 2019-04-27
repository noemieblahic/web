from django import forms
from page.models import Snp, Article, Snp2Phenotype2Ref
##from django.shortcuts import render, redirect, render_to_response
##from django.http import HttpResponse

# Formulaire de recherche des SNP
# Recherche par numero de chromosome (chrom) ou bien par identifiant (rs_search)
class snpform(forms.Form):
    rs_search = forms.IntegerField(label= 'Recherche SNP : saissiez un identifiant (rs_id)', required=False)
    chrom = forms.IntegerField(label= 'Recherche SNP : saissiez un numéro de chromosome', required=False)
    def clean(self):
        cleaned_data = super(snpform,self).clean()
        rs_search = cleaned_data.get('rs_search')
        chrom = cleaned_data.get('chrom')
        if rs_search :
            trouve_rsid =  Snp.objects.filter(rsid_current__contains=rs_search)
            if len(trouve_rsid) != 0 :
                return cleaned_data
            else :
                raise forms.ValidationError('SNP inconnu')
        elif chrom :
            trouve_chrom =  Snp.objects.filter(chr_id=chrom)
            if len(trouve_chrom) != 0 :
                return cleaned_data
            else :
                raise forms.ValidationError('Chromosome incorrect')
            
        return cleaned_data 

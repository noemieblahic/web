from django.contrib import admin

# Register your models here.
from .models import Snp
admin.site.register(Snp)
from .models import Article
admin.site.register(Article)
from .models import Snp2Phenotype2Ref
admin.site.register(Snp2Phenotype2Ref)
from .models import TableDisease
admin.site.register(TableDisease)

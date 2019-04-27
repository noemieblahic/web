# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Table Article qui contient les informations de chaque article
class Article(models.Model):
    rowid = models.IntegerField(unique=True, blank=True, primary_key=True)
    pubmedid = models.IntegerField(db_column='PUBMEDID', blank=True, null=True)  # Field name made lowercase.
    journal = models.TextField(db_column='JOURNAL', blank=True, null=True)  # Field name made lowercase.
    link = models.TextField(db_column='LINK', blank=True, null=True)  # Field name made lowercase.
    study = models.TextField(db_column='STUDY', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ARTICLE'

# Table Snp qui contient les informations biologiques de chaque SNP
class Snp(models.Model):
    rowid = models.IntegerField(unique=True, blank=True, primary_key=True)
    chr_id = models.IntegerField(db_column='CHR_ID', blank=True, null=True)  # Field name made lowercase.
    chr_pos = models.TextField(db_column='CHR_POS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rsid_current = models.IntegerField(db_column='RSID_CURRENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SNP'

# Table qui fait le lien entre les autres tables grace aux clés uniques
class Snp2Phenotype2Ref(models.Model):
    rowid = models.IntegerField(unique=True, blank=True, primary_key=True)
    snp_id = models.IntegerField(db_column='SNP_ID', blank=True, null=True)  # Field name made lowercase.
    disease_trait_id = models.IntegerField(db_column='DISEASE_TRAIT_ID', blank=True, null=True)  # Field name made lowercase.
    reference_id = models.IntegerField(db_column='REFERENCE_ID', blank=True, null=True)  # Field name made lowercase.
    p_value = models.IntegerField(db_column='P_VALUE', blank=True, null=True)  # Field name made lowercase.
    pvalue_mlog = models.TextField(db_column='PVALUE_MLOG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SNP2PHENOTYPE2REF'

# Table qui réfère toutes les maladies 
class TableDisease(models.Model):
    rowid = models.IntegerField(unique=True, blank=True, primary_key=True)
    disease_trait = models.TextField(db_column='DISEASE_TRAIT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABLE_DISEASE'

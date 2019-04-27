import sqlite3
import csv

conn = sqlite3.connect('base_projet.sqlite3')
#conn.text_factory = lambda s: unicode(s, 'latin-1')
#conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')

conn.execute('drop table if exists SNP')
conn.execute('drop table if exists TABLE_DISEASE')
conn.execute('drop table if exists ARTICLE')
conn.execute('drop table if exists TABLE_DISEASE')
conn.execute('drop table if exists SNP2PHENOTYPE2REF')

c = conn.cursor()
c.execute('''CREATE TABLE TABLE_DISEASE (
	rowid integer primary key AUTOINCREMENT UNIQUE, 
	DISEASE_TRAIT TEXT)''')
c.execute('''CREATE TABLE ARTICLE (
        rowid integer primary key AUTOINCREMENT UNIQUE,
        PUBMEDID INTEGER,
        JOURNAL TEXT,
        LINK TEXT,
        STUDY TEXT,
        DATE TEXT)''')          
c.execute('''CREATE TABLE SNP (
            rowid integer primary key AUTOINCREMENT UNIQUE,
            CHR_ID INTEGER,
            CHR_POS INTERGER,
            RSID_CURRENT INTEGER)''')

c.execute('''CREATE TABLE SNP2PHENOTYPE2REF (
            rowid integer primary key AUTOINCREMENT UNIQUE,
            SNP_ID INTEGER,
            DISEASE_TRAIT_ID INTEGER,
            REFERENCE_ID INTEGER,
            P_VALUE INTEGER,
            PVALUE_MLOG INTERGER)''')
conn.commit()


with open('data.tsv', 'r', encoding='utf-8') as f:
    header=f.readline()
    reader = csv.reader(f, delimiter='\t')
    inc_disease=0
    inc_ARTICLE=0
    inc_snp=0
    for row in reader:
        #print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        data=[]
        c.execute("SELECT rowid FROM ARTICLE WHERE PUBMEDID = ?", (row[0],))
        data=c.fetchone()
        if data is None:
            c.execute('''INSERT INTO ARTICLE(PUBMEDID,JOURNAL,LINK,STUDY,DATE) VALUES(?,?,?,?,?)''', (row[0],row[2],row[3],row[4],row[1]))
            ref_ARTICLE=inc_ARTICLE
            inc_ARTICLE=inc_ARTICLE+1
            #print ("Existe ARTICLE : Non")
        else:
             #print ("Existe ARTICLE: Oui")
             ref_ARTICLE=data[0]
                            
        
        c.execute('''INSERT INTO SNP(CHR_ID,CHR_POS,RSID_CURRENT) VALUES (?,?,?)''', (row[6],row[7],row[8]))
        inc_snp=inc_snp+1
                      
        data=[]
        c.execute("SELECT rowid FROM TABLE_DISEASE WHERE DISEASE_TRAIT = ?", (row[5],))
        data=c.fetchone()
        if data is None:
            c.execute('''INSERT INTO TABLE_DISEASE VALUES (?,?)''', (inc_disease,row[5]))
            ref_disease=inc_disease
            inc_disease=inc_disease+1
            #print ("Existe DISEASE : Non")
        else:
             #print ("Existe DISEASE: Oui")
             ref_disease=data[0]
            
        c.execute('''INSERT INTO SNP2PHENOTYPE2REF(SNP_ID,DISEASE_TRAIT_ID,REFERENCE_ID,P_VALUE,PVALUE_MLOG) VALUES(?,?,?,?,?)''', (inc_snp,ref_disease,ref_ARTICLE,row[9],row[10]))
conn.commit()

#----------------------------------------
# display SQL data
#----------------------------------------
##print('****SNP********')
##c.execute(' SELECT * FROM snp')
##for row in c:
##    print(row)
##
##
##print('****ARTICLE********')
##c.execute(' SELECT * FROM ARTICLE')
##for row in c:
##    print(row)
##
##print('****TABLE_DISEASE********')
##c.execute(' SELECT * FROM TABLE_DISEASE')
##for row in c:
##    print(row)
##
##
##print('****SNP2PHENOTYPE2REF********')
##c.execute(' SELECT * FROM SNP2PHENOTYPE2REF ')
##for row in c:
##    print(row)

print('************')
##
##c.execute(' SELECT rowid FROM SNP')
##for row in c:
##    print(row)

print('************')

c.execute(' SELECT TABLE_DISEASE.DISEASE_TRAIT, SNP.RSID_CURRENT FROM TABLE_DISEASE, SNP2PHENOTYPE2REF, ARTICLE, SNP where TABLE_DISEASE.DISEASE_TRAIT = "Breast cancer" and TABLE_DISEASE.rowid = SNP2PHENOTYPE2REF.DISEASE_TRAIT_ID \
    and SNP2PHENOTYPE2REF.REFERENCE_ID = ARTICLE.rowid  and SNP.rowid = SNP2PHENOTYPE2REF.SNP_ID')
for row in c:
    print(row)


print('************')

c.execute(' SELECT TABLE_DISEASE.DISEASE_TRAIT, SNP.RSID_CURRENT FROM TABLE_DISEASE, SNP2PHENOTYPE2REF, ARTICLE, SNP where TABLE_DISEASE.rowid = SNP2PHENOTYPE2REF.DISEASE_TRAIT_ID \
    and SNP2PHENOTYPE2REF.REFERENCE_ID = ARTICLE.rowid  and SNP.rowid = SNP2PHENOTYPE2REF.SNP_ID and SNP.RSID_CURRENT like "6%" ')
for row in c:
    print(row)





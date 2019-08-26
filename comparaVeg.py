# -*- coding: utf-8 -*-
class Dados:

    def __init__(self, presntVG,ENS45,ENS85_1000,ENS85_420,pr45,pr85_420,pr85_1000,area_m,area_km,area_ha):
        self.presntVG=int(presntVG);
        self.ENS45=int(ENS45);
        self.ENS85_1000=int(ENS85_1000);
        self.ENS85_420=int(ENS85_420);
        self.pr45=pr45;
        self.pr85_420=pr85_420;
        self.pr85_1000=pr85_1000;
        self.area_m=float(area_m.replace(",","."));
        self.area_km=float(area_km.replace(",","."));
        self.area_ha=int(area_ha);

    def __str__(self):
        return self.presntVG+" "+self.presntVG+" "+self.ENS45+" "+self.ENS85_1000+" "+self.ENS85_420+" "+self.pr45+" "+self.pr85_420+" "+self.pr85_1000+" "+self.area_m+" "+self.area_km+" "+self.area_ha




f = open("tabela.CSV", encoding="utf8")
linhas=[]
i=0

for x in f:
    x=x.split(";")
    i=i+1
    if (i!=1):
        d=Dados(x[28],x[29],x[30],x[31],x[32],x[33],x[34],x[35],x[36],x[37])
        linhas.append(d);


#print("Áreas presntVG")
presntVG={}
for d in linhas:
    if d.presntVG in presntVG.keys(): 
        presntVG[d.presntVG]=presntVG[d.presntVG]+d.area_km
    else:
        presntVG[d.presntVG]=d.area_km
#presntVG=sorted(presntVG.items())
#print (presntVG)

#print("Áreas ENS45")
ENS45={}
histENS45add={}
histENS45ori={}
histENS45del={}
for d in linhas:
    if d.ENS45 in ENS45.keys(): 
        ENS45[d.ENS45]=ENS45[d.ENS45]+d.area_km
    else:
        ENS45[d.ENS45]=d.area_km
    
    if d.presntVG==d.ENS45:
        if d.presntVG in histENS45ori.keys():
            histENS45ori[d.presntVG]=histENS45ori[d.presntVG]+d.area_km
        else:
            histENS45ori[d.presntVG]=d.area_km
    else:
        if d.ENS45 in histENS45add.keys():
            histENS45add[d.ENS45]=histENS45add[d.ENS45]+d.area_km
        else:
            histENS45add[d.ENS45]=d.area_km
            
        if d.presntVG in histENS45del.keys():
            histENS45del[d.presntVG]=histENS45del[d.presntVG]+d.area_km
        else:
            histENS45del[d.presntVG]=d.area_km
#ENS45=sorted(ENS45.items())
#print (ENS45)


#print("Áreas ENS85_1000")
ENS85_1000={}
histENS85_1000add={}
histENS85_1000ori={}
histENS85_1000del={}
for d in linhas:
    if d.ENS85_1000 in ENS85_1000.keys(): 
        ENS85_1000[d.ENS85_1000]=ENS85_1000[d.ENS85_1000]+d.area_km
    else:
        ENS85_1000[d.ENS85_1000]=d.area_km
        
    if d.presntVG==d.ENS85_1000:
        if d.presntVG in histENS85_1000ori.keys():
            histENS85_1000ori[d.presntVG]=histENS85_1000ori[d.presntVG]+d.area_km
        else:
            histENS85_1000ori[d.presntVG]=d.area_km
    else:
        if d.ENS85_1000 in histENS85_1000add.keys():
            histENS85_1000add[d.ENS85_1000]=histENS85_1000add[d.ENS85_1000]+d.area_km
        else:
            histENS85_1000add[d.ENS85_1000]=d.area_km
            
        if d.presntVG in histENS85_1000del.keys():
            histENS85_1000del[d.presntVG]=histENS85_1000del[d.presntVG]+d.area_km
        else:
            histENS85_1000del[d.presntVG]=d.area_km
#ENS85_1000=sorted(ENS85_1000.items())
#print (ENS85_1000)


#print("Áreas ENS85_420")
ENS85_420={}
histENS85_420add={}
histENS85_420ori={}
histENS85_420del={}
for d in linhas:
    if d.ENS85_420 in ENS85_420.keys(): 
        ENS85_420[d.ENS85_420]=ENS85_420[d.ENS85_420]+d.area_km
    else:
        ENS85_420[d.ENS85_420]=d.area_km
        
    if d.presntVG==d.ENS85_420:
        if d.presntVG in histENS85_420ori.keys():
            histENS85_420ori[d.presntVG]=histENS85_420ori[d.presntVG]+d.area_km
        else:
            histENS85_420ori[d.presntVG]=d.area_km
    else:
        if d.ENS85_420 in histENS85_420add.keys():
            histENS85_420add[d.ENS85_420]=histENS85_420add[d.ENS85_420]+d.area_km
        else:
            histENS85_420add[d.ENS85_420]=d.area_km
            
        if d.presntVG in histENS85_420del.keys():
            histENS85_420del[d.presntVG]=histENS85_420del[d.presntVG]+d.area_km
        else:
            histENS85_420del[d.presntVG]=d.area_km
#ENS85_420=sorted(ENS85_420.items())
#print (ENS85_420)

print("Veg\t\tpresntVG\tENS45\t\tENS85_1000\tENS85_420")
vegs=[1,2,6,7,8,9,11,13]
for i in vegs:
    if not i in presntVG.keys():
        presntVG[i]=0
    if not i in ENS45.keys():
        ENS45[i]=0
    if not i in histENS45add.keys():
        histENS45add[i]=0
    if not i in histENS45ori.keys():
        histENS45ori[i]=0
    if not i in histENS45del.keys():
        histENS45del[i]=0
        
    if not i in ENS85_1000.keys():
        ENS85_1000[i]=0
    if not i in histENS45add.keys():
        histENS85_1000add[i]=0
    if not i in histENS85_1000ori.keys():
        histENS85_1000ori[i]=0
    if not i in histENS85_1000del.keys():
        histENS85_1000del[i]=0
        
    if not i in ENS85_420.keys():
        ENS85_420[i]=0 
    if not i in histENS85_420add.keys():
        histENS85_420add[i]=0
    if not i in histENS85_420ori.keys():
        histENS85_420ori[i]=0
    if not i in histENS85_420del.keys():
        histENS85_420del[i]=0    
        
    print ('%d' % (i)+" Total Km²\t"+
           '%10d' % (presntVG[i])+ "\t"+
           '%10d' % (ENS45[i])+"\t"+
           '%10d' % (ENS85_1000[i])+"\t"+
           '%10d' % (ENS85_420[i]))
    print ('%d' %(i)+" Exp-Presnt Km²"+
           '%+10d' %(presntVG[i]-presntVG[i])+ "\t"+
           '%+10d' %(ENS45[i]-presntVG[i])+ "\t"+
           '%+10d' %(ENS85_1000[i]-presntVG[i])+ "\t"+
           '%+10d' %(ENS85_420[i]-presntVG[i])+ "\t")
    print ('%d' %(i)+"\t\t"+ 
           '%10d' %(100*presntVG[i]/presntVG[i])+ "%\t"+
           '%10d' %(100*ENS45[i]/presntVG[i])+ "%\t"+
           '%10d' %(100*ENS85_1000[i]/presntVG[i])+ "%\t"+
           '%10d' %(100*ENS85_420[i]/presntVG[i])+ "%\t") 
    
    print ('%d' % (i)+" Add \t\t"+
           '%10d' % (0)+ "\t"+
           '%10d' % (histENS45add[i])+ "\t"+
           '%10d' % (histENS85_1000add[i])+ "\t"+
           '%10d' % (histENS85_420add[i]))
    
    print ('%d' % (i)+" Ori\t\t"+
           '%10d' % (0)+ "\t"+
           '%10d' % (histENS45ori[i])+ "\t"+
           '%10d' % (histENS85_1000ori[i])+ "\t"+
           '%10d' % (histENS85_420ori[i]))
    print ('%d' % (i)+" Del\t\t"+
           '%10d' % (0)+ "\t"+
           '%10d' % (histENS45del[i])+ "\t"+
           '%10d' % (histENS85_1000del[i])+ "\t"+
           '%10d' % (histENS85_420del[i]))
    print (' ')
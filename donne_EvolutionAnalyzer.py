import mysql.connector as db
import sys


def dbConnect():
    try:
        conn= db.connect(host= "localhost",
                        user="admin_CovidModeler",
                        password="dic2tr",
                        database="covidModeler")
                

    except db.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    return conn

def dicoRegion_Departement():
    conn=dbConnect()
    curseur= conn.cursor()
    request= """ SELECT R.nom_localite AS region, D.nom_localite AS departement, R.region_id
                FROM region R JOIN departement D ON R.region_id= D.region_id"""
    curseur.execute(request)
    result=curseur.fetchall()
    regions={}
    departements={}
    for val in result:
        regions.update({val[0] : val[2]})
        departements.update({val[1] : val[2]})
    
    curseur.close()
    return(regions, departements)

def cumulCasSurPop(mois):
    conn=dbConnect()
    curseur= conn.cursor()
    request= """SELECT nom_localite, (SUM(nbre_cas)*1000/population) AS cumul FROM 
            departement NATURAL JOIN cas_localite WHERE Date_format(date_communique, '%Y-%m')<%s GROUP BY depart_id;"""
    date=(mois,)
    curseur.execute(request, date)
    result=curseur.fetchall()
    cumul={}
    for val in result:
        if val[1] == None:
            cumul[val[0]] = 0
        else:
            cumul[val[0]] = float(val[1])

    curseur.close()
    return cumul

def dateFirstCas():
    conn=dbConnect()
    curseur= conn.cursor()
    request="""SELECT nom_localite, MIN(date_communique) AS date_min FROM cas_localite NATURAL JOIN DEPARTEMENT 
                GROUP BY depart_id HAVING date_min>'2020-04-30' ORDER BY date_min"""
    curseur.execute(request)
    result=curseur.fetchall()
    dateMin={}
    for val in result:
        dateMin[val[0]]=str(val[1].isoformat())
    
    curseur.close()
    return dateMin

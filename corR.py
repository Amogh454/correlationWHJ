import csv
import plotly.express as pl
import numpy as N

with open('data1.csv') as f:
    df = csv.DictReader(f)
    fig = pl.scatter(df, x = 'rollNo', y='marksInPercentage')
    fig.show()

def getData(f):
    rollNo = []
    marksInPercentage = []   

    with open('data1.csv') as td:
         cvR = csv.DictReader(td)
         for i in cvR:
           rollNo.append(float(i['rollNo']))
           marksInPercentage.append(float(i['marksInPercentage']))

    
    return{
        "x":rollNo,
        "y":marksInPercentage
    }         

def corRelation(c):
    correlation = N.corrcoef(c['x'], c['y'])       
    print('Correlation between roll number and marks in percentage:',correlation[0, 1])


c = getData(f)    
corRelation(c)
    

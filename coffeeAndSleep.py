import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    coffeeDrunk=[]
    sleep=[]

    with open (data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)

        for row in csv_reader:
            coffeeDrunk.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x":sleep,"y":coffeeDrunk}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation between Cups of coffee and hours of sleep \n ---> ",correlation[0,1])

def setup():
    data_path="cups of coffee vs hours of sleep.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)

setup()
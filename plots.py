import datetime
import sqlite3
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
# connect to a database in order to create tables

data = pd.read_csv('merged.csv')
data[:-10]

con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
# create try/except statement since we do not want to overwrite existing tables
try:
    cmd = "DROP table vaccinedat"
    cur.execute(cmd)
except:
    pass
cur.execute('CREATE TABLE vaccinedat (FIPS,Province_State,Country_Region,Date,Lat,Long_,Vaccine_Type,Doses_alloc,Doses_shipped,Doses_admin,Stage_One_Doses,Stage_Two_Doses,Combined_Key,State,TotalPop,Men,Women,Hispanic,White,Native,Asian,Pacific,VotingAge,Income,IncomePerCap)')
con.commit()
data.to_sql("vaccinedat", con, if_exists='replace', index=False)


def simpleplots(demographic):
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat")

    dataset = cur.fetchall()

    plt.scatter(*zip(*dataset))
    plt.xlabel(demographic)
    plt.ylabel("Doses Administered")
    plt.savefig('DosesVsDemographic.png')


# simpleplots("Income")


def comparisonplots(state1, state2, demographic):

    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State = '"+state1+"'")

    datasetplot1 = cur.fetchall()

    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State ='"+state2+"'")

    # datasetplot2 =
    datasetplot2 = cur.fetchall()

    income1 = datasetplot1[0][0]
    doses1 = datasetplot1[0][1]

    income2 = datasetplot2[0][0]
    doses2 = datasetplot2[0][1]

    N = 2
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35

    States = [state1, state2]
    Income = [math.log(income1), math.log(income2)]
    Doses = [math.log(doses1), math.log(doses2)]

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, Doses, width, color='r')
    rects2 = ax.bar(ind + width, Income, width, color='y')

    ax.set_ylabel('Log of Income and doses count')
    ax.set_title('Log Income vs dose count by state')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((state1, state2))

    plt.show()

    plt.savefig('comparisonplot.png')


comparisonplots("Alaska", "North Carolina", "Income")

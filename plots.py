"""
Analyzing and Visualizing Demographic and Vaccine Data
"""
from bioinfokit.analys import stat
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from sklearn.linear_model import LinearRegression
import sqlite3

# read and format data for plots
data = pd.read_csv('merged.csv')
data[:-10]
df = data.iloc[:,[1,2,10]]

# Interactive map of vaccine does across states
fig = go.Figure(data=go.Choropleth(
    locations=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"], # Spatial coordinates
    z = df['Doses_admin'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'tealgrn',
    colorbar_title = "Doses Administered",
))
fig.update_layout(
    title_text = 'Covid Vaccine Doses Administered By State',
    geo_scope='usa', # limite map scope to USA
)
fig.show()

# establish database connection
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
    """Create plots, regression models, and compute r^2 values of vaccine doses v. continuous demographic variables"""
    
    # Retreiving data for plots
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat")
    dataset = cur.fetchall()

    # Retreiving and shaping data for regression line
    cmd = "SELECT "+demographic+", Doses_admin FROM vaccinedat"
    stat_df = pd.read_sql_query(cmd, con)
    stat_df = stat_df.drop([51,52,53,54,55,56,57,58,59,60]) #dropping missing data of US territories
    X = stat_df.iloc[:, 0].values
    X = X.reshape(-1,1)
    y = stat_df.iloc[:, 1].values
    reg = LinearRegression().fit(X, y)

    # Creating plots
    plt.scatter(*zip(*dataset))
    plt.plot(X, reg.predict(X), color='blue', linewidth=3)
    plt.xlabel(demographic)
    plt.ylabel("Doses Administered")
    plt.title("Doses Administered v." + str(demographic) + "    R^2:" + str(reg.score(X,y,)))
    plt.savefig('DosesVsDemographic.png')


def vaccine_by_income(variable):
    """Analyze vaccine doses by demographics of states using ANOVA"""
    if variable not in ("IncomePerCap", "Hispanic", "Women"):
        raise Exception("Variable must be IncomePerCap, Hispanic, or Women") 
    res = stat()
    if variable == "IncomePerCap":
        data['category'] = pd.cut(data['IncomePerCap'], bins=[0, data['IncomePerCap'].median(), float('Inf')], labels=['High', 'Low'])
        ax = sns.boxplot(x="category", y="Doses_admin", data=data, color='#99c2a2')
        res.anova_stat(df=data, res_var='Doses_admin', anova_model='Doses_admin ~ C(category)')
        print(res.anova_summary)
        plt.xlabel("Income per Capita of States")
        plt.title("Does Administered by " + str(variable) + "  ANOVA p-val>0.10")
    elif variable == "Hispanic":
        data['category'] = pd.cut(data['Hispanic'], bins=[0, data['Hispanic'].median(), float('Inf')], labels=['High', 'Low'])
        ax = sns.boxplot(x="category", y="Doses_admin", data=data, color='#99c2a2')
        res.anova_stat(df=data, res_var='Doses_admin', anova_model='Doses_admin ~ C(category)')
        print(res.anova_summary)
        plt.xlabel("Hispanic Populaton of States")
        plt.title("Does Administered by " + str(variable) + "  ANOVA p-val>0.10")
    else:
        data['gender_cat'] = pd.cut(data['Women'], bins=[0, data['Women'].median(), float('Inf')], labels=['High', 'Low'])
        ax = sns.boxplot(x="gender_cat", y="Doses_admin", data=data, color='#99c2a2')
        res.anova_stat(df=data, res_var='Doses_admin', anova_model='Doses_admin ~ C(gender_cat)')
        print(res.anova_summary)
        plt.xlabel("Population of Women in States")
        plt.title("Does Administered by " + str(variable) + "  ANOVA p-val<0.01")
    
    plt.ylabel("Doses Administered")
    plt.savefig('boxplot.png')


def comparisonplots(state1, state2, demographic):
    """Comparing doses administered and demographic variables across states"""
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State = '"+state1+"'")
    datasetplot1 = cur.fetchall()
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State ='"+state2+"'")

    # datasetplot2
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

if __name__ == '__main__':
    simpleplots("Income")
    vaccine_by_income("Hispanic")
    comparisonplots("Alaska", "North Carolina", "Income")

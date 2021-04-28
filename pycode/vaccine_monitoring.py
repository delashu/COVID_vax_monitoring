"""
Analyzing and Visualizing Demographic and Vaccine Data

Four separate figures are created with additional analyses performed on the plots

Figures created include: interactive chloropeth map, scatter plot, boxplot, and bar plot
Analyses performed include: linear regression, R^2, and one-way ANOVA 
"""

from bioinfokit.analys import stat
import datetime
import json
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
from pycode.var_analysis import state_to_df, open_state

# read and format data for plots
data = state_to_df()
data[:-10]
df = data.iloc[:,[0,1,9]]

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

def interactiveplot():
    """ 
    BEHAVIOR: creates interactive map of vaccine doses across states, 
    OUTPUT: map is plotted in separate window.
    """
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

def simpleplots(demographic):
    """
    INPUT: demographic variable
    BEHAVIOR: create scatter plot of vaccine doses v. continuous demographic variable,
                plot points for each of the 50 US states,
                compute and plot regression line and R^2 value,
    OUTPUT: figure saved into working directory
    """
    # retrieve data for plots using SQL
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat")
    dataset = cur.fetchall()

    # retrieve and shape data for regression line
    cmd = "SELECT "+demographic+", Doses_admin FROM vaccinedat"
    stat_df = pd.read_sql_query(cmd, con)
    stat_df = stat_df.drop([51,52,53,54,55,56,57,58,59,60]) #dropping missing data of US territories
    X = stat_df.iloc[:, 0].values
    X = X.reshape(-1,1)
    y = stat_df.iloc[:, 1].values
    reg = LinearRegression().fit(X, y)

    # create plot and save into directory 
    plt.scatter(*zip(*dataset))
    plt.plot(X, reg.predict(X), color='blue', linewidth=3)
    plt.xlabel(demographic)
    plt.ylabel("Doses Administered")
    plt.title("Doses Administered v." + str(demographic) + "    R^2:" + str(reg.score(X,y,)))
    plt.savefig('DosesVs' + str(demographic) + '.png')


def vaccine_by_demographics(variable):
    """
    INPUT: demographic variable
    BEHAVIOR: analyze vaccine doses by demographics dichotomized into low (below median) and high groups,
                plot boxplots showing spread of vaccine doses administered
                perform ANOVA analysis 
    OUTPUT: ANOVA summary printed to terminal
                plot saved into working directory
    """
    if variable not in ("TotalPop", "Income", "IncomePerCap", "Hispanic", "White", "Native", "Asian", "Pacific", "Men", "Women"):
        raise Exception("Variable must be a demographic characteristic: TotalPop, Income, IncomePerCap, Hispanic, White, Native, Asian, Pacific, Men, Women") 
    
    # boxplot
    data['category'] = pd.cut(data[variable], bins=[0, data[variable].median(), float('Inf')], labels=['High', 'Low'])
    ax = sns.boxplot(x="category", y="Doses_admin", data=data, color='#99c2a2')
    # ANOVA model
    res = stat()
    res.anova_stat(df=data, res_var='Doses_admin', anova_model='Doses_admin ~ C(category)')
    
    # output analysis and plot
    print(res.anova_summary)
    print("If the pvalue is > 0.10, there is no difference in the high and low groups (at a confidence level of 0.10)")
    plt.title("Does Administered by " + str(variable))
    plt.xlabel(variable)
    plt.ylabel("Doses Administered")
    plt.savefig('boxplot_' + str(variable) + '.png')


def comparisonplots(state1, state2, demographic):
    """
    INPUTS: US state, US state, demographic variable
    BEHAVIOR: perform pairwise comparisons of doses administered and demographic variables,
                plot bar plots
    OUTPUT: figure saved into working directory
    """
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State = '"+state1+"'")
    datasetplot1 = cur.fetchall()
    cur.execute(
        "SELECT "+demographic+", Doses_admin FROM vaccinedat WHERE Province_State ='"+state2+"'")
    
    # assign data values for each set of bar plots 
    datasetplot2 = cur.fetchall()
    income1 = datasetplot1[0][0]
    doses1 = datasetplot1[0][1]
    income2 = datasetplot2[0][0]
    doses2 = datasetplot2[0][1]

    N = 2
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35

    States = [state1, state2]
    # log transformation to visualize variables on same plot
    Income = [math.log(income1), math.log(income2)]
    Doses = [math.log(doses1), math.log(doses2)]

    # create plot
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, Doses, width, color='r')
    rects2 = ax.bar(ind + width, Income, width, color='y')
    ax.set_ylabel('Log of Income and doses count')
    ax.set_title('Log Income vs dose count by state')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels((state1, state2))
    plt.show()
    plt.savefig('comparisonplot_'+ str(state1) + str(state2) + str(demographic) +'.png')

if __name__ == '__main__':
    simpleplots("Income")
    vaccine_by_demographics("IncomePerCap")
    comparisonplots("Alaska", "North Carolina", "Income")
    mystate = open_state()
    print(mystate["North Carolina"].Stage_One_Doses)
    interactiveplot()
"""
Demographic Data Retrieval 
Census-level demographics are read from csv file (link below) that was uploaded to Github repository.
Data is aggregated by state and inserted into the CovidVax SQl database.

Data Source: 
US Census via Kaggle
https://www.kaggle.com/muonneutrino/us-census-demographic-data?select=acs2017_county_data.csv)
"""
import sqlite3
import pandas as pd

# establish database connection
con = sqlite3.connect('CovidVax.db')
cur = con.cursor()

# #create try/except statement since we do not want to overwrite existing tables
try:
    cmd = "DROP table statedemo"
    cur.execute(cmd)
except:
    pass

# read data on county level demographics from github and summarize by states
dg_df = pd.read_csv("https://raw.githubusercontent.com/delashu/COVID_vax_monitoring/main/acs2017_county_data.csv")
columns = ['State', 'TotalPop', 'Men', 'Women', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'VotingAge', 'Income', 'IncomePerCap']
df1 = pd.DataFrame(dg_df, columns=columns)
df2 = df1.groupby('State', as_index=False).agg({'TotalPop':'sum','Men':'sum','Women':'sum','Hispanic':'mean','White':'mean','Native':'mean','Asian':'mean','Pacific':'mean','VotingAge':'mean','Income':'mean','IncomePerCap':'mean'})
df2.to_sql("statedemo", con, if_exists='replace', index=False)

# close SQL connection
con.commit()
con.close()
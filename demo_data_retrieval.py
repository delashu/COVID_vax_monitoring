import datetime
import sqlite3
import pandas as pd
#connect to a database in order to create tables
con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
#create try/except statement since we do not want to overwrite existing tables
try:
    cmd = "DROP table statedemo"
    cur.execute(cmd)
except:
    pass
cmd = "CREATE TABLE statedemo (SUMLEV REAL,REGION REAL,DIVISION REAL,STATE REAL,NAME text,SEX REAL,ORIGIN REAL,RACE REAL,AGE REAL,CENSUS2010POP REAL,ESTIMATESBASE2010 REAL,POPESTIMATE2010 REAL,POPESTIMATE2011 REAL, POPESTIMATE2012 REAL,POPESTIMATE2013 REAL, POPESTIMATE2014 REAL,POPESTIMATE2015 REAL,POPESTIMATE2016 REAL,POPESTIMATE2017 REAL,POPESTIMATE2018 REAL,POPESTIMATE2019 REAL)"

cur.execute(cmd)
dg_df = pd.read_csv("https://www2.census.gov/programs-surveys/popest/tables/2010-2019/state/asrh/sc-est2019-alldata5.csv")
dg_df.to_sql("statedemo", con, if_exists='replace', index=False)
#cur.execute("SELECT * FROM statedemo LIMIT 3;")
#print(cur.fetchall())
con.commit()
con.close()
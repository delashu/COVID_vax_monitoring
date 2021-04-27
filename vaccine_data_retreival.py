"""
Retrieve most recent state-level vaccine data.
The data comes from a github repository maintained by  Johns Hopkins Medicine and the Center for Health Security in the Bloomberg School of Public Health.
The data is downloaded via the link to the raw csv data.
The script then places this data into a table in 'CovidVax.db'.
"""
import datetime
import sqlite3
import pandas as pd
#connect to database in order to create tables
con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
#create try/except statement since we do not want to overwrite existing tables
try:
    cmd = "DROP table statevax"
    cur.execute(cmd)
except:
    pass
#retrieve data from raw csv link (JHU) and place into sql db
vx_df = pd.read_csv("https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/us_data/hourly/vaccine_data_us.csv")
vx_df.to_sql("statevax", con, if_exists='replace', index=False)
con.commit()
con.close()
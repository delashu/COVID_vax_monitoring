import datetime
import sqlite3
import pandas as pd
#connect to a database in order to create tables
con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
#create try/except statement since we do not want to overwrite existing tables
try:
    cmd = "DROP table statevax"
    cur.execute(cmd)
except:
    pass
cmd = "CREATE TABLE statevax (FIPS REAL,state text,country CHAR(2),date CHAR(10),lat REAL,long REAL,vaccine_type text,doses_alloc REAL,doses_shipped REAL, doses_admin REAL,stage_one_dose REAL,stage_two_dose REAL, comb_key text)"
cur.execute(cmd)
vx_df = pd.read_csv("https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/us_data/hourly/vaccine_data_us.csv")
vx_df.to_sql("statevax", con, if_exists='replace', index=False)
#cur.execute("SELECT * FROM statevax LIMIT 3;")
#print(cur.fetchall())
con.commit()
con.close()
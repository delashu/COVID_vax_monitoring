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
vx_df = pd.read_csv("https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/us_data/hourly/vaccine_data_us.csv")
vx_df.to_sql("statevax", con, if_exists='replace', index=False)
#cur.execute("SELECT * FROM statevax LIMIT 3;")
#print(cur.fetchall())
con.commit()
con.close()
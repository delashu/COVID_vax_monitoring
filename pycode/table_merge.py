"""
merging of the vaccine data and the state level data
"""
import datetime
import sqlite3
import pandas as pd
#connect to a database in order to create tables
con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
#perform a FULL JOIN on the two tables
cmd = """
SELECT statevax.*, statedemo.*
FROM statedemo 
LEFT JOIN statevax ON statevax.Province_State = statedemo.NAME
UNION ALL
SELECT statevax.*, statedemo.*
FROM statevax
LEFT JOIN statedemo ON statevax.Province_State = statedemo.NAME
WHERE statevax.Province_State IS NULL
"""
merged_df = pd.read_sql_query(cmd, con)
#print(merged_df.head())
con.close()
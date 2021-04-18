"""
Create python code that will visualize continuous variables against vaccine rates per state.
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
class State:
    def __init__(self, ID, demovar1, demovar2, demovar3, demovar4):  #method call   
        self.ID = ID #instance attribute
        self.x = x 
        self.y = y
        self.z = z
        self.m = m
    #add a decorator
    @property
    def percentage(self): 
        pct = float(self.percentage_vaccinated)
        return pct
    #greater than comparison operator
    def __gt__(self, other): 
        if ininstance(other, Patient):
            if self.percentage > other.percentage:
                return True
        elif ininstance(other, int):
            if self.percentage > other:
                return True
        elif ininstance(other, float):
            if self.percentage > other:
                return True
        return False
        raise ValueError("Comparison is not supported")
    #less than comparison operator
    def __lt__(self, other): 
        if ininstance(other, Patient):
            if self.percentage < other.percentage:
                return True
        elif ininstance(other, int):
            if self.percentage < other.percentage:
                return True
        elif ininstance(other, float):
            if self.percentage < other.percentage:
                return True
        return False
        raise ValueError("Comparison is not supported")
    def plot(self, xvar, outsave):
        #plot function here

def open_state(datatable = "PatientCorePopulatedTable.txt"): 
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
    statedat={} #key by STATE
    for line in pat_txt:
        values = line.replace("\n", "")
        values = values.split("\t")
        statedat[values[0]]=State(ID = values[0], 
            demovar1=values[1],
            demovar2=values[2],
            demovar3=values[3], 
            demovar4=values[4], 
            demovar5=values[5], 
            demovar6=values[6])
    return statedat
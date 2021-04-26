"""
Create python code that will visualize continuous variables against vaccine rates per state.
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sqlite3
import pandas as pd
import os
import vaccine_data_retreival
import demo_data_retrieval

con = sqlite3.connect('CovidVax.db')
cur = con.cursor()
class State():
    def __init__(self, state, Date, Lat, Long, Vaccine_Type, Doses_alloc, Doses_shipped,Doses_admin,Stage_One_Doses,Stage_Two_Doses,TotalPop,Men,Women,Hispanic,White,Native,Asian,Pacific,VotingAge,Income,IncomePerCap):
        self.state = state
        self.Date = Date
        self.Lat = Lat
        self.Long = Long 
        self.Vaccine_Type = Vaccine_Type
        self.Doses_alloc = Doses_alloc
        self.Doses_shipped = Doses_shipped
        self.Doses_admin = Doses_admin
        self.Stage_One_Doses = Stage_One_Doses
        self.Stage_Two_Doses = Stage_Two_Doses
        self.TotalPop = TotalPop
        self.Men = Men
        self.Women = Women
        self.Hispanic = Hispanic
        self.White = White
        self.Native = Native
        self.Asian = Asian
        self.Pacific = Pacific 
        self.VotingAge = VotingAge 
        self.Income = Income 
        self.IncomePerCap = IncomePerCap
    #add a decorator
    # @property
    # def percentage_vaccinated(self):
    #     pct = float(self.Doses_admin)/float(self.TotalPop) 
    #     return pct
    #greater than comparison operator
    def __gt__(self, other): 
        if ininstance(other, State):
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
        if ininstance(other, State):
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

def state_to_df(your_db="CovidVax.db"): 
    con = sqlite3.connect(your_db)
    cur = con.cursor()
    #perform a FULL JOIN on the two tables
    cmd = """
    SELECT * FROM statevax
    LEFT JOIN statedemo ON statevax.Province_State = statedemo.State
    WHERE statevax.Vaccine_Type = "All";
    """
    merged_df_dat = pd.read_sql_query(cmd, con)
    return merged_df_dat

def open_state(your_db="CovidVax.db"): 
    con = sqlite3.connect(your_db)
    cur = con.cursor()
    #perform a FULL JOIN on the two tables
    cmd = """
    SELECT * FROM statevax
    LEFT JOIN statedemo ON statevax.Province_State = statedemo.State
    WHERE statevax.Vaccine_Type = "All";
    """
    merged_df = pd.read_sql_query(cmd, con)
    merged_df = merged_df.drop([51,52,53,54,55,56,57,58,59,60])
    state_lists = merged_df.values.tolist()
    state_dict={}
    for us_state in state_lists:
        state_dict[us_state[1]]=State(state=us_state[1],
        Date = us_state[3],
        Lat = us_state[4],
        Long = us_state[5], 
        Vaccine_Type = us_state[6], 
        Doses_alloc = us_state[7],
        Doses_shipped = us_state[8],
        Doses_admin = us_state[9],
        Stage_One_Doses = us_state[10],
        Stage_Two_Doses = us_state[11],
        TotalPop = us_state[14],
        Men = us_state[15],
        Women = us_state[16],
        Hispanic = us_state[17],
        White = us_state[18],
        Native = us_state[19],
        Asian = us_state[20],
        Pacific = us_state[21], 
        VotingAge = us_state[22], 
        Income = us_state[23], 
        IncomePerCap = us_state[24])
    return state_dict

# if __name__ == "__main__":
#     mystate = open_state()
#     print(mystate["North Carolina"].Stage_One_Doses)
#     print(mystate["South Carolina"].Stage_One_Doses)
#     print(mystate["North Carolina"].Stage_Two_Doses)
#     print(mystate["South Carolina"].Stage_Two_Doses)
#     print(mystate["North Carolina"].Stage_Two_Doses > mystate["South Carolina"].Stage_Two_Doses)
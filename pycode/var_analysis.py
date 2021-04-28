"""
'var_analysis.py' imports 'vaccine_data_retreival.py' and 'demo_data_retrieval.py'
    'vaccine_data_retreival.py' pulls vaccine data. 
    'demo_data_retrieval.py' pulls demographic data. 
This script will then join the two tables craeted in 'vaccine_data_retreival.py' and 'demo_data_retrieval.py'
The joined table will then be placed in a dictionary and then a Class Object titled, "State()"
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
    """
    Create a class object called state using the __init__() function
    Assign various state level characteristic values to the State object property
    """
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
    @property
    def percentage_stage_one(self):
        """
        INPUT: this function takes in the "Stage_One_Doses" and "TotalPop" from self as 
                defined in the class object above. 
                ensure to add a decorator "@property"
        BEHAVIOR: We ensure that both "Stage_One_Doses" and "TotalPop" are floats
                    We divide "Stage_One_Doses" by "TotalPop" to obtain 
                    the percentage of the state that has recieved a stage one dose. 
        OUTPUT: return a object "pct_stg_one" that contains the percentage of the state that has recieved a stage one dose. 
        """
        pct_stg_one = float(self.Stage_One_Doses)/float(self.TotalPop) 
        return pct_stg_one
    @property
    def percentage_stage_two(self):
        """
        INPUT: this function takes in the "Stage_Two_Doses" and "TotalPop" from self as 
                defined in the class object above. 
                ensure to add a decorator "@property"
        BEHAVIOR: We ensure that both "Stage_Two_Doses" and "TotalPop" are floats
                    We divide "Stage_Two_Doses" by "TotalPop" to obtain 
                    the percentage of the state that has recieved a stage two dose. 
        OUTPUT: return a object "pct_stg_two" that contains the percentage of the state that has recieved a stage two dose. 
        """
        pct_stg_two = float(self.Stage_Two_Doses)/float(self.TotalPop) 
        return pct_stg_two

def state_to_df(your_db="CovidVax.db"): 
    """
    INPUT: database name (default: "CovidVax.db")
    BEHAVIOR: connect to the databse, 
                perform a left join on the two tables
                where each row is a state.
                place the output of the join into a pandas dataframe
    OUTPUT: pandas dataframe where each row is a state
    """
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

def open_state(your_db = "CovidVax.db"): 
    """
    INPUT: database name (default: "CovidVax.db")
    BEHAVIOR: connect to the databse, 
                perform a left join on the two tables
                where each row is a state.
                place the output of the join into a pandas dataframe
                the pandas dataframe is then output into a list. 
                We iterate through the list and place into a dictionary and class object "State"
    OUTPUT: dictionary, titled, "state_dict" where index is state name
            This dictionary is also placed into a class object, "State"
    """
    con = sqlite3.connect(your_db)
    cur = con.cursor()
    #perform a LEFT JOIN on the two tables
    cmd = """
    SELECT * FROM statevax
    LEFT JOIN statedemo ON statevax.Province_State = statedemo.State
    WHERE statevax.Vaccine_Type = "All";
    """
    merged_df = pd.read_sql_query(cmd, con)
    merged_df = merged_df.drop([51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
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
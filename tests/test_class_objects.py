"""
Testing file for the file, "var_analysis.py"
    This testing file will test all functions in the script, "var_analysis.py"
    contributors should add to these tests
"""
from .. pycode import var_analysis
import pytest

def test_open_state():
    """ 
    test open_state() function 
    test to ensure that the number of Men in Nebraska is '943547.0'
    """
    state = var_analysis.open_state()
    assert state["Nebraska"].Men == 943547.0, "value is incorrect - test_open_state() does not pass"

def test_state_to_df():
    """
    test state_to_df() function 
    test to ensure that the State found in state.iloc[1][1] is "Alaska"
    """
    state = var_analysis.state_to_df()
    assert state.iloc[1][1] == "Alaska", "value is incorrect - test_state_to_df() does not pass"

def test_open_state():
    """ 
    test state_to_df() function 
    test to ensure that the correct len dictionary is output from "open_state()"
    """
    my_state = var_analysis.open_state()
    assert len(my_state) == 51, "value is incorrect - test_open_state() does not pass"

def test_percentage_stage_two():
    """ 
    test percentage_stage_two() function 
    test to ensure that the correct percentage of stage two doses from South Carolina population is correct
    """
    my_state = var_analysis.open_state()
    #create a SC object 
    SC = my_state["South Carolina"]
    #output the number of Stage_Two_Doses
    stg_two=SC.Stage_Two_Doses
    #output the total population
    totpop=SC.TotalPop
    #manually calculate the percentage stage two doses
    my_div = stg_two/totpop
    #assert that the manual division is the same as the class object
    assert my_div == SC.percentage_stage_two, "value is incorrect - test_percentage_stage_two() does not pass"

def test_percentage_stage_one():
    """ 
    test percentage_stage_one() function 
    test to ensure that the correct percentage of stage one doses from Maryland population is correct
    """
    my_state = var_analysis.open_state()
    #create a Maryland object 
    MD = my_state["Maryland"]
    #output the number of Stage_One_Doses
    stg_one = MD.Stage_One_Doses
    #output the total population
    totpop = MD.TotalPop
    #manually calculate the percentage stage one doses
    my_div = stg_one/totpop
    #assert that the manual division is the same as the class object
    assert my_div == MD.percentage_stage_one, "value is incorrect - test_percentage_stage_one() does not pass"
import var_analysis
import pytest


def test___lt__():
    """ test lt function  """
    mystate = var_analysis.open_state()
    assert (mystate["North Carolina"].Stage_Two_Doses >
            mystate["South Carolina"].Stage_Two_Doses) == True, "value is incorrect"


def test___gt__():
    """ test gt function  """
    mystate = var_analysis.open_state()
    assert (mystate["South Carolina"].Stage_Two_Doses <
            mystate["North Carolina"].Stage_Two_Doses) == True, "value is incorrect"


def test_open_state():
    """ test open state function """
    state = var_analysis.open_state()
    assert (
        state["Nebraska"].Men) == 10145.666666666666, "value is incorrect"


def test_state_to_df():
    """ test state to df """
    state = var_analysis.state_to_df()
    assert (state.iloc[1][1]) == "Alaska", "value is incorrect"


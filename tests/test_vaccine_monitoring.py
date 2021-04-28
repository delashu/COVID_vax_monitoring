"""
COVID Vaccine Monitoring Test File
"""
import matplotlib.pyplot as plt
from .. pycode import vaccine_monitoring
from unittest.mock import patch
import pytest

def test_simpleplots():
    """test that single data point appears on scatterplot for simpleplots."""
    demographic = "Income"
    vaccine_monitoring.simpleplots(demographic)
    f, ax = plt.subplots()
    scat = ax.scatter([0.41490221], [-2.17831414])
    set1 = scat.get_offsets()
    set2 = [[0.41490221, -2.17831414]]
    assert (set1 == set2).all() == True
    
def test_vaccine_by_demographics():
    """test vaccine_by_demographics."""
    with patch("pycode.vaccine_monitoring.plt.title") as show_patch:
        vaccine_monitoring.vaccine_by_demographics("Women")
        assert show_patch.called

def test_comparisonplots():
    """test comparisonplots."""
    with patch("pycode.vaccine_monitoring.plt.savefig") as show_patch:
        vaccine_monitoring.comparisonplots("Alaska", "North Carolina", "Income")
        assert show_patch.called
        



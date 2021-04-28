"""
COVID Vaccine Monitoring Test File
"""
from vaccine_monitoring import interactiveplot, simpleplots, vaccine_by_demographics, comparisonplots
from unittest.mock import patch
import pytest

def test_simpleplots():
    """test that single data point appears on scatterplot for simpleplots."""
    demographic = "Income"
    plots.simpleplots(demographic)
    f, ax = plt.subplots()
    scat = ax.scatter([0.41490221], [-2.17831414])
    set1 = scat.get_offsets()
    set2 = [[0.41490221, -2.17831414]]
    assert (set1 == set2).all() == True

def test_interactiveplot():
    """test interactiveplot."""
    with patch("plots.go.show") as show_patch:
        interactiveplot()
        assert show_patch.called
    
def test_vaccine_by_demographics():
    """test vaccine_by_demographics."""
    with patch("plots.plt.title") as show_patch:
        vaccine_by_demographics("Women")
        assert show_patch.called

def test_comparisonplots():
    """test comparisonplots."""
    with patch("plots.plt.savefig") as show_patch:
        comparisonplots("Alaska", "North Carolina", "Income")
        assert show_patch.called
        



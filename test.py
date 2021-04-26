"""
COVID Vaccine Monitoring Test File
"""
from plots import simpleplots, vaccine_by_demographics, comparisonplots
from unittest.mock import patch

def test_simpleplots():
    """test simpleplots."""
    with patch("plots.plt.savefig") as show_patch:
        simpleplots("IncomePerCap")
        assert show_patch.called
    
def test_vaccine_by_demographics():
    """test vaccine_by_demographics."""
    with patch("plots.plt.title") as show_patch:
        vaccine_by_demographics("Women")
        assert show_patch.called

def test_comparisonplots():
    """test comparisonplots."""
    with patch("plots.plt.show") as show_patch:
        comparisonplots("Alaska", "North Carolina", "Income")
        assert show_patch.called


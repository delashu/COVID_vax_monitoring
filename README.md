# COVID Vaccine Monitoring
**Library Name**: "COVID_vax_monitoring"  
**Team Member Names**: Noel Allen, Shusaku Asai, Saahithi Rao   
**General Software Architecture**: Python based programs to scrape, visualize, and monitor COVID-19 vaccination rates

  
## End User Instructions:  
Workflow will follow the basic steps:  
 1. Download requried files found in github repository  
 2. Import functions of interest  
 3. Perform desired analysis using provided functions  

### Installation and set-up  
1. Download the files, ["*vaccine_data_retrival.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_data_retreival.py), ["acs2017_county_data.csv"](https://github.com/delashu/COVID_vax_monitoring/blob/main/acs2017_county_data.csv),["*demo_data_retrieval.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/demo_data_retrieval.py), ["*vaccine_monitoring.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_monitoring.py), and ["*var_analysis.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/var_analysis.py), found in the github repository. Ensure that all of these files are placed in the same directory/folder.    
2. Open a new python script where you will perform your analyses  
3. Import functions into your environment based on desired analysis/capabilities.  
4. Create an object to house the analytic dataset (a pandas dataframe) where each row is a state in which demographic and vaccine data is present. In the below example, we call this dataset, "mystate"
```python
>> mystate = open_state()
```

5. Run desired analysis. For example, if you wish to output the number of Stage One Vaccine doses for the state of North Carolina, run the following line:   
```python
>> mystate = open_state()
>> NC = mystate["North Carolina"]
>> print(NC.Stage_One_Doses)
```


**Note that a full description and examples of functions and capabilities are found in the rest of this README.**  

## API description  
Below is a guide for each function found in this github repository:  

```python
>> open_state()
```
open_state() is a function that will merge state level vaccine data to state level demographic data. Under the hood, this function runs sqlite3 to merge the vaccine table and the demographic table to create one pandas dataframe.  
  
```python
>> mystate["North Carolina"].VARIABLE_OF_INTEREST
```
Class objects are utilized to allow for the end user to easily explore vaccine and demographic information for each state. In the above code, the characters, "VARIABLE_OF_INTEREST" should be replaced by the exploratory variable of interest. For example, if the user wishes to examine the Doses Administered in Illinois, the user would run the following line:  
```python
>> mystate["Illinois"].Doses_admin
```

Other exploratory variables include:  
- *Date* (when the vaccine data was updated)
- *Lat* (state latitude)
- *Long* (state longitude)
- *Doses_alloc* (Total doses allcoated)
- *Doses_shipped* (Doses shipped)
- *Doses_admin* (Doses administered)
- *Stage_One_Doses* (Total sum of stage one doses administered)
- *Stage_Two_Doses* (Total sum of stage two doses administered)
- *TotalPop* (State total population)
- *Men* (State population Men)
- *Women* (State population Women)
- *Hispanic* (State population Hispanic)
- *White* (State population White)
- *Native* (State population Native)
- *Asian* (State population Asian)
- *Pacific*  (State population Pacific)
- *Income* (Mean income)
- *IncomePerCap* (Mean ncome per capita) 

```python
>> simpleplots("demographic")
```
A scatter plot of vaccine doses administered v. the demographic characteristic for each of the 50 states and Puerto Rico along with the regression line and corresponding R^2 statistic is saved into the working directory. SQL queries are utilized for efficient retrieval of the data. Demographic should be replaced with a demographic variable of interest: *TotalPop*, *Income*, *IncomePerCap*, *Hispanic*, *White*, *Native*, *Asian*, *Pacific*, *Men*, *Women*

```python
>> vaccine_by_demographics("variable")
```
This function prints an ANOVA analysis summary comparing high and low catergories (based on median) of *variable* and vaccine doses administered. A boxplot comparing the variables is saved as a png file into the working directory to better visualize the spread of the data and ANOVA results. Variable should be replaced with a demographic variable of interest: *TotalPop*, *Income*, *IncomePerCap*, *Hispanic*, *White*, *Native*, *Asian*, *Pacific*, *Men*, *Women*

```python
>> comparisonplots(state1, state2, demographic)
```
To perform pairwise comparisons of states, a bar plot with logarithmic scales of vaccine doses administered and a selected demographic variable of two specified states is saved into the working directory. State1 and State2 should be replaced with a name of one of the 50 US states and demographic should be replaced with a demographic variable of interest: *TotalPop*, *Income*, *IncomePerCap*, *Hispanic*, *White*, *Native*, *Asian*, *Pacific*, *Men*, *Women*

```python
>> interactiveplot()
```
This function prints a choropleth map of the united states, with color representing the number of vaccine doses administered by each state. 

### Example Use Cases   
*Example One:*  
Consider the user wants to compare the Stage One Doses administered in North Carolina to the Stage Two Doses administered in South Carolina. The user would first "open" the data into a new dataframe, then run the comparison using the previously described Class objects:  

```python
>> from pycode.var_analysis import open_state
>> mystate = open_state()
>> mystate["North Carolina"].Stage_One_Doses > mystate["South Carolina"].Stage_Two_Doses
```

*Example Two:*  
Similarly, we can consider the user wants to compare the percentage of the total North Carolina population that has recieved a first dose of the vaccine to the percentage of the total Minnesota population that has recieved a first dose of the vaccine. The user can alternatively place the class into python objects and print a comparison statement to discover which state has more percentage of dose one vaccine administered:  

```python
>> from pycode.var_analysis import open_state
>> mystate = open_state()
>> myMN = mystate["Minnesota"]
>> myNC = mystate["North Carolina"]
>> my_MN_stgone = myMN.percentage_stage_one
>> my_NC_stgone = myNC.percentage_stage_one
>> print(my_MN_stgone > my_NC_stgone)
```



*Example Three:*   
Consider the user wants to compare a demographic characteristic like the percentage of the state's population that is Hispanic and the number of doses that that state has administered. The plot is saved into the parent directory as, "DosesVsDEMOGRAPHIC_OF_INTEREST.png" where "DEMOGRAPHIC_OF_INTEREST" is the user input's demographic. In our example, the plot output will be, "DosesVsHispanic.png". The user would first import the function, then run the comparison using the previously described inputs:  
```python
>> from pycode.vaccine_monitoring import simpleplots
>> simpleplots("Hispanic")
```

*Example Four:*   
Consider the user wants to compare states with a below median income per capita and states with an above median per capita and the amount of vaccine doses administered. The user would first import the function, then run the comparison using the previously described inputs. The output to this function is a plot titled, "boxplot_VARIABLE_OF_INTEREST.png" where "VARIABLE_OF_INTEREST" is the user input of the function. In this example, the variable of interest is 'IncomePerCap' and the png output is, "boxplot_IncomePerCap.png".    
```python
>> from pycode.vaccine_monitoring import vaccine_by_demographics
>> vaccine_by_demographics("IncomePerCap")
```

*Example Five:*   
Create plot comparing two selected states based on selected demographic variable and Doses Administered. The output to this function is a plot titled, "comparisonplot_STATE1STATE2DEMOGRAPHIC.png" where "STATE1", "STATE2", and "DEMOGRPAHIC" are the user inputs of the function. In the below example, the output will be found in the parent directory and will be titled, "comparisonplot_AlaskaNorth CarolinaIncome.png".    
```python
>> from pycode.vaccine_monitoring import comparisonplots
>> comparisonplots("Alaska", "North Carolina", "Income")
```

*Example Six:* 
Interactive choropleth map to show number of doses administered by state. This will open interactively in an internet browser such as google chrome.  
```python
>> from pycode.vaccine_monitoring import interactiveplot
>> interactiveplot()
```

Below is a screenshot of the interactive map.  
![alt text](https://github.com/delashu/COVID_vax_monitoring/blob/main/Vaccinedosesadministeredbystate.png)


## Contributor Instructions: 
### Contributor Workflow Overview:  
The general flow of data to analysis goes as follows:  
1. Run ["*vaccine_data_retrival.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_data_retreival.py). This file pulls the most recent state-level vaccine data. We download the data and place it into a SQLite3 table.  
2. Run ["*demo_data_retrieval.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/demo_data_retrieval.py). This file places a pre-downloaded state-level demogaphics csv data file, and places it into a SQLite3 table.  
3. Run ["*var_analysis.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/var_analysis.py). This file will run ["*vaccine_data_retrival.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_data_retreival.py) and ["*demo_data_retrieval.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/demo_data_retrieval.py) via import statements, and then joins the table via a SQL query into a pandas dataframe. The data in the pandas dataframe are then placed into a Class object, called **State**. The user can now navigate various characteristics about each state.  
4. Run ["*vaccine_monitoring.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_monitoring.py). This python file imports all the previous files from steps (1) - (3) and thus provides the user a joined analytic dataset. The user can now explore state level data via class objects, plot vaccine doses, visualize vaccine doses via a map, and run analyses such as ANOVA.   

**NOTE** that the following steps (1-4) was a workflow that was followed by the developers and contributors. All three files do not need to be run by the end user. This is because the final file, ["*vaccine_monitoring.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_monitoring.py) imports the previous three files in order such that the tables are created and merged properly (["*vaccine_data_retrival.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/vaccine_data_retreival.py),["*demo_data_retrieval.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/demo_data_retrieval.py), and ["*var_analysis.py*"](https://github.com/delashu/COVID_vax_monitoring/blob/main/var_analysis.py)).


### Tests  
A separate directory in the github repository called, ["tests"](https://github.com/delashu/COVID_vax_monitoring/tree/main/tests) houses python test files for the various python files found in the repository. We encourage contributors to add to these tests and create their own test files. Below we highlight one test found in our repository. The first is found in ["test_vaccine_monitoring.py"](https://github.com/delashu/COVID_vax_monitoring/blob/main/tests/test_vaccine_monitoring.py)   

```python
>> import matplotlib.pyplot as plt
>> from .. pycode import vaccine_monitoring
>> from unittest.mock import patch
>> import pytest

>> def test_simpleplots():
      """test that single data point appears on scatterplot for simpleplots."""
      demographic = "Income"
      vaccine_monitoring.simpleplots(demographic)
      f, ax = plt.subplots()
      scat = ax.scatter([0.41490221], [-2.17831414])
      set1 = scat.get_offsets()
      set2 = [[0.41490221, -2.17831414]]
      assert (set1 == set2).all() == True
```

After all tests have been written, run the below in the commandline and ensure all tests pass/clear.  
Make sure that the tests are run in the parent directory.     
```console
$ python -m pytest tests
```

Developers have also used 'pylint' to ensure clean and consistent coding. We encourage contributors to follow the 'pylint' consistency as well.  

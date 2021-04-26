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
1. Download the python files, "*vaccine_data_retrival.py*","*demo_data_retrieval.py*", "*plots.py*", and "*var_analysis.py*", found in the github repository   
2. Open a new python script where you will perform your analyses  
3. Import functions into your environment based on desired analysis/capabilities.  

```python
>> from var_analysis import open_state
>> from plots import simpleplots, vaccine_by_demographics
```

4. Create an object to house the analytic dataset. In the below example, we call this dataset, "mystate"
```python
>> mystate = open_state()
```

5. Run desired analysis. For example, if you wish to output the number of Stage One Vaccine doses for the state of North Carolina, run the following line:   
```python
>> mystate["North Carolina"].Stage_One_Doses
```


## API description  
Below is a guide for each function found in this github repository:  

```python
>> open_state()
```
open_state() is a function that will merge state level vaccine data to state level demographic data. Under the hood, this function runs sqlite3 to merge the two tables from a sqlite3 database. The function outputs a dictionary in which the keys are state names.  
  
```python
>> mystate["North Carolina"].VARIABLE_OF_INTEREST
```
Class objects are utilized to allow for the end user to easily explore vaccine and demographic information for each state. In the above code, the characters, "VARIABLE_OF_INTEREST" should be replaced by the exploratory variable of interest. Possible variables include:  
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
A scatter plot of vaccine doses administered v. the demographic characteristic for each of the 50 states along with the regression line and corresponding R^2 statistic is saved into the working directory. SQL queries are utilized for efficient retrieval of the data. Demographic should be replaced with a demographic variable of interest: *TotalPop*, *Income*, *IncomePerCap*, *Hispanic*, *White*, *Native*, *Asian*, *Pacific*, *Men*, *Women*

```python
>> vaccine_by_demographics("variable")
```
This function prints an ANOVA analysis summary comparing high and low catergories (based on median) of *variable* and vaccine doses administered. A boxplot comparing the variables is saved as a png file into the working directory to better visualize the spread of the data and ANOVA results. Variable should be replaced with a demographic variable of interest: *TotalPop*, *Income*, *IncomePerCap*, *Hispanic*, *White*, *Native*, *Asian*, *Pacific*, *Men*, *Women*

```python
>> 
```
Description here

### Example Use Cases   
*Example One:*  
Consider the user wants to compare the Stage One Doses administered in North Carolina to the Stage Two Doses administered in South Carolina. The user would first "open" the data into a new dataframe, then run the comparison using the previously described Class objects:  

```python
>> from var_analysis import open_state
>> mystate = open_state()
>> mystate["North Carolina"].Stage_One_Doses > mystate["South Carolina"].Stage_Two_Doses
```

*Example Two:*   
Consider the user wants to compare a demographic characteristic like the percentage of the state's population that is Hispanic and the number of doses that that state has administered. The user would first import the function, then run the comparison using the previously described inputs: 
```python
>> from plots import vaccine_by_demographics
>> vaccine_by_demographics("IncomePerCap")
```

*Example Three:*   
Consider the user wants to compare states with a below median income per capita and states with a above median per capita and the amount of vaccine doses administered. The user would first import the function, then run the comparison using the previously described inputs: 
```python
>> from plots import vaccine_by_demographics
>> vaccine_by_demographics("IncomePerCap")
```

*Example Four:*   
Create plot comparing two selected states based on selected demographic variable and Doses Administered. 
```python
>>from plots import comparisonplots
>>comparisonplots("Alaska", "North Carolina", "Income")
```
*Example Five:* 
Interactive choropleth map to show number of doses administered by state. 
![alt text](https://github.com/delashu/COVID_vax_monitoring/blob/main/Vaccinedosesadministeredbystate.png)

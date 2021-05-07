# About the code tree

`Src` folder has the business logic layer present. 

`run.py` in the root directory is the driver file. 

### Pre-requisite

`pip install -r requirements.txt`

Populate run.py with File name. 

Preferred to place the input file csv in the root directory. 

If input file wants to be placed elsewhere, please provide appropriate path in line num: 9 in `run.py`

## To Run

`python run.py`


## Expected Output

`mean_players_IN_US.csv`

All Players who are part of IN, US countries and Mean Revenues calculated from Day 3 of their installation.

`highest_revenue_group.csv` 

Mean Revenue aggregated based on groups of the player from all countries.

`highest_revenue_group_byCountry.csv`

Mean Revenue aggregated based on groups of the player from the countries IN, US.
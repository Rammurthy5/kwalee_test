'''
..module.. 
The objective of the module is read the given file path, and find aggregated 
revenue for each player, and produce a user-readable format output. 

..author..      Rammurty Subrahmaniyan
..license..     Kwalee Inc. 
'''


# standard imports
from collections import defaultdict

# 3rd part libraries
import pandas


def process_player_data(file_path):
        
    # File loading
    file_content_dataframe = pandas.read_csv(file_path)

    # input & variable decl. contingent
    result_dict = defaultdict(list)
    highest_revenue_group_country_dict = defaultdict(list)
    highest_revenue_group_dict = defaultdict(list)

    # filter the players who are based out of "US", "IN", "in" countries, and players revenue from Day 3 of installation
    filtered_data = file_content_dataframe[(file_content_dataframe.country.isin(["US", "IN", "in"])) & (file_content_dataframe.day > 2)]

    mean_for_players = filtered_data.groupby(["player_id", "country", "ab_group"])["daily_total_revenue"].mean()

    highest_revenue_group_country = filtered_data.groupby(["ab_group", "country"])["daily_total_revenue"].mean().to_dict()

    highest_revenue_group = filtered_data.groupby("ab_group")["daily_total_revenue"].mean().to_dict()

    mean_players_dict = mean_for_players.to_dict()

    # Put together the data
    for k, v in mean_players_dict.items():
        result_dict['Country'].append(k[1])
        result_dict['Group'].append(k[2])
        result_dict['Players'].append(k[0])
        result_dict['Mean Revenue'].append(v)

    result_dataframe = pandas.DataFrame(result_dict)
    result_dataframe.to_csv("mean_players_IN_US.csv")

    # Highest Revenue based on Country and Group
    for k, v in highest_revenue_group.items():
        highest_revenue_group_dict["Group"].append(k[0])
        highest_revenue_group_dict["Mean Revenue"].append(v)

    highest_revenue_group_df = pandas.DataFrame(highest_revenue_group_dict)
    highest_revenue_group_df.to_csv("highest_revenue_group.csv")

    # highest Revenue based on Group alone
    for k, v in highest_revenue_group_country.items():
        highest_revenue_group_country_dict["Group"].append(k[0])
        highest_revenue_group_country_dict["Country"].append(k[1])
        highest_revenue_group_country_dict["Mean Revenue"].append(v)

    highest_revenue_group_country_df = pandas.DataFrame(highest_revenue_group_country_dict)
    highest_revenue_group_country_df.to_csv("highest_revenue_group_byCountry.csv")

    return "mean_players_IN_US.csv", "highest_revenue_group.csv", "highest_revenue_group_byCountry.csv"
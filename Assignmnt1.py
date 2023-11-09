"""
Name: KURRE SAI KRISHNA REDDY 
Student ID: 22073063
Module: 7PAM2000-0901-2023 - Applied Data Science 1
Course: Msc Data Science (SW) with Placement Year
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#creating the function to represent Bar Graph
def barChart(df):
    """
    Parameters
    ----------
    df : dataframe collected which is passeed argument from the main function
    position: It assigns the position for every year in the bar chart

    Returns
    -------
    The function plots the bar graph with all provided inputs it represents the rate of total crimes,
    violent crimes, Property crimes.

    """
    
    plt.figure()
    
    # Set Bar values and positions
    width = 0.45
    positions = np.arange(len(df['Year']))

    # Plot the Bar graph for total number of cases
    plt.bar(positions - width/3, df['Total'], width=width, label='Total Crimes', color='blue')
    
    # Plot the bar graph over the above graph which represents total deaths among the total cases
    plt.bar(positions + width/3, df['Property'], width=width, label='Property Crimes', color='Green')
    
    # Plot the bar graph over the above graph which represents total deaths among the total cases
    plt.bar(positions + width/3 + width/3, df['Violent'], width=width, label='Violent Crimes', color='Red')
    
    # Label the plot for X and Y axes
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.title('Bar Graph representation for Total number of Crimes to Property crimes and violent crimes')
    plt.xticks(positions, df['Year'])
    plt.legend()
    
    # Display the Graph
    plt.show()
    
def pieChar(df):
    """
    Parameters
    ----------
    df : This is the parsed dataframe argument from the main function
    
    fig,axs : creating subplot with grid of 1x3 format
    years: considering the years 1960, 1980, 2000
    
    Returns
    -------
    The function plots the pie charts among various categories of crime over the years.

    """
    fig, axs = plt.subplots(1, 3, figsize=(10, 4))
    # Loop over years and create pie charts
    years = [1960,1980,2000]
    for i, year in enumerate(years):
        try:
            data = df[df['Year'] == year][['Murder', 'Robbery', 'Forcible_Rape', 'Aggravated_assault', 'Vehicle_Theft', 'Burglary']].values.tolist()
            labels = ['Murder', 'Robbery', 'Forcible Rape', 'Aggravated Assault', 'Vehicle Theft', 'Burglary']
            axs[i].pie(data[0], explode=[0, 0, 0, 0, 0, 0], labels=labels, startangle=140, pctdistance=0.85)
            axs[i].set_title(year)
        except Exception as e:
            print(f"Error plotting pie chart for {year}: {e}")

    # Display the Total cases value which is sum of Active Cases + Recovered + Total Deaths
   # plt.legend()
    # Display the graph
    plt.tight_layout()
    plt.show()
    
def lineChart(df):
    """
    Parameters
    ----------
    df : This is the parsed argument dataframe from the main function
    
    years, murder,foricibleRape,Burglary: these the list of values based categories (represents of given name)
    
    Returns
    -------
    The function will plot the line chart based on the parse graph. It plots 4 line graphs in single plot
    """
    
    plt.figure()
    
    #assigning values for the mentioned variables for using them as parsed values for plotting the graph
    
    years = df['Year']
    murder = df['Murder']
    forcibleRape = df['Forcible_Rape']
    Burglary = df['Burglary']
    vehicleTheft = df['Vehicle_Theft']
    
    #plotting the graph
    plt.plot(years, murder, label='Murder')
    plt.plot(years, forcibleRape,label='Forcible Rape')
    plt.plot(years,Burglary,label='Burglary')
    plt.plot(years,vehicleTheft,label='Vehicle Theft')
    
    #displaying the labels
    plt.legend()
    plt.show()


# Main Function
# Reading the CSV file using pandas
dataframe = pd.read_csv("US_Crime_Rates_1960_2014.csv")

# Filtering data with range of 10 years
Year = [1960,1970, 1980,1990, 2000,2010]
dataframe = dataframe[dataframe['Year'].isin(Year)]

#calling the functions for plotting the graphs
barChart(dataframe)
pieChar(dataframe)
lineChart(dataframe)
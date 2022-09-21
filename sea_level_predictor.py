import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    df.plot.scatter(x='Year',y='CSIRO Adjusted Sea Level', ylabel = 'Sea Level (inches)', title = 'Rise in Sea Level')
    # Create first line of best fit
    year = pd.Series([1880+x for x in range(0,2050-1880+1)])
    res = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(year, res.intercept + res.slope*year)
    #plt.axline((1880, res.intercept + res.slope*1880),(2050,res.intercept + res.slope*2050))
    # Create second line of best fit
    newyear = pd.Series([2000+x for x in range(0,2050-2000+1)])
    newdf = df.loc[df['Year']>=2000]
    newres = linregress(newdf['Year'],newdf['CSIRO Adjusted Sea Level'])
    plt.plot(newyear, newres.intercept + newres.slope*newyear)
    #plt.axline((1880, newres.intercept + newres.slope*1880),(2050,newres.intercept + newres.slope*2050))
    # Add labels and title
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
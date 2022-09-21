import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col = 'date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    plt.clf()
    plt.cla()
    fig = plt.figure(figsize=(10,5))
    plt.plot(df)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.index = pd.to_datetime(df_bar.index)
    df_bar = df_bar.groupby([df_bar.index.year, df_bar.index.month]).mean()
    df_bar.index = df_bar.index.rename(['Years','Months'])
    df_bar = df_bar.rename(columns={'value':'Average Page Views'})
    df_bar = df_bar.reset_index()
    df_bar=df_bar.sort_values(by=['Months'])
    df_bar['Months'] = pd.to_datetime(df_bar['Months'], format='%m').dt.month_name()
  # Draw bar plot
    
    plt.clf()
    plt.cla()
    plt.close()
    fig = sns.barplot(data=df_bar, x='Years', y='Average Page Views', hue = 'Months').get_figure()
    




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt.clf()
    plt.cla()
    plt.close()
    fig, axes = plt.subplots(1, 2, figsize=(15,5))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    sns.boxplot(ax=axes[0], data=df_box, x='year', y='value').set(
    xlabel='Year', ylabel = 'Page Views')
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value', order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']).set(
    xlabel='Month', ylabel = 'Page Views')
    




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

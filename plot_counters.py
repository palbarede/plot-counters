#!/usr/bin/env python3
#import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import sys
import re
import csv
# requested by pandas to avoids warnings
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from redress import redress
from renumber import renumber
from ScrollableWindow import ScrollableWindow

fname = sys.argv[1] # direct settings of fname on example for testing in ipyhton
#fname='av_des_Cigales.txt'
#fname='av_Jules_Cantini.txt'
#fname='res_Valvert.txt'
#fname='rua_das_Vinhas_pretas.txt'
#fname='rue_Jean_Martin.txt'
#fname='test_comment.txt'

########### default settings ############
# Warning: sep=' *\t' kills df.index.name.
separator='\t'
min_point_number_for_plot=3
verbose=False
plot=True
title=fname.replace('_',' ')
######### can be overridden in data file #############


if verbose:print("Reading", fname)

stream1=open(fname)
header=''
while True:
    line=stream1.readline()
    if re.match('end_of_python_code',line) or line=='':
        break
    header+=line

exec(header)

# next line that is not comment is plot structure
while True:
    line=stream1.readline()
    if not re.match('#',line) or line=='':
        break

if not(re.match('\s*\t',line)):
    sys.exit('Error: bad plot structure line.')

# one could also read into dataframe but this is not much simpler
plot_structure=list(map(int,re.sub("\s*\t","",line,1).split(sep=separator)))

# read the bulk of data
df = pd.read_csv(stream1, parse_dates=True, sep=separator, comment='#',index_col=0)

if len(plot_structure)!=len(df.columns):
    sys.exit('Error: plot structure does not match columns.')

# drop columns marked 0
    
plot_structure=dict(zip(df.columns, plot_structure))
columns_to_drop=list(map(lambda x:x[0],list(filter(lambda x:x[1]==0,plot_structure.items()))))

df=df.drop(columns_to_drop,axis=1)
# filter plot structure accordingly
# some subplot numbers may be missing thereafter
plot_structure=dict(filter(lambda x:x[1]!=0,plot_structure.items()))
    
# remove white space in labels
df.columns=df.columns.str.strip()
df.index.name=df.index.name.strip()

def redressnona(series):
    nona=series.dropna()
    series1=pd.Series(redress(list(nona.ravel())),index=nona.index)
    # /!\ duplicated indices in series break reindex
    return series1.reindex(series.index)

# 'apply' calls func twice on the first column/row to decide whether it can take a fast or slow code path (see pandas doc)
df=df.apply(redressnona,axis=0,raw=False)

# drop columns with too few points for interesting plot
plotQ = df.apply((lambda series: len(series.dropna()) >= min_point_number_for_plot), axis=0)
df = df.loc(axis=1)[[*plotQ]]
# filter plot structure accordingly
plot_structure=pd.Series(plot_structure).loc[[*plotQ]].sort_values()

# renumber plot_structure to avoid empty subplot
plot_structure.update(pd.Series(renumber(plot_structure.to_list()),index=plot_structure.index))

# exchange index and values or reverse as a relation
plot_structure=pd.Series(plot_structure.index,plot_structure.values)

if verbose:print(df)

# We are now ready to plot.

# df.plot(marker='o')
# df.eau.plot(marker='+', title='Eau mˆ3')
# df.loc[:,['chaud', 'froid']].plot(title='Thermique kWh',marker='+')
# df.loc[:,['HP', 'HC']].plot(title='Électrique kWh',marker='+')

# https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots
# pandas plot does not allow subplot => use matplotlib.



####### figure layout ################
if plot:
    subplot_number=plot_structure.index[-1]+1
    fig, axes = plt.subplots(subplot_number,sharex=True,figsize=(6,1+subplot_number*2))

    try:
        fig.suptitle('Consumed at '+title)
    except NameError: # default title from file name
        fig.suptitle('Consumed at '+fname)
    # rotate date labels to avoid overwriting
    fig.autofmt_xdate()
    # fig.tight_layout(pad=3)

#    plt.subplots_adjust(top=.93)

    plt.xlabel('date')
######## end of figure layout #########

def plot_list(df,subplot_index,to_plot_list:list):
    if type(to_plot_list)!=list:
        sys.exit('Error: to_plot must be list.')
    axes[subplot_index].fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    axes[subplot_index].grid(True)
    for to_plot in to_plot_list:
         axes[subplot_index].plot(df.index,df[to_plot],'+',label=to_plot)
    axes[subplot_index].legend()

#axes[subplot_index].set_title(to_plot)
#axes[subplot_index].xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1,4,7,10)))

# nothing special actually for a single plot
def plot1(df,subplot_index,to_plot:int):
    to_plot_list=[to_plot]
    plot_list(df,subplot_index,to_plot_list)

if verbose:
    print('---')

for subplot_index in range(subplot_number):
    # this returns string or series if result not unique
    if type(plot_structure.get(subplot_index))!=str:
        to_plot_list=list(plot_structure.get(subplot_index).values)
    else:
        to_plot_list=[plot_structure.get(subplot_index)]
    if verbose:
        print("subplot",subplot_index)
        print(to_plot_list)
    if plot:
        if len(to_plot_list)==1:
            # single plot
            plot1(df,subplot_index,to_plot_list[0])
        else:
            # mutiple plot
            plot_list(df,subplot_index,to_plot_list)
    if verbose:
        print('---')
    
if plot:
    ScrollableWindow(fig)
#    plt.show()

#sys.exit('stop')
#import ipdb;ipdb.set_trace()




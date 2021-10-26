# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:29:50 2020

@author: zamcr

This is a module of functions to create figures or plots with the DATA_PAR
structure in python


FRAKE for Anura3D
    Copyright (C) 2020  Luis E. Zambrano-Cruzatty

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%% PlotAll(DATA,x,y,style,xlabel,ylabel,xsize,ysize,mod)
#DATA: list structure containing the data
#IDs: IDs list structure
#xx: is the x header as string
#yy: is the y header as string
#style: is a style label will change the presentation of the figure
#xlabel: Optional x label
#ylabel: Optional y label
#xsize: Size in in x
#ysize: Size in in y
#mode: Type of plot
#Hold: 0 to plot and 1 to hold plot and add more features
#palete set color palete

def PlotAll(DATA, IDs, xx, yy, style='Paper', xlabel='default', ylabel='default', xsize=3, ysize=3, mode='-', hold=0 \
            , palete='Normal', legendMode=True, lims=[0,0,0,0,0], varst=0, PlotName='default', sample_span=1\
               , linewith=0, markers=0, makersize=0):
    
    if (xlabel=='default'):
        xlabel=xx
    if (ylabel=='default'):
        ylabel=yy
        #DEtermine the number of dataframes in list
    NIds=len(DATA)
    #Set color palete
    if (palete=='Normal'):
        Pt=sns.color_palette('husl')
    elif (palete=='VTANURA'):
        personalized_color=["#8b1f41", '#011627', '#ff6600', '#41ead4', '#808080', '#5f8297', '#000000']
        Pt=sns.color_palette(personalized_color)
    elif (palete=='HCONTRAST'):
        personalized_color=["#004488", '#BB5566', '#575757', '#DDAA33', '#000000', '#8A8A8A']
        Pt=sns.color_palette(personalized_color)        
    else:
        Pt=palete
        #sns.set_palette(Pt)



    # Select style

    if (style=='Paper'):
            SMALL_SIZE = 8
            MEDIUM_SIZE = 10
            BIGGER_SIZE = 12
            plt.rc('text', usetex=True)
            plt.rcParams['text.latex.preamble'] = [r'\usepackage{bm}']
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            if (linewith==0):
                lw=1
            else:
                lw=linewith

    elif (style=='Slide'):

            SMALL_SIZE = 14
            MEDIUM_SIZE = 16
            BIGGER_SIZE = 24
            plt.rc('text', usetex=True)
            plt.rcParams['text.latex.preamble'] = [r'\usepackage{bm}']
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            plt.rc('axes', linewidth=2)
            if (linewith==0):
                lw=3
            else:
                lw=linewith
    elif (style=='Paths'):
            SMALL_SIZE = 8
            MEDIUM_SIZE = 10
            BIGGER_SIZE = 12
            plt.rc('text', usetex=True)
            plt.rcParams['text.latex.preamble'] = [r'\usepackage{bm}']
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            if (linewith==0):
                lw=1
            else:
                lw=linewith
    elif (style=='Scatter'):
            SMALL_SIZE = 8
            MEDIUM_SIZE = 10
            BIGGER_SIZE = 12
            plt.rc('text', usetex=True)
            plt.rcParams['text.latex.preamble'] = [r'\usepackage{bm}']
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            if (linewith==0):
                lw=1
            else:
                lw=linewith


        #else:

    #Loop trough data
    a=0
    for Frame in DATA:
        a=a+1
        if (style=='Paths'):
            plt.plot(Frame[xx],Frame[yy], mode, label=IDs[a-1],linewidth=lw,color=palete)
        elif (style=='Scatter'):
            if (varst==0):
                sns.scatterplot(x=xx, y=yy, data= Frame ,marker= mode, color=Pt[a-1], label=IDs[a-1])
            else:
                if(varst[0]==0):
                    sns.scatterplot(x=xx, y=yy, data= Frame ,marker= mode, color=Pt[a-1], style= varst[1],\
                                 legend=False)
                else:
                    sns.scatterplot(x=xx, y=yy, data= Frame ,marker= mode, color=Pt[a-1], style= varst[1],\
                                hue= varst[0], legend=False)
        else:
            
            if (markers==0):
                aux_mode=mode
            else:                    
                aux_mode= '%s%s' %(mode, markers[a-1])
            if (PlotName=='default'):
 
                plt.plot(Frame[xx][::sample_span],Frame[yy][::sample_span], aux_mode, label=IDs[a-1],\
                         linewidth=lw,color=Pt[a-1])
            else:
                PlotName.plot(Frame[xx][::sample_span],Frame[yy][::sample_span], aux_mode, label=IDs[a-1],\
                              linewidth=lw,color=Pt[a-1])

    #plt.xlabel(xlabel)
    #plt.ylabel(ylabel)
    if (PlotName=='default'):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if (lims[4]==1):
            plt.ylim(lims[1])
            plt.xlim(lims[0])
            if (lims[2]==1):
                plt.gca().invert_xaxis()
            if (lims[3]==1):
                plt.gca().invert_yaxis()
        # # show a legend on the plot
        if (legendMode):
           plt.legend(edgecolor='k',fancybox=False, framealpha=1, shadow=False, borderpad=1)
        if (hold==0):
            plt.show()
    else:
        PlotName.set_xlabel(xlabel)
        PlotName.set_ylabel(ylabel)
        if (lims[4]==1):
            PlotName.set_ylim(lims[1])
            PlotName.set_xlim(lims[0])
            if (lims[2]==1):
                PlotName.invert_xaxis()
            if (lims[3]==1):
                PlotName.invert_yaxis()
        # # show a legend on the plot
        if (legendMode):
           PlotName.legend(edgecolor='k',fancybox=False, framealpha=1, shadow=False, borderpad=1)
        if (hold==0):
           PlotName.show()

#     # naming the x axis
# plt.xlabel('x [km]')
# plt.xlim(0,50)
# # naming the y axis
#
# plt.ylim(0,0.12)


# # Show grid
# plt.grid()

#%% Individial plot
def PlotID(DATA, IDs, ID, xx, yy, style='Paper', xlabel='default', ylabel='default', xsize=3, ysize=3, mode='-', \
           hold=0, palete='Normal', legendMode=True, PlotName='default'):
            #DEtermine the number of dataframes in list
            
    if (xlabel=='default'):
        xlabel=xx
    if (ylabel=='default'):
        ylabel=yy
    NIds=1
    #Set color palete
    if (palete=='Normal'):
        Pt=sns.color_palette('husl')
    elif (palete=='VTANURA'):
        personalized_color=["#8b1f41", '#011627', '#ff6600', '#41ead4', '#808080', '#5f8297', '#000000']
        Pt=sns.color_palette(personalized_color)
    elif (palete=='HCONTRAST'):
        personalized_color=["#004488", '#BB5566', '#575757', '#DDAA33', '#000000', '#8A8A8A']
        Pt=sns.color_palette(personalized_color)     
    else:
        Pt=sns.light_palette(sns.xkcd_rgb[palete],NIds+1,reverse=True)
        #sns.set_palette(Pt)



    # Select style
    if (style=='Paper'):
            SMALL_SIZE = 8
            MEDIUM_SIZE = 10
            BIGGER_SIZE = 12
            plt.rc('text', usetex=True)
            plt.rcParams['text.latex.preamble'] = [r'\usepackage{bm}']
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            lw=1

    elif (style=='Slide'):

            SMALL_SIZE = 14
            MEDIUM_SIZE = 16
            BIGGER_SIZE = 24
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
            plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
            plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
            plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
            plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
            plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
            plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
            plt.rcParams['figure.dpi'] = 400
            plt.rcParams["figure.figsize"] = (xsize,ysize)
            lw=2
        #else:

    #Loop trough data

    if (isinstance(ID,str)): #Id is string
        a=0
        for Frame in DATA:
            a=a+1
            if (ID==IDs[a-1]):
                if (PlotName=='default'):
                    plt.plot(Frame[xx],Frame[yy], mode, \
                             label=IDs[a-1],linewidth=lw, color=Pt[0])
                else:
                    PlotName.plot(Frame[xx],Frame[yy], mode, \
                             label=IDs[a-1],linewidth=lw, color=Pt[0])
                            
                break
    else:
        if (PlotName=='default'):
            plt.plot(DATA[ID][xx],DATA[ID][yy], mode , label=IDs[ID]\
                     ,linewidth=lw, color=Pt[0])
        else:
            PlotName.plot(DATA[ID][xx],DATA[ID][yy], mode , label=IDs[ID]\
                     ,linewidth=lw, color=Pt[0])

    if (PlotName=='default'):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        # # show a legend on the plot
        if (legendMode==True):
            plt.legend(edgecolor='k',fancybox=False, framealpha=1, shadow=False, \
                       borderpad=1)
    
    
        if (hold==0):
            plt.show()
    else:
        PlotName.set_xlabel(xlabel)
        PlotName.set_ylabel(ylabel)
        # # show a legend on the plot
        if (legendMode==True):
            PlotName.legend(edgecolor='k',fancybox=False, framealpha=1, shadow=False, \
                       borderpad=1)
    
    
        if (hold==0):
            PlotName.show()

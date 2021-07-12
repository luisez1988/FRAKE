# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:45:24 2020

@author: zamcr
This script contains the functions for obtaining samples of the DATA structures


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
from scipy import interpolate 
import pandas as pd
#%% GetInterpolatedData
#DATA is the DATAPar structure
#xx, is the string containing the x domain of sampling
#yy, is the targeted yy to be interpolated
#tipo: defines what input is given:
#tipo: 'vector', user provides a sampling vector
#tipo= 'range' user inputs range and number of points
#samplex: is the sampling vector if tipo is vector ot the range if tipo is ran
#N: number of points in sampling, 0 if tipo=vector
#mode: is the interpolation type
#mode: a string containing the interpolation tipe: 'linear', 'quad', 'cub'..
#tsingle: 1 if only for a single ID, or 0 if for all the IDs
#ID: ID string
#IDlist: Contains the ID identifiers
#Returns the SampleData in vector

def GetInterpolatedData(DATA,xx,yy,samplex,IDlist,tipo='range',N=1,mode='linear'\
                        ,tsingle=0,ID=0):
    if (tsingle==1):#Single ID
        #Have to get index position from IDlist
        IsThere=ismember(IDlist,ID)
        i=0
        for t in IsThere:
            i=i+1
            if (t==1):
                break
        subdata=DATA[i-1]
        xd=subdata[xx]
        xd=xd.dropna()
        yd=subdata[yy]
        yd=yd.dropna()
        if (tipo=='vector'):#Vector input
            if (mode=='linear'):
                SampledData=np.interp(samplex,xd,yd)
            elif (mode=='quad'):
                func=interpolate.interp1d(xd,yd,\
                                          kind='quadratic')
                SampledData=func(samplex)
            elif (mode=='cub'):                
                func=interpolate.interp1d(xd,yd,\
                                          kind='cubic')
                SampledData=func(samplex)
        elif(tipo=='range'):#range input
            samplex=np.linspace(samplex[0],samplex[1],N)
            if (mode=='linear'):                
                SampledData=np.interp(samplex,xd,yd)
            elif (mode=='quad'):                
                func=interpolate.interp1d(xd,yd,\
                                          kind='quadratic')
                SampledData=func(samplex)
            elif (mode=='cub'):                
                func=interpolate.interp1d(xd,yd,\
                                          kind='cubic')
                SampledData=func(samplex)
    else:# All IDs
        i=0
        for Frame in DATA:#loop trough the data sets
            i=i+1
            if (tipo=='vector'):#Vector input
                if (mode=='linear'):
                    if (i==1):
                        SampledData=[np.interp(samplex,Frame[xx],Frame[yy])]
                    else:
                        aux=np.interp(samplex,Frame[xx],Frame[yy])
                        SampledData.append(aux)
                elif (mode=='quad'):
                    if (i==1):
                        aux=Frame.dropna()
                        func=interpolate.interp1d(aux[xx],aux[yy],\
                                              kind='quadratic')
                        SampledData=[func(samplex)]
                    else:
                        aux=Frame.dropna()
                        func=interpolate.interp1d(aux[xx],aux[yy],\
                                              kind='quadratic')
                        aux=func(samplex)
                        SampledData.append(aux)                            
                    
                elif (mode=='cub'):
                    if (i==1):
                        aux=Frame.dropna()
                        func=interpolate.interp1d(aux[xx],aux[yy],\
                                              kind='cubic')
                        SampledData=[func(samplex)]
                    else:
                        aux=Frame.dropna()
                        func=interpolate.interp1d(aux[xx],aux[yy],\
                                              kind='cubic')
                        aux=func(samplex)
                        SampledData.append(aux)  
            elif(tipo=='range'):#range input
                samplex=np.linspace(Frame[0],Frame[1],N)
                if (mode=='linear'):
                    if (i==1):
                        SampledData=np.interp(samplex,Frame[xx],Frame[yy])
                    else:
                        aux=np.interp(samplex,Frame[xx],Frame[yy])
                        SampledData.append(aux)
                elif (mode=='quad'):
                    if (i==1):
                        func=interpolate.interp1d(Frame[xx],Frame[yy],\
                                              kind='quadratic')
                        SampledData=func(samplex)
                    else:
                        func=interpolate.interp1d(Frame[xx],Frame[yy],\
                                              kind='quadratic')
                        aux=func(samplex)
                        SampledData.append(aux)                            
                    
                elif (mode=='cub'):
                    if (i==1):
                        func=interpolate.interp1d(Frame[xx],Frame[yy],\
                                              kind='cubic')
                        SampledData=func(samplex)
                    else:
                        func=interpolate.interp1d(Frame[xx],Frame[yy],\
                                              kind='cubic')
                        aux=func(samplex)
                        SampledData.append(aux)            

    return SampledData

#%% imember function
def ismember(A, B):
    return [ np.sum(a == B) for a in A ]

#%% Singled value function
    
    
def GetSingleValue(DATA,stat,var, IDlist,tsingle=0, ID=0):
    if (tsingle==1):
        #Have to get index position from IDlist
        IsThere=ismember(IDlist,ID)
        i=0
        for t in IsThere:
            i=i+1
            if (t==1):
                break
        subdata=DATA[i-1][var]
        if (stat=='max'):
            SingleValue=np.amax(subdata)
            j=subdata.idxmax()
        elif(stat=='min'):
            SingleValue=np.amin(subdata)
            j=subdata.idxmin()
    else:
        i=0
        for Frame in DATA:
            i=i+1
            IDlab=IDlist[i-1]
            [aux,ja]=GetSingleValue(DATA,stat,var, IDlist,tsingle=1,ID=IDlab)
            
            if (i==1):
                SingleValue=[aux]
                j=[ja]
            else:
                SingleValue.append(aux)
                j.append(ja)
                
    return SingleValue, j
    
#%% Singled indexed data

def GetSingleIndexed(DATA, IndexList ,var,tsingle,ID,IDlist):
    if (tsingle==1):
        #Have to get index position from IDlist
        IsThere=ismember(IDlist,ID)
        i=0
        for t in IsThere:
            i=i+1
            if (t==1):
                break
        subdata=DATA[i-1][var]
        SingleValue=subdata[IndexList]
    else:
        i=0
        for Frame in DATA:
            i=i+1
            IDlab=IDlist[i-1]
            aux=GetSingleIndexed(DATA,IndexList[i-1],var,1,IDlab,IDlist)
            
            if (i==1):
                SingleValue=[aux]
            else:
                SingleValue.append(aux)
                
    return SingleValue

#%% Split single Frame with criteria.

def SplitWithCriteria(DATA, Criteria, val, var, ID, IDlist):
    IsThere=ismember(IDlist,ID)
    i=0
    for t in IsThere:
        i=i+1
        if (t==1):
            break
    subdata=DATA[i-1]
    if (Criteria=='>'):
        c=subdata[var]>val
        Retrieved_Data=subdata[c]
    elif (Criteria=='<'):
        c=subdata[var]<val
        Retrieved_Data=subdata[c]
    elif (Criteria=='<<'):
        c=subdata[var]>val[0]
        Retrieved_Data=subdata[c]
        c=Retrieved_Data[var]<val[1]
        Retrieved_Data=Retrieved_Data[c]
    elif (Criteria=='='):
        c=subdata[var]==val
        Retrieved_Data=subdata[c]
    return Retrieved_Data

#%% Get a vector of all data
def GetAllinVector(DATA, var):
    Result=[]
    for frame in DATA:
        Aux=frame[var]
        Aux=Aux.to_numpy(dtype ='float32')
        Result.append(Aux)
    #Result=np.array(Result)
    #Result=Result.T
    return Result


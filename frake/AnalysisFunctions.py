# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:50:55 2020

@author: zamcr
This module contains functions to analyse the data


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
import pandas as pd
import SamplingFunctions as Sf
import scipy.optimize as optimization
from lmfit import Model
#%% LSF fit to functions
#DATA= Data structure list
#IDs= contains a label of what each dataframe in DATA is
#ID= specific ID on which to perform the fit
#mode= True if all data is combined togheter
#False otherwise
#tsingle= True for single ID
#function= a previously defined function to fit
#varList= a list of variable strings
#coefguess= Initial testing guess
def LSQFit(DATA, IDs, function, x0,  varList, tsingle=0, mode=True, ID=0\
           ,ExtraArg=False, ExtraArgList=0, FixVar=False, VarFixedList=0):
    if mode:
        #Have to create a vector of all DATA
        Y=Sf.GetAllinVector(DATA, varList[0])
        n=len(varList)        
        for i in range(1,n):
            if (i==1):
                X=Sf.GetAllinVector(DATA, varList[i])
            else:
                X=np.append(X, Sf.GetAllinVector(DATA, varList[i]))
        Result=optimization.curve_fit(function, X, Y, x0)
        xf=Result[0]
        R2=(Result[1][0][1]/(np.sqrt(Result[1][0][0]*Result[1][1][1])))**2
        
        args=xf
        y_ihat=function(X, *args)
        y_bar=np.mean(Y)
        SSTi=(Y - y_bar)**2
        SSRegi=(y_ihat - y_bar)**2
        SST = sum(SSTi)
        SSReg = sum(SSRegi)
        Rsquared = SSReg/SST
        Result=[xf, R2, Rsquared]
    else:#Data is analysed independently
        if tsingle==1: #For a single ID
            #Have to get index position from IDlist
            IsThere=Sf.ismember(IDs,ID)
            p=0
            for t in IsThere:
                p=p+1
                if (t==1):
                    break
            if ExtraArg==False:                     
                 Y=DATA[p][ varList[0]]        
                 a=0
                 for i in range(len(varList)):
                    a=a+1
                    if (i==0):
                        X=DATA[p][varList[i]]
                    else:
                        X=np.vstack((X, DATA[p][varList[i]]))
                        
                 X=X.T       
                 Result=optimization.curve_fit(function, X, Y, x0)
                 xf=Result[0]
                 R2=(Result[1][0][1]/(np.sqrt(Result[1][0][0]*Result[1][1][1])))**2
                 
                 args=xf
                 y_ihat=function(X, *args)
                 y_bar=np.mean(Y)
                 SSTi=(Y - y_bar)**2
                 SSRegi=(y_ihat - y_bar)**2
                 SST = sum(SSTi)
                 SSReg = sum(SSRegi)
                 Rsquared = SSReg/SST
                 Result=[xf, R2, Rsquared]
            else: #Pass arguments as some fitting and fixed parameters
                Y=DATA[t][ varList[0]]
                n=len(varList) 
                for j in range(len(varList)):
                    if (j==0):
                        X=DATA[t][varList[j]]
                    else:
                        X=np.append(DATA[t][ varList[j]])  
                mymodel=Model(function)
                n=len(ExtraArgList)
                t=len(x0)
                k=0
                for j in range((t-n), t):
                    x0[j]=DATA[t][ExtraArgList[k]][0]
                    k=k+1
                x0=mymodel.make_params()
                if FixVar:
                    for j in range(len(VarFixedList)):
                        x0[VarFixedList[j]].vary=False
                Result=mymodel.fit(Y, x0, x=X)                        
        
    return Result


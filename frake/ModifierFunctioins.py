# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 09:36:38 2020

@author: zamcr
Set of functions to operate or modify the DATA PAR


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
import math as mt
import SamplingFunctions as sp
from scipy.signal import savgol_filter
#%% Operation function.
#DATA: DATA_PAR structure
#Oper: is an string defining the operation to be performed
#var1: Is a string containing the col name which is ibject of the operation
#var2: Is a string containing the name of a value operatin on var1 or a single
#value, can be empty depending on the operation
#colname: Is a string containing the name of the new column
def DataOperation(DATA,Oper, var1, var2, colname):
    #Loop trough data
    for frame in DATA:
        if (Oper=='+'):
            if (isinstance(var2,str)):#Operation between columns
                aux=frame[var1]+frame[var2]
                frame[colname]=aux
            else: #var2 is a number
                aux=frame[var1]+var2                    
                frame[colname]=aux    
        elif(Oper=='-'):
            if (isinstance(var2,str)):#Operation between columns
                aux=frame[var1]-frame[var2]
                frame[colname]=aux
            else: #var2 is a number
                aux=frame[var1]-var2 
                frame[colname]=aux
        elif(Oper=='*'):
            if (isinstance(var2,str)):#Operation between columns
                aux=frame[var1]*frame[var2]
                frame[colname]=aux
            else: #var2 is a number
                aux=frame[var1]*var2 
                frame[colname]=aux
        elif(Oper=='/'):
            if (isinstance(var2,str)):#Operation between columns
                aux=frame[var1]/frame[var2]
                frame[colname]=aux
            else: #var2 is a number
                aux=frame[var1]/var2 
                frame[colname]=aux
        elif(Oper=='^'):
            if (isinstance(var2,str)):#Operation between columns
                aux=frame[var1]**frame[var2]
                frame[colname]=aux
            else: #var2 is a number
                aux=frame[var1]**var2 
                frame[colname]=aux
        elif(Oper=='ln'):            
            aux=np.log(frame[var1])
            frame[colname]=aux

        elif(Oper=='log'):
            aux=np.log10(frame[var1])
            frame[colname]=aux
            
        elif(Oper=='logbx'):            
            if (isinstance(var2,str)):#Operation between columns
                aux=np.log(frame[var1])/np.log(frame[var2])
                frame[colname]=aux
            else: #var2 is a number
                aux=np.log(frame[var1])/np.log(var2) 
                frame[colname]=aux
        elif(Oper=='exp'):
            aux=np.exp(frame[var1])
            frame[colname]=aux
        elif(Oper=='sin'):
            aux=np.sin(frame[var1])
            frame[colname]=aux
        elif (Oper=='sindeg'):
            aux=np.sin(frame[var1]*mt.pi/180)
            frame[colname]=aux
        elif(Oper=='cos'):
            aux=np.cos(frame[var1])
            frame[colname]=aux
        elif(Oper=='cosdeg'):   
            aux=np.cos(frame[var1]*mt.pi/180)
            frame[colname]=aux
        elif(Oper=='tan'):
            aux=np.tan(frame[var1])
            frame[colname]=aux
        elif(Oper=='tandeg'):
            aux=np.tan(frame[var1]*mt.pi/180)
            frame[colname]=aux
        elif (Oper=='asin'):
            aux=np.arcsin(frame[var1])
            frame[colname]=aux
        elif (Oper=='asindeg'):
            aux=np.arcsin(frame[var1])*180/mt.pi
            frame[colname]=aux
        elif (Oper=='acos'):
            aux=np.arccos(frame[var1])
            frame[colname]=aux
        elif (Oper=='acosdeg'):
            aux=np.arccos(frame[var1])*180/mt.pi
            frame[colname]=aux
        elif (Oper=='atan'):
            aux=np.arctan(frame[var1])
            frame[colname]=aux
        elif (Oper=='atandeg'):
            aux=np.arctan(frame[var1])*180/mt.pi
            frame[colname]=aux
        elif (Oper=='='):
            if (isinstance(var1,str)):#Operation between columns
                aux=frame[var1]
                frame[colname]=aux
            else: #var1 is a number
                aux=np.ones(len(frame))*var1 
                #frame.assign(colname=[aux])                   
                frame[colname]=aux 
        elif (Oper=='max'):
            aux=np.ones(len(frame))*max(frame[var1])
            frame[colname]=aux
        elif (Oper=='min'):
            aux=np.ones(len(frame))*min(frame[var1])
            frame[colname]=aux
        else:
            if (isinstance(var2,str)): #Operation between columns
                aux=Oper(frame[var1], frame[var2])
                frame[colname]=aux
            else:
                aux=Oper(frame[var1], var2)
                frame[colname]=aux
            
            
#%% Smooth Function
#Function to smooth the data around var 1, var2 is optional
#Colname is the new name for the column
# deg: Degree
# span: window of smoothness

            
def SmoothData(DATA, var1, colname, deg, span):
    # Get the id position of ID    
    for Dat in DATA:
        subdata=Dat[var1]
        aux=savgol_filter(subdata, span, deg)
        Dat[colname]=aux
        
#%% Derivative function
#Function to obtain the numerical derivative of var1 with respect to var2
#DATA is the data structure
#mode: 'F' for forward, 'B' for backwards, 'C' for centered
#span: If mode is C, the centered can be spanned 
#Column where the data is to be saved
        
def Derivative(DATA, var1, var2, mode, span, colname):
    for frame in DATA:
        if (mode=='F'):#Forward difference
            n=len(frame)
            aux=np.zeros(n)          
            for i in range(1,n):
                aux[i-1]=(frame[var1][i]-frame[var1][i-1])/(frame[var2][i]\
                                                          -frame[var2][i-1])
            aux[n-1]=aux[n-2]
            
            frame[colname]=aux
        elif(mode=='B'):
            n=len(frame)
            aux=np.zeros(n)            
            for i in range(1,n):
                aux[i]=(frame[var1][i]-frame[var1][i-1])/(frame[var2][i]\
                                                          -frame[var2][i-1])
            frame[colname]=aux
        elif(mode=='C'):
            n=len(frame)
            aux=np.zeros(n)
            for i in range(1,span+1):
                aux[i-1]=(frame[var1][i]-frame[var1][i-1])/(frame[var2][i]\
                                                          -frame[var2][i-1])                
            for i in range((span+1),(n-span+1)):
                aux[i-1]=(frame[var1][i+span-1]-frame[var1][i-span-1])/(frame[var2][i+span-1]\
                                                          -frame[var2][i-span-1])
            for i in range((n-span+1),n+1):
                aux[i-1]=(frame[var1][i-1]-frame[var1][i-2])/(frame[var2][i-1]\
                                                        -frame[var2][i-2])
        elif(mode=='S'):
            n=len(frame)
            aux=np.zeros(n)
            for i in range(2, n):
                aux[i-1]=(frame[var1][i-2]-2*frame[var1][i-1]+frame[var1][i])/(frame[var2][i-1]-frame[var2][i-2])**2
                

                
        frame[colname]=aux

#%% Delete complement function
#Vars: Is a list of the variables that will remain in the data strc
def DeleteComplement(DATA, Vars):
    if (isinstance(Vars[1],str)): #String variables
        for frame in DATA:
            n=len(Vars)
            for col in frame.columns:
                Save=False
                for i in range(1,n+1):                
                    if (col==Vars[i-1]):
                        Save=True                   
                        break
                if (Save==False):
                    frame.drop(labels=col, axis=1, inplace=True)
    else:
        for frame in DATA:
            n=len(Vars)
            a=0
            for col in frame.columns:
                a=a+1
                Save=False
                for i in range(1,n+1):                   
                    if (a-1==Vars[i-1]):
                        Save=True
                        break
                if (Save==False):
                    frame.drop(labels=col, axis=1, inplace=True)
                    
#%% Second derivative function
#Second Derivative of Var1 with respect to Var2
#Colname: Name to store the derivative
#deg: order 1 or 2 only


def SDerivative(DATA, var1, var2, colname):
    for frame in DATA:
         n=len(frame)
         aux=np.zeros(n)
         for i in range(1,n+1):
             if (i==1):
                 # d1=frame[var1][i]-frame[var1][i-1]/(frame[var2][i]\
                 #                               -frame[var2][i-1])
                 # d2=frame[var1][i+1]-frame[var1][i]/(frame[var2][i+1]\
                 #                               -frame[var2][i])
                 aux[i-1]=0
             elif(i==n):
                 # d1=frame[var1][i-1]-frame[var1][i-2]/(frame[var2][i-1]\
                 #                               -frame[var2][i-2])
                 # d2=frame[var1][i-2]-frame[var1][i-3]/(frame[var2][i-2]\
                 #                               -frame[var2][i-3])
                 aux[i-1]=0
             else:
                 aux[i-1]=(frame[var1][i-2]-2*frame[var1][i-1]+frame[var1][i])/\
                 (frame[var2][i]-frame[var2][i-2])**2
     
         frame[colname]=aux

            
                      
#%% ID modifier.
#DATA: DATA_PAR structure
#Oper: is an string defining the operation to be performed
#var1: Is a string containing the col name which is ibject of the operation
#var2: Is a string containing the name of a value operatin on var1 or a single
#value, can be empty depending on the operation
#colname: Is a string containing the name of the new column
def IDModifier(DATA, ID ,IDs,Oper, var1, var2):
    #Loop trough data
    if (isinstance(ID,str)): #Id is string
        a=0
        for Frame in DATA:
            a=a+1
            if (ID==IDs[a-1]):
                break
    else:
        a=ID
        
    if (Oper=='='):
        if (isinstance(var2,str)):#Operation between columns
            DATA[a][var1]=DATA[a][var2]
        else: #var2 is a number
            aux=np.ones(len(DATA[a]))*var2
            DATA[a][var1]=aux

            
                
                    

                
                
        
        
    

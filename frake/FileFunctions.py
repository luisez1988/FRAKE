# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:44:58 2020

@author: zamcr

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


import tkinter.filedialog as TK
from tkinter import *
import os.path
import scipy.io as sio
import numpy as np
import pandas as pd
import re


numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

#%% Opening the files
def OpenFromFolder(Path='', filetype='csv', auto_mode=True):
    if (Path==''): #Default case
        FolderName=TK.askdirectory() #promt user to get a folder  
    else: # User writes path
        FolderName=Path
    
    #Create a cell array for future structures
    a=0
    
    #loop trough files
    for filename in sorted(os.listdir(FolderName), key=numericalSort):
        if (filetype=='csv'):
            if filename.endswith(".csv"):
                a=a+1        
                FullName="{}/{}".format(FolderName, filename) 
                data = pd.read_csv(FullName)    
                prompt="ID for input# {} : ".format(filename)
                if (auto_mode):
                    label= str(a)
                else:
                    label=input(prompt)
                    
                if (a==1) :
                    DATA_PAR=[data]
                    ID_list=[label]
                else:
                    DATA_PAR.append(data)
                    ID_list.append(label)            
                continue
        elif (filetype=='txt'): #txt file
            if filename.endswith(".txt"):
                a=a+1        
                FullName="{}/{}".format(FolderName, filename) 
                data = pd.read_csv(FullName, sep='\s+')    
                prompt="ID for input# {} : ".format(filename)
                
                if (auto_mode):
                    label= str(a)
                else:
                    label=input(prompt)
                    
                if (a==1) :
                    DATA_PAR=[data]
                    ID_list=[label]
                else:
                    DATA_PAR.append(data)
                    ID_list.append(label)            
                continue
        continue
    
    return DATA_PAR, ID_list, FolderName;

def OpenSingleFile(filetype='csv', fullpath='default'):
    if (fullpath=='default'):
        if (filetype=='csv'):
            FileName=TK.askopenfilename(initialdir = "/",title = "Select file",filetypes\
                                        = (("csv files","*.csv"),("all files","*.*")))
            data = pd.read_csv(FileName) 
            prompt="ID for input# {} : ".format(FileName)
            label=input(prompt)
            DATA_PAR=[data]
            ID_list=[label]
        elif (filetype=='txt'):
            FileName=TK.askopenfilename(initialdir = "/",title = "Select file",filetypes\
                                        = (("txt files","*.txt"),("all files","*.*")))
            data = pd.read_csv(FileName, sep='\s+')
            prompt="ID for input# {} : ".format(FileName)
            label=input(prompt)
            DATA_PAR=[data]
            ID_list=[label]            
    else:
        if (filetype=='csv'):
            data = pd.read_csv(fullpath) 
            prompt="ID for input# {} : ".format(fullpath)
            label=input(prompt)
            DATA_PAR=[data]
            ID_list=[label]
            FileName=fullpath
        elif (filetype=='txt'):
            data = pd.read_csv(fullpath, sep='\s+')
            prompt="ID for input# {} : ".format(fullpath)
            label=input(prompt)
            DATA_PAR=[data]
            ID_list=[label]
            FileName=fullpath
        
    return DATA_PAR, ID_list, FileName;
    
    
        

#%% Exporting to csv files

def SaveasCsv(Data, IDs):
    FolderName=TK.askdirectory() #promt user to get a folder
    i=0
    for frame in Data:
        i=i+1
        Path="%s\%s.csv" % (FolderName, IDs[i-1])
        frame.to_csv(Path, index= False)



    

       
 

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:18:42 2020

@author: zamcr
Functions to open, analyse, and graph data from results obtained using ANURA 3D

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
#%% Supporting libraries
import tkinter.filedialog as TK
import pandas as pd
import SamplingFunctions as SF
import GraphFunctions as GF
import ModifierFunctioins as MF
import numpy as np
import os
#%% Definition of the ANURA3D class
class Anura3D:
    def __init__(self, project, path, FileList, IDs, DATA):
        self.project=project
        self.path=path
        self.FileList=FileList
        self.IDs=IDs
        self.DATA=DATA
        
        
#%% Open Models function
#This function allows python to know the folder containing a set of results from
#a model. Typically an .A3D folder
#IsMultiple= boolean. True for analysisng multiple models results, false for a
#single model analysis.
#Import: IF 'entire' then it will import all the data files into python
#        if 'single' it will import only one file which number or name is the ID
#GetNames: 'automatic' will assign a name base on the file name and point number
#          'manual' will promt the user to add a name
# Returns a list containing all the PAR and SRF files on the folder
def OpenModels(IsMultiple=False, Import='entire', ID=0, GetNames='automatic'):
    ThereAreFiles=False
    if IsMultiple: #For more than a single folder results
        Results=['nada']
    else: #For a single results only
        FolderName=TK.askdirectory() #promt user to get a folder  
        FileList=[] #Output list to be filled
        for filename in os.listdir(FolderName): #Loop the files on the project
            NameSplit=os.path.splitext(filename)
            check=NameSplit[1].split('_')[0]
            if (check=='.PAR'):
                Aux=[filename, 'Particle']
                FileList.append(Aux)
                ThereAreFiles=True
            elif (check=='.SRF'):
                Aux=[filename, 'Surface']
                FileList.append(Aux)
                ThereAreFiles=True
        if not(ThereAreFiles):
            FileList=['No-Results']
        if (FileList[0]=='No-Results'): #case of no PAR or SRF files in project
            ID_list=['No-Results']
            DATA_PAR=['No_Results']
        else:# There are some PAR or SRF files in folder
            a=0
            if (Import=='entire'):
                for i in FileList: #Loop Filelists an import files
                    a=a+1 
                    FullName="{}/{}".format(FolderName, i[0])
                    data = pd.read_table(FullName, sep='\s+')
                    if (a==1) :
                            DATA_PAR=[data]
                    else:
                            DATA_PAR.append(data) 
                    if (GetNames=='manual'):
                        prompt="ID for file {} : ".format(filename)
                        label=input(prompt)
                        if (a==1) :
                            ID_list=[label]
                        else:
                            ID_list.append(label) 
                    elif (GetNames=='automatic'):
                        label=i[0].split('_')
                        label=label[len(label)-1]
                        if (a==1):
                            ID_list=[label]
                        else:
                            ID_list.append(label) 
                    else:
                        label=str(a)
                        if (a==1):
                            ID_list=[label]
                        else:
                            ID_list.append(label)
            elif (Import=='single'):
                if (isinstance(ID,str)):#ID is entered as string
                    FullName="{}/{}".format(FolderName, ID)
                    data = pd.read_table(FullName, sep='\s+')
                    DATA_PAR=[data]
                    if (GetNames=='manual'):
                        prompt="ID for file {} : ".format(ID)
                        label=input(prompt)
                        ID_list=[label]
                    elif (GetNames=='automatic'):
                        label=ID.split('_')
                        label=label[len(label)-1]
                        ID_list=[label]
                    else:
                        label=str(1)
                        ID_list=[label]
               
                else:# ID is a number
                    FullName="{}/{}".format(FolderName, FileList[ID])
                    data = pd.read_table(FullName, sep='\s+')
                    DATA_PAR=[data]
                    if (GetNames=='manual'):
                        prompt="ID for file {} : ".format(FileList[ID])
                        label=input(prompt)
                        ID_list=[label]
                    elif (GetNames=='automatic'):
                        label=FileList[ID].split('_')
                        label=label[len(label)-1]
                        ID_list=[label]
                    else:
                        label=str(1)
                        ID_list=[label]
                        
        Results=pd.DataFrame(FileList, columns=['File name', 'File type'])
        Results=Anura3D([os.path.basename(FolderName)], FolderName, Results, ID_list, DATA_PAR)
        #Results=[[os.path.basename(FolderName)], Results, ID_list, DATA_PAR]               
            
            
    return Results
#%% PlotInitial function
# This function creates a plot of initial values of X vs Y variables
#For instance a plot of initial stresses vs depth. More optional
#arguments can be included for manipulating the figure size and style on predefined
#styles.
# xvar= a string definfing the data columns name in DATA pandas dataframe obtained 
#with OpenModels. Eg: 'SigmaYY' is the name of the vertical stresses in Anura
# yvar= a string defining the name of the vertical axis in the plot. Eg. 'Y'
#for the vertical elevation of the point.
#Results is a Anura3D class object

def PlotInitial(Results, xvar, yvar, style='Paper', xlabel='default', ylabel='default'\
                , xsize=5, ysize=5, mode='o', hold=0, palete='VTANURA',legendMode=False, lims=[0], varst=0):
    n=len(Results.DATA)  
    IndexList=[0]*n
    X=SF.GetSingleIndexed(Results.DATA, IndexList, xvar, 0, 0, Results.IDs)
    Y=SF.GetSingleIndexed(Results.DATA, IndexList, yvar, 0, 0, Results.IDs)
    NewData=np.array([X, Y]).T
    NewData=pd.DataFrame(NewData, columns=[xvar, yvar])
    NewData=[NewData]
    FakeID=['fake']
    if (xlabel=='default'):
        xlabel=GetName(xvar)
    if (ylabel=='default'):
        ylabel=GetName(yvar)
    GF.PlotAll(NewData, FakeID, xvar, yvar, style, xlabel, ylabel, xsize, ysize, mode, hold \
            , palete, legendMode, lims, varst)
    
#%% GetName function
#This function associates a string var with its label in common ANURA 3D 
#PAR file notation

def GetName(var):
    if (var=='LoadStep'):
        label=r'Load step'
    elif (var=='TimeStep'):
        label=r'Time step'
    elif (var=='Time'):
        label=r'Time [s]'
    elif (var=='PGravity'):
        label=r'Gravity load factor'
    elif (var=='ID_MP'):
        label=r'Material point ID'
    elif (var=='X'):
        label=r'$x$ coordinate [m]'
    elif (var=='Y'):
        label=r'$y$ coordinate [m]'
    elif (var=='Z'):
        label=r'$z$ coordinate [m]'
    elif (var=='Ux'):
        label=r'$x$ displacement [m]'
    elif (var=='Uy'):
        label=r'$y$ displacement [m]'
    elif (var=='Uz'):
        label=r'$z$ displacement [m]'
    elif (var=='Vx'):
        label=r'$x$ velocity [m/s]'
    elif (var=='Vy'):
        label=r'$y$ velocity [m/s]'
    elif (var=='Vz'):
        label=r'$z$ velocity [m/s]'
    elif (var=='ax'):
        label=r'$x$ acceleration $[m^2/s]$'
    elif (var=='ay'):
        label=r'$y$ acceleration $[m^2/s]$'
    elif (var=='az'):
        label=r'$z$ acceleration $[m^2/s]$'
    elif (var=='SigmaXX'):
        label=r'$\sigma_{xx}$ [kPa]'
    elif (var=='SigmaYY'):
        label=r'$\sigma_{yy}$ [kPa]'
    elif (var=='SigmaZZ'):
        label=r'$\sigma_{zz}$ [kPa]'
    elif (var=='SigmaXY'):
        label=r'$\tau_{xy}$ [kPa]'
    elif (var=='SigmaXZ'):
        label=r'$\tau_{xz}$ [kPa]'
    elif (var=='SigmaYZ'):
        label=r'$\tau_{yz}$ [kPa]'
    elif (var=='WPressure'):
        label=r'Water pressure $u$ [kPa]'
    elif (var=='EpsilonXX'):
        label=r'$\varepsilon_{xx}$ [-]'
    elif (var=='EpsilonYY'):
        label=r'$\varepsilon_{yy}$ [-]'
    elif (var=='EpsilonZZ'):
        label=r'$\varepsilon_{zz}$ [-]'
    elif (var=='GammaXY'):
        label=r'$\gamma_{xy}$ [-]'
    elif (var=='GammaXZ'):
        label=r'$\gamma_{xz}$ [-]'
    elif (var=='GammaYZ'):
        label=r'$\gamma_{yz}$ [-]'
    elif (var=='IntWeight'):
        label=r'Integration weigth'
    elif (var=='MatID'):
        label=r'Material ID'
    else:
        label=var
    return label

#%% Function K_0Procedure
#This function is use to calculate the theoretical stresses in a horizontal
#multilayerd profile.
#NLayers= number of layers in the profile
#SurfElevation= Surface elevation
#Overload=uniform load on the surface
#n= porosity vector
#ps=Density vector
#K_0= K_0 vector
#pw=Water density vector

def K_0Procedure(Thickness, n, K_0, NLayers=1, SurfElevation=0, Overload=0,  ps=[2650], pw=[1000]):
    #Firs computes the elevation of the points of interes
    Depth=np.zeros(NLayers*2)
    sigma=np.zeros(NLayers*2)#Total stress
    u=np.zeros(NLayers*2)#Pore Pressure
    sigmap=np.zeros(NLayers*2)#Effective vertical stress
    sigmahp=np.zeros(NLayers*2)#Effective horizontal stress
    sigmah=np.zeros(NLayers*2)#Horizontal total stress
    for i in range(1,NLayers+1):
        if (i==1):
            Depth[2*(i-1)]=SurfElevation
            sigma[2*(i-1)]=Overload
            u[2*(i-1)]=0
        else:
            Depth[2*(i-1)]=Depth[2*(i-1)-1]
            sigma[2*(i-1)]=sigma[2*(i-1)-1]
            u[2*(i-1)]=u[2*(i-1)-1]
            
        Depth[2*(i-1)+1]=Depth[2*(i-1)]-Thickness[i-1]
        sigma[2*(i-1)+1]=sigma[2*(i-1)]-Thickness[i-1]*((ps[i-1]*(1-n[i-1])+n[i-1]*pw[i-1])*9.81/1000)
        u[2*(i-1)+1]=u[2*(i-1)]-Thickness[i-1]*((pw[i-1])*9.81/1000)
        sigmap[2*(i-1)]=sigma[2*(i-1)]-u[2*(i-1)]
        sigmap[2*(i-1)+1]=sigma[2*(i-1)+1]-u[2*(i-1)+1]
        sigmahp[2*(i-1)]=sigmap[2*(i-1)]*K_0[i-1]
        sigmahp[2*(i-1)+1]=sigmap[2*(i-1)+1]*K_0[i-1]
        sigmah[2*(i-1)]=sigmahp[2*(i-1)]+u[2*(i-1)]
        sigmah[2*(i-1)+1]=sigmahp[2*(i-1)+1]+u[2*(i-1)+1]
    Stresses=np.array([Depth, sigma, u, sigmap, sigmahp, sigmah]).T
    Stresses=pd.DataFrame(Stresses, columns=['Elevation', 'sigma', 'u', 'sigmap', 'sigmahp', 'sigmah'])
    return Stresses
            

#%% ismember function
def ismember(A, B):
    return [ np.sum(a == B) for a in A ]
                
#%% Plot function
# This function uses the graphic functions and add more functionallity


def Plot(Results, xvar, yvar, style='Paper', xlabel='default', ylabel='default', xsize=5, ysize=5, mode='-', hold=0,\
         palete='VTANURA', legendMode=True, lims=[0], varts=0, useData='PAR', PlotSingle=False, DataMode='PS',ID=0):
    if (xlabel=='default'):
        xlabel=GetName(xvar)
    if (ylabel=='default'):
        ylabel=GetName(yvar)
    GF.PlotAll(Results.DATA, Results.IDs, xvar, yvar, style, xlabel, ylabel, xsize, ysize, mode, hold, palete, legendMode\
               , lims, varts)
        
#%% ApplyOperation function
        
def ApplyOperation(Results, Operation, varx, vary='', Name='Default', mode='F', span=5, deg=3):
    if (Operation=='d/dx'):
        if (Name=='Default'):
            Name='d%s/d%s' % (vary, varx)
        MF.Derivative(Results.DATA,vary,varx,mode,span,Name)
    elif (Operation=='S_x'):
        if (Name=='Default'):
            Name='%s_s' % (varx)
        MF.SmoothData(Results.DATA,varx,Name,deg,span)
    elif (Operation=='sqrt(eijeij)'):
        for frame in Results.DATA:
            if (Name=='Default'):
                Name='Epsilon_Norm'
            aux=frame['EpsilonXX']**2+frame['EpsilonYY']**2+0.5*frame['GammaXY']**2
            if 'GammaXZ' in frame:#3D
                a=frame.columns.get_loc("GammaXZ")
                b=frame.columns.get_loc("GammaYZ")
                aux=aux+frame['EpsilonZZ']**2+0.5*frame[a]**2+0.5*frame[b]**2
            
            aux=np.sqrt(aux)
            frame[Name]=aux
    else:
        if (Name=='Default'):
            Name='%s %s %s' % (varx, Operation, vary)
        MF.DataOperation(Results.DATA, Operation,varx,vary,Name)
        
#%% Rename VtK files for Blender BTVK animation
# Experimental code to rename vtk files so an animation can be executed in Blender
#Requires the OpenModels funciton to open a folder project and the it examines
# the vtk files on that folder and renames with this format: filename_000#.vtk
# with # being the timestep number

def RenameVtk4Blender(Anura3DProject):
    FolderName=Anura3DProject.path
    for file in  os.listdir(FolderName):
        NameSplit=os.path.splitext(file)
        check=NameSplit[1]
        if (check=='.vtk'):
            #Step 1 rename ending
            Ending=NameSplit[0].split('_')[-1]
            Ending=Ending[:3] #Remove the unnnecesary numbers
            Opening=NameSplit[0].split('_')[0]
            NewName='%s_%s.vtk' % (Opening, Ending) #Concatenate the newName
            os.rename(file, '%s/%s' % (FolderName, NewName)) #Renames the file
            
            
    

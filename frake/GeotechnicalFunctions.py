# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:55:58 2020

@author: zamcr
Geotechnical functions


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
#%% Critical state soil mechanics
def GetphiFromM(M):
    phi=np.arcsin(3*M/(6+M))
    return phi

#%% Soil behavior
def GetKp(phi):
    Kp=np.tan(0.25*np.pi+0.5*phi)**2
    return Kp

def Getp(Sig1, Sig3):
    p=Sig1+2*Sig3
    p=p/3
    return p

def GetEpsvol(Eps1, Eps2):
    #This is assuming Eps2=Eps3 for triaxial testing
    Epsv=Eps1+2*Eps2
    return Epsv
    

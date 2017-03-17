# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:59:31 2016

@author: rsaitkoulovgmailcom
"""
import sys
sys.path.append('..')

import numpy as np
from scene import *
from camera import *
from light import *
from matplotlib.image import *

material1=Material(np.array([0,0,1]),0.2,0.2,0.5,10,0.5)
material2=Material(np.array([1,0,0]),0.2,0.2,0.5,10,0.5)
s1=Sphere(np.array([0,0,3]),0.8,material1)
s2=Sphere(np.array([0.5,0.5,2]),1,material2)
l1=Spotlight(np.array([1,1,0]),np.array([1,1,1]))
sce=Scene([s1,s2],[l1])
#sce=Scene([s2],[l1])
c=Camera(200,200,1)
A=raytracer_render(c,sce)
imsave('shadow8.png', A)
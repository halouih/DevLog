# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 14:16:26 2016

@author: rsaitkoulovgmailcom
"""
import sys
sys.path.append('..')

import numpy as np
from scene import *
from camera import *
from light import *
from matplotlib.image import *

material=Material(np.array([0,0,1]),0.5,0.5,0.5,5,0) 
s=Sphere(np.array([0,0,3]),1,material)

l1=Spotlight(np.array([1,1,0]),np.array([1,1,1]))
sce=Scene([s],[l1])
c=Camera(200,200,1)
A=raytracer_render(c,sce)
imsave('one_sphere4.png', A)
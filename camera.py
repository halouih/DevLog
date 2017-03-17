# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:09:01 2015

@author: rsaitkoulovgmailcom
"""
import numpy as np

from ray_tracer import *

# @param image_nrows : nombre de lignes de l'image rendue
# @param image_ncols : nombre de colonnes de l'image rendue
# @param focal_length : distance focale
class Camera:
    def __init__(self , image_nrows, image_ncols, focal_length):
        self.image_nrows = image_nrows
        self.image_ncols = image_ncols
        self.focal_length = focal_length

# Fonction donnant les coordonnées 3D du rayon passant par un pixel donné (en 2D)
# Coordonnées en variable réduite dans [-1,1] pour les 2 premiers arguments
# Il s'agit donc d'une translation de (x,y) suivi d'un adimensionnement
# Arguments : position 2D du pixel de l'image rendue
# @param row : position de la ligne du pixel
# @param col : position de la colonne du pixel
# @return coordonnées du rayon en 3D
    def ray_at(self,row,col):
        R = Ray(np.array([0,0,0]),np.array([-2*(col-self.image_ncols/2)/self.image_ncols,-2*(row-self.image_nrows/2)/self.image_nrows,self.focal_length]))
        return R
    
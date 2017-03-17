# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 15:30:13 2016

@author: rsaitkoulovgmailcom
"""
from numpy import linalg as la
import numpy as np
from ray_tracer import *
from scene import *

# @param position : coordonnées 3D de l'intersection
# @param normal : vecteur 3D normal à l'intersection
# @param objet : l'objet impliqué dans l'intersection
class Intersection:
    def __init__(self , position, normal, objet):
        self.position=position
        self.normal=normal
        self.objet=objet
        
# Fonction donnant l'intersection entre un rayon et un objet
# Tous les vecteurs utilisés sont normés
# On utilise les formules pour l'équation d'intersection ligne/sphère de l'article avec les mêmes notations
# On distingue les cas suivants :
        # Le rayon démarre en dehors de la sphère et ne l'intersecte pas
        # Le rayon démarre en dehors de la sphère et l'intersecte, on choisit le premier point d'intersection
        # Le rayon démarre de l'intérieur de la sphère et l'intersecte donc en un ou deux points, on choisit le premier point

# Arguments :
# @param objet : un objet de l'espace, qui doit être une sphère pour que la fonction marche
                # la sphère a un centre, un rayon et des caractéristiques (material)
# @param ray : rayon, c'est un vecteur avec une direction et un starting_point
# @return : le premier point d'intersection du la sphère et du rayon
def intersect(objet, ray):
    if type(objet) is Sphere:
        l=ray.direction/la.norm(ray.direction) # vecteur directeur du rayon
        o=ray.starting_point
        c=objet.center
        r=objet.rayon
    
        a=(l.dot(o-c))**2-(la.norm(o-c))**2+r**2
        if a<0:
            return None
        else:
            d1=-(l.dot(o-c))+np.sqrt(a)
            d2=-(l.dot(o-c))-np.sqrt(a)
            dmin=min(d1,d2) # distance minimale entre starting_point et intersection
            dmax=max(d1,d2) # distance maximale entre starting_point et intersection
            xmin=o+dmin*l # position de l'intersection associée à dmin
            xmax=o+dmax*l # position de l'intersection associée à dmax
            if dmax<0:
                return None
            elif la.norm(o-c)>r: # rayon démarre hors de la sphère, on prend le 1er point d'intersection
                x=xmin
                normale=(xmin-c)/la.norm(xmin-c) # normale sortante
            elif la.norm(o-c)<r: # rayon démarre dans la sphère
                x=xmax
                normale=-(xmax-c)/la.norm(xmax-c) # normale vers l'intérieur
            else:
                x=xmax
                normale=-(xmax-c)/la.norm(xmax-c) # normale vers l'intérieur
            return(Intersection(x,normale,objet))
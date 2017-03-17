# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:05:54 2016

@author: rsaitkoulovgmailcom
"""
import numpy as np
from numpy import linalg as la

# @param position : coordonnées 3D de la lumière ponctuelle
# @param color : couleur de la lumière émise sous forme d'un vecteur 3D RGB
class Spotlight:
    def __init__(self, position, color):
        self.position=np.array(position)
        self.color=color

# Fonction donnant la couleur RBG résultant des composantes diffuses et spéculaires de Phong
# Les vecteurs sont normalisés
# On applique les formules données dans l'article
# On retourne la couleur noire si la surface n'est pas orientée vers la lumière
# Arguments :
# @param light : objet Sportlight éclairant l'objet
# @param position : coordonnées 3D du point à éclairer
# @param normal : normale à la surface à cette position
# @param objet : objet à éclairer
# @param viewer : position de l'observateur
# @return couleur RGB résultant des composantes diffuses et spéculaires de Phong
def phong_illuminate(light, position, normal, objet, viewer):
    kd=objet.material.diffuse # constante de réflexion diffuse
    ks=objet.material.specular # constante de réflexion spéculaire
    l1=(np.array(light.position)-np.array(position)) # vecteur directeur du point à éclairer vers la lumière
    l=l1/la.norm(l1)
    n=normal/la.norm(normal) # normale à la surface à cette position
    v=(viewer-position)/la.norm(viewer-position) # direction de l'observateur
    if l.dot(n)<0: # surface non orientée vers la lumière
        return [0,0,0] # couleur noire
    else:
        alpha=objet.material.shininess # brillance
        r=2*n.dot(l)*n-l # direction que prendrait un rayon parfaitement réfléchi
        I=kd*l.dot(n)+ks*max((r.dot(v))**alpha,0) # intensité calculée par le modèle de Phong
        if I<0:
            print("erreur")
        return I*np.array([light.color[0]*objet.material.color[0],light.color[1]*objet.material.color[1],light.color[2]*objet.material.color[2]])

# Fonction donnant 
# 
# Arguments :
# @param objet : objet autour duquel on calcule la lumière ambiante
# @return la composante de couleur résultant de la lumière ambiante
def ambiant_illuminate(objet):
    Ia=objet.material.ambiant # lumière ambiante
    return Ia*objet.material.color # intensité ambiante pour cet objet
    

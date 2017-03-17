# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:14:37 2016

@author: rsaitkoulovgmailcom
"""
import numpy as np
class Sphere:
# @param center : coordonnées 3D du centre
# @param rayon : rayon de la sphère
# @param material : caractéristiques de couleurs et effets
    def __init__(self, center, rayon, material):
        self.center=np.array(center)
        self.rayon=rayon
        self.material=material
    
# @param color : couleur intrinsèque de l'objet sous forme d'un vecteur 3D (rouge, vert, bleu)
# @param ambiant : coefficient de lumière ambiante dans [0,1]
# @param diffuse : coefficient de lumière diffuse dans [0,1]
# @param specular : coefficient de lumière spéculaire dans [0,1]
# @param shininess : coefficient de brillance dans [0,1]
# @param reflection : coefficient de réflexion dans [0,1]
class Material:
    def __init__(self, color, ambiant, diffuse, specular, shininess, reflection):
        self.color=np.array(color)
        self.ambiant=ambiant
        self.diffuse=diffuse
        self.specular=specular
        self.shininess=shininess
        self.reflection=reflection

# @param objects : liste d'objets à stocker
# @param lights : liste de lumières à stocker
class Scene:
    def __init__(self, objets, lights):
        self.objets=objets
        self.lights=lights

# Fonction permettant d'ajouter un objet aux objets de la scène
# Argument :
# @param o : objet à rajouter
    def add_object(self, o):
        self.objets.append(o)

# Fonction permettant d'ajouter une lumière aux lumières de la scène
# Argument :
# @param l : lumière à rajouter
    def add_light(self, l):
        self.lights.append(l)
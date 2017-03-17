# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:34:57 2015

@author: rsaitkoulovgmailcom
"""
from scene import *
from intersection import *
from camera import *
from light import *
import numpy as np
from numpy import linalg as la

# @param starting_point : coordonnées 3D du départ du rayon
# @param direction : vecteur 3D directeur du rayon
class Ray:
    def __init__(self , starting_point, direction):
        self.starting_point=starting_point
        self.direction=direction

# Fonction donnant la couleur de la première intersection rencontrée par un rayon
# # On retourne la couleur noire si le rayon n'intercepte pas d'objet
# Arguments :
# @param ray : rayon à tracer
# @param scene : une instance de la classe Scene
# @param camera : une instance de la classe Camera
# @return couleur de la première intersection rencontrée par le rayon ray
# On parcout tous les objets de la scène et on cherche la première intersection éventuelle pour chacun d'eux
def trace_ray(ray, scene, camera):
    inter=intersect(scene.objets[0],ray)
    for o in scene.objets :
        i=intersect(o,ray) # intersection de l'objet et du rayon
        if i == None:
            pass
        else:
            if inter == None: # on n'a pas trouvé d'intersection précédemment, l'intersection est la première intersection
                inter = i
            else:
                if la.norm(i.position-ray.starting_point) < la.norm(inter.position-ray.starting_point): # on prend la première intersection
                    inter = i
    if inter == None: # le rayon n'a pas d'intersection
        return np.array([0,0,0]) # couleur noire
    else:
        couleur=ambiant_illuminate(o) # on initialise à la couleur ambiante, qu'il ne faut ajouter qu'une seule fois
        for x in scene.lights: # on parcourt toutes les lumières possibles
            couleur+=phong_illuminate(x, inter.position, inter.normal, inter.objet, ray.starting_point)
            #couleur+=compute_light(x, scene, inter, ray.starting_point)
    assert(couleur[0]>=0) # vérification que les couleurs sont données par des nombres positifs
    assert(couleur[1]>=0)
    assert(couleur[2]>=0)
    
    return [min(couleur[0],1),min(couleur[1],1),min(couleur[2],1)] # les coueurs sont données par des nombres inférieurs à 1

# Fonction permettant de renseigner chaque pixel de l'image du rendu
# On stocke les pixels dans une matrice correspondant à l'image du rendu
# Arguments :
# @param camera : une instance de la classe Camera
# @param scene : une instance de la classe Scene
# @return matrice de l'image RGB du rendu
def raytracer_render(camera,scene):
    A=np.zeros([camera.image_nrows,camera.image_nrows,3]) # initialisation de la matrice
    for i in range(camera.image_ncols): # parcourt des colonnes
        for j in range(camera.image_nrows): # parcourt des lignes
            R=camera.ray_at(i,j) # coordonnées 3D du rayon
            A[i][j]=trace_ray(R,scene,camera) # couleurs des pixels
    return A

# Fonction donnant la couleur donnée par le module de Phong seulement si aucun objet n'est positionné entre la lumière et l'intersection
# On travaille sur l'intersection ou non du rayon avec les objets
# Arguments :
# @param light : lumière éclairant l'objet de type Spotlight
# @param scene : scène de type Scene
# @param intersection : intersection à illuminer
# @param viewer : coordonnées 3D de l'observateur
# @return couleur RBG résultant des composantes diffuses et spéculaires de Phong
def compute_light(light,scene,intersection,viewer):
    rayon=Ray(light.position,intersection.position - light.position)
    occ=False # True si un objet est positionné entre la lumière et l'intersection
    i=0 # compteur jusqu'au nombre d'objets
    while occultation == False and i<len(scene.objets):
        inter=intersect(scene.objets[i],rayon) # intersection de l'objet i et du rayon
        if inter != None : # pas d'intersection
            occ = False # pas d'occultation
        i=i+1
    if occ == True : # un objet rencontre le rayon
        return np.array([0,0,0]) # couleur noire
    else :
        return phong_illuminate(light,intersection.position,intersection.normal,intersection.objet,viewer)

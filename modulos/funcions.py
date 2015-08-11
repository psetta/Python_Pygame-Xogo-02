# -*- coding: utf-8 -*-

import pygame
from clases import *
from constantes import *

#FUNCIONS ##############################################################

def crear_cadro(posicion,color=[0,0,0]):
	return cadro(punto(posicion[0],posicion[1]),pygame.Rect(posicion[0] * ANCHO_CADRO, posicion[1] * ALTO_CADRO, ANCHO_CADRO, ALTO_CADRO),color)
	
def crear_cadro_en_lista(posicion,color=[0,0,0]):
	p = posicion[0] + NUMERO_CADROS_ANCHO_XOGO * posicion[1]
	LISTA_CADROS[p] = cadro(punto(posicion[0],posicion[1]),pygame.Rect(posicion[0] * ANCHO_CADRO, posicion[1] * ALTO_CADRO, ANCHO_CADRO, ALTO_CADRO),color)
	
def borrar_cadro_en_lista(posicion):
	p = posicion[0] + NUMERO_CADROS_ANCHO_XOGO * posicion[1]
	LISTA_CADROS[p] = 0
	
def crear_cadro_redores(pos,color=[0,0,0],borrar=False):
	lista_salida = []
	lista_puntos = []
	lista_pos = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]
	if pos.x in range(0,NUMERO_CADROS_TOTALES_XOGO,NUMERO_CADROS_ANCHO_XOGO):
		lista_pos.remove([-1,-1])
		lista_pos.remove([-1,0])
		lista_pos.remove([-1,1])
	if pos.x in range(NUMERO_CADROS_ANCHO_XOGO-1,NUMERO_CADROS_TOTALES_XOGO,NUMERO_CADROS_ANCHO_XOGO):
		lista_pos.remove([1,-1])
		lista_pos.remove([1,0])
		lista_pos.remove([1,1])
	if pos.y in range(0,NUMERO_CADROS_TOTALES_XOGO,NUMERO_CADROS_ALTO_XOGO):
		if [-1,-1] in lista_pos:
			lista_pos.remove([-1,-1])
		lista_pos.remove([0,-1])
		if [1,-1] in lista_pos:
			lista_pos.remove([1,-1])
	if pos.y in range(NUMERO_CADROS_ALTO_XOGO-1,NUMERO_CADROS_TOTALES_XOGO,NUMERO_CADROS_ALTO_XOGO):
		if [-1,1] in lista_pos:
			lista_pos.remove([-1,1])
		lista_pos.remove([0,1])
		if [1,1] in lista_pos:
			lista_pos.remove([1,1])
	for i in lista_pos:
		lista_puntos.append(punto(i[0],i[1]))
	for i in lista_puntos:
		if not borrar:
			cadro = crear_cadro(pos+i,color)
		else:
			cadro = crear_cadro(pos+i,[0,0,0,0])
		lista_salida.append(cadro)
	return lista_salida

#COLISIONS ##############################################################

def posicion_a_indice(pos):
	indice = pos[0] + NUMERO_CADROS_ANCHO_XOGO * pos[1]
	return indice
	
def indices_lista_pos(list_pos):
	lista_salida = []
	for i in list_pos:
		indice = posicion_a_indice(i)
		lista_salida.append(indice)
	return lista_salida
	
#CADROS SUPERIORES

def pos_superiores(p):
	lista_salida = []
	pos0 = punto(int((p.x-MARCO_VENTANA_LATERAL) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO))
	posF = punto(int((p.x+ANCHO_PJ-MARCO_VENTANA_LATERAL-1) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO))
	lista_sum_pos_x = range(posF.x-pos0.x)
	for i in lista_sum_pos_x:
		pos_a_sumar = punto(i,0)
		lista_salida.append(pos0+pos_a_sumar)
	lista_salida.append(posF)
	lista_mod_y = lista_salida[:]
	for i in lista_mod_y:
		punto_mod_y = punto(i.x,i.y-1)
		lista_salida.append(punto_mod_y)
	return lista_salida
	
def lista_cadros_superiores(p):
	list_posiciones_superiores = pos_superiores(p)
	list_indices_superiores = indices_lista_pos(list_posiciones_superiores)
	lista_salida = []
	for i in list_indices_superiores:
		if i < NUMERO_CADROS_TOTALES_XOGO and LISTA_CADROS[i]:
			lista_salida.append(LISTA_CADROS[i])
	return lista_salida
	
#CADROS INFERIORES

def pos_inferiores(p):
	lista_salida = []
	pos0 = punto(int((p.x-MARCO_VENTANA_LATERAL) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO + ALTO_CADRO))
	posF = punto(int((p.x+ANCHO_PJ-MARCO_VENTANA_LATERAL-1) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO + ALTO_CADRO))
	lista_sum_pos_x = range(posF.x-pos0.x)
	for i in lista_sum_pos_x:
		pos_a_sumar = punto(i,0)
		lista_salida.append(pos0+pos_a_sumar)
	lista_salida.append(posF)
	lista_mod_y = lista_salida[:]
	for i in lista_mod_y:
		punto_mod_y = punto(i.x,i.y-1)
		lista_salida.append(punto_mod_y)
	return lista_salida
	
def lista_cadros_inferiores(p):
	list_posiciones_inferiores = pos_inferiores(p)
	list_indices_inferiores = indices_lista_pos(list_posiciones_inferiores)
	lista_salida = []
	for i in list_indices_inferiores:
		if i < NUMERO_CADROS_TOTALES_XOGO and LISTA_CADROS[i]:
			lista_salida.append(LISTA_CADROS[i])
	return lista_salida

#CADROS DEREITA

def pos_dereita(p):
	lista_salida = []
	pos0 = punto(int((p.x+ANCHO_PJ-MARCO_VENTANA_LATERAL) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO))
	posF = punto(int((p.x+ANCHO_PJ-MARCO_VENTANA_LATERAL) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO + ALTO_CADRO))
	lista_sum_pos_y = range(posF.y-pos0.y)
	for i in lista_sum_pos_y:
		pos_a_sumar = punto(0,i)
		lista_salida.append(pos0+pos_a_sumar)
	lista_salida.append(posF)
	lista_mod_y = lista_salida[:]
	for i in lista_mod_y:
		punto_mod_y = punto(i.x+1,i.y)
		lista_salida.append(punto_mod_y)
	return lista_salida
	
def lista_cadros_dereita(p):
	list_posiciones_dereita = pos_dereita(p)
	list_indices_dereita = indices_lista_pos(list_posiciones_dereita)
	lista_salida = []
	for i in list_indices_dereita:
		if i < NUMERO_CADROS_TOTALES_XOGO and LISTA_CADROS[i]:
			lista_salida.append(LISTA_CADROS[i])
	return lista_salida

#CADROS ESQUERDA

def pos_esquerda(p):
	lista_salida = []
	pos0 = punto(int((p.x-(MARCO_VENTANA_LATERAL+ANCHO_CADRO)) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO))
	posF = punto(int((p.x-(MARCO_VENTANA_LATERAL+ANCHO_CADRO)) / ANCHO_CADRO), int((p.y-MARCO_VENTANA_VERTICAL) / ALTO_CADRO + ALTO_CADRO))
	lista_sum_pos_y = range(posF.y-pos0.y)
	for i in lista_sum_pos_y:
		pos_a_sumar = punto(0,i)
		lista_salida.append(pos0+pos_a_sumar)
	lista_salida.append(posF)
	lista_mod_y = lista_salida[:]
	for i in lista_mod_y:
		punto_mod_y = punto(i.x+1,i.y)
		lista_salida.append(punto_mod_y)
	return lista_salida
	
def lista_cadros_esquerda(p):
	list_posiciones_esquerda = pos_esquerda(p)
	list_indices_esquerda = indices_lista_pos(list_posiciones_esquerda)
	lista_salida = []
	for i in list_indices_esquerda:
		if i < NUMERO_CADROS_TOTALES_XOGO and LISTA_CADROS[i]:
			lista_salida.append(LISTA_CADROS[i])
	return lista_salida

#COLISIONS

def colision_pj_cadro(pj_p,lista_cadros):
	for i in lista_cadros:
		if pj_p.x+ANCHO_PJ > i.rect.left+MARCO_VENTANA_LATERAL and pj_p.x < i.rect.left+i.rect.width+MARCO_VENTANA_LATERAL and pj_p.y+ALTO_PJ > i.rect.top+MARCO_VENTANA_VERTICAL and pj_p.y < i.rect.top+i.rect.height+MARCO_VENTANA_VERTICAL:
			return True
	return False


	
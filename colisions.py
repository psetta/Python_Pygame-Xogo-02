# -*- coding: utf-8 -*-

from clases import *

#FUNCIONS PARA COLISIONS

def posicion_a_indice(pos,numero_cadros_ancho_xogo):
	indice = pos[0] + numero_cadros_ancho_xogo * pos[1]
	return indice

def pos_superiores(p,marco_lateral,marco_vertical,ancho_cadro,alto_cadro,ancho_pj):
	lista_salida = []
	pos0 = punto(int((p.x-marco_lateral) / ancho_cadro), int((p.y-marco_vertical) / alto_cadro))
	posF = punto(int((p.x+ancho_pj-marco_lateral-1) / ancho_cadro), int((p.y-marco_vertical) / alto_cadro))
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
	
def indices_superiores(list_pos,numero_cadros_ancho_xogo):
	lista_salida = []
	for i in list_pos:
		indice = posicion_a_indice(i,numero_cadros_ancho_xogo)
		lista_salida.append(indice)
	return lista_salida
	
def lista_cadros_superiores(p,marco_lateral,marco_vertical,ancho_cadro,alto_cadro,ancho_pj,numero_cadros_ancho_xogo,lista_cadros):
	list_posiciones_superiores = pos_superiores(p,marco_lateral,marco_vertical,ancho_cadro,alto_cadro,ancho_pj)
	list_indices_superiores = indices_superiores(list_posiciones_superiores,numero_cadros_ancho_xogo)
	lista_salida = []
	for i in list_indices_superiores:
		if lista_cadros[i]:
			lista_salida.append(lista_cadros[i])
	return lista_salida
	
	
'''
def distancia_bloque_superior(p,lista_ind,lista_cadros,alto_cadro,marco_ventana_vert):
	if len(lista_ind) > 0:
		cadro_mas_cercano = max(lista_ind)
		punto_cadro_y = lista_cadros[cadro_mas_cercano].rect.top+alto_cadro+marco_ventana_vert
		return p.y - punto_cadro_y
	else:
		return False
'''
		
def colision_pj_cadro(pj_p,lista_cadros,ancho_pj,alto_pj,marco_lateral,marco_vertical):
	for i in lista_cadros:
		if pj_p.x+ancho_pj > i.rect.left+marco_lateral and pj_p.x < i.rect.left+i.rect.width+marco_lateral and pj_p.y+alto_pj > i.rect.top+marco_vertical and pj_p.y < i.rect.top+i.rect.height+marco_vertical:
			return True
	return False
	
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from modulos.clases import *
from modulos.funcions import *
from modulos.constantes import *


import ctypes
import os
import sys

if os.name == 'nt' and sys.getwindowsversion()[0] >= 6:
    ctypes.windll.user32.SetProcessDPIAware()

#CREAR SURFACE COS CADROS

superficie_cadros = pygame.Surface((ANCHO_XOGO_REAL,ALTO_XOGO_REAL), pygame.SRCALPHA)

#FUNCION DEBUXAR CADROS EN SURFACE

def debuxar_cadro(cadro):
	superficie_cadros.fill(cadro.color,cadro.rect)
	
#DEBUXAR CADROS NA SURFACE

for i in LISTA_CADROS:
	if i:
		debuxar_cadro(i)
	
#CREAR SURFACE DOS MARCOS

marco_lateral = pygame.Surface((MARCO_VENTANA_LATERAL,ALTO_VENTANA))
marco_vertical = pygame.Surface((ANCHO_VENTANA,MARCO_VENTANA_VERTICAL))

#VARIABLES

punto_camara = punto(0,0)

punto_camara_ref = punto(0,0)

punto_pj = punto(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2)

pj = pj(punto(punto_pj.x,punto_pj.y),punto(punto_pj.x,punto_pj.y))

cadricula = False

mostrar_puntos = False

pincel_gordo = False

pj_mira = "abaixo"

lista_cadros_superiores_pj = []
lista_cadros_inferiores_pj = []
lista_cadros_dereita_pj = []
lista_cadros_esquerda_pj = []

lista_cadros_cercanos = lista_cadros_superiores_pj + lista_cadros_inferiores_pj + lista_cadros_esquerda_pj + lista_cadros_dereita_pj

#INICIAR PYGAME

pygame.init()

#PANTALLA

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

pygame.display.set_caption("Conceptos_2")

#CARGA DE IMAXES

#PJ

if (os.access("sprites/pj/abaixo0.png",0) and os.access("sprites/pj/arriba0.png",0) 
	and os.access("sprites/pj/dereita0.png",0) and os.access("sprites/pj/esquerda0.png",0)):
	imagen_abaixo0 = pygame.image.load("sprites/pj/abaixo0.png").convert_alpha()
	imagen_arriba0 = pygame.image.load("sprites/pj/arriba0.png").convert_alpha()
	imagen_dereita0 = pygame.image.load("sprites/pj/dereita0.png").convert_alpha()
	imagen_esquerda0 = pygame.image.load("sprites/pj/esquerda0.png").convert_alpha()
	imagen_pj = True
else:
	imagen_pj = False

if imagen_pj:
	imagen_abaixo0 = pygame.transform.scale(imagen_abaixo0,(int(ANCHO_PJ),int(ALTO_PJ*2)))
	imagen_arriba0 = pygame.transform.scale(imagen_arriba0,(int(ANCHO_PJ),int(ALTO_PJ*2)))
	imagen_dereita0 = pygame.transform.scale(imagen_dereita0,(int(ANCHO_PJ),int(ALTO_PJ*2)))
	imagen_esquerda0 = pygame.transform.scale(imagen_esquerda0,(int(ANCHO_PJ),int(ALTO_PJ*2)))

if imagen_pj:
	if pj_mira == "abaixo":
		imagen_pj = imagen_abaixo0
	elif pj_mira == "arriba":
		imagen_pj = imagen_arriba0
	elif pj_mira == "dereita":
		imagen_pj = imagen_dereita0
	elif pj_mira == "esquerda":
		imagen_pj = imagen_esquerda0

#FONT

font_1 = pygame.font.SysFont("System", ANCHO_VENTANA/25)

ON = True

#BUCLE XOGO
#------------------------------------------------------------------------

while ON:

	reloj = pygame.time.Clock()

	ventana.fill((255,255,255))

	#DEBUXADO #############################################################################
	
	#DEBUXAR LIMITES
	
	limite_superior = pygame.Rect(MARCO_VENTANA_LATERAL-punto_camara.x,MARCO_VENTANA_VERTICAL-punto_camara.y,ANCHO_XOGO,ALTO_CADRO*2)
	pygame.draw.rect(ventana,[255,210,210],limite_superior)
	
	limite_inferior = pygame.Rect(MARCO_VENTANA_LATERAL-punto_camara.x,(ALTO_XOGO-ALTO_CADRO*2)-(punto_camara.y+MARCO_VENTANA_VERTICAL),ANCHO_XOGO,ALTO_CADRO*2)
	pygame.draw.rect(ventana,[255,210,210],limite_inferior)
	
	limite_esquerdo = pygame.Rect(MARCO_VENTANA_LATERAL-punto_camara.x,MARCO_VENTANA_VERTICAL-punto_camara.y,ANCHO_CADRO*2,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,210,210],limite_esquerdo)
	
	limite_dereito = pygame.Rect((ANCHO_XOGO-ANCHO_CADRO*2)-(punto_camara.x+MARCO_VENTANA_LATERAL),MARCO_VENTANA_VERTICAL-punto_camara.y,ANCHO_CADRO*2,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,210,210],limite_dereito)

	#DEBUXAR CADROS
	
	ventana.blit(superficie_cadros,(MARCO_VENTANA_LATERAL-punto_camara.x,MARCO_VENTANA_VERTICAL-punto_camara.y))

	#DEBUXAR CADRO-FONDO-REFERENCIA
	
	if ANCHO_VENTANA == ANCHO_XOGO:
		cadro_fondo_ref = pygame.Surface((ANCHO_VENTANA_INICIAL-MARCO_VENTANA_LATERAL*2,ALTO_VENTANA_INICIAL-MARCO_VENTANA_VERTICAL*2),pygame.SRCALPHA)
		cadro_fondo_ref.fill((200,240,200,100))
		ventana.blit(cadro_fondo_ref,(punto_camara_ref.x,punto_camara_ref.y))
			
	#DEBUXAR PJ_RECT_CENTRADO
	
	if mostrar_puntos:
		pj_centr = pygame.Rect(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2,ANCHO_PJ,ALTO_PJ)
		pygame.draw.rect(ventana,[150,150,150],pj_centr,1)
	
	#DEBUXAR PJ
	
	if imagen_pj:
		if pj_mira == "abaixo":
			imagen_pj = imagen_abaixo0
		elif pj_mira == "arriba":
			imagen_pj = imagen_arriba0
		elif pj_mira == "dereita":
			imagen_pj = imagen_dereita0
		elif pj_mira == "esquerda":
			imagen_pj = imagen_esquerda0

	if imagen_pj:
		#pj_rect = pygame.Rect(pj.punto_ventana.x,pj.punto_ventana.y,ANCHO_PJ,ALTO_PJ)
		#pygame.draw.rect(ventana,[255,0,255],pj_rect)
		ventana.blit(imagen_pj,(pj.punto_ventana.x-(imagen_pj.get_width()-ANCHO_PJ+1)/2,pj.punto_ventana.y-imagen_pj.get_height()/2))
	else:
		pj_rect = pygame.Rect(pj.punto_ventana.x,pj.punto_ventana.y,ANCHO_PJ,ALTO_PJ)
		pygame.draw.rect(ventana,[0,0,0],pj_rect)
		
	if cadricula:
		for i in lista_cadros_cercanos:
			rect_inf = pygame.Rect(i.rect.left-(punto_camara.x-MARCO_VENTANA_LATERAL),i.rect.top-(punto_camara.y-MARCO_VENTANA_VERTICAL),ANCHO_CADRO,ALTO_CADRO)
			pygame.draw.rect(ventana,[255,0,0],rect_inf,2)
	
	#DEBUXAR CUADRICULA
	
	if cadricula:
		for i in range(MARCO_VENTANA_LATERAL,(ANCHO_XOGO-MARCO_VENTANA_LATERAL)+ANCHO_CADRO,ANCHO_CADRO):
			pygame.draw.line(ventana,(200,200,200),(i-punto_camara.x,MARCO_VENTANA_VERTICAL-punto_camara.y),(i-punto_camara.x,ALTO_XOGO-(punto_camara.y+MARCO_VENTANA_VERTICAL)))
		for i in range(MARCO_VENTANA_VERTICAL,(ALTO_XOGO-MARCO_VENTANA_VERTICAL)+ALTO_CADRO,ALTO_CADRO):
			pygame.draw.line(ventana,(200,200,200),(MARCO_VENTANA_LATERAL-punto_camara.x,i-punto_camara.y),(ANCHO_XOGO-(punto_camara.x+MARCO_VENTANA_LATERAL),i-punto_camara.y))
	
	#DEBUXAR TEXTO
	
	if mostrar_puntos:
		text_punto = font_1.render(("pj_punto("+str(pj.punto.x)+","+str(pj.punto.y)),True,[0,0,0])
		ventana.blit(text_punto,[ANCHO_CADRO+MARCO_VENTANA_LATERAL,ALTO_CADRO+MARCO_VENTANA_VERTICAL])
	
		text_punto_ventana = font_1.render(("pj_punto_ventana("+str(pj.punto_ventana.x)+","+str(pj.punto_ventana.y)+")"),True,[0,0,0])
		ventana.blit(text_punto_ventana,[ANCHO_CADRO+MARCO_VENTANA_LATERAL,ALTO_CADRO+MARCO_VENTANA_VERTICAL+text_punto_ventana.get_height()])
	
		text_punto_camara = font_1.render(("punto_camara("+str(punto_camara.x)+","+str(punto_camara.y)+")"),True,[0,0,0])
		ventana.blit(text_punto_camara,[ANCHO_CADRO+MARCO_VENTANA_LATERAL,ALTO_CADRO+MARCO_VENTANA_VERTICAL+text_punto_camara.get_height()*2])
		
	#DEBUXAR MARCOS
	
	ventana.blit(marco_lateral,(0,0))
	ventana.blit(marco_lateral,(ANCHO_VENTANA-MARCO_VENTANA_LATERAL,0))
	ventana.blit(marco_vertical,(0,0))
	ventana.blit(marco_vertical,(0,ALTO_VENTANA-MARCO_VENTANA_VERTICAL))
	
	#MOVEMENTO DE PJ-PUNTO #############################################################################
	
	lista_mov = []
	
	tecla_pulsada = pygame.key.get_pressed()
	
	punto_destino = punto(pj.punto.x,pj.punto.y)
	
	if tecla_pulsada[K_UP] or tecla_pulsada[K_w]:
		punto_destino.y -= VELOCIDADE_PJ
		lista_mov.append("arriba")
		
	if tecla_pulsada[K_DOWN] or tecla_pulsada[K_s]:
		punto_destino.y  += VELOCIDADE_PJ
		lista_mov.append("abaixo")
		
	if tecla_pulsada[K_RIGHT] or tecla_pulsada[K_d]:
		punto_destino.x += VELOCIDADE_PJ
		lista_mov.append("dereita")
		
	if tecla_pulsada[K_LEFT] or tecla_pulsada[K_a]:
		punto_destino.x -= VELOCIDADE_PJ
		lista_mov.append("esquerda")
		
	if "arriba" in lista_mov and "abaixo" in lista_mov:
		lista_mov.remove("arriba")
		lista_mov.remove("abaixo")
	if "dereita" in lista_mov and "esquerda" in lista_mov:
		lista_mov.remove("dereita")
		lista_mov.remove("esquerda")
		
	if len(lista_mov) > 0:
		pj_mira = lista_mov[0]
		
	#MOVEMENTO CON VECTOR
	
	vector_pj = vector(pj.punto.x,pj.punto.y)
	vector_pj_destino = vector(punto_destino.x,punto_destino.y)
	
	vector_dir = vector_pj_destino - vector_pj
	
	pj_punto_futuro = punto(pj.punto.x,pj.punto.y)
	
	if abs(vector_dir.x) > 0 or abs(vector_dir.y) > 0:
		vector_final = vector_pj + vector_dir * VELOCIDADE_PJ / vector_dir.longitude()
		pj_punto_futuro = punto(vector_final.x,vector_final.y)
		
	#COLISIONS PJ - BLOQUES
	
	lista_cadros_superiores_pj = []
	lista_cadros_inferiores_pj = []
	lista_cadros_dereita_pj = []
	lista_cadros_esquerda_pj = []
	
	if "arriba" in lista_mov:
		lista_cadros_superiores_pj =  lista_cadros_superiores(pj.punto)
	if "abaixo" in lista_mov:
		lista_cadros_inferiores_pj = lista_cadros_inferiores(pj.punto)
	if "dereita" in lista_mov:
		lista_cadros_dereita_pj =  lista_cadros_dereita(pj.punto)
	if "esquerda" in lista_mov:
		lista_cadros_esquerda_pj =  lista_cadros_esquerda(pj.punto)
	
	lista_cadros_cercanos = lista_cadros_superiores_pj + lista_cadros_inferiores_pj + lista_cadros_esquerda_pj + lista_cadros_dereita_pj
	
	if colision_pj_cadro(pj_punto_futuro,lista_cadros_cercanos):
		if colision_pj_cadro(punto(pj_punto_futuro.x,pj.punto.y),lista_cadros_cercanos):
			pj_punto_futuro.x = pj.punto.x
		if colision_pj_cadro(punto(pj.punto.x,pj_punto_futuro.y),lista_cadros_cercanos):
			pj_punto_futuro.y = pj.punto.y
		
		
	pj.punto = punto(pj_punto_futuro.x,pj_punto_futuro.y)

	#REAXUSTE DO PUNTO
	
	pj.punto.x = min(ANCHO_XOGO-(ANCHO_PJ+MARCO_VENTANA_LATERAL),pj.punto.x)
	pj.punto.x = max(MARCO_VENTANA_LATERAL,pj.punto.x)
	pj.punto.y = min(ALTO_XOGO-(ALTO_PJ+MARCO_VENTANA_VERTICAL),pj.punto.y)
	pj.punto.y = max(MARCO_VENTANA_VERTICAL,pj.punto.y)
		
	#MOVEMENTO DO PUNTO-CAMARA
	
	punto_camara.y = pj.punto.y - ALTO_VENTANA/2+ALTO_PJ/2
	punto_camara.x = pj.punto.x - ANCHO_VENTANA/2+ANCHO_PJ/2

	#REAXUSTE DO PUNTO-CAMARA
	
	punto_camara.x = min(ANCHO_XOGO-ANCHO_VENTANA,punto_camara.x)
	punto_camara.x = max(0,punto_camara.x)
	punto_camara.y = min(ALTO_XOGO-ALTO_VENTANA,punto_camara.y)
	punto_camara.y = max(0,punto_camara.y)
	
	#MOVEMENTO DE PUNTO-CAMARA-REFERENCIAS
	
	punto_camara_ref.x = pj.punto.x - (ANCHO_VENTANA_INICIAL/2 - (ANCHO_PJ/2 + MARCO_VENTANA_LATERAL))
	punto_camara_ref.y = pj.punto.y - (ALTO_VENTANA_INICIAL/2 - (ALTO_PJ/2 + MARCO_VENTANA_VERTICAL))
	
	punto_camara_ref.x = min(ANCHO_XOGO-(MARCO_VENTANA_LATERAL+(ANCHO_VENTANA_INICIAL-MARCO_VENTANA_LATERAL*2)),punto_camara_ref.x)
	punto_camara_ref.x = max(MARCO_VENTANA_LATERAL,punto_camara_ref.x)
	punto_camara_ref.y = min(ALTO_XOGO-(MARCO_VENTANA_VERTICAL+(ALTO_VENTANA_INICIAL-MARCO_VENTANA_VERTICAL*2)),punto_camara_ref.y)
	punto_camara_ref.y = max(MARCO_VENTANA_VERTICAL,punto_camara_ref.y)
	
	#MOVEMENTO DE PUNTO-VENTANA

	pj.punto_ventana.y = pj.punto.y - punto_camara.y
	pj.punto_ventana.x = pj.punto.x - punto_camara.x
	
	#ACTUALIZAR PANTALLA
	
	pygame.display.update()
	
	#MOUSE #############################################################################
	
	pos_mouse = pygame.mouse.get_pos()
	
		#CREACION DE CADROS
		
	color_cadro = [130,80,80]
		
	if (pygame.mouse.get_pressed()[0] == 1 or pygame.mouse.get_pressed()[2] == 1) and (pos_mouse[0] > MARCO_VENTANA_LATERAL and pos_mouse[0] < ANCHO_VENTANA-MARCO_VENTANA_LATERAL) and (pos_mouse[1] > MARCO_VENTANA_VERTICAL and pos_mouse[1] < ALTO_VENTANA-MARCO_VENTANA_VERTICAL):
		cadro_mouse = punto(int((pos_mouse[0]-MARCO_VENTANA_LATERAL)/ANCHO_CADRO+punto_camara.x/ANCHO_CADRO),int((pos_mouse[1]-MARCO_VENTANA_VERTICAL)/ALTO_CADRO+punto_camara.y/ALTO_CADRO))
		
		if pygame.mouse.get_pressed()[0] == 1:
			if not pincel_gordo:
				cadro_a_debuxar = crear_cadro(cadro_mouse,color_cadro)
				debuxar_cadro(cadro_a_debuxar)
				crear_cadro_en_lista(cadro_mouse,color_cadro)
			else:
				lista_cadros_debuxar = crear_cadro_redores(punto(cadro_mouse[0],cadro_mouse[1]),color_cadro)
				for i in lista_cadros_debuxar:
					debuxar_cadro(i)
					crear_cadro_en_lista(i.pos,color_cadro)
					
		elif pygame.mouse.get_pressed()[2] == 1:
			if not pincel_gordo:
				cadro_a_borrar = crear_cadro(cadro_mouse,[0,0,0,0])
				debuxar_cadro(cadro_a_borrar)
				borrar_cadro_en_lista(cadro_mouse)
			else:
				lista_cadros_borrar = crear_cadro_redores(punto(cadro_mouse[0],cadro_mouse[1]),[0,0,0,0])
				for i in lista_cadros_borrar:
					debuxar_cadro(i)
					borrar_cadro_en_lista(i.pos)

	#EVENTOS

	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
		#PONHER-QUITAR CADRICULA
			if e.key == pygame.K_c:
				if cadricula:
					cadricula = False
				else:
					cadricula = True
		#CAMBIAR TAMANHO DE PANTALLA
			if e.key == pygame.K_r:
				if ANCHO_VENTANA == ANCHO_VENTANA_INICIAL:
					ANCHO_VENTANA = ANCHO_XOGO
					ALTO_VENTANA = ALTO_XOGO
					ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
					marco_lateral = pygame.Surface((MARCO_VENTANA_LATERAL,ALTO_VENTANA))
					marco_vertical = pygame.Surface((ANCHO_VENTANA,MARCO_VENTANA_VERTICAL))
				else:
					ANCHO_VENTANA = ANCHO_VENTANA_INICIAL
					ALTO_VENTANA = ALTO_VENTANA_INICIAL
					ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
					marco_lateral = pygame.Surface((MARCO_VENTANA_LATERAL,ALTO_VENTANA))
					marco_vertical = pygame.Surface((ANCHO_VENTANA,MARCO_VENTANA_VERTICAL))
		#MOSTRAR PUNTOS
			if e.key == pygame.K_t:
				if mostrar_puntos:
					mostrar_puntos = False
				else:
					mostrar_puntos = True
		#CAMBIAR TAMANHO PINCEL
			if e.key == pygame.K_f:
				if pincel_gordo:
					pincel_gordo = False
				else:
					pincel_gordo = True
		#ESC
			if e.key == pygame.K_ESCAPE:
				pygame.display.quit()
				ON = False
		#QUIT
		if e.type == pygame.QUIT:
			pygame.display.quit()
			ON = False
			
	reloj.tick(60)

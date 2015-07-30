# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from clases import *

#CONSTANTES

ANCHO_XOGO = 700
ALTO_XOGO = 500

ANCHO_VENTANA_INICIAL = 400
ALTO_VENTANA_INICIAL = 300

ANCHO_VENTANA = 400
ALTO_VENTANA = 300

NUMERO_CADROS_ANCHO = 100
NUMERO_CADROS_ALTO = 100

NUMERO_CADROS_TOTALES = NUMERO_CADROS_ANCHO*NUMERO_CADROS_ALTO

ANCHO_CADRO = ANCHO_VENTANA / NUMERO_CADROS_ANCHO
ALTO_CADRO = ALTO_VENTANA / NUMERO_CADROS_ALTO

ANCHO_PJ = ANCHO_CADRO * 3
ALTO_PJ = ALTO_CADRO * 5

VELOCIDADE_PJ = 3

LISTA_CADROS = []

for i in range (NUMERO_CADROS_TOTALES):
	LISTA_CADROS.append(0)
	
#FUNCIONS

def crear_cadros(posicion,color):
	p = posicion[0] + NUMERO_CADROS_ANCHO * posicion[1]
	LISTA_CADROS[p] = cadro(punto(posicion[0],posicion[1]),pygame.Rect(posicion[0] * ANCHO_CADRO, posicion[1] * ALTO_CADRO, ANCHO_CADRO, ALTO_CADRO),color)

#ENGADIR CADROS A LISTA	
	
for i in range(10,NUMERO_CADROS_ALTO/2,1):
	crear_cadros([4,i],[0,0,0])
	crear_cadros([5,i],[0,0,0])
	crear_cadros([6,i],[0,0,0])
	
for i in range(50,NUMERO_CADROS_ALTO-10,1):
	crear_cadros([15,i],[0,0,100])
	crear_cadros([16,i],[0,0,100])
	crear_cadros([17,i],[0,0,100])
	
for i in range(10,NUMERO_CADROS_ANCHO-10,1):
	crear_cadros([i,2],[0,100,0])
	crear_cadros([i,3],[0,100,0])
	crear_cadros([i,4],[0,100,0])

#VARIABLES

punto_camara = punto(0,0)

punto_camara_ref = punto(0,0)

punto_pj = punto(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2)

pj = pj(punto(punto_pj.x,punto_pj.y),punto(punto_pj.x,punto_pj.y))

cadricula = False

mostrar_puntos = False

#INICIAR PYGAME

pygame.init()

#PANTALLA

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

pygame.display.set_caption("Conceptos_2")

#FONT

font_1 = pygame.font.SysFont("System", ANCHO_VENTANA/25)

ON = True

#BUCLE XOGO

while ON:

	reloj = pygame.time.Clock()

	ventana.fill((255,255,255))
	
	#DEBUXAR CUADRICULA
	
	if cadricula:
		for i in range(0,ANCHO_XOGO+ANCHO_CADRO,ANCHO_CADRO):
			pygame.draw.line(ventana,(200,200,200),(i-punto_camara.x,0-punto_camara.y),(i-punto_camara.x,ALTO_XOGO-punto_camara.y))
		for i in range(0,ALTO_XOGO+ALTO_CADRO,ALTO_CADRO):
			pygame.draw.line(ventana,(200,200,200),(0-punto_camara.x,i-punto_camara.y),(ANCHO_XOGO-punto_camara.x,i-punto_camara.y))
	
	#DEBUXAR CADROS
	

	#DEBUXAR LIMITES
	
	limite_superior = pygame.Rect(0-punto_camara.x,0-punto_camara.y,ANCHO_XOGO,ALTO_CADRO*2)
	pygame.draw.rect(ventana,[255,210,210],limite_superior)
	
	limite_inferior = pygame.Rect(0-punto_camara.x,(ALTO_XOGO-ALTO_CADRO*2)-punto_camara.y,ANCHO_XOGO,ALTO_CADRO*2)
	pygame.draw.rect(ventana,[255,210,210],limite_inferior)
	
	limite_esquerdo = pygame.Rect(0-punto_camara.x,0-punto_camara.y,ANCHO_CADRO*2,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,210,210],limite_esquerdo)
	
	limite_dereito = pygame.Rect((ANCHO_XOGO-ANCHO_CADRO*2)-punto_camara.x,0-punto_camara.y,ANCHO_CADRO*2,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,210,210],limite_dereito)
	
	#DEBUXAR REFERENCIAS
	
	cont_ref = 0
	
	for u in range(ALTO_XOGO/4,ALTO_XOGO+1-ALTO_XOGO/4,ALTO_CADRO*20):
		for i in range(ANCHO_XOGO/4,ANCHO_XOGO+1-ANCHO_XOGO/4,ANCHO_CADRO*10):
			texto_num = font_1.render(str(cont_ref),True,[150,150,255])
			ventana.blit(texto_num,[i-punto_camara.x,u-punto_camara.y])
			cont_ref += 1
			
	#DEBUXAR CADRO-FONDO-REFERENCIA
	
	if ANCHO_VENTANA == ANCHO_XOGO:
		cadro_fondo_ref = pygame.Surface((ANCHO_VENTANA_INICIAL,ALTO_VENTANA_INICIAL),pygame.SRCALPHA)
		cadro_fondo_ref.fill((200,240,200,100))
		ventana.blit(cadro_fondo_ref,(punto_camara_ref.x,punto_camara_ref.y))
			
	#DEBUXAR PJ_RECT_CENTRADO
	
	if mostrar_puntos:
		pj_centr = pygame.Rect(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2,ANCHO_PJ,ALTO_PJ)
		pygame.draw.rect(ventana,[150,150,150],pj_centr,1)
	
	#DEBUXAR PJ
	
	pj_rect = pygame.Rect(pj.punto_ventana.x,pj.punto_ventana.y,ANCHO_PJ,ALTO_PJ)
	pygame.draw.rect(ventana,[0,0,0],pj_rect)
	
	#DEBUXAR TEXTO
	
	if mostrar_puntos:
		text_punto = font_1.render(("pj_punto("+str(pj.punto.x)+","+str(pj.punto.y)),True,[0,0,0])
		ventana.blit(text_punto,[ANCHO_CADRO,ALTO_CADRO])
	
		text_punto_ventana = font_1.render(("pj_punto_ventana("+str(pj.punto_ventana.x)+","+str(pj.punto_ventana.y)+")"),True,[0,0,0])
		ventana.blit(text_punto_ventana,[ANCHO_CADRO,ALTO_CADRO+text_punto_ventana.get_height()])
	
		text_punto_camara = font_1.render(("punto_camara("+str(punto_camara.x)+","+str(punto_camara.y)+")"),True,[0,0,0])
		ventana.blit(text_punto_camara,[ANCHO_CADRO,ALTO_CADRO+text_punto_camara.get_height()*2])
	
	#MOVEMENTO DE PJ-PUNTO
	
	tecla_pulsada = pygame.key.get_pressed()
	
	punto_futuro = punto(pj.punto.x,pj.punto.y)
	
	if tecla_pulsada[K_UP] or tecla_pulsada[K_w]:
		punto_futuro.y -= VELOCIDADE_PJ
		
	if tecla_pulsada[K_DOWN] or tecla_pulsada[K_s]:
		punto_futuro.y  += VELOCIDADE_PJ
		
	if tecla_pulsada[K_RIGHT] or tecla_pulsada[K_d]:
		punto_futuro.x += VELOCIDADE_PJ
		
	if tecla_pulsada[K_LEFT] or tecla_pulsada[K_a]:
		punto_futuro.x -= VELOCIDADE_PJ
		
	#MOVEMENTO CON VECTOR
	
	vector_pj = vector(pj.punto.x,pj.punto.y)
	vector_pj_futuro = vector(punto_futuro.x,punto_futuro.y)
	
	vector_dir = vector_pj_futuro - vector_pj
	
	if abs(vector_dir.x) > 0 or abs(vector_dir.y) > 0:
		vector_final = vector_pj + vector_dir * VELOCIDADE_PJ / vector_dir.longitude()
		pj.punto = punto(vector_final.x,vector_final.y)
	
	#REAXUSTE DO PUNTO
	
	pj.punto.x = min(ANCHO_XOGO-ANCHO_PJ,pj.punto.x)
	pj.punto.x = max(0,pj.punto.x)
	pj.punto.y = min(ALTO_XOGO-ALTO_PJ,pj.punto.y)
	pj.punto.y = max(0,pj.punto.y)
		
	#MOVEMENTO DE PUNTO-CAMARA
	
	punto_camara.y = pj.punto.y - ALTO_VENTANA/2+ALTO_PJ/2
	punto_camara.x = pj.punto.x - ANCHO_VENTANA/2+ANCHO_PJ/2

	#REAXUSTE DO PUNTO
	
	punto_camara.x = min(ANCHO_XOGO-ANCHO_VENTANA,punto_camara.x)
	punto_camara.x = max(0,punto_camara.x)
	punto_camara.y = min(ALTO_XOGO-ALTO_VENTANA,punto_camara.y)
	punto_camara.y = max(0,punto_camara.y)
	
	#MOVEMENTO DE PUNTO-CAMARA-REFERENCIAS
	
	punto_camara_ref.y = pj.punto.y - ALTO_VENTANA_INICIAL/2+ALTO_PJ/2
	punto_camara_ref.x = pj.punto.x - ANCHO_VENTANA_INICIAL/2+ANCHO_PJ/2
	
	punto_camara_ref.x = min(ANCHO_XOGO-ANCHO_VENTANA_INICIAL,punto_camara_ref.x)
	punto_camara_ref.x = max(0,punto_camara_ref.x)
	punto_camara_ref.y = min(ALTO_XOGO-ALTO_VENTANA_INICIAL,punto_camara_ref.y)
	punto_camara_ref.y = max(0,punto_camara_ref.y)
	
	#MOVEMENTO DE PUNTO-VENTANA
	
	if punto_camara.y == 0 or punto_camara.y == ALTO_XOGO - ALTO_VENTANA:
		pj.punto_ventana.y = pj.punto.y - punto_camara.y
	else:
		pj.punto_ventana.y = ALTO_VENTANA/2-ALTO_PJ/2
		
	if punto_camara.x == 0 or punto_camara.x == ANCHO_XOGO - ANCHO_VENTANA:
		pj.punto_ventana.x = pj.punto.x - punto_camara.x
	else:
		pj.punto_ventana.x = ANCHO_VENTANA/2-ANCHO_PJ/2
		
	#ACTUALIZAR PANTALLA
	
	pygame.display.update()
	
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
				else:
					ANCHO_VENTANA = ANCHO_VENTANA_INICIAL
					ALTO_VENTANA = ALTO_VENTANA_INICIAL
					ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
		#MOSTRAR PUNTOS
			if e.key == pygame.K_t:
				if mostrar_puntos:
					mostrar_puntos = False
				else:
					mostrar_puntos = True
		#QUIT
		if e.type == pygame.QUIT:
			pygame.display.quit()
			ON = False
			
	reloj.tick(60)

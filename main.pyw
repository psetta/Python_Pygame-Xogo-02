# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from clases import *

#CONSTANTES

ANCHO_XOGO = 800
ALTO_XOGO = 600

ANCHO_VENTANA_INICIAL = 500
ALTO_VENTANA_INICIAL = 400

ANCHO_VENTANA = ANCHO_VENTANA_INICIAL
ALTO_VENTANA = ALTO_VENTANA_INICIAL

NUMERO_CADROS_ANCHO = 100
NUMERO_CADROS_ALTO = 100

ANCHO_CADRO = ANCHO_VENTANA / NUMERO_CADROS_ANCHO
ALTO_CADRO = ALTO_VENTANA / NUMERO_CADROS_ALTO

MARCO_VENTANA_LATERAL = ANCHO_CADRO * 5
MARCO_VENTANA_VERTICAL = ALTO_CADRO * 2

ANCHO_VENTANA_REAL = ANCHO_VENTANA - MARCO_VENTANA_LATERAL*2
ALTO_VENTANA_REAL = ALTO_VENTANA - MARCO_VENTANA_VERTICAL*2	

ANCHO_XOGO_REAL = ANCHO_XOGO - MARCO_VENTANA_LATERAL*2
ALTO_XOGO_REAL = ALTO_XOGO - MARCO_VENTANA_VERTICAL*2

NUMERO_CADROS_ANCHO_XOGO = int(ANCHO_XOGO_REAL / ANCHO_CADRO)
NUMERO_CADROS_ALTO_XOGO = int(ALTO_XOGO_REAL / ALTO_CADRO)

NUMERO_CADROS_TOTALES_VENTANA = NUMERO_CADROS_ANCHO*NUMERO_CADROS_ALTO
NUMERO_CADROS_TOTALES_XOGO = NUMERO_CADROS_ANCHO_XOGO*NUMERO_CADROS_ALTO_XOGO

ANCHO_PJ = ANCHO_CADRO * 4
ALTO_PJ = ALTO_CADRO * 5

VELOCIDADE_PJ = 3

LISTA_CADROS = []

for i in range(NUMERO_CADROS_TOTALES_XOGO):
	LISTA_CADROS.append(0)
	
#FUNCIONS

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

#INICIAR PYGAME

pygame.init()

#PANTALLA

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

pygame.display.set_caption("Conceptos_2")

#FONT

font_1 = pygame.font.SysFont("System", ANCHO_VENTANA/25)

ON = True

#BUCLE XOGO
#------------------------------------------------------------------------

while ON:

	reloj = pygame.time.Clock()

	ventana.fill((255,255,255))

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
	
	'''
	for i in LISTA_CADROS:
		if i:
			rectangulo = pygame.Rect(i.rect.left-punto_camara.x,i.rect.top-punto_camara.y,i.rect.width,i.rect.height)
			pygame.draw.rect(ventana,i.color,rectangulo)
	'''
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
	
	pj_rect = pygame.Rect(pj.punto_ventana.x,pj.punto_ventana.y,ANCHO_PJ,ALTO_PJ)
	pygame.draw.rect(ventana,[0,0,0],pj_rect)
	
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
	
	pj.punto.x = min(ANCHO_XOGO-(ANCHO_PJ+MARCO_VENTANA_LATERAL),pj.punto.x)
	pj.punto.x = max(MARCO_VENTANA_LATERAL,pj.punto.x)
	pj.punto.y = min(ALTO_XOGO-(ALTO_PJ+MARCO_VENTANA_VERTICAL),pj.punto.y)
	pj.punto.y = max(MARCO_VENTANA_VERTICAL,pj.punto.y)
		
	#MOVEMENTO DE PUNTO-CAMARA
	
	punto_camara.y = pj.punto.y - ALTO_VENTANA/2+ALTO_PJ/2
	punto_camara.x = pj.punto.x - ANCHO_VENTANA/2+ANCHO_PJ/2

	#REAXUSTE DO PUNTO
	
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
	
	#MOUSE
	
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

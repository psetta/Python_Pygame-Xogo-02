# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

#CLASES

class punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __getitem__(self,n):
		if n == 0:
			return self.x
		elif n == 1:
			return self.y
		else:
			raise IndexError(n)

class cadro:
	def __init__(self,pos,rect,color):
		self.pos = pos
		self.rect = rect
		self.color = color
		
class pj:
	def __init__(self,punto,punto_ventana):
		self.punto = punto
		self.punto_ventana = punto_ventana
		
#CONSTANTES

ANCHO_XOGO = 1200
ALTO_XOGO = 1000

ANCHO_VENTANA = 600
ALTO_VENTANA = 400

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

punto_pj = punto(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2)

pj = pj(punto(punto_pj.x,punto_pj.y),punto(punto_pj.x,punto_pj.y))

cadricula = False

#INICIAR PYGAME

pygame.init()

#PANTALLA

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])

pygame.display.set_caption("Conceptos_2")

#FONT

font_1 = pygame.font.SysFont("System", ANCHO_VENTANA/30)

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
	
	limite_superior = pygame.Rect(0-punto_camara.x,0-punto_camara.y,ANCHO_XOGO,ALTO_CADRO)
	pygame.draw.rect(ventana,[255,200,200],limite_superior)
	
	limite_inferior = pygame.Rect(0-punto_camara.x,(ALTO_XOGO-ALTO_CADRO)-punto_camara.y,ANCHO_XOGO,ALTO_CADRO)
	pygame.draw.rect(ventana,[255,200,200],limite_inferior)
	
	limite_esquerdo = pygame.Rect(0-punto_camara.x,0-punto_camara.y,ANCHO_CADRO,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,200,200],limite_esquerdo)
	
	limite_dereito = pygame.Rect((ANCHO_XOGO-ANCHO_CADRO)-punto_camara.x,0-punto_camara.y,ANCHO_CADRO,ALTO_XOGO)
	pygame.draw.rect(ventana,[255,200,200],limite_dereito)
	
	#DEBUXAR REFERENCIAS
	
	cont = 0
	
	for u in range(ALTO_VENTANA/2,ALTO_XOGO+1-ALTO_VENTANA/2,ALTO_CADRO*20):
		for i in range(ANCHO_VENTANA/2,ANCHO_XOGO+1-ANCHO_VENTANA/2,ANCHO_CADRO*10):
			texto_num = font_1.render(str(cont),True,[150,150,255])
			ventana.blit(texto_num,[i-punto_camara.x,u-punto_camara.y])
			cont += 1
			
			
	#DEBUXAR PJ_RECT_CENTRADO
	
	pj_centr = pygame.Rect(ANCHO_VENTANA/2-ANCHO_PJ/2,ALTO_VENTANA/2-ALTO_PJ/2,ANCHO_PJ,ALTO_PJ)
	pygame.draw.rect(ventana,[150,150,150],pj_centr,1)
	
	#DEBUXAR PJ
	
	pj_rect = pygame.Rect(pj.punto_ventana.x,pj.punto_ventana.y,ANCHO_PJ,ALTO_PJ)
	pygame.draw.rect(ventana,[0,0,0],pj_rect)
	
	#DEBUXAR TEXTO
	
	text_punto = font_1.render(("pj_punto("+str(pj.punto.x)+","+str(pj.punto.y)),True,[0,0,0])
	ventana.blit(text_punto,[ANCHO_CADRO,ALTO_CADRO])
	
	text_punto_ventana = font_1.render(("pj_punto_ventana("+str(pj.punto_ventana.x)+","+str(pj.punto_ventana.y)+")"),True,[0,0,0])
	ventana.blit(text_punto_ventana,[ANCHO_CADRO,ALTO_CADRO+text_punto_ventana.get_height()])
	
	text_punto_camara = font_1.render(("punto_camara("+str(punto_camara.x)+","+str(punto_camara.y)+")"),True,[0,0,0])
	ventana.blit(text_punto_camara,[ANCHO_CADRO,ALTO_CADRO+text_punto_camara.get_height()*2])
	
	#MOVEMENTO DA CAMARA
	
	tecla_pulsada = pygame.key.get_pressed()
	
	if tecla_pulsada[K_UP] or tecla_pulsada[K_w]:
		pj.punto.y -= VELOCIDADE_PJ
		if pj.punto.y < (ALTO_XOGO-ALTO_VENTANA/2)-ALTO_CADRO/2:
			punto_camara.y -= VELOCIDADE_PJ
		if punto_camara.y <= 0 or punto_camara.y >= ALTO_XOGO-ALTO_VENTANA:
			pj.punto_ventana.y = (pj.punto.y - VELOCIDADE_PJ) - punto_camara.y
		
	if tecla_pulsada[K_DOWN] or tecla_pulsada[K_s]:
		pj.punto.y  += VELOCIDADE_PJ
		if pj.punto.y > ALTO_VENTANA/2-ALTO_CADRO/2:
			punto_camara.y += VELOCIDADE_PJ
		if punto_camara.y >= ALTO_XOGO-ALTO_VENTANA or punto_camara.y <= 0:
			pj.punto_ventana.y = pj.punto.y - punto_camara.y
		
	if tecla_pulsada[K_RIGHT] or tecla_pulsada[K_d]:
		pj.punto.x += VELOCIDADE_PJ
		if pj.punto.x > ANCHO_VENTANA/2-ANCHO_CADRO/2:
			punto_camara.x += VELOCIDADE_PJ
		if punto_camara.x >= ANCHO_XOGO-ANCHO_VENTANA or punto_camara.x <= 0:
			pj.punto_ventana.x = pj.punto.x - punto_camara.x
		
	if tecla_pulsada[K_LEFT] or tecla_pulsada[K_a]:
		pj.punto.x -= VELOCIDADE_PJ
		if pj.punto.x < (ANCHO_XOGO-ANCHO_VENTANA/2)-ANCHO_CADRO/2:
			punto_camara.x -= VELOCIDADE_PJ
		if punto_camara.x <= 0 or punto_camara.x >= ANCHO_XOGO-ANCHO_VENTANA:
			pj.punto_ventana.x = pj.punto.x - punto_camara.x
		
	punto_camara.x = min(ANCHO_XOGO-ANCHO_VENTANA,punto_camara.x)
	punto_camara.x = max(0,punto_camara.x)
	punto_camara.y = min(ALTO_XOGO-ALTO_VENTANA,punto_camara.y)
	punto_camara.y = max(0,punto_camara.y)
	
	pj.punto.x = min(ANCHO_XOGO-ANCHO_PJ,pj.punto.x)
	pj.punto.x = max(0,pj.punto.x)
	pj.punto.y = min(ALTO_XOGO-ALTO_PJ,pj.punto.y)
	pj.punto.y = max(0,pj.punto.y)
	
	'''
	if not (punto_camara.x <= 0 or punto_camara.x >= ANCHO_XOGO-ANCHO_VENTANA):
		pj.punto_ventana.x = ANCHO_VENTANA/2-ANCHO_PJ/2
	if not (punto_camara.y <= 0 or punto_camara.y >= ALTO_XOGO-ALTO_VENTANA):
		pj.punto_ventana.y = ALTO_VENTANA/2-ALTO_PJ/2
	'''
	'''
	if pj.punto.x >= ANCHO_VENTANA/2:
		pj.punto_ventana.x = min(ANCHO_VENTANA-ANCHO_PJ,pj.punto_ventana.x)
	else:
		pj.punto_ventana.x = min((ANCHO_VENTANA/2),pj.punto_ventana.x)
	
	if pj.punto.x <= ANCHO_XOGO-ANCHO_VENTANA/2:
		pj.punto_ventana.x = max(ANCHO_VENTANA,pj.punto_ventana.x)
	else:
		pj.punto_ventana.x = max(0,pj.punto_ventana.x)
	'''
	
	pj.punto_ventana.y = min(ALTO_VENTANA-ALTO_PJ,pj.punto_ventana.y)
	pj.punto_ventana.y = max(0,pj.punto_ventana.y)
	
	
	#ACTUALIZAR PANTALLA
	
	pygame.display.update()
	
	#EVENTOS
	
	for e in pygame.event.get():
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_c:
				if cadricula:
					cadricula = False
				else:
					cadricula = True
		if e.type == pygame.QUIT:
			pygame.display.quit()
			ON = False
			
	reloj.tick(60)

from constant import *
import pygame
import math
from time import sleep

class Ball(pygame.sprite.Sprite):
	def __init__(self):
		super(Ball, self).__init__()
		self.speed = 20
		self.size = 10
		self.origin_image = pygame.transform.scale(pygame.image.load("image/dot.png"),(self.size,self.size))
		self.image = pygame.transform.scale(pygame.image.load("image/dot.png"),(self.size,self.size))
		self.rect = self.image.get_rect()
		self.rect.x = 20
		self.rect.y = 20
		self.angle = 0
		self.last_position = (0,0)
		self.mx = 0 
		self.my = 0 
		self.counter = 1

	def follow(self,mx,my):
		self.rect.x, self.rect.y = mx-self.size/2-5,my-self.size/2-5

	def throw(self,mx,my):
		u = (self.last_position[0]-mx,self.last_position[1]-my)
		v = (1,0)

		self.angle = self.angleWithVector(u,v)
		if -self.last_position[1]+my<0:
			self.angle *= -1

	def running(self):
		self.rect.x += -math.cos(self.angle)*self.speed
		self.rect.y += math.sin(self.angle)*self.speed

	def scalarProduct(self,u,v):
		return u[0]*v[0] + u[1]*v[1]
	def vectorNorm(self,vector):
		return math.sqrt(vector[0]**2+vector[1]**2)
	def angleWithVector(self,u,v):
		return math.acos(self.scalarProduct(u,v)/(self.vectorNorm(u)*self.vectorNorm(v)))
	def collide(self,XOrY):
		if XOrY == True:
			self.angle = -self.angle
		elif XOrY == False:
			self.angle = math.pi-self.angle




import pygame
from constant import *

class Case(pygame.sprite.Sprite):
	def __init__(self,x,y,case_size):
		super(Case, self).__init__()
		self.case_size = case_size
		self.x = x
		self.y = y
		self.image_list = ["image/square_full.png","image/square.png"]
		self.image_number = 1
		self.image = pygame.transform.scale(pygame.image.load(self.image_list[self.image_number]),(self.case_size,self.case_size))
		self.rect = self.image.get_rect()
		self.rect.x = x * self.case_size
		self.rect.y = y * self.case_size
	def changeColor(self):
		if self.image_number == 0:
			self.image_number = 1
			self.image = pygame.transform.scale(pygame.image.load(self.image_list[self.image_number]),(self.case_size,self.case_size))
		else:
			self.image_number = 0
			self.image = pygame.transform.scale(pygame.image.load(self.image_list[self.image_number]),(self.case_size,self.case_size))


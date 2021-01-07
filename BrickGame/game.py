from constant import *
from case import *
from ball import *
import math

class Game:
	def __init__(self):
		self.follow = False
		self.ball_click = False
		self.case = 0
		self.ball_throwing = False
		self.last_case = 0
		self.clicking = False
		self.case_size = 45
		self.handleCase()

	def handleCase(self):
		self.number_case_x = win[0] // self.case_size
		self.number_case_y = win[1] // self.case_size
		self.grid = []
		self.ball = Ball()
		for y in range(self.number_case_y):
			x = 0
			for x in range(self.number_case_x):
				self.grid.append(Case(x,y,self.case_size))

	def draw(self):
		for case in range(self.number_case_x*self.number_case_y):
			screen.blit(self.grid[case].image, self.grid[case].rect)
		screen.blit(self.ball.image, self.ball.rect)

	def checkClick(self):
		if self.clicking == True:
			mx ,my = pygame.mouse.get_pos()
			self.mouseClick(mx, my)
		elif self.ball_click == True:
			mx ,my = pygame.mouse.get_pos()
			self.ball_throwing = False
			if (self.ball.rect.x-self.ball.size < mx <self.ball.rect.x+self.ball.size and self.ball.rect.y-self.ball.size < my <self.ball.rect.y+self.ball.size) or self.follow:
				self.ball.follow(mx,my)
				self.follow = True
				self.ball.last_position = mx,my

	def mouseClick(self,mx,my):
		self.case = (mx // self.case_size) + (my // self.case_size*self.number_case_x)
		if self.case != self.last_case:
			self.grid[self.case].changeColor()
		self.last_case = (mx // self.case_size) + (my // self.case_size*self.number_case_x)

	def changeMode(self,mode):
		if mode == True:
			return False
		else :
			return True

	def changeCaseSize(self,add):
		if add:
			self.case_size-=10
		else:
			self.case_size+=10
		self.handleCase()

	def throw(self):
		mx,my = pygame.mouse.get_pos()
		if not (0<=abs(self.ball.last_position[0]-mx)<30 and 0<=abs(self.ball.last_position[1]-my)<30):
			self.ball_throwing = True
			self.ball.mx = mx
			self.ball.my = my
			self.ball.throw(self.ball.mx,self.ball.my)
			self.running()
	def running(self):
			self.ball.running()
	def reset(self):
		self.ball.rect.x = 10
		self.ball.rect.y = 10
		for i in self.grid:
			i.image_number = 0
			i.changeColor()
	def checkCollide(self):
		if win[0]-self.ball.image.get_width() < self.ball.rect.x :
			self.ball.collide(False)
		elif 0> self.ball.rect.x:
			self.ball.collide(False)
		elif 0 > self.ball.rect.y:
			self.ball.collide(True)
		elif win[1]-self.ball.image.get_width() < self.ball.rect.y:
			self.ball.collide(True)
		for i in self.grid:
			if i.image_number == 1:
				if (i.rect.x-1<self.ball.rect.center[0]<i.rect.x+self.case_size) and (i.rect.y-10<self.ball.rect.center[1]<i.rect.y):
					self.ball.collide(True)
					i.image_number = 0
					i.image = pygame.transform.scale(pygame.image.load(i.image_list[i.image_number]),(i.case_size,i.case_size))
				if (i.rect.x-1<self.ball.rect.center[0]<i.rect.x+self.case_size) and i.rect.y+self.case_size<self.ball.rect.center[1]<i.rect.y+self.case_size+10:
					self.ball.collide(True)
					i.image_number = 0
					i.image = pygame.transform.scale(pygame.image.load(i.image_list[i.image_number]),(i.case_size,i.case_size))
				if (i.rect.y-1<self.ball.rect.center[1]<i.rect.y+self.case_size) and (i.rect.x-10<self.ball.rect.center[0]<i.rect.x):
					self.ball.collide(False)
					i.image_number = 0
					i.image = pygame.transform.scale(pygame.image.load(i.image_list[i.image_number]),(i.case_size,i.case_size))
				if (i.rect.y-1<self.ball.rect.center[1]<i.rect.y+self.case_size) and  (i.rect.x+self.case_size<self.ball.rect.center[0]<i.rect.x+self.case_size+10):
					self.ball.collide(False)
					i.image_number = 0
					i.image = pygame.transform.scale(pygame.image.load(i.image_list[i.image_number]),(i.case_size,i.case_size))
				if (i.rect.x<self.ball.rect.center[0]<i.rect.x+self.case_size) and (i.rect.y<self.ball.rect.center[1]<i.rect.y+self.case_size):
					i.image_number = 0
					i.image = pygame.transform.scale(pygame.image.load(i.image_list[i.image_number]),(i.case_size,i.case_size))

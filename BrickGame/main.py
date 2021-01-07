import sys, pygame
from game import *
from constant import *

game = Game()

running = True
building = True
playing = False

while running:
	clock.tick(30)
	for event in pygame.event.get():

		if event.type == pygame.QUIT :
			pygame.quit()
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN and building:

			if event.button == 1:
				game.clicking = True

		elif event.type == pygame.MOUSEBUTTONUP and building:

			if event.button == 1:
				game.clicking = False

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_RETURN:
				building = game.changeMode(building)
				playing = game.changeMode(playing)
				game.ball_throwing = False
				if playing == False:
					game.reset()

			elif event.key == pygame.K_KP_PLUS:
				game.changeCaseSize(True)

			elif event.key == pygame.K_KP_MINUS:
				game.changeCaseSize(False)

		elif event.type == pygame.MOUSEBUTTONDOWN and playing:
			game.ball_click = True
		elif event.type == pygame.MOUSEBUTTONUP and playing:
			if game.follow:
				game.throw()
			game.ball_click = False
			game.follow = False
			


	if game.ball_throwing == True:
		game.running()

	game.checkCollide()
	game.draw()
	pygame.display.flip()
	game.checkClick()
	screen.fill([214, 219, 223])
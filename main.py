import pygame

import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS

from logger import log_state, log_event

from player import *

from asteroid import Asteroid

from asteroidfield import AsteroidField

from circleshape import *

def main():
	print("Starting Asteroids with pygame version:", pygame.version.ver)
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	player_chara = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
	asteroid_field = AsteroidField()

	while True:
		log_state()

		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return

		screen.fill("black")

		for sprite in drawable:
			sprite.draw(screen)

		updatable.update(dt)

		for asteroid in asteroids:
			if player_chara.collides_with(asteroid) is True:
				log_event("player_hit")
				print("Game over!")
				sys.exit()

		pygame.display.flip()
		clock.tick(60)
		dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
	main()

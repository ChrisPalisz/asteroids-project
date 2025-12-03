import pygame

import random

from circleshape import CircleShape

from constants import LINE_WIDTH, LINE_COLOR, ASTEROID_MIN_RADIUS

from logger import log_event

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		return pygame.draw.circle(screen, LINE_COLOR, self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		
		if self.radius < ASTEROID_MIN_RADIUS:
			return

		else:
			log_event("asteroid_split")
			split_angle = random.uniform(20, 50)
			new_velocity_1 = self.velocity.rotate(split_angle)
			new_velocity_2 = self.velocity.rotate(split_angle * -1)

			new_radius = self.radius - ASTEROID_MIN_RADIUS

			baby_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			baby_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

			baby_asteroid_1.velocity = new_velocity_1 * 1.2
			baby_asteroid_2.velocity = new_velocity_2 * 1.2

		

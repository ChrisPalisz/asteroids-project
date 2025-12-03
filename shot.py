from constants import *

from circleshape import *

class Shot(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		return pygame.draw.circle(screen, LINE_COLOR, self.position, self.radius, LINE_WIDTH)

	def update(self, dt):
		self.position += self.velocity * dt		
